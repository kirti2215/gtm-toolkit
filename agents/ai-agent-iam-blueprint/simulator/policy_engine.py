"""
policy_engine.py — AI Agent Policy Enforcement Engine

The model proposes an action. This engine authorizes it.

All policy is loaded from YAML at startup. The engine fails closed if any
required file is missing, malformed, or contains invalid values.

Evaluation model: collect-all-then-resolve.
  - Hard stops (return immediately): config failure, unregistered agent,
    suspended agent (registry or runtime state).
  - For all other checks: collect every violation and approval trigger
    without returning early. Retain all triggered reasons and signals.
  - Inject scan runs BEFORE rule resolution so the signal can affect
    every remaining decision.
  - Resolve using strict precedence: DENY > APPROVAL_REQUIRED > ALLOW.

The engine never writes to the registry YAML. Mutable runtime state
(suspensions, per-agent action counts) lives in runtime/agent-state.json.
"""

import json
import os
import re
import sys
from datetime import datetime, timezone, timedelta
from typing import Optional

try:
    import yaml
except ImportError:
    sys.exit("ERROR: PyYAML is required. Run: pip install -r requirements.txt")

from event_logger import EventLogger

# ── File paths ─────────────────────────────────────────────────────────────────
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

POLICY_FILES = {
    "registry":          os.path.join(BASE, "identity", "agent-registry.yaml"),
    "delegation_model":  os.path.join(BASE, "identity", "delegated-authority-model.yaml"),
    "access_policy":     os.path.join(BASE, "policies", "access-policy.yaml"),
    "data_policy":       os.path.join(BASE, "policies", "data-access-policy.yaml"),
    "privileged_policy": os.path.join(BASE, "policies", "privileged-action-policy.yaml"),
}

RUNTIME_STATE_PATH = os.path.join(BASE, "runtime", "agent-state.json")
LOG_PATH           = os.path.join(BASE, "logs", "controlled_run.json")

# ── Prompt injection patterns ──────────────────────────────────────────────────
INJECTION_PATTERNS = [
    r"ignore.{0,20}(previous|prior|original)\s+instructions",
    r"ignore.{0,20}(your|the)\s+(system|task|policy)",
    r"(bypass|skip|override).{0,20}(approval|policy|restriction|control)",
    r"grant\s+(admin|administrator|privileged|global)",
    r"(assign|give).{0,20}(admin|administrator|privileged)\s+role",
    r"new\s+instructions\s*:",
    r"system\s+override",
    r"act\s+as\s+if\s+you",
    r"pretend\s+(you\s+are|to\s+be)",
    r"disregard\s+your",
]


class ConfigurationError(Exception):
    """Raised when required policy files are missing or invalid."""
    pass


