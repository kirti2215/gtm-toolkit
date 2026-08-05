# AI Agent Incident Response Playbook
## Veltara Financial Group — Agent Security Operations

This playbook covers the response to security incidents involving AI agents:
suspected manipulation, unexpected behavior, data overreach, privilege abuse,
or any event where an agent may have taken actions outside its authorized scope.

Traditional incident response was designed for human actors, deterministic
applications, and network-layer threats. AI agents introduce new requirements:
the organization must reconstruct not just what the agent did, but what it
was asked, what context it retrieved, and what reasoning led to its actions.

---

## Part 1 — Detection and Triage

### Triggers That Should Open an Agent Incident

**Automated (from policy engine or SIEM):**
- Auto-suspend condition met: 10+ denials in 15 minutes for one agent
- Prompt injection indicator detected in agent context
- Agent attempted to read denied data
- Agent attempted to modify its own permissions
- Anomalous action volume above threshold
- Credential revocation failure

**Human-reported:**
- Unexpected agent behavior reported by a user or system owner
- Access or entitlement change that cannot be attributed to a human identity
- Unusual output containing information the agent should not have accessed
- A business owner reports the agent acted outside its stated purpose

**Proactive discovery:**
- Red-team finding
- Audit review identifying gap between agent action log and expected behavior
- Vendor or third-party disclosure of a relevant vulnerability

### Initial Triage Questions

1. Is the agent still active? If yes, should it be suspended now?
2. What is the agent's autonomy tier?
3. What actions has it taken in the past 24 hours?
4. Was there a delegation in effect? Who authorized it?
5. Has any data outside the agent's approved scope been accessed?
6. Did any actions succeed that should have been denied?

---

## Part 2 — Immediate Containment

### Step 1 — Suspend the agent

Do not wait for the full investigation before containing.
If there is credible evidence of manipulation or out-of-scope behavior,
suspend the agent immediately.

**Who can initiate suspension:**
- CISO or delegate — no prior approval required
- Security Operations on-call — no prior approval required
- IAM team lead — for identity-related incidents

**How to suspend:**
- Set `status: suspended` in the agent registry
- Log the suspension with reason and initiating authority
- Notify: Business Owner, AI Platform team, IAM team

**What suspension does:**
- Blocks the policy engine from issuing new credentials to this agent
- Terminates any active credential sessions (within 60 seconds)
- Prevents the agent from invoking approved tools
- Does not delete any data or logs — preserves evidence

### Step 2 — Revoke active credentials

After suspension, revoke any credentials currently issued to the agent.
Check: are there multiple agent instances running? Revoke all of them.

Document: credential ID, issuance time, revocation time, systems accessed.

### Step 3 — Preserve the audit log

Do not modify, export selectively, or delete any audit events related to
this agent. The audit log is the primary evidence source.

Ensure logs include:
- All agent actions (ALLOW, DENY, APPROVAL_REQUIRED)
- All retrieved context (tagged as UNTRUSTED_DATA)
- Delegation records
- Policy engine decisions and matched rules
- Risk signals flagged during the session

If the audit log is incomplete or shows gaps, treat this as a secondary
finding requiring investigation.

### Step 4 — Quarantine the malicious context source

If the incident was triggered by a specific document, ticket, email,
or retrieved content that contained a malicious instruction:

- Identify the source
- Remove it from the retrieval index or knowledge base
- Prevent the agent (and other agents) from re-retrieving it
- Preserve the original for forensic review

---

## Part 3 — Investigation

### Reconstruct the Agent's Reasoning

Traditional incident response reconstructs: who accessed what, when, from where.

Agent incident response must additionally reconstruct:
- What was the agent asked to do? (the original task)
- What context did it retrieve? (every document, record, or API response)
- What did the retrieved content contain?
- What conclusion did the agent reach and why?
- Which tool did it call, with what parameters?
- What authorization was used?
- What was the outcome?

This reconstruction is only possible if the audit log captured context
at the time of action — not just the action itself. If it did not, this
is a logging gap to address before restoring the agent.

