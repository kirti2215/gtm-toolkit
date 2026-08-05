# Decision Rights Matrix — AI Agent Governance

The most common failure in enterprise AI security is not a missing control.
It is unclear ownership: who approved this agent, who can suspend it,
who accepts the risk if it behaves unexpectedly, and who decides when it
is safe to restore service.

This matrix defines accountability across every major agent governance decision.

---

## Stakeholders

| Role | Abbreviation | Accountable for |
|---|---|---|
| Business Owner | BO | Agent purpose, outcomes, residual risk acceptance |
| AI Platform Team | APT | Agent deployment, versioning, tooling |
| IAM / Identity Team | IAM | Agent identity, credentials, access provisioning |
| Security Operations | SecOps | Threat monitoring, incident detection, response |
| Data Governance | DG | Data classification, access scope, retention |
| Risk and Compliance | RC | Regulatory requirements, audit, policy |
| CISO | CISO | Enterprise security strategy, escalated approvals |
| Legal | Legal | Legal holds, regulatory filings, e-discovery |

---

## Decision Rights

### Agent Lifecycle

| Decision | Approves | Consulted | Informed |
|---|---|---|---|
| Register a new agent identity | APT + IAM | BO, SecOps | CISO |
| Assign initial autonomy tier | APT + BO | IAM, SecOps | CISO |
| Increase autonomy tier | CISO + APT | BO, IAM, SecOps, DG | RC |
| Decrease autonomy tier | APT | BO, SecOps | CISO |
| Modify approved_tools list | APT + BO | IAM, SecOps | CISO |
| Expand approved_data scope | DG + BO | IAM, SecOps | CISO, RC |
| Restrict approved_data scope | DG | APT, BO | — |
| Deploy new agent version | APT | BO, IAM | SecOps |
| Retire an agent | BO + APT | IAM, DG | SecOps, RC |

### Access and Permissions

| Decision | Approves | Consulted | Informed |
|---|---|---|---|
| Grant standard data access | IAM | DG | BO |
| Grant confidential data access | IAM + DG | SecOps, BO | CISO |
| Grant delegated user authority | User + IAM | BO | SecOps |
| Allow impersonation mode | CISO + BO | IAM, SecOps, Legal | RC |
| Approve action above volume threshold | IAM Ops Lead | SecOps | BO |
| Approve privileged role provisioning | IAM Governance Lead | SecOps | CISO |
| Approve emergency access grant | CISO or delegate | IAM, BO | SecOps, Legal |

### Incident and Response

| Decision | Approves | Consulted | Informed |
|---|---|---|---|
| Suspend agent immediately | SecOps or CISO | APT, BO | IAM |
| Revoke agent credentials | IAM + SecOps | APT | BO |
| Quarantine malicious context source | SecOps | APT, DG | BO |
| Initiate incident investigation | SecOps | IAM, APT, DG | BO, CISO |
| Determine scope of affected records | DG + IAM | SecOps, Legal | RC |
| Notify affected users or regulators | Legal + RC | BO, SecOps | CISO |
| Restore suspended agent to service | APT + BO + SecOps | IAM, DG | CISO |
| Accept residual risk after incident | BO (in writing) | RC, Legal | CISO |
| Update policy following incident | IAM + SecOps | APT, DG, BO | CISO |

### Risk and Compliance

| Decision | Approves | Consulted | Informed |
|---|---|---|---|
| Classify data an agent may access | DG | IAM, SecOps | BO, RC |
| Set retention policy for agent logs | DG + Legal | SecOps, RC | IAM |
| Define cross-border data restrictions | Legal + DG | RC | CISO |
| Approve agent for regulated data access | RC + Legal | DG, IAM, SecOps | CISO |
| Accept residual risk of agent deployment | BO | RC, SecOps | CISO |
| Waive a control requirement | CISO | RC, BO, IAM | Legal |

---

## Who Can Suspend an Agent

This question must have a clear, practiced answer before any Tier 2 or
Tier 3 agent is deployed. The answer is not "it depends."

**Any of the following may initiate an immediate agent suspension:**

1. The CISO or Security Operations on-call — no approval required
2. The IAM team lead — no approval required, for identity-related incidents
3. The Business Owner — for agents in their domain
4. The policy engine — automatically, when auto-suspend conditions are met

**Restoration requires:**
- Written request from the Business Owner
- Confirmation from Security Operations that the incident is resolved
- Approval from the AI Platform Team lead
- CISO notification

There is no "quick restore" path for a suspended Tier 3 agent.

---

## Who Accepts Residual Risk

Every deployed agent carries residual risk: the possibility that controls fail,
that a novel attack path is exploited, or that the agent behaves unexpectedly
in a scenario the design did not anticipate.

Residual risk must be formally accepted in writing by the Business Owner
before any Tier 2 or Tier 3 agent goes into production. This document states:

- What the agent is authorized to do
- What controls are in place
- What risks have been identified and accepted
- Who is accountable if the agent causes harm
- When the acceptance must be renewed (maximum: annually)

Risk acceptance does not transfer accountability to the security team.
The Business Owner remains accountable for the agent's outcomes.