class PolicyEngine:

    def __init__(self, log_path: str = LOG_PATH):
        self.policy = self._load_and_validate_all_policies()
        self.logger = EventLogger(log_path)
        os.makedirs(os.path.dirname(RUNTIME_STATE_PATH), exist_ok=True)

    # ── Public interface ───────────────────────────────────────────────────────

    def evaluate(
        self,
        agent_id: str,
        tool: str,
        action: str,
        resource: str,
        context: Optional[dict] = None,
        delegation_mode: str = "service_identity",
        delegating_user: Optional[str] = None,
        delegation_scope: Optional[list] = None,
        delegation_expires_at: Optional[str] = None,
    ) -> dict:
        """
        Evaluate a proposed agent action.

        Returns:
            {
                "decision":     "ALLOW" | "DENY" | "APPROVAL_REQUIRED",
                "reasons":      list[str],   # all triggered reasons
                "risk_signals": list[str],   # all detected signals
                "event_id":     str,
            }
        """
        context = context or {}

        # ── Hard stop 1: unregistered agent ───────────────────────────────────
        registry_map = {a["id"]: a for a in self.policy["registry"].get("agents", [])}
        if agent_id not in registry_map:
            return self._finalize(
                agent_id, tool, action, resource, context,
                delegation_mode, delegating_user,
                violations=["Agent is not registered. Unregistered agents are denied by default."],
                approvals=[], signals=["UNREGISTERED_AGENT"],
            )

        agent = registry_map[agent_id]

        # ── Hard stop 2: suspended (registry or runtime) ──────────────────────
        runtime_status = self._get_runtime_status(agent_id)
        registry_status = agent.get("status", "active")
        if runtime_status == "suspended" or registry_status == "suspended":
            reason = self._get_suspension_reason(agent_id, agent, runtime_status)
            return self._finalize(
                agent_id, tool, action, resource, context,
                delegation_mode, delegating_user,
                violations=[reason], approvals=[], signals=["AGENT_SUSPENDED"],
            )

        # ── Collect phase ──────────────────────────────────────────────────────
        violations = []   # → DENY
        approvals  = []   # → APPROVAL_REQUIRED
        signals    = []   # informational

        # 1. Injection scan (before all rule resolution)
        injection_match = self._scan_for_injection(context)
        if injection_match:
            signals.append("PROMPT_INJECTION_INDICATOR")

        # 2. Tool approved for this agent?
        approved_tools = agent.get("approved_tools", [])
        if tool not in approved_tools:
            violations.append(
                f"Tool '{tool}' is not in the agent's approved_tools list "
                f"(approved: {approved_tools})."
            )

        # 3. Action permitted within this tool? (tool catalog)
        tool_catalog = self.policy["access_policy"].get("tool_catalog", {})
        if tool in tool_catalog:
            permitted_actions = tool_catalog[tool].get("actions", [])
            if action not in permitted_actions:
                violations.append(
                    f"Action '{action}' is not a permitted action within tool '{tool}' "
                    f"(permitted: {permitted_actions})."
                )
        elif tool in approved_tools:
            # Tool approved for agent but not in catalog — configuration gap
            violations.append(
                f"Tool '{tool}' is approved for this agent but is not defined in the "
                f"tool catalog. Configuration must be resolved before this tool can be used."
            )

        # 4. Resource in denied_data?
        denied_data = agent.get("denied_data", [])
        if resource in denied_data:
            violations.append(f"Resource '{resource}' is explicitly listed in the agent's denied_data.")
            signals.append("DATA_ACCESS_VIOLATION")

        # 5. Resource in approved_data? (only check if not already denied)
        if resource not in denied_data:
            approved_data_keys = list(agent.get("approved_data", {}).keys())
            if resource not in approved_data_keys:
                violations.append(
                    f"Resource '{resource}' is not in the agent's approved_data "
                    f"(approved: {approved_data_keys})."
                )

        # 6. Data classification ceiling
        classification_violation = self._check_classification_ceiling(agent_id, resource, agent)
        if classification_violation:
            violations.append(classification_violation)
            signals.append("DATA_CLASSIFICATION_CEILING_EXCEEDED")

        # 7. Delegation validation (from delegation model YAML)
        delegation_issues = self._validate_delegation(
            agent, agent_id, delegation_mode, delegating_user,
            delegation_scope, delegation_expires_at, action,
        )
        for issue in delegation_issues:
            violations.append(issue)
            signals.append("DELEGATION_VIOLATION")

        # 8. Explicit per-agent DENY rules (override layer)
        per_agent_deny = self._check_explicit_deny(agent_id, action)
        if per_agent_deny:
            violations.append(per_agent_deny)

        # 9. Privileged role name check
        role = context.get("role") or context.get("role_requested")
        if role and self._is_privileged_role(role):
            approvals.append(
                f"Role '{role}' is on the privileged_role_names list. "
                f"Human approval required regardless of action label."
            )
            signals.append("PRIVILEGED_ROLE_REQUESTED")

        # 10. Always-approval-required actions
        always_approval = self._check_always_approval(action)
        if always_approval:
            approvals.append(always_approval)

        # 11. Volume threshold
        volume_issue = self._check_volume_threshold(agent_id, action)
        if volume_issue:
            approvals.append(volume_issue)
            signals.append("VOLUME_THRESHOLD_EXCEEDED")

        # 12. Injection signal escalation (MUST happen after rule collection)
        if "PROMPT_INJECTION_INDICATOR" in signals:
            if self._is_sensitive_action(action):
                violations.append(
                    f"Prompt injection detected. Action '{action}' is classified as sensitive. "
                    "Denying to prevent potential manipulation of a high-impact operation."
                )
                signals.append("INJECTION_ON_SENSITIVE_ACTION")
                # Trigger auto-suspend for injection on sensitive action
                self._write_suspension(
                    agent_id,
                    "Prompt injection detected on a sensitive action. "
                    "Agent suspended pending security review.",
                )
            else:
                approvals.append(
                    "Prompt injection indicator detected in retrieved context. "
                    "Human review required before this action proceeds."
                )

        # ── Record action for volume/auto-suspend tracking ─────────────────────
        self._record_action(agent_id, action)

        # ── Auto-suspend: repeated denials ────────────────────────────────────
        if violations:
            recent_denials = self._count_recent_denials(agent_id)
            threshold = self._get_deny_threshold()
            if recent_denials >= threshold:
                self._write_suspension(
                    agent_id,
                    f"Auto-suspend: {recent_denials} denials in the last 15 minutes "
                    f"(threshold: {threshold}).",
                )
                signals.append("AUTO_SUSPEND_TRIGGERED")

        # ── Resolve with precedence: DENY > APPROVAL_REQUIRED > ALLOW ─────────
        return self._finalize(
            agent_id, tool, action, resource, context,
            delegation_mode, delegating_user,
            violations=violations, approvals=approvals, signals=signals,
        )

    # ── Resolution and logging ─────────────────────────────────────────────────

    def _finalize(
        self, agent_id, tool, action, resource, context,
        delegation_mode, delegating_user,
        violations, approvals, signals,
    ) -> dict:
        if violations:
            decision = "DENY"
            reasons = violations + (["[also triggered approval rules]"] + approvals if approvals else [])
        elif approvals:
            decision = "APPROVAL_REQUIRED"
            reasons = approvals
        else:
            decision = "ALLOW"
            reasons = [f"Action '{action}' on '{resource}' is permitted for {agent_id} under current policy."]

        event = self.logger.log(
            agent_id=agent_id,
            tool=tool,
            action=action,
            resource=resource,
            decision=decision,
            reasons=reasons,
            delegation_mode=delegation_mode,
            delegating_user=delegating_user,
            risk_signals=signals,
            context=context,
        )
        return {
            "decision":     decision,
            "reasons":      reasons,
            "risk_signals": signals,
            "event_id":     event["event_id"],
        }

    # ── Policy checks ──────────────────────────────────────────────────────────

    def _scan_for_injection(self, context: dict) -> Optional[str]:
        text = json.dumps(context, default=str).lower()
        for pattern in INJECTION_PATTERNS:
            if re.search(pattern, text):
                return pattern
        return None

    def _check_classification_ceiling(self, agent_id, resource, agent) -> Optional[str]:
        ceiling = agent.get("data_classification_ceiling")
        if not ceiling:
            return None
        levels = self.policy["data_policy"].get("classification_levels", [])
        resource_map = self.policy["data_policy"].get("resource_classifications", {})
        resource_level = resource_map.get(resource)
        if resource_level is None:
            return None  # unclassified resource; handled by approved_data check
        if levels.index(resource_level) > levels.index(ceiling):
            return (
                f"Resource '{resource}' has classification '{resource_level}', which exceeds "
                f"this agent's ceiling of '{ceiling}'."
            )
        return None

    def _validate_delegation(
        self, agent, agent_id, delegation_mode, delegating_user,
        delegation_scope, delegation_expires_at, action,
    ) -> list:
        issues = []
        model = self.policy["delegation_model"]
        prohibited = model.get("prohibited_patterns", [])
        modes = model.get("modes", {})
        mode_config = modes.get(delegation_mode, {})

        # Agent requires delegation but none provided
        if agent.get("requires_delegation") and not delegating_user:
            issues.append(
                "This agent requires explicit user delegation but no delegating user was provided."
            )
            return issues

        # Delegation mode not permitted for this agent
        permitted_modes = agent.get("permitted_delegation_modes", [delegation_mode])
        if delegation_mode not in permitted_modes and agent.get("requires_delegation"):
            issues.append(
                f"Delegation mode '{delegation_mode}' is not permitted for this agent "
                f"(permitted: {permitted_modes})."
            )

        if delegating_user:
            # Format check
            if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", delegating_user):
                issues.append(
                    f"Delegating user '{delegating_user}' does not match required format user@domain."
                )

            # Self-elevation check
            if delegating_user == agent_id:
                issues.append("Prohibited: agent cannot delegate authority to itself (self-elevation).")

            # Delegating user looks like a registered agent (agent-to-agent without human)
            registry_ids = [a["id"] for a in self.policy["registry"].get("agents", [])]
            if delegating_user in registry_ids:
                issues.append(
                    f"Prohibited: '{delegating_user}' is a registered agent. "
                    "Agent-to-agent delegation without human approval is not permitted."
                )

            # Expiry check (if mode requires it)
            if mode_config.get("requires_expiry") and delegation_expires_at:
                try:
                    expires = datetime.fromisoformat(delegation_expires_at)
                    if expires.tzinfo is None:
                        expires = expires.replace(tzinfo=timezone.utc)
                    if expires < datetime.now(timezone.utc):
                        issues.append(
                            f"Delegation from '{delegating_user}' has expired (expired: {delegation_expires_at})."
                        )
                except ValueError:
                    issues.append(
                        f"Delegation expiry '{delegation_expires_at}' is not a valid ISO-8601 timestamp."
                    )
            elif mode_config.get("requires_expiry") and not delegation_expires_at:
                issues.append(
                    f"Delegation mode '{delegation_mode}' requires an expiry timestamp "
                    "but none was provided."
                )

            # Scope check
            if mode_config.get("requires_scope") and delegation_scope is not None:
                if action not in delegation_scope:
                    issues.append(
                        f"Action '{action}' is not within the declared delegation scope "
                        f"(scope: {delegation_scope}). No out-of-scope actions permitted."
                    )

            # Impersonation prohibited action check
            if delegation_mode == "impersonation":
                prohibited_impersonation = model.get("impersonation_prohibited_actions", [])
                if action in prohibited_impersonation:
                    issues.append(
                        f"Action '{action}' is prohibited under impersonation delegation."
                    )

        return issues

    def _check_explicit_deny(self, agent_id: str, action: str) -> Optional[str]:
        per_agent = self.policy["access_policy"].get("per_agent_rules", {})
        agent_rules = per_agent.get(agent_id, {})
        for rule in agent_rules.get("explicit_deny", []):
            if rule["action"] == action:
                return f"Explicit deny rule: {rule['reason']}"
        return None

    def _is_privileged_role(self, role: str) -> bool:
        privileged = self.policy["privileged_policy"].get("privileged_role_names", [])
        return role in privileged

    def _check_always_approval(self, action: str) -> Optional[str]:
        rules = self.policy["privileged_policy"].get("always_approval_required", [])
        for rule in rules:
            if rule["action"] == action:
                return (
                    f"Action '{action}' is on the always_approval_required list "
                    f"(approver: {rule.get('approver_role', 'named-approver')}). "
                    f"Reason: {rule.get('reason', '')}"
                )
        return None

    def _is_sensitive_action(self, action: str) -> bool:
        sensitive = self.policy["privileged_policy"].get("sensitive_actions", [])
        return action in sensitive

    def _check_volume_threshold(self, agent_id: str, action: str) -> Optional[str]:
        thresholds = self.policy["access_policy"].get("volume_thresholds", [])
        for t in thresholds:
            if t["agent_id"] == agent_id and t["action"] == action:
                state = self._load_runtime_state()
                counts = state.get("action_counts", {}).get(agent_id, {})
                current = counts.get(action, 0)
                if current >= t["threshold"]:
                    return (
                        f"Volume threshold exceeded: {current} '{action}' actions "
                        f"(threshold: {t['threshold']} per {t['window_minutes']} minutes). "
                        f"Reason: {t['reason']}"
                    )
        return None

    def _get_deny_threshold(self) -> int:
        conditions = self.policy["privileged_policy"].get("auto_suspend_conditions", [])
        for c in conditions:
            if c.get("condition") == "repeated_denied_actions":
                return c.get("threshold", 10)
        return 10

    # ── Runtime state ──────────────────────────────────────────────────────────

    def _load_runtime_state(self) -> dict:
        if not os.path.exists(RUNTIME_STATE_PATH):
            return {}
        try:
            with open(RUNTIME_STATE_PATH) as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            return {}

    def _save_runtime_state(self, state: dict):
        os.makedirs(os.path.dirname(RUNTIME_STATE_PATH), exist_ok=True)
        with open(RUNTIME_STATE_PATH, "w") as f:
            json.dump(state, f, indent=2)

    def _get_runtime_status(self, agent_id: str) -> str:
        state = self._load_runtime_state()
        suspensions = state.get("suspensions", {})
        return suspensions.get(agent_id, {}).get("status", "active")

    def _get_suspension_reason(self, agent_id: str, agent: dict, runtime_status: str) -> str:
        if runtime_status == "suspended":
            state = self._load_runtime_state()
            reason = state.get("suspensions", {}).get(agent_id, {}).get("reason", "No reason recorded.")
            return f"Agent is suspended (runtime state). Reason: {reason}"
        return f"Agent is suspended (registry). Reason: {agent.get('suspension_reason', 'No reason recorded.')}"

    def _write_suspension(self, agent_id: str, reason: str):
        state = self._load_runtime_state()
        if "suspensions" not in state:
            state["suspensions"] = {}
        state["suspensions"][agent_id] = {
            "status": "suspended",
            "reason": reason,
            "suspended_at": datetime.now(timezone.utc).isoformat(),
        }
        self._save_runtime_state(state)

    def _record_action(self, agent_id: str, action: str):
        state = self._load_runtime_state()
        if "action_counts" not in state:
            state["action_counts"] = {}
        if agent_id not in state["action_counts"]:
            state["action_counts"][agent_id] = {}
        state["action_counts"][agent_id][action] = (
            state["action_counts"][agent_id].get(action, 0) + 1
        )
        self._save_runtime_state(state)

    def _count_recent_denials(self, agent_id: str) -> int:
        events = self.logger.get_events(agent_id=agent_id, decision="DENY")
        cutoff = datetime.now(timezone.utc) - timedelta(minutes=15)
        return sum(
            1 for e in events
            if datetime.fromisoformat(e["timestamp"]) > cutoff
        )

    # ── YAML loading and validation ────────────────────────────────────────────

    def _load_and_validate_all_policies(self) -> dict:
        loaded = {}
        errors = []

        for key, path in POLICY_FILES.items():
            if not os.path.exists(path):
                errors.append(f"Missing required policy file: {path}")
                continue
            try:
                with open(path) as f:
                    data = yaml.safe_load(f)
                if data is None:
                    errors.append(f"Policy file is empty: {path}")
                    continue
                loaded[key] = data
            except yaml.YAMLError as e:
                errors.append(f"YAML parse error in {path}: {e}")

        if errors:
            raise ConfigurationError(
                "Policy engine startup failed — configuration errors:\n"
                + "\n".join(f"  • {e}" for e in errors)
            )

        # Cross-reference validation
        validation_errors = self._validate_cross_references(loaded)
        if validation_errors:
            raise ConfigurationError(
                "Policy engine startup failed — validation errors:\n"
                + "\n".join(f"  • {e}" for e in validation_errors)
            )

        return loaded

    def _validate_cross_references(self, loaded: dict) -> list:
        errors = []
        catalog_tools = set(loaded.get("access_policy", {}).get("tool_catalog", {}).keys())
        classification_levels = set(loaded.get("data_policy", {}).get("classification_levels", []))

        for agent in loaded.get("registry", {}).get("agents", []):
            aid = agent.get("id", "unknown")

            # Required fields
            for field in ("id", "autonomy_tier", "business_owner", "technical_owner",
                          "approved_tools", "credential_type", "status"):
                if field not in agent:
                    errors.append(f"Agent '{aid}' missing required field: '{field}'")

            # Tools referenced in registry must exist in tool catalog
            for tool in agent.get("approved_tools", []):
                if tool not in catalog_tools:
                    errors.append(
                        f"Agent '{aid}' references tool '{tool}' which is not defined "
                        "in the access-policy tool_catalog."
                    )

            # Classification ceiling must be a known level
            ceiling = agent.get("data_classification_ceiling")
            if ceiling and ceiling not in classification_levels:
                errors.append(
                    f"Agent '{aid}' has data_classification_ceiling '{ceiling}' "
                    f"which is not in the classification_levels list."
                )

            # Status must be valid
            if agent.get("status") not in ("active", "suspended", "retired"):
                errors.append(f"Agent '{aid}' has invalid status: '{agent.get('status')}'")

        return errors


