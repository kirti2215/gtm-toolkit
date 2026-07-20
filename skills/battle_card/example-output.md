# Competitive Battle Card — Example Output

> Generated from the fictionalized scenario in `example-input.md`. All company names, product names, claims, and figures are illustrative only.

---

## Competitive Motion Diagnosis

**Motion type:** Developer preference  
**Confidence:** High

**Rationale:**  
The engineering team recommended FlexData based on prior experience, familiarity with its query model, and a preference for its developer workflow. Broader evaluation criteria have not yet been established by the economic buyer.

The competitor’s current advantage is rooted primarily in familiarity, developer preference, and early-stage workflow fit—not yet in a demonstrated technical advantage for the full production use case.

---

## Deal Strategy

Do not open with a product comparison.

The engineering team’s preference is real and should be acknowledged. Dismissing it would reduce credibility with the technical evaluators.

The strategy is to broaden the evaluation before the architecture decision is finalized:

From:

> Which database do developers prefer?

To:

> Which platform best supports the organization’s development, reliability, compliance, and operating requirements over time?

The CFO and Head of Infrastructure have not yet defined the evaluation criteria. That creates an opportunity to ensure operational risk, compliance readiness, reliability, and long-term cost are included before the decision is locked.

**Primary objective:**  
Expand the evaluation criteria beyond developer experience before the architecture decision is finalized.

**Secondary objective:**  
Give the engineering team a credible, evidence-based path to reconsider or qualify its recommendation without undermining its expertise.

---

## Winnability Assessment

**Current standing:**  
Disadvantaged. Engineering momentum currently favors FlexData.

**Potential:**  
Winnable. The economic buyer has not yet weighed in, and the regulated nature of the workload introduces evaluation criteria beyond developer experience.

**Key condition:**  
The team must broaden the evaluation criteria before the engineering recommendation becomes the default organizational decision.

---

## Buyer & Stakeholder Map

### VP of Engineering

- **Role:** Primary decision-maker
- **Current position:** Leaning toward FlexData
- **Likely priorities:** Development speed, team productivity, architecture flexibility, delivery timelines
- **Recommended approach:** Acknowledge the development advantages and introduce the broader production and operating criteria the decision must satisfy

### Senior Engineers

- **Role:** Technical evaluators
- **Current position:** Strong FlexData preference
- **Likely priorities:** Developer experience, schema flexibility, familiarity, speed of iteration
- **Recommended approach:** Do not challenge their experience directly. Ask how the preferred architecture will satisfy production reliability, auditability, and operating requirements

### CFO / Head of Infrastructure

- **Role:** Economic and operational stakeholders
- **Current position:** Unknown
- **Likely priorities:** Cost, operational risk, reliability, compliance, long-term maintainability
- **Recommended approach:** Introduce a structured evaluation of operational risk, compliance requirements, and three-year cost

### Internal Champion

None identified.

**Priority:**  
Identify a stakeholder who is accountable for reliability, compliance, infrastructure operations, or audit readiness.

### Potential Detractors

The engineering team may resist a change that appears to discount its technical judgment or slow development.

---

## Honest Competitive Positioning

### Where EnterpriseDB Pro may win

Subject to verification:

- ACID transactions and strong consistency guarantees
- Capabilities relevant to transaction integrity and auditability
- Reliability features designed for production workloads
- Support for structured governance and operational controls
- Stronger alignment with use cases where consistency and transaction integrity are heavily weighted

### Where FlexData genuinely wins

- Flexible schema during early-stage development
- Faster initial iteration for teams familiar with the platform
- Strong existing developer familiarity
- Lower perceived development friction

### How to frame the tradeoff honestly

FlexData may provide a better experience for rapid early-stage iteration.

EnterpriseDB Pro may be a stronger fit when the evaluation places greater weight on transaction integrity, operational controls, auditability, and long-term production requirements.

The decision should not be framed as development speed versus compliance. It should be framed as a full-lifecycle architecture decision that includes both.

---

## Objection Handling

### “Our engineers prefer FlexData. They have used it before.”

**Recommended response:**

> That makes sense. Their experience is valuable, and familiarity can materially improve development speed. I would also want to understand how the broader team is evaluating production reliability, auditability, and operational ownership. Has the infrastructure or compliance team defined the requirements the platform will need to satisfy after launch?

---

### “We need schema flexibility because we are still iterating.”

**Recommended response:**

> Understood. Which parts of the data model are still changing, and which transaction records will eventually require stronger controls or auditability? It may be useful to separate where flexibility is essential from where consistency and governance will become more important over time.

Avoid implying that flexible schemas are inherently incompatible with compliance.

---

### “FlexData is cheaper upfront.”

**Recommended response:**

> I would not want to compare costs without understanding transaction volume, uptime requirements, operational staffing, and the compliance controls each option would require. Could we build a three-year cost model using the same workload assumptions for both platforms?

Do not make a counterclaim without a customer-specific workload model.

---

## Landmine Discovery Questions

- What happens operationally and commercially if a transaction misses its required service level?
- When do you expect the platform to enter PCI scope, and who owns that requirement?
- What uptime or recovery commitments will you make to customers?
- Has the infrastructure, security, or compliance team participated in the architecture decision?
- What auditability and data-lineage requirements will apply to transaction records?
- What is the incident-response model for a production database failure during peak transaction volume?
- Which evaluation criteria are mandatory for launch, and which become important as the platform scales?

---

## Do Not Say This

### “FlexData cannot handle payments workloads.”

Unsupported and likely false. The competitor may be capable of supporting the workload with an appropriate architecture.

### “We are cheaper.”

Do not make a cost claim without a customer-specific workload and operating model.

### “FlexData has security vulnerabilities.”

Do not make security allegations without current, verified, and relevant public evidence.

### “Most payments companies use us.”

Do not make market-share or customer-adoption claims without verified evidence and appropriate customer-reference approval.

### Anything that implies the engineering team made a poor decision

The goal is to broaden the evaluation, not embarrass the technical evaluators. They need a credible reason to update their recommendation as new criteria emerge.

---

## Stage-Specific Next Action

### This week

Request a discussion with the Head of Infrastructure, compliance owner, or economic buyer.

Frame the meeting as an architecture-risk and operating-requirements discussion, not as a product demo.

The goal is to establish the full evaluation criteria before the engineering recommendation is formalized.

### Suggested opening question

> Before we compare products, could you walk me through the operational, customer, and compliance impact if a transaction misses its required service level? I ask because that will help us understand which architecture criteria should carry the most weight.

### If access to the economic buyer is not available

Ask the VP of Engineering:

> Have the infrastructure, security, or compliance teams defined the production requirements for this decision? I want to make sure the evaluation includes the requirements the platform will need to satisfy after launch, not only during development.

---

## Evidence Standards

| Claim | Evidence label | Current status |
|---|---|---|
| EnterpriseDB Pro supports ACID transactions and strong consistency guarantees | Verified | Confirm against official product documentation |
| EnterpriseDB Pro meets the required latency target | Unverified | Requires benchmark evidence under a comparable workload |
| FlexData provides a better developer experience for this team | Customer-reported | Based on engineering-team feedback |
| FlexData is cheaper upfront | Assumption | Requires a customer-specific cost model |
| EnterpriseDB Pro supports relevant auditability and compliance controls | Partially verified | Confirm against official documentation and the proposed deployment architecture |
| FlexData has stronger schema flexibility | Verified / customer-reported | Confirm against official documentation and team experience |

All claims must be checked against current sources before external use.
