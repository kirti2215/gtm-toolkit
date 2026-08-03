# Win/Loss Pattern Loop

## What This Loop Does

Most win/loss analysis is a point-in-time exercise: pull the data, find patterns,
write a summary, share it once. The patterns sit in a document. The next quarter's
losses don't update them. A new exit interview doesn't get incorporated.

This Loop treats win/loss patterns as a living model — updated as new deals close,
calibrated by interview evidence, and used to drive specific downstream interventions.
The difference between a Win/Loss Skill and a Win/Loss Loop is not just persistence.
A Skill produces an analysis when given data. A Loop maintains a hypothesis across
deals, tracks what it predicted and what actually happened, and decides when a pattern
has enough evidence to drive action — versus when it needs more evidence before it
can be trusted.

This Loop is designed for PMM, GTM strategy, RevOps, and sales leadership. It is
not a rep-facing tool. It operates on closed deals to understand what is systematically
driving outcomes — not on open deals to determine what to do next in a live quarter.
For open deal risk, use the Pipeline Risk Loop. Confirmed Win/Loss patterns may later
calibrate the risk taxonomy and confidence thresholds in that Loop, but the two
systems operate independently.

---

## The Five-Level Learning Chain

The Loop operates through five sequential levels. A pattern cannot move directly
from observation to strategy. Each level requires specific evidence before the next
becomes accessible.

**Level 1 — Outcome**
What happened? A deal closed won, lost, or without a decision. This is the event.
It has no explanatory power on its own.

**Level 2 — Association**
What variables co-occur disproportionately with this outcome across multiple deals?
Champion title. Competitor presence. Deal source. Stage at entry. Economic buyer
engagement. This is correlation. Association tells the Loop where to investigate,
not what to do.

**Level 3 — Mechanism hypothesis**
What pathway may connect the observed variable to the outcome? Why would IT Director
champions be associated with losses? Not simply "because they are" — through what
process? A stated and testable mechanism is required before a pattern can influence
strategy. Without a stated mechanism, the pattern may still reach High Prevalence
confidence as an association, but it cannot generate a strategy-changing artifact
or move to Mechanism Supported.

**Level 4 — Counterfactual evidence**
What would have needed to be different for the outcome plausibly to change? Exit
interview counterfactual responses are the closest available evidence to causal
reasoning in a GTM context. They are buyer-reported claims, not experimentally
established facts. They strengthen Mechanism confidence when corroborated. They do
not prove causation.

**Level 5 — Intervention evaluation**
When the suspected mechanism is addressed, how does the treated cohort perform
relative to a credible comparison? A pre/post improvement in the treated cohort
alone produces a Directional signal, not a validated effect. A same-period matched
comparison cohort is required for Matched Evidence.

---

Correlation identifies the pattern cohort. Mechanism explains what may be happening.
Counterfactual evidence strengthens the mechanism hypothesis. Intervention evaluation
determines whether changing the mechanism changes outcomes. The Loop's job is to be
honest about which level a pattern has reached.

---

## The Pattern State Model

Each active pattern has two independent fields: **Pattern Maturity** and
**Operational Status**. These fields are not mutually exclusive. A pattern can be
Mechanism Supported, Active, and Escalated simultaneously.

### Pattern Maturity

Maturity tracks where the pattern stands in the five-level learning chain.

| Maturity | Meaning |
|---|---|
| Association observed | Variable co-occurs with outcome across multiple eligible deals. No mechanism stated. Pattern is logged and monitored. |
| Mechanism supported | Causal chain stated in two-statement format. Alternative mechanisms evaluated. Proxy variable check complete. Tier 1–3 evidence supports the proposed pathway. |
| Intervention testing | Intervention deployed. Full evaluation design recorded. Treated cohort, comparison cohort, observation window, and minimum deal threshold are all defined. Observation in progress. |
| Monitoring result | Observation window complete or minimum threshold reached. Intervention confidence is Directional or above. Pattern continues under monitoring for recurrence or drift. Not yet Validated. |
| Validated | Intervention confidence is Matched Evidence or Controlled Evidence; or Replicated directional evidence across independent cohorts with major alternative explanations evaluated and stated limitations recorded. Validation is operational — it records that the intervention performed as hypothesized under the tested conditions. It does not imply causal proof or generalizability beyond the validated cohort, period, and context. |