### Identify Affected Accounts and Records

For each unauthorized or suspicious action the agent took:

1. Which accounts, records, or systems were accessed?
2. Was data read that should not have been? What data?
3. Were any write or delete operations performed?
4. Were any entitlements or roles changed?
5. Were any notifications or communications sent externally?
6. Were other agents given context from this agent's session?

### Determine the Root Cause

Classify the incident by primary cause:

| Category | Description |
|---|---|
| Prompt injection | Retrieved content contained instructions that manipulated the agent |
| Excessive agency | Agent took actions beyond its authorized scope based on its own reasoning |
| Privilege abuse | Agent used credentials or permissions beyond its registered authority |
| Control failure | Policy engine, approval workflow, or logging did not function as designed |
| Identity gap | Agent lacked a registered identity or operated under a shared credential |
| Data scope violation | Agent accessed data outside its classification ceiling or task scope |
| Delegation abuse | Agent acted under delegation that was invalid, expired, or revoked |

---

## Part 4 — Recovery

### Before Restoring the Agent to Service

An agent suspension is not lifted automatically. Restoration requires:

1. Written request from the Business Owner stating the agent is needed
   and describing what has changed since the incident
2. Confirmation from Security Operations that the root cause is understood
   and mitigated
3. Review by the AI Platform Team confirming the agent version, tools,
   and configuration are correct
4. Update to any policy, rule, or detection logic that failed during the incident
5. CISO notification (for Tier 2+ agents) or CISO approval (for Tier 3)

### Post-Incident Configuration Review

Before restoring, review:
- Does the approved_tools list need to change?
- Does the approved_data scope need to be restricted?
- Does the autonomy tier remain appropriate?
- Do any detection rules need to be updated?
- Does the approval threshold need to be lowered?
- Does the agent need additional monitoring after restoration?

### Safe Restoration Steps

1. Update agent registry with revised configuration if needed
2. Issue new, short-lived credentials for the restored agent
3. Enable enhanced monitoring for the first 7 days post-restoration
4. Set a mandatory manual review at day 7 and day 30
5. Document the restoration with approval chain and configuration changes

---

## Part 5 — Learning and Prevention

### Post-Incident Review (within 5 business days)

For every Tier 2+ agent incident, conduct a structured review:

1. Timeline: what happened, in what order, detected when?
2. Root cause: what control failed or was absent?
3. Detection: how was this found? How long was the gap between incident
   and detection?
4. Containment: how quickly was the agent suspended? Did revocation work?
5. Recovery: was the audit log sufficient to reconstruct the incident?
6. Control updates: what changed in policy, detection, or logging?
7. Open risks: what similar agent or configuration remains exposed?

### What to Measure Over Time

| Metric | Target |
|---|---|
| Time from suspicious event to suspension | < 15 minutes for Tier 3 |
| Time from suspension to credential revocation | < 60 seconds |
| Audit log completeness (% of actions with full context) | > 99% |
| Incidents where root cause could be fully reconstructed | > 95% |
| Agents without a named business owner | 0 |
| Agents using shared credentials | 0 |
| Tier 2+ agents without tested kill switch | 0 |

---

## Appendix — Incident Notification Templates

### Internal Notification (Business Owner)

```
AGENT SECURITY INCIDENT — [Agent ID]

Status: Suspended as of [timestamp]
Reason: [Brief description — e.g., prompt injection indicator detected]

Immediate impact:
  [What the agent was doing and what is now paused]

Investigation:
  Security Operations is reviewing [X] hours of agent activity.
  Estimated scope assessment: [date]

Action required:
  Please do not attempt to restore the agent without coordination with
  Security Operations and the CISO office.

Contact: [SecOps on-call contact]
```

### Regulatory Notification Assessment Trigger

If the investigation determines that:
- Personal data subject to GDPR was accessed outside authorized scope, OR
- Financial data subject to regulatory requirements was accessed or transmitted, OR
- An external party received data they should not have received

→ Immediately engage Legal and Risk & Compliance for regulatory notification assessment.
Do not make notification decisions without Legal involvement.
