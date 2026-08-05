# AI Agent IAM & Security Adoption Blueprint

Enterprise IAM architectures were designed around a specific assumption:
every actor that accesses data, modifies records, or invokes enterprise systems
is a human identity, a service account with deterministic behavior, or an
explicitly coded integration.

AI agents break that assumption.

An AI agent can receive natural-language instructions, retrieve external context,
select tools, and initiate multi-step actions across enterprise systems — all
without a human explicitly approving each step. Traditional IAM was not designed
to govern that class of actor.

This blueprint shows:

1. What a traditional cloud enterprise IAM architecture looks like
2. Which assumptions break when AI agents are introduced as non-human identities
3. How that architecture must be redesigned to secure agents from identity
   through runtime and incident response
4. How to classify agents by autonomy and risk to decide where controls are required
5. How to assign ownership, approval authority, and accountability across the enterprise
6. How to sequence adoption so that autonomy expands only when evidence supports it

---

## What Is in This Repository

```
ai-agent-iam-blueprint/
├── README.md                          ← This file
├── architecture/
│   ├── 01-traditional-iam-architecture.svg       ← Baseline enterprise IAM
│   ├── 02-ai-agent-expanded-architecture.svg     ← What breaks when agents are introduced
│   ├── 03-secured-ai-agent-architecture.svg      ← The redesigned control architecture
│   └── 04-master-ai-agent-security-operating-model.svg  ← Full 6-plane operating model
├── threat-model/
│   ├── changed-threat-actors.md      ← External AI attackers + internal adaptive agents
│   ├── agent-attack-paths.md         ← Injection, hijacking, escalation, overreach, suspension
│   └── trust-boundaries.md           ← Why cloud vs on-premises is not the trust boundary
├── identity/
│   ├── agent-registry.yaml            ← Sample agent identity definitions
│   └── delegated-authority-model.yaml ← Delegation and impersonation controls
├── policies/
│   ├── access-policy.yaml             ← Per-agent permission model
│   ├── privileged-action-policy.yaml  ← High-impact action thresholds
│   └── data-access-policy.yaml        ← Data classification and retrieval rules
├── simulator/
│   ├── policy_engine.py               ← Evaluates proposed agent actions
│   ├── event_logger.py                ← Writes tamper-evident audit events (SHA-256 chain)
│   └── sample_actions.json            ← Proposed actions for testing
├── tests/
│   ├── prompt_injection_test.py       ← Scenario 1: malicious instruction in ticket
│   ├── excessive_provisioning_test.py ← Scenario 2: bulk account changes
│   ├── sensitive_data_overreach_test.py ← Scenario 3: data scope beyond task
│   └── auto_suspend_test.py           ← Scenario 4: denial threshold → runtime suspension
├── examples/
│   ├── insecure-trace.json            ← Before controls: what executes unchecked
│   └── controlled-trace.json          ← After controls: what each layer intercepts
├── strategy/
│   ├── value-autonomy-blast-radius.md ← Core framework: the deployment decision
│   ├── agent-autonomy-risk-tiers.md   ← Four-tier classification model
│   ├── decision-rights-matrix.md      ← Who approves, owns, and can suspend agents
│   └── adoption-roadmap.md            ← Phased enterprise rollout plan
└── response/
    └── agent-incident-response-playbook.md
```

---

## The Fictional Environment

All examples use a fictional enterprise: **Veltara Financial Group**, a mid-size
asset management firm deploying AI agents across identity governance, customer
operations, and compliance workflows.

All agents, accounts, systems, policies, and incident scenarios described here
are invented for illustration. No real company, product, or security implementation
is represented.

---

## Three Architecture States

### State 1 — Traditional Enterprise IAM
The baseline: human identities, service accounts, deterministic workflows,
SIEM-based monitoring. See `architecture/traditional-iam-architecture.svg`.

### State 2 — AI-Expanded Architecture
The same infrastructure after AI agents are introduced. Which systems can they
access? Which assumptions no longer hold? Where are the new attack paths?
See `architecture/ai-agent-expanded-architecture.svg`.

### State 3 — Secured AI-Agent Architecture
The redesigned system: agent identity registry, tool gateway, external policy
enforcement, approval thresholds, runtime monitoring, and credential revocation.
See `architecture/secured-ai-agent-architecture.svg`.

---

## Running the Simulator

The policy engine evaluates any proposed agent action against the agent's
registered identity, permission model, autonomy tier, and data-access policy.

```bash
cd simulator
python policy_engine.py
```

This runs all actions in `sample_actions.json` and writes decisions to stdout
and to `../logs/controlled_run.json`.

To run the threat scenario tests:

```bash
cd tests
python prompt_injection_test.py
python excessive_provisioning_test.py
python sensitive_data_overreach_test.py
python auto_suspend_test.py
```

Each test demonstrates the attack path, then shows the policy decision and
the audit event produced. All tests use isolated log files and back up/restore
runtime state, so they can be run in any order and are safe to repeat.

---

## The Core Architectural Principle

The model may propose an action. The policy layer authorizes it.

```
Agent proposes action
        ↓
Check agent identity and registered owner
        ↓
Check delegated authority and impersonation scope
        ↓
Check resource sensitivity and data classification
        ↓
Check autonomy tier and action threshold
        ↓
Allow / Deny / Human Approval Required
        ↓
Tamper-evident audit event logged (SHA-256 hash chain)
```

No agent determines its own permissions. No action above its autonomy tier
executes without an external decision. Every decision — including denials —
is recorded.

---

## Five Assumptions Traditional IAM Did Not Need to Make

| Assumption | Traditional IAM | AI Agents |
|---|---|---|
| Identity | Human, service account, or deterministic app | Non-human identity acting probabilistically, on behalf of a user, or independently |
| Authorization | Permission to access an API describes what the application does | A broadly authorized agent may dynamically decide when, why, and how often to call that API |
| Input | Data entering a workflow is data | A ticket, email, or retrieved document may contain instructions that change agent behavior |
| Audit | Logs show which identity invoked an action | Logs must also show what the agent was asked, what it retrieved, what it concluded, and which authority it used |
| Detection | Detect credential abuse, network anomalies, and unusual system behavior | Also detect unusual agent intentions, unexpected tool sequences, and behavioral changes after consuming new context |

---

## Who This Is For

- **IAM and security architects** designing controls for AI agent deployments
- **AI product and platform teams** building agents that touch enterprise systems
- **Risk, compliance, and data teams** assessing what agents can access and retain
- **Enterprise leaders** deciding how much autonomy to permit and under what conditions

---

## Related Frameworks

- OWASP Top 10 for Agentic Applications (2026)
- MITRE ATLAS — Adversarial Threat Landscape for AI Systems
- NIST AI Risk Management Framework (AI RMF 1.0)
- NIST Zero Trust Architecture (SP 800-207)
- NIST Cloud-Native Zero Trust for IAM

---

---

## Implementation Note

The architecture diagrams use generic capability labels (Identity Provider,
Identity Governance and Administration, Provisioning and Lifecycle Management,
etc.) to represent the platform layer rather than naming specific products.

In practice, this layer can be implemented with enterprise IAM platforms such
as Ping Identity / PingIDM, SailPoint, Microsoft Entra ID Governance, or
Okta Identity Governance. The agent identity and policy controls described in
this blueprint apply regardless of which platform is in use — the architectural
requirements do not change with the vendor choice.

---

*This blueprint was developed to accompany the article:*
*"AI Did Not Replace IAM. It Broke Its Assumptions."*