**On Validated:** Record at validation: validated cohort, tested period, intervention
version, evidence class, known scope boundaries, next drift-review date. An
intervention validated in enterprise North American financial services may not
generalize to SMB, another region, another competitor, partner-sourced deals, or a
different sales motion. State the boundaries explicitly.

### Operational Status

Operational status tracks what is currently happening to the pattern. Applied
independently of maturity.

| Status | Meaning |
|---|---|
| Active | Evidence accumulating. Pattern is being tracked. Applied at any maturity level. |
| Contradicted | Evidence-weighted contradictions materially weaken the observed outcome differential or directly challenge the proposed mechanism. Artifact held. Evidence gathering resumes. |
| Retired | Pattern has not recurred across the configured minimum eligible deals and one complete sales cycle. Preserved in historical log. |
| Escalated | Pattern flagged for cross-functional decision outside Loop authority. Maturity state is preserved — Escalated is a flag, not a replacement for analytical maturity. |

---

## Pattern Type Taxonomy

Eleven pattern types the Loop monitors across deals. A single deal may exhibit
multiple types — name both when they are genuinely linked.

**Type 1 — Qualification pattern**
Win rate is low not because of execution but because deals that should not enter the
pipeline are entering it. Signals: loss reasons cluster around fit, early-stage churn,
or ICP attributes consistently absent in lost deals and present in won deals.

**Type 2 — Champion profile pattern**
Deals won and lost by the same rep, same product, same segment — but with different
internal champions. The pattern is in who drives the decision, not how the sale is
run. Signals: champion title, seniority, or department correlates with outcome across
multiple deals.

**Type 3 — Value pattern**
Specific use cases, outcomes, or value propositions land or fall flat. Win when the
conversation centers on use case A; lose when it centers on use case B. Signals:
recurring themes in call transcripts and exit interviews that correlate with outcome,
not with rep or segment.

**Type 4 — Competitive pattern**
Win rate shifts when a specific competitor is in the deal. The sub-pattern is
critical: is this a feature evaluation, a pricing comparison, an incumbent
relationship, or a timing/entry dynamic? Each requires a different intervention.
Do not generate a competitive artifact until the sub-pattern is confirmed.

**Type 5 — Process / stall pattern**
Deals stall or die at a specific stage not because of the product or pitch but
because of what happens between stage transitions. Signals: average days in stage,
stage regression, consistent deal age at close or loss.

**Type 6 — Commercial pattern**
Pricing, packaging, or contract structure causes losses. Can be triggered by a
pricing change, a new competitor offer, or a market expectation shift. Signals:
loss reasons citing price, deals where discounting was requested and then lost.

**Type 7 — Timing / entry pattern**
Win rate shifts based on when in the customer's buying cycle the team engages.
Winning when first in the door; losing when entering after another vendor has already
framed the decision. Signals: deal source, time between first contact and evaluation
start.

**Type 8 — Stakeholder breadth pattern**
Single-threaded deals behave differently from multi-stakeholder deals. Loss rate
correlates with number of contacts engaged or with whether the economic buyer was
ever directly reached. Signals: contacts added per deal, economic buyer identified
in CRM, executive engagement history.

**Type 9 — Segment / vertical pattern**
Win rate, deal velocity, or deal size differs systematically by segment, vertical, or
geography in a way not explained by rep, product, or competitive factors. Signals:
vertical clustering in win/loss rates across multiple reps and quarters.

**Type 10 — Product / capability pattern**
The product cannot currently meet a required capability, integration, security, or
regulatory condition that a subset of buyers requires. This is distinct from a Value
pattern: the product can solve the problem in a Value pattern; in this pattern, it
cannot. Signals: loss reasons citing a specific feature, compliance standard, or
integration requirement; exit interviews confirming the gap was disqualifying rather
than persuadable.

**Type 11 — Sales execution / coverage pattern**
Outcome differences persist by rep, team, or territory after controlling for segment,
deal source, deal size, champion profile, and competitor mix. This type should only
be classified when confounders have been tested and ruled out. A rep whose outbound
win rate matches the team average is not underperforming — they are working a harder
deal source. Signals: consistent outcome differences that survive controlled comparison
across multiple deal dimensions.

**Note on Types 2 and 8:** Champion profile and stakeholder breadth are related but
distinct. Champion profile is about who the primary champion is. Stakeholder breadth
is about whether the deal is single-threaded and whether an economic buyer was ever
directly engaged. Many deals exhibit both — label as "Types 2 + 8" when both
dimensions are present in the evidence.

