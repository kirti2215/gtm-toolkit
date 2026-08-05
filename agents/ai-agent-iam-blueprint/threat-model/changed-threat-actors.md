# Changed Threat Actors

The introduction of AI agents into enterprise systems changes cybersecurity from both directions simultaneously. The attacker is different. The trusted actor is different. Neither observation alone captures the problem.

---

## The External Actor: AI-Enhanced Attackers

Traditional external threats followed predictable patterns. Reconnaissance was manual and time-consuming. Credential exploitation required targeting known vulnerability types. Multi-step attacks demanded coordination between specialized tools and human operators.

AI-enabled attackers change each of these assumptions.

**Faster reconnaissance.** An attacker using AI tooling can analyze infrastructure configurations, API documentation, and code repositories at a speed and scale that human operators cannot match. What once took days of manual review takes hours.

**Code and configuration analysis.** AI can interpret configuration files, identify misconfigured access policies, and surface exploitable logic flows in application code. Vulnerabilities that would be difficult to find manually become discoverable at scale.

**Credential and vulnerability exploitation.** AI tooling can identify credentials exposed in repositories, logs, or metadata, and correlate them against known system configurations. It can generate tailored exploitation attempts that adapt to observed access control patterns.

**Adaptive multi-step attacks.** A traditional bot follows a decision tree. An AI-assisted attacker can receive the output of one step, reason about the next, and choose a new path based on what it observes. This adaptive quality makes traditional signature-based detection less effective.

The enterprise defensive posture must therefore assume that the speed and adaptability of the attacker has materially increased.

---

## The Internal Actor: The Adaptive AI Agent

Historically, internal non-human actors fell into two categories: service accounts with deterministic behavior, and explicitly coded integrations that called specific APIs in predictable sequences.

An AI agent is neither.

An AI agent can:

- receive a goal expressed in natural language
- retrieve information from external sources, documents, emails, or APIs
- reason about which tools to use
- execute actions across multiple enterprise systems
- observe the results and adjust its next step

A service account or deterministic integration cannot do any of these things. It cannot read a document and change its behavior based on what it contains. An agent can.

This creates a new class of internal actor with the following properties:

**Goal-directed.** The agent is given an objective, not a script. It determines the path to that objective dynamically.

**Context-sensitive.** The agent's behavior changes based on what it retrieves. A different document, ticket, or knowledge base entry may produce different tool calls.

**Multi-step.** The agent may invoke many tools in sequence, with each step informed by the output of the previous one.

**Bounded by identity and authority — or not.** In an uncontrolled deployment, the agent inherits whatever credentials it was given and acts within whatever scope those credentials permit. There is no internal stopping point unless one was designed.

---

## The Critical Difference from Prior Bots

Earlier automation bots could also be compromised. A misconfigured integration could be abused. A service account with excessive permissions could be exploited.

A deterministic integration normally follows a fixed script. If its service identity is compromised, an attacker may abuse any permissions attached to that identity. But the scope of the damage is bounded by what that identity was permitted to do.

An agent under influence can reason toward a different objective:

```
Receive a manipulated input or objective
           ↓
Choose one legitimate, approved tool
           ↓
Observe the outcome
           ↓
Select another legitimate, approved tool
           ↓
Continue adapting toward the corrupted objective
```

Every individual tool call may appear permitted. The sequence as a whole serves the attacker's goal. This is what makes the agent threat categorically different: it is not a matter of blocking a specific action. It is a matter of detecting a pattern of individually legitimate actions that collectively form an attack.

---

## The Implication for Security Architecture

The stopping point cannot live inside the agent's reasoning. If the agent's reasoning has been influenced, that reasoning cannot be trusted to constrain itself.

The stopping point must be external: a policy enforcement layer that evaluates every proposed action against the agent's registered identity, approved scope, delegation authority, and behavioral thresholds — before execution.

This is why the five broken IAM assumptions matter:

| Assumption | Traditional IAM | AI Agents |
|---|---|---|
| Identity | Human, service account, or deterministic app | Non-human identity acting probabilistically or on behalf of a user |
| Authorization | Permission to access an API describes what the system does | A broadly authorized agent may dynamically decide when, why, and how often to call that API |
| Input | Data entering a workflow is data | A ticket, email, or retrieved document may contain instructions that change agent behavior |
| Audit | Logs show which identity invoked an action | Logs must show what the agent was asked, what it retrieved, what it concluded, and which authority it used |
| Detection | Detect credential abuse, network anomalies, and unusual system behavior | Also detect unusual agent intentions, unexpected tool sequences, and behavioral changes after consuming new context |

Defending against both changed actors requires the same foundation: verified identity, scoped authority, enforced policy, and full observability across every agent action.
