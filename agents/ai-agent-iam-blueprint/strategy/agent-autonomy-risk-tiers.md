# Agent Autonomy and Risk Tiers

Not every AI agent needs the same controls. The question is not whether
to secure agents — it is how to calibrate controls to the actual risk an
agent carries: what it can access, what it can change, and what happens
if it is manipulated or fails.

This tier model classifies agents by autonomy and potential impact.
It answers the leadership question: where can we move quickly, where must
we add controls first, and where should autonomous action not yet be permitted?

---

## The Four Tiers

### Tier 0 — Advisory Only

The agent generates analysis, summaries, recommendations, or reports.
It does not take any action in an enterprise system. Its output is consumed
by a human who then decides what to do.

**Examples:**
- Summarizes access review findings for a human certifier
- Identifies dormant accounts and surfaces them in a dashboard
- Drafts a provisioning recommendation for human approval
- Generates an anomaly investigation summary for a SOC analyst

**What it can do:**
- Read approved data sources
- Generate text output

**What it cannot do:**
- Call any write, modify, or delete API
- Invoke any system action
- Send external communications

**Required controls:**

| Control | Required |
|---|---|
| Registered agent identity | Yes |
| Business and technical owner | Yes |
| Data classification ceiling | Yes |
| Output content classification check | Yes |
| Action logging | Yes |
| Approval workflow | Not required |
| Credential revocation capability | Basic |

**Adoption risk:** Low. Tier 0 agents can be deployed relatively quickly
once data access is scoped and output review is in place.

---

### Tier 1 — Read-Only Enterprise Access

The agent reads enterprise systems and surfaces findings, but does not
write, modify, or invoke actions on any system.

**Examples:**
- Security investigation agent that reads authentication logs and correlates events
- Compliance agent that checks access entitlements against policy
- Reporting agent that queries multiple internal systems to build a status view

**What it can do:**
- Read from multiple authorized data sources
- Correlate and synthesize information across sources
- Create internal records such as tickets or summaries
- Send notifications to named internal recipients

**What it cannot do:**
- Modify any identity, account, entitlement, or system record
- Send external communications autonomously
- Invoke any privileged API

**Required controls:**

| Control | Required |
|---|---|
| Registered agent identity | Yes |
| Approved data scope with classification ceiling | Yes |
| Data minimization enforcement | Yes |
| Retrieved content tagged UNTRUSTED_DATA | Yes |
| Delegation requirements (if acting for a user) | Yes |
| Output classification check | Yes |
| Comprehensive action logging | Yes |
| Prompt injection monitoring | Yes |

**Adoption risk:** Low to moderate. The agent cannot change anything,
but it can aggregate sensitive data. Data scope and output controls
are the primary risk surface.

---

### Tier 2 — Constrained Actions

The agent can take approved, bounded actions within defined thresholds.
It routes anything above its threshold to a human approver.

**Examples:**
- Provisioning agent that handles standard role requests up to a daily limit
- Access review agent that creates certification tickets and sends notifications
- Workflow agent that updates ticket status and routes items in a queue

**What it can do:**
- Everything in Tier 1
- Write to specific approved systems within defined limits
- Provision approved, non-privileged roles below a quantity threshold
- Update defined record types (not identity structure or entitlements)
- Route items within an approved workflow

**What requires approval:**
- Volume above the daily or hourly threshold
- Provisioning of roles outside the approved catalog
- Actions on high-value accounts
- Anything not explicitly listed in the approved_tools registry entry

**Required controls:**

| Control | Required |
|---|---|
| All Tier 1 controls | Yes |
| External policy enforcement (not inside the model) | Yes |
| Action volume thresholds with approval routing | Yes |
| Approval workflow integration | Yes |
| Anomalous volume detection | Yes |
| Short-lived, task-scoped credentials | Yes |
| Kill switch and auto-suspend conditions | Yes |
| Rollback capability for reversible actions | Recommended |

**Adoption risk:** Moderate. The agent changes real systems. Policy
enforcement must sit outside the model. Human approval routing must work.

---

### Tier 3 — Privileged or High-Impact Actions

The agent can take actions that are difficult or impossible to reverse,
affect high-value accounts or systems, or carry significant business risk.

**Examples:**
- Customer offboarding agent that revokes access and archives data
- Emergency access provisioning agent
- Any agent that can disable accounts, modify security configurations,
  or invoke financial transactions

**What it can do:**
- Everything in Tier 2
- Execute high-impact, potentially irreversible actions
- Operate across multiple high-value systems in sequence

**What always requires human approval (regardless of tier):**
- Granting privileged roles
- Disabling accounts above a defined value threshold
- Bulk disablement above 5 accounts in 60 minutes
- Modifying security configurations
- Modifying the agent's own permissions
- Creating new agent identities
- Exporting bulk identity data

**Required controls:**

| Control | Required |
|---|---|
| All Tier 2 controls | Yes |
| Mandatory human approval for all privileged actions | Yes |
| Separation of duties enforcement | Yes |
| Named business owner accepts residual risk in writing | Yes |
| Enhanced logging with tamper protection | Yes |
| Named incident responder on-call at all times | Yes |
| Regular red-team testing | Yes |
| Autonomy tier increase requires CISO approval | Yes |

**Adoption risk:** High. Tier 3 agents should be deployed only after
Tier 1 and 2 controls are proven in the same environment. Autonomy
expands only when monitoring data supports it.

---

## Tier Assignment and Review

Every agent must be assigned a tier at registration. Tier assignment
is reviewed at the following triggers:

- Scheduled quarterly review
- After any security incident involving the agent
- Before any expansion of the agent's approved_tools list
- Before any expansion of the agent's approved_data scope
- When the agent's deployment environment changes

Increasing an agent's autonomy tier requires approval from the AI
Platform lead and CISO. No agent self-promotes to a higher tier.

---

## Tier vs. Sensitivity — Two Independent Dimensions

Autonomy tier governs what the agent can *do*.
Data classification governs what the agent can *see*.

An agent can be Tier 0 (advisory only) but handle CONFIDENTIAL data —
for example, a reporting agent that reads sensitive access logs but only
produces summaries. Both dimensions must be independently controlled.

| | Advisory (Tier 0) | Read-Only (Tier 1) | Constrained Actions (Tier 2) | Privileged Actions (Tier 3) |
|---|---|---|---|---|
| Public data | Low risk | Low risk | Moderate | High |
| Internal data | Low risk | Moderate | Moderate | High |
| Confidential data | Moderate | Moderate | High | Very high |
| Restricted data | High | Very high | Prohibited | Prohibited |