---

## Evidence Hierarchy

The Loop weights evidence by tier. Confidence cannot exceed what the evidence
supports. Contradictions between tiers are flagged explicitly — never silently resolved.

**Tier 1 — Direct customer statement**
Exit interview, direct buyer feedback after decision. One Tier 1 interview can move
Mechanism confidence significantly and can reframe the pattern type entirely. Tier 1
evidence elevates Mechanism confidence. It does not by itself establish Prevalence
confidence — that requires denominators and comparison rates, not interview count.

**Tier 2 — Observed buyer behavior**
Call transcripts, response timing, meeting attendance, email patterns, product usage
data. Observed during the deal, not retrospective. Avoids post-hoc rationalization
but requires interpretation.

**Tier 3 — Multi-source corroboration**
The same signal appearing across rep notes, CRM data, and field intelligence
simultaneously. Three or more deals with corroborating signals from multiple internal
sources reach Medium confidence and justify hypothesis formation.

**Tier 4 — CRM field data**
Stage history, close dates, deal value, contacts, forecast category, loss reason
codes. Useful for volume patterns. Filtered through rep interpretation and CRM
hygiene.

**Tier 5 — Rep notes and post-mortems**
Rep's account of what happened. High recency when captured immediately post-deal,
but subject to self-serving interpretation. Sufficient as corroborating signal; not
sufficient as primary evidence for patterns driving ICP changes or management actions.

**Tier 6 — Inferred from ratio alone**
Win rate X in segment Y, without explanation of cause. Hypothesis-generating only.
Not sufficient for artifact generation.

---

## Three-Part Confidence Architecture

Three separate confidence dimensions track different questions. Do not collapse them
into a single score — they require different evidence and produce different decisions.

### Mechanism Confidence

How certain are we about why a particular deal or type of deal produced this outcome?

| Level | Meaning |
|---|---|
| High | Tier 1–2 evidence directly explains the pathway. Causal chain stated in two-statement format. Proxy variables evaluated. Alternative mechanisms considered and distinguished. |
| Medium | Plausible pathway. Tier 3–4 evidence. Causal chain stated but not directly confirmed by buyer. |
| Low | Pattern observed. Mechanism hypothesized but not supported by evidence beyond the association itself. |

Mechanism confidence caps at Medium if the causal chain cannot be written in the
required two-statement format.

### Prevalence Confidence

How certain are we that this mechanism explains a material share of outcomes across
the broader deal set?

| Level | Evidence basis | Action |
|---|---|---|
| Insufficient | Fewer than 3 confirming deals; no denominator or comparison rate established | Log. Monitor. No artifact. |
| Low | 1–2 confirming deals; no comparison cohort; differential direction positive but magnitude unclear | Track. Name hypothesis. Do not act. |
| Medium | 3+ confirming deals; positive outcome differential vs. a stated comparison group; pattern appears across at least 2 deals from different reps or periods | Flag. Plan evidence acquisition. Consider diagnostic actions only. |
| High | Sufficiently sized exposed cohort shows a meaningful and persistent outcome differential relative to a relevant comparison cohort; low evidence-weighted contradiction rate | Generate artifact. Specify type, segment, routing, approver. |
| Contradicted | Evidence-weighted contradictions materially weaken the differential or directly challenge the proposed mechanism | Reclassify. Hold artifact. Return to evidence gathering. |

**Critical rule:** Tier 1–2 interviews elevate Mechanism confidence. They do not
establish Prevalence confidence. Two exit interviews confirm a repeated pathway —
they do not establish how broadly that pathway operates across the deal set. Prevalence
requires denominators, comparison rates, and outcome differentials.

### Intervention Confidence

How validated is the recommended intervention?

**Primary evidence class:**

| Class | Basis |
|---|---|
| Untested | Intervention recommended or deployed; no eligible cohort has matured; or observation threshold not yet reached |
| Directional | Treated cohort moved in expected direction vs. its own pre-intervention baseline; no same-period comparison cohort |
| Matched Evidence | Treated cohort outperformed a same-period matched cohort after controlling for observable pre-treatment differences |
| Controlled Evidence | Randomized holdout, staggered rollout, or credible quasi-experimental comparison |

