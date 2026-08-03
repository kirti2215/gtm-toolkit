# Win/Loss Pattern Loop — Input Template

The Loop maintains a pattern model that updates continuously. Inputs fall into three
categories: (1) baseline context that establishes the operating scope, (2) the
initial deal set that seeds the first pattern model, and (3) ongoing evidence that
feeds each update cycle.

---

## Part 1 — Baseline Context (provide once at initialization)

**Segment scope**
Which segment(s) should this Loop monitor? (e.g., enterprise fintech, mid-market
logistics, growth-stage SaaS)

**Time window for pattern formation**
How many months of deal history should seed the initial model? Recommended: 6–12
months, minimum 3 months or 10 closed deals, whichever is larger.

**Win/loss ratio baseline**
What is the current overall win rate in the target segment? This becomes the
benchmark against which pattern-specific win rates are compared.

**Prior year or comparison baseline**
What was the win rate 12 months ago in the same segment, if known?

**Primary concern**
What pattern does leadership most want to understand? This does not constrain the
Loop — it will surface all patterns the evidence supports — but it sets the first
hypothesis to test. Examples:
* "Why are we losing competitive evaluations in the mid-market?"
* "Is there a champion profile difference between won and lost deals?"
* "Is there a stage or process step where deals are dying at a higher rate?"

**Artifact generation preferences**
Which artifact types should this Loop be authorized to generate recommendations for?
(All recommendations require human review and approval before deployment)
* [ ] ICP criteria update
* [ ] Competitive battle card
* [ ] Sales play / motion description
* [ ] Qualification criteria change
* [ ] Messaging update recommendation
* [ ] Product signal / gap report
* [ ] Leadership escalation brief

**Escalation contacts**
Who should receive escalation briefs? (Name, role — e.g., VP of Sales, Head of
Product, Regional GM)

**Observation thresholds**
What minimum deal count and time window should the Loop use before interpreting
intervention results? Default: 15 closed eligible deals or one complete sales cycle,
whichever is later. Adjust based on your deal velocity.

**Deal velocity**
Approximate average sales cycle length in this segment. Used for retirement
threshold calibration.

---

## Part 2 — Initial Deal Set (provide at initialization)

**Closed deal log**

For each closed deal in the time window:

| Field | What to include |
|---|---|
| Account name | Can be anonymized (e.g., "Fintech Co A") |
| Segment / vertical | e.g., enterprise fintech, mid-market logistics |
| Deal value | ARR or TCV |
| Stage at close / loss | Which stage the deal was in when it closed or was lost |
| Loss reason (CRM) | The coded reason, even if generic |
| Competitor(s) present | Any competitors who were actively evaluated |
| Champion title | Title and department of the primary champion |
| Economic buyer engaged | Yes / No / Unknown — and if yes, their title |
| Deal source | Inbound, outbound, partner, customer referral |
| Days in pipeline | Total days from open to close / loss |
| Outcome | Won / Lost / No decision |

**Exit interview data** (highest priority — include all available)

For any deal where an exit interview was conducted:
* What the buyer said was the primary reason for their decision
* Whether a competitor was chosen, and the stated reason
* Any secondary factors mentioned
* Interviewer confidence in the answer (did the buyer seem candid?)
* Any counterfactual responses: did the buyer indicate what would have changed
  their decision? Record verbatim if possible.
* Whether the stated reason matches or contradicts the CRM loss reason code

**Call transcript themes** (if available)

Key themes observed in discovery, demo, or late-stage calls for lost deals:
* Concerns raised repeatedly
* Objections that were not resolved
* Topics the buyer was most vs. least engaged on

**Rep notes / post-mortems** (if available)

Rep's account of what happened in lost deals. Flag if captured within 48 hours of
the loss (more reliable) vs. weeks later.

---

## Part 3 — Ongoing Deal Evidence (provide on each Loop update)

Each time a new deal closes, provide:

**New deal record**
* Account, segment, value, outcome
* Competitor(s) present
* Champion profile (title, department)
* Economic buyer engaged (yes/no/unknown)
* Loss reason or win driver
* Stage sequence (normal path or anomalies?)
* Deal source