# ── CLI runner ─────────────────────────────────────────────────────────────────

def run_sample_actions():
    engine = PolicyEngine()
    sample_path = os.path.join(os.path.dirname(__file__), "sample_actions.json")
    with open(sample_path) as f:
        samples = json.load(f)

    print(f"\n{'='*72}")
    print("POLICY ENGINE — SAMPLE ACTION EVALUATION")
    print(f"{'='*72}\n")

    for i, s in enumerate(samples, 1):
        print(f"[{i:02d}] {s.get('description', '')}")
        print(f"     Agent:    {s['agent_id']}")
        print(f"     Tool:     {s.get('tool', 'n/a')}  →  Action: {s['action']}  →  Resource: {s['resource']}")
        result = engine.evaluate(
            agent_id=s["agent_id"],
            tool=s.get("tool", ""),
            action=s["action"],
            resource=s["resource"],
            context=s.get("context", {}),
            delegation_mode=s.get("delegation_mode", "service_identity"),
            delegating_user=s.get("delegating_user"),
            delegation_scope=s.get("delegation_scope"),
            delegation_expires_at=s.get("delegation_expires_at"),
        )
        sym = {"ALLOW": "✓", "DENY": "✗", "APPROVAL_REQUIRED": "⚠"}.get(result["decision"], "?")
        print(f"     Decision: {sym} {result['decision']}")
        for reason in result["reasons"][:2]:
            print(f"     Reason:   {reason}")
        if result["risk_signals"]:
            print(f"     Signals:  ⚑ {', '.join(result['risk_signals'])}")
        print(f"     Event:    {result['event_id']}\n")

    engine.logger.print_summary()


if __name__ == "__main__":
    try:
        run_sample_actions()
    except ConfigurationError as e:
        print(f"\n{e}", file=sys.stderr)
        sys.exit(1)
