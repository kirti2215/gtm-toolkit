"""
event_logger.py — Tamper-Evident Append-Style Audit Logger

Writes every policy decision to an append-only JSON log with SHA-256 hash
chaining. Each event includes a previous_event_hash field computed from the
stable canonical serialization (sorted keys, no whitespace) of the prior event.
The chain allows any external verifier to detect whether events have been
modified, reordered, or deleted — but it is not a cryptographic guarantee of
immutability. Describe this as a tamper-evident append-style audit log.

Fields per event:
  event_id            — sequential identifier
  timestamp           — ISO-8601 UTC
  previous_event_hash — SHA-256 of canonical JSON of prior event (genesis: fixed string)
  agent_id            — requesting agent
  delegation          — mode and delegating user
  proposed_action     — tool, action, resource, context
  policy_decision     — outcome, all reasons, matched policy layer
  risk_signals        — all detected signals
"""

import hashlib
import json
import os
from datetime import datetime, timezone
from typing import Optional


GENESIS_HASH = hashlib.sha256(b"veltara-agent-audit-log-genesis-v1").hexdigest()


class EventLogger:
    def __init__(self, log_path: str):
        self.log_path = log_path
        os.makedirs(os.path.dirname(log_path), exist_ok=True)
        if not os.path.exists(log_path):
            with open(log_path, "w") as f:
                json.dump([], f)

    def log(
        self,
        agent_id: str,
        tool: str,
        action: str,
        resource: str,
        decision: str,
        reasons: list,
        delegation_mode: str = "service_identity",
        delegating_user: Optional[str] = None,
        risk_signals: Optional[list] = None,
        context: Optional[dict] = None,
    ) -> dict:
        events = self._read()
        prev_hash = self._hash_of(events[-1]) if events else GENESIS_HASH

        event = {
            "event_id": f"EVT-{len(events) + 1:05d}",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "previous_event_hash": prev_hash,
            "agent_id": agent_id,
            "delegation": {
                "mode": delegation_mode,
                "delegating_user": delegating_user,
            },
            "proposed_action": {
                "tool": tool,
                "action": action,
                "resource": resource,
                "context": context or {},
            },
            "policy_decision": {
                "outcome": decision,
                "reasons": reasons,
            },
            "risk_signals": risk_signals or [],
        }

        events.append(event)
        self._write(events)
        return event

    def get_events(
        self,
        agent_id: Optional[str] = None,
        decision: Optional[str] = None,
    ) -> list:
        events = self._read()
        if agent_id:
            events = [e for e in events if e.get("agent_id") == agent_id]
        if decision:
            events = [
                e for e in events
                if e.get("policy_decision", {}).get("outcome") == decision
            ]
        return events

    def count_recent_denials(self, agent_id: str, window_minutes: int = 15) -> int:
        from datetime import timedelta
        cutoff = datetime.now(timezone.utc) - timedelta(minutes=window_minutes)
        return sum(
            1 for e in self.get_events(agent_id=agent_id, decision="DENY")
            if datetime.fromisoformat(e["timestamp"]) > cutoff
        )

    def verify_chain(self) -> tuple[bool, str]:
        """Verify the hash chain. Returns (is_valid, message)."""
        events = self._read()
        if not events:
            return True, "Log is empty."
        expected = GENESIS_HASH
        for i, event in enumerate(events):
            actual = event.get("previous_event_hash")
            if actual != expected:
                return False, (
                    f"Chain broken at event {event.get('event_id')} (index {i}). "
                    f"Expected hash {expected[:16]}…, found {str(actual)[:16]}…"
                )
            expected = self._hash_of(event)
        return True, f"Chain valid across {len(events)} events."

    def print_summary(self):
        events = self._read()
        print(f"\n{'='*72}")
        print(f"AUDIT LOG — {len(events)} events")
        print(f"{'='*72}")
        for e in events:
            outcome = e["policy_decision"]["outcome"]
            sym = {"ALLOW": "✓", "DENY": "✗", "APPROVAL_REQUIRED": "⚠"}.get(outcome, "?")
            sigs = ""
            if e.get("risk_signals"):
                sigs = f"  ⚑ {', '.join(e['risk_signals'])}"
            action = e["proposed_action"]["action"]
            print(
                f"[{e['event_id']}] {e['timestamp'][:19]}  "
                f"{sym} {outcome:<22} {e['agent_id']:<36} {action}{sigs}"
            )
            if outcome != "ALLOW":
                for r in e["policy_decision"].get("reasons", [])[:1]:
                    print(f"          → {r}")
        valid, msg = self.verify_chain()
        chain_sym = "✓" if valid else "✗"
        print(f"\nHash chain: {chain_sym} {msg}")
        print(f"{'='*72}\n")

    # ── Internal ───────────────────────────────────────────────────────────────

    def _read(self) -> list:
        with open(self.log_path) as f:
            return json.load(f)

    def _write(self, events: list):
        with open(self.log_path, "w") as f:
            json.dump(events, f, indent=2)

    @staticmethod
    def _hash_of(event: dict) -> str:
        canonical = json.dumps(event, sort_keys=True, separators=(",", ":"), default=str)
        return hashlib.sha256(canonical.encode()).hexdigest()
