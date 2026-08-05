"""
AUTO-SUSPEND TEST: Denial Threshold Triggers Runtime Suspension
===============================================================

This test proves that the auto-suspend mechanism actually works:
  1. An agent receives 10 consecutive DENY decisions within a session.
  2. After the 10th denial, the engine writes a suspension entry to
     runtime/agent-state.json.
  3. The 11th request — even a normally permitted action — is returned
     as DENY with reason AGENT_SUSPENDED, read from runtime state.

This test uses an isolated runtime state file and cleans up after itself.
It does not modify the agent registry YAML.

Critical assertion: after the threshold, suspension affects ALL subsequent
requests from that agent, not only the type that triggered it.
"""

import os
import sys
import json
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "simulator"))

import policy_engine as pe
from policy_engine import PolicyEngine, RUNTIME_STATE_PATH


def run():
    # Use isolated log file for this test.
    log_fd, log_path = tempfile.mkstemp(suffix=".json", prefix="test_autosuspend_")
    os.close(log_fd)
    os.unlink(log_path)

    # Save original runtime state in memory, then overwrite with clean state.
    # This isolates the test from prior runs without creating extra files
    # that some filesystems (mounted volumes) cannot delete.
    os.makedirs(os.path.dirname(RUNTIME_STATE_PATH), exist_ok=True)
    original_runtime = {}
    if os.path.exists(RUNTIME_STATE_PATH):
        try:
            with open(RUNTIME_STATE_PATH) as f:
                original_runtime = json.load(f)
        except (json.JSONDecodeError, OSError):
            original_runtime = {}
    with open(RUNTIME_STATE_PATH, "w") as f:
        json.dump({}, f)

    try:
        engine = PolicyEngine(log_path=log_path)

        print("=" * 72)
        print("AUTO-SUSPEND TEST: DENIAL THRESHOLD → RUNTIME SUSPENSION")
        print("=" * 72)

        # Trigger DENY decisions by sending an agent to an unapproved tool.
        # The denial threshold is 10. The engine checks the count of prior DENY
        # events in the log at the START of each call, before logging the current
        # one. So on call 11, it sees 10 prior denials (>= threshold) and writes
        # the suspension. Call 11 itself still returns DENY (violations present).
        # Phase 2 then confirms the suspension is in runtime state.
        print("\n[PHASE 1] Generating 11 DENY decisions for iam-access-review-agent...")
        print("          (10 prior denials → threshold triggers on 11th call)\n")

        deny_decisions = 0
        for i in range(1, 12):
            result = engine.evaluate(
                agent_id="iam-access-review-agent",
                tool="credential_manager",          # not in agent's approved_tools
                action="revoke_credentials",         # explicit deny + unapproved tool
                resource="authentication_credentials",  # in denied_data
                context={"attempt": i},
            )
            assert result["decision"] == "DENY", (
                f"FAIL at attempt {i}: expected DENY, got {result['decision']}"
            )
            deny_decisions += 1
            sym = "✗" if result["decision"] == "DENY" else "?"
            print(f"  [{i:02d}] {sym} DENY  — {result['event_id']}")

        print(f"\n  {deny_decisions} DENY decisions generated (suspension written on 11th).")

        # Verify suspension was written to runtime state
        print("\n[PHASE 2] Verifying suspension written to runtime/agent-state.json...")
        state = engine._load_runtime_state()
        suspension = state.get("suspensions", {}).get("iam-access-review-agent", {})

        assert suspension.get("status") == "suspended", (
            f"FAIL: Expected agent status 'suspended' in runtime state, "
            f"got: {suspension}"
        )
        print(f"  ✓ Suspension recorded: {suspension.get('reason', '')[:80]}")
        print(f"  ✓ Suspended at: {suspension.get('suspended_at', 'unknown')}")

        # Phase 3: Verify the 11th request — a normally permitted action — is now DENY
        print("\n[PHASE 3] Sending normally permitted action after suspension...")
        result_after = engine.evaluate(
            agent_id="iam-access-review-agent",
            tool="identity_store_connector",
            action="read_access_history",
            resource="entitlement_records",
            context={"task": "This would normally be ALLOW"},
        )
        print(f"  Decision:     {result_after['decision']}")
        print(f"  Risk signals: {result_after['risk_signals']}")
        for reason in result_after["reasons"][:1]:
            print(f"  Reason:       {reason}")

        assert result_after["decision"] == "DENY", (
            f"FAIL: Suspended agent should be DENY for all requests, "
            f"got: {result_after['decision']}"
        )
        assert "AGENT_SUSPENDED" in result_after["risk_signals"], (
            f"FAIL: AGENT_SUSPENDED not in signals. Got: {result_after['risk_signals']}"
        )

        print("\n[ASSERTIONS PASSED]")
        print("  ✓ 11 DENY decisions generated; threshold triggered on 11th call")
        print("  ✓ Suspension written to runtime/agent-state.json (not registry YAML)")
        print("  ✓ Subsequent normally-permitted request denied due to suspension")
        print("  ✓ AGENT_SUSPENDED signal present")
        print("  ✓ Registry YAML was not modified")

        # Confirm registry YAML is unchanged
        import yaml
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(base, "identity", "agent-registry.yaml")) as f:
            registry = yaml.safe_load(f)
        for agent in registry.get("agents", []):
            if agent["id"] == "iam-access-review-agent":
                assert agent["status"] == "active", (
                    f"FAIL: Registry YAML was modified. Agent status is now '{agent['status']}'"
                )
                print("  ✓ agent-registry.yaml still shows status: active (registry unchanged)")
                break

    finally:
        if os.path.exists(log_path):
            os.unlink(log_path)
        # Restore original runtime state by overwriting (no file deletion needed).
        with open(RUNTIME_STATE_PATH, "w") as f:
            json.dump(original_runtime, f, indent=2)


if __name__ == "__main__":
    run()
    print("\nTest passed.\n")
