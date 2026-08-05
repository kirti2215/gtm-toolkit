# Value × Autonomy × Blast Radius

## The Strategic Framework

Every decision to deploy an AI agent in an enterprise environment is a trade-off between three variables:

**Value** — what the agent creates by acting autonomously.  
**Autonomy** — the minimum authority it needs to create that value.  
**Blast Radius** — what happens if it acts on a corrupted objective, makes a wrong judgment, or is manipulated.

The framework is not a formula. It is a set of questions that must be answered before the deployment decision is made, and again before autonomy is expanded.

```
What value does this agent create by acting autonomously?
                         ↓
What is the minimum autonomy required to create that value?
                         ↓
What is the worst-case outcome if it is manipulated or wrong?
                         ↓
What controls and approval gates are required at that blast radius?
                         ↓
Is the product, customer environment, and internal control
posture ready to support that level of autonomy today?
```

The answer to the last question determines whether the agent deploys — and at which autonomy tier.

---

## Why Minimum Autonomy Matters

Autonomy is not a feature. It is a risk parameter.

An agent that can only read and summarize has a blast radius of zero on data integrity and system state. An agent that can provision accounts, grant roles, disable identities, or send communications has a blast radius that must be bounded by controls proportional to that authority.

The mistake enterprises make is granting agents the autonomy they might eventually need, rather than the autonomy they need today. A broadly authorized agent that operates correctly is not safer than a narrowly authorized agent. It simply has not yet been manipulated.

The right question is not: "What could this agent usefully do if it had broad authority?"

The right question is: "What is the minimum authority this agent needs to deliver its value — and can we demonstrate that value before expanding that authority?"

---

## Four Roles, Four Responsibilities

The Value × Autonomy × Blast Radius decision requires input from four organizational functions. Each owns a distinct piece of the answer.

### Product Management

The PM defines what the agent is for and what it genuinely needs to accomplish its purpose.

Responsibilities:
- Define the job the agent performs with precision
- Identify the specific tools it needs, not all tools that might be useful
- Define the minimum autonomy required to deliver the stated value
- Define how the agent should behave under uncertainty: ask for clarification, escalate, or halt
- Define the approval boundaries: which actions require human review before execution
- Define the safe failure mode: what should happen when the agent cannot complete its task

A PM who cannot answer these questions clearly cannot authorize deployment. Vague purpose definitions lead to over-scoped authority.

### Security and IAM

Security and IAM translate the PM's purpose definition into an enforceable identity and control architecture.

Responsibilities:
- Register the agent with a unique identity and a declared purpose
- Assign the appropriate autonomy tier based on the blast radius assessment
- Define approved tools, approved data, and data classification ceiling
- Define delegation model: service identity, delegated user, or impersonation
- Specify volume thresholds and behavioral triggers
- Define the suspension and recovery conditions
- Ensure every policy is versioned, auditable, and loaded by an external enforcement engine

Security does not deploy controls that match what the PM requested. Security deploys controls that match what the blast radius requires. The PM's purpose definition is an input; the blast radius is the constraint.

### Product Marketing

PMM defines the public and customer-facing representation of the agent's capabilities and controls.

Responsibilities:
- Define what the agent can and cannot do, in terms customers can evaluate
- Define what the customer controls: which actions require customer approval, what can be stopped
- Define what is logged and accessible to the customer for review
- Define what security claims can be substantiated and how
- Avoid claims about agent safety that cannot be demonstrated operationally

The PMM role is not marketing copy. It is the accuracy layer between what the system actually does and how it is represented to the people who rely on it. Claims about agent trustworthiness that cannot be substantiated by the identity and policy architecture are liabilities.

### Go-to-Market

GTM determines where and when the agent is deployed, given the controls that exist and the customers who are ready.

Responsibilities:
- Identify which use cases and customer segments can absorb the current autonomy tier without unacceptable risk
- Determine what security maturity a customer must have before this agent is appropriate for them
- Map which objections will block adoption and what evidence the field needs to address them
- Define the proof points that must be demonstrated before autonomy is expanded in the next release
- Design the adoption sequence: lower-risk use cases first, higher-autonomy capabilities only after operational evidence

GTM does not sell the agent at its maximum theoretical value. GTM sells the agent at the value it can credibly deliver, within the controls that exist today, to the customers who are ready to receive it.

---

## The Autonomy Expansion Decision

Autonomy should expand only when operational evidence supports it.

Evidence means: the agent ran in production, at scale, across real tasks, and the audit logs and behavioral monitoring showed that it operated within its expected scope, did not generate anomalous signals, and delivered the expected value.

Evidence does not mean: the agent worked correctly in testing, or the PM believes it is ready, or a customer asked for it.

Before expanding autonomy:

- Review the audit log for the current tier. Were there anomalous signals? Threshold breaches? Denied actions that suggest the agent tested its boundaries?
- Review any incidents or near-incidents in the current tier.
- Confirm that the policy configuration, monitoring, and incident response playbook have been updated to cover the capabilities being added.
- Confirm that the approval authority chain for the new tier is in place and named.

If any of these reviews surface unresolved issues, autonomy does not expand until they are resolved.

---

## The Framework Applied: Veltara Financial Group

The three agents in this reference implementation illustrate the framework at different autonomy tiers.

**`iam-access-review-agent` (Tier 2 — Constrained Actions)**

Value: automates the quarterly access certification process for the finance department.  
Minimum autonomy: read entitlement records, read access history, create review tickets, compare usage patterns.  
Blast radius: incorrect review results could allow excessive access to persist. The agent cannot act on its findings — it can only flag them for human review.  
Controls: denied data list excludes sensitive records. No provisioning actions. No account disablement. Explicit deny on disable_account.

**`iam-provisioning-agent` (Tier 2 — Constrained Actions)**

Value: automates standard role provisioning within defined daily volume.  
Minimum autonomy: provision standard roles, disable accounts under specific conditions, log provisioning events.  
Blast radius: incorrect provisioning could grant inappropriate access. Privileged role grants could elevate attacker positions.  
Controls: volume threshold at 20 per hour. Privileged role name check escalates to APPROVAL_REQUIRED. Explicit deny on grant_privileged_role. Injection on provisioning context → auto-suspend.

**`security-investigation-agent` (Tier 2 — Constrained Actions with Delegation)**

Value: assists analysts in investigating security incidents by correlating authentication events.  
Minimum autonomy: requires explicit delegation from a named analyst for every investigation.  
Blast radius: unauthorized data access during investigation could expose sensitive identity records.  
Controls: requires_delegation enforced. Delegation scope validated per investigation. Denied data includes full_identity_record and MFA seeds. Classification ceiling at confidential. Credential revocation explicitly blocked.

In each case, the autonomy tier was chosen not by what the agent could theoretically do, but by what value it needed to deliver and what blast radius that created. The controls constrain the blast radius to the level the enterprise has determined is acceptable.

---

## The Strategic Position

This framework is not a product decision. It is an organizational stance.

Enterprises that deploy AI agents without answering these questions are not moving faster. They are taking on risk they have not priced, with blast radii they have not mapped, in use cases where the controls are not yet proportional to the authority granted.

The competitive advantage is not having agents. It is having agents that can be trusted — because their authority is scoped, their behavior is observed, their actions are enforced by policy, and the organization has demonstrated operationally that the value they deliver exceeds the risk they introduce.

That demonstration is the output of this framework applied consistently.