**New interview data** (highest priority)
* Verbatim or paraphrased buyer statement on the decision
* Any counterfactual response from the buyer
* Whether the stated reason matches or contradicts the CRM loss reason

**Pattern match or contradiction**
* Does this deal appear to confirm an existing pattern hypothesis?
* Does it appear to contradict one?
* Is it ambiguous?

You do not need to answer these questions — the Loop will make its own assessment.
They are optional flags to speed up the update cycle.

---

## Part 4 — Prior or Active Interventions (if applicable)

If an intervention has already been deployed based on a prior analysis or earlier
Loop pass, provide the following. This allows the Loop to continue tracking the
intervention rather than starting the evaluation design from scratch.

**Intervention deployed:**

**Deployment date:**

**Eligibility criteria:** [what deals qualify for the treated cohort]

**Assignment method:** [all eligible / random subset / staggered rollout / other]

**Treated cohort as defined:** [segment, source, stage, time window]

**Comparison cohort (if any):** [type and definition; matching variables used]

**Pre-intervention baseline win rate (treated cohort segment, prior period):**

**Observation window defined:** [start date, minimum deal count, planned end]

**Leading indicator being tracked:**

**Closed-deal outcome metric:**

**Current status of observation window:**
* Eligible deals opened since deployment: [N]
* Eligible deals closed since deployment: [N of minimum required]
* Current treated cohort win rate (if any closed): [X%]
* Current comparison cohort win rate (if any closed): [Y%]
* Observation threshold reached: Yes / No
* Note: if below threshold, flag these as early descriptive results only

**Adoption / exposure data:** [% of eligible deals that received the intervention;
fidelity issues observed if any]

**Concurrent changes since deployment:** [product releases, pricing changes,
territory changes, competitive shifts, sourcing mix changes]

**Known implementation problems or fidelity issues:**

**Control-group contamination:** [did comparison deals receive parts of the
intervention?]

---

## Part 5 — Context and Confounders (include if relevant)

**Recent product or pricing changes**
Any changes in the last 6 months that could be a confounding variable — new feature
releases, pricing restructure, packaging changes, new SKUs.

**Market or competitive changes**
Competitor funding, new product launches, pricing moves, or market events that could
explain a pattern shift.

**Rep or territory changes**
Significant rep changes (attrition, new reps, territory reorganization) that could
confound pattern interpretation.

**Sourcing mix changes**
Changes in deal source mix (inbound vs. outbound vs. partner vs. referral) that could
shift win rate independent of the patterns being tested.

**Known data quality issues**
CRM hygiene problems, loss reason codes that are inconsistently applied, or time
periods where data is unreliable.

---

## Interview Guidance — Counterfactual Framing

When conducting exit interviews for deals that contribute to active patterns, use
the following structure. The counterfactual question is the most valuable — it asks
the buyer what would have needed to change, rather than just why they decided as they
did.

**Decision description question:**
"What were the key factors in your decision?"

**Mechanism question:**
"At what point in the process did the direction become clear to you?"
"What would it have taken for this to go differently?"

**Counterfactual question:**
"If [specific element] had been different — for example, if [mechanism component]
had been in place — do you think the outcome might have changed?"

**Authority question:**
"Who ultimately made the final decision, and what information were they weighing?"
"Were there stakeholders above your level who were part of the process?"

**Label buyer counterfactual responses correctly** when reporting to the Loop:
* Use: "Buyer reported that [X] would likely have changed the decision."
* Do not use: "The deal would have been won if [X] had been in place."

The first is a buyer claim. The second is an unsupported causal conclusion.

---

## What You Do Not Need to Provide

You do not need to identify patterns yourself. The Loop will form hypotheses from
the deal evidence.

You do not need to recommend the intervention. The Loop will recommend artifact
types when patterns reach confidence thresholds.

You do not need complete data for every field. The Loop will reflect confidence
limitations based on what evidence is missing and will specify which fields would
most improve pattern quality if provided.
