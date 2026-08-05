# Trust Boundaries

## The Old Boundary

Enterprise security architecture has historically been organized around a network perimeter. Systems inside the perimeter were trusted. Systems outside it were not. As enterprises moved to cloud, this boundary became harder to define, and the industry response — zero trust — moved the enforcement point from the network edge to individual resource access.

Zero trust improved the architecture significantly. But it was designed around a specific actor model: a human user, with an authenticated identity, requesting access to a specific resource from a specific device.

AI agents do not fit this model.

---

## Why Cloud vs. On-Premises Is Not the Relevant Boundary

An AI agent is not contained by network topology. By design, it may access:

- a knowledge base hosted on a cloud SaaS platform
- an identity store on a private network
- a ticketing system behind a corporate VPN
- an API exposed publicly

All of these may occur within a single agentic workflow. The agent crosses deployment boundaries as a normal operating condition, not as an exception.

If the trust boundary is defined by where a system lives — cloud or on-premises — then the agent's cross-environment behavior falls outside any defined perimeter. There is no perimeter that cleanly contains a multi-step agent operating across cloud and on-premises resources simultaneously.

The question "is this system in the cloud or on-premises?" cannot determine whether an agent action is permitted.

---

## What the Trust Boundary Actually Is

For AI agents, the trust boundary is defined by three things:

**Identity.** Does this agent have a registered, verified, non-anonymous identity? Is that identity associated with a specific purpose, a named owner, and an approved scope?

**Policy.** Does an external enforcement layer evaluate every proposed action before execution? Is that layer loaded from versioned, auditable configuration? Does it fail closed if its configuration is missing or malformed?

**Enforced authority.** Does the agent's actual permission to act on a resource derive from a policy decision, not from the credentials it was given at startup? Is the authority scoped to the minimum needed for the current task, with an expiry?

These three properties travel with the agent across deployment boundaries. A cloud resource accessed by an agent with a verified identity, evaluated against an external policy, using scoped credentials — is more secure than an on-premises resource accessed by an agent with broad static credentials and no policy enforcement.

The deployment environment does not determine the trust level. The identity, policy, and enforced authority do.

---

## What This Means Architecturally

Traditional IAM designs a trust boundary that maps to infrastructure topology: this network is trusted, that network is not; this VPN grants internal access, that endpoint does not.

AI agent security requires a trust boundary that maps to decision authority: this agent has been granted permission to propose this action against this resource, under this delegation, at this point in time — and that permission was granted by an external policy enforcement point, not derived from static credential scope.

The enforcement point is not a network gateway. It is a policy evaluation engine that sits between the agent's reasoning and the resources it wants to reach. It does not matter whether the resource is in a cloud environment or on-premises. What matters is whether the policy enforcement point was consulted before the action executed.

Three consequences follow from this:

**Consequence 1: Credentials alone are not the boundary.** An agent with broad, long-lived credentials can reach many resources. But reaching a resource is not the same as being authorized to act on it. The authorization decision must be made at action time by the policy layer, not at credential issuance time.

**Consequence 2: Short-lived, scoped credentials narrow the blast radius.** When an agent operates with credentials that expire, and those credentials are scoped to the minimum required for the current task, the damage from a compromised agent is bounded. The credentials cannot be reused after expiry. They cannot be used for actions outside their defined scope.

**Consequence 3: The policy enforcement point must be external to the agent.** If the agent itself enforces its own permissions, a compromised or manipulated agent can choose not to enforce them. The enforcement must happen in a layer the agent cannot influence — outside its reasoning, loaded from configuration it does not control.

---

## The Boundary Statement

Cloud versus on-premises is not the trust boundary for AI agents.

The trust boundary is identity, policy, and enforced authority — applied consistently across every environment the agent operates in, evaluated at every action the agent proposes, and maintained in configuration that the agent cannot modify.

An agent that crosses this boundary has already been denied, suspended, or escalated to human review before the harmful action reached the resource.