**Replication status** (independent flag):
None / Partial (2 independent cohorts) / Replicated (3+ independent cohorts, periods,
territories, or segments)

**Combined descriptions:** "Directional — replicated across two periods."
"Matched Evidence — single cohort." "Controlled Evidence — replicated."
Replication of Directional evidence is not automatically stronger than a single
credible controlled comparison.

**Observation threshold rule:** Confidence is not upgraded until the predefined
observation window or minimum deal threshold is reached, except when ethical,
commercial, or operational risk requires early escalation. Partial results before
the threshold are labeled "early descriptive result" and do not trigger a confidence
upgrade.

---

## Causal Chain and Proxy Variable Requirements

Before a pattern moves from Association observed to Mechanism supported, two
statements are required.

**Required association statement** (factual):
> "In [defined cohort, defined period], [variable] is associated with [outcome] at
> [rate X%] compared to [rate Y%] in [comparison group]."

**Required mechanism hypothesis** (explicitly hedged):
> "We hypothesize that [variable] may influence [outcome] through [proposed mechanism]."

Then before generating a strategy-changing artifact:
* List alternative mechanisms that could produce the same association
* Complete the proxy variable check: could the observed variable be a proxy for a
  different underlying variable? If yes, does the intervention address the underlying
  variable or the proxy?
* List confounders evaluated and findings
* Identify distinguishing evidence: what would tell us which mechanism is operating?
* Confirm the intervention targets the proposed mechanism, not merely the proxy

Mechanism confidence caps at Medium if the two-statement causal chain cannot be
written. A clearly stated and plausible pathway may reach High if Tier 1–2 evidence
directly supports it.

---

## Evidence Acquisition Planning

For every pattern at Medium Prevalence or Medium Mechanism confidence, the Loop
produces an evidence acquisition plan. Missing data should produce a prioritized
interview brief, not just a confidence limitation.

For each plan, specify:
* Which lost deals are the highest-value interview targets and why
* Which won deals provide the best comparison
* What mechanism question would most improve confidence
* What counterfactual question would test whether changing the mechanism might have
  changed the outcome
* Who should conduct the interview
* What result would confirm, contradict, or reframe the hypothesis

**Counterfactual framing in interviews:** Ask not only "why did you decide this way"
but "if [mechanism element] had been different, do you think the outcome might have
changed?" The first produces a post-hoc rationalization. The second produces a
buyer-reported counterfactual. Label responses correctly: "Buyer reported that
[X] would likely have changed the decision" — not "the deal would have been won if [X]."

---

## Intervention Evaluation Design

Before a pattern moves to Intervention testing maturity, record the full evaluation
design. Without this, the Loop cannot distinguish an intervention that improved
outcomes from one that appeared to succeed due to pipeline timing, market changes,
or concurrent business changes.

```
Intervention: [what changed]
Deployment date:
Eligibility criteria:

Assignment:
  Method: [all eligible / random subset / staggered rollout / other]

Exposure:
  Exposure status per deal: received / partially received / not received
  Fidelity: applied as designed / modified / unknown
  Adoption rate:

Treated cohort:
  Definition:
  N at deployment:
  Exclusions and attrition:

Comparison cohort:
  Type: [same-period matched / staggered control / historical / none — Directional only]
  Matching variables (pre-treatment only):
  Control-group contamination:

Baselines:
  Treated cohort prior-period win rate:
  Comparison cohort prior-period win rate:

Observation window:
  Start:
  Minimum deal count before interpretation:
  Planned end:

Metrics:
  Leading indicator:
  Final outcome metric:
  Unit of analysis:
  Analysis population: [intention-to-treat / actually treated / both]

Concurrent changes during window:
  [product / pricing / territory / competitive / sourcing — describe or none]

Confounders:
  Observable not controlled:
  Unobserved (acknowledged):

Current intervention confidence:
Evidence basis:
```

**Matching variable rule:** Match only on variables measured before treatment
assignment and not caused by the intervention. A variable that the intervention is
designed to change cannot be used to select the comparison group.

---

## Sequencing Principle

Resolve the mechanism before generating the artifact. Two patterns that look
identical at the surface level require completely different interventions once the
mechanism is understood.

For competitive patterns: confirm whether the motion is a feature evaluation, a
pricing comparison, or an incumbent relationship before generating any artifact.

For champion profile patterns: confirm the pattern holds across multiple reps and
territories before updating ICP criteria.

For rep performance patterns: control for territory composition and deal-source mix
before any performance or coaching recommendation.

Name the uncertainty explicitly. State what evidence would resolve it and who should
gather it.

---

## Prioritization

When multiple patterns are active, prioritize by revenue exposure, recency,
actionability, Mechanism confidence, and reversibility of the intervention. High-
consequence, low-reversibility interventions (ICP changes, SDR targeting changes,
rep performance actions) require more evidence than low-consequence, easily-revised
ones (a battle card, a discovery question set).

---

## Recommendation vs. Authority

The Loop identifies patterns and recommends interventions. It does not execute ICP
changes, sales play updates, product roadmap changes, or performance management
decisions.

For Type 11 (Sales execution / coverage), the Loop classifies the pattern after
confounders are tested and routes the finding jointly to RevOps, sales enablement,
and sales leadership. The same leader responsible for team performance should not
be the sole interpreter of evidence about their team.

When a recommended action requires management authority, name the evidence, name the
decision required, and name the appropriate approver.

---

## Default Routing Table

Customize to the company's operating model.

| Pattern | Insight owner | Decision owner | Intervention owner | Measurement | Approver |
|---|---|---|---|---|---|
| 1. Qualification | PMM / RevOps | VP Sales + VP Marketing | RevOps + SDR | RevOps | VP Sales + VP Marketing |
| 2. Champion profile | PMM / GTM | VP Sales | Sales enablement + SDR | RevOps | VP Sales |
| 3. Value | PMM | PMM + VP Sales | PMM | PMM + RevOps | VP Marketing + VP Sales |
| 4. Competitive | PMM | PMM + VP Sales | PMM (artifact); Sales (deploy) | Sales + RevOps | VP Sales + PMM |
| 5. Process / stall | RevOps | VP Sales | Sales enablement + RevOps | RevOps | VP Sales |
| 6. Commercial | RevOps + Finance | VP Sales + Finance | Finance + RevOps | Finance + RevOps | VP Sales + CFO |
| 7. Timing / entry | PMM + RevOps | Demand gen + SDR | SDR + PMM | RevOps | VP Marketing + VP Sales |
| 8. Stakeholder breadth | PMM / GTM | VP Sales | Sales enablement | RevOps | VP Sales |
| 9. Segment / vertical | PMM | CMO + VP Sales | PMM | RevOps | CMO + VP Sales |
| 10. Product / capability | PMM + RevOps | VP Product (roadmap); VP Sales (interim GTM policy) | Product + GTM | Product analytics + RevOps | VP Product + VP Sales |
| 11. Sales execution / coverage | RevOps + Enablement + Sales leadership (jointly) | VP Sales + HR | Sales enablement; coaching | Sales leadership | VP Sales + HR |

---

## Loop-Skill Relationship

The Win/Loss Pattern Loop decides when to invoke Skills and which Skills to invoke
based on pattern evidence. It does not invoke Skills speculatively.

When a Competitive pattern reaches High Prevalence confidence and the sub-pattern
is confirmed: invoke the Battle Card Skill with the specific competitor, motion, and
segment. When a Value pattern reaches High confidence: invoke the Messaging Alignment
Skill with the specific use case shift. When a Qualification pattern reaches High
confidence: invoke the ICP Definition Skill with the specific criteria changes.

---

## Exit Conditions

**Contradiction threshold:** Contradiction status is triggered when evidence-weighted
contradictions materially weaken the observed outcome differential or directly
challenge the proposed mechanism. Evaluate proportion, evidence tier, and whether
the contradiction challenges the association, the mechanism, or both. Do not apply
a fixed contradiction count across all patterns.

**Retirement threshold:** Retire after at least one complete sales cycle and a
configured minimum of newly eligible deals pass without recurrence. Default: five
eligible deals and one full sales cycle. Configure for deal velocity.

**Validated exit conditions:** Pattern Maturity reaches Validated only when
Intervention confidence is Matched Evidence, Controlled Evidence, or Replicated
Directional across independent cohorts with major alternative explanations evaluated.
Record: validated cohort, tested period, intervention version, evidence class, scope
boundaries, drift-review date. Validated does not imply universal causal proof.

**Escalated status:** Escalated is an Operational Status flag. It does not change
Pattern Maturity. A product-capability pattern can be Mechanism Supported and
Escalated simultaneously — the escalation does not pause the analytical work.
