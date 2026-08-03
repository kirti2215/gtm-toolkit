# Win/Loss Pattern Loop — Before/After Evaluations

**Fictional scenario.** All companies, products, people, deal data, quotes, and outcomes in this file are fictional and created solely to demonstrate the Loop's analytical behavior. Any resemblance to real organizations, products, or individuals is unintentional.

**Methodology note:** These are illustrative behavioral evaluations designed to
demonstrate the effect of GTM judgment, persistent state, and feedback across passes.
They are not a controlled benchmark isolating each component independently. The
comparison demonstrates the combined value of better context, encoded GTM judgment,
pattern state continuity, feedback incorporation, and sequencing — not each component
measured separately.

**Purpose:** Show what changes when you move from a static win/loss prompt to a
feedback-driven Loop — and specifically, where in the Loop feedback enters and how
it shifts the output.

---

## Scenario 1 — The Wrong Intervention for the Right Observation

**Setup:** Enterprise SaaS company. 15 losses in enterprise financial services in
6 months, many to Luvexis. Sales leader runs a prompt-based analysis and gets a
recommendation. That recommendation is acted on. It doesn't work. A new deal closes
and an exit interview is conducted.

**The core question this scenario answers:** How does the Loop behave when the first
intervention was a plausible response to the pattern — but feedback reveals the
mechanism was misread?

---

### WITHOUT LOOP

**Prompt given:**
"We've lost 5 deals to Luvexis in enterprise financial services in the last 6 months.
What should we do?"

**Output received:**
"To improve win rates against Luvexis in financial services, consider the following:

1. Strengthen your competitive battle card for Luvexis. Focus on performance
   benchmarks, total cost of ownership, and data governance capabilities.

2. Prepare a financial services-specific value proposition that addresses regulatory
   compliance needs.

3. Train reps on Luvexis objection handling — common objections include query
   performance and pricing.

4. Consider producing a financial services customer case study to build credibility
   against Luvexis's brand recognition."

**What the team did:** Produced a Luvexis battle card and ran competitive training.
Cost: 3 weeks of sales enablement time.

**Result:** Win rate against Luvexis in the next quarter: 32% (down from the 38%
baseline). The data does not establish whether the battle card caused, contributed to,
or was unrelated to the decline — win rate volatility across 5 competitive deals is
high and other factors may have contributed. The observed win rate did not improve
following the intervention.

---

### WITH LOOP — PASS 1

**Inputs provided:** 24 closed deals, 4 exit interviews including Corvath Capital Wealth
Partners (interview: "The decision was made before the evaluation really started.
Luvexis was already in our environment."), competitive context on Luvexis's Q1
promotional campaign.

**Where the Loop enters the feedback cycle:** After observing 5 Luvexis losses and
reading the Corvath Capital interview, the Loop does not treat this as a standard competitive
loss. The exit interview creates a fork — is this a feature competition loss or an
incumbent displacement loss? The Loop does not proceed to generate a battle card
until it knows which one.

**Pass 1 output (Pattern 3 — Competitive Entry):**

"Five deals lost to Luvexis. CRM loss reasons coded as 'competitor better fit' and
'competitor better price.' However, Corvath Capital's exit interview contradicts the CRM
framing: 'Luvexis was already in our environment... the decision was made before
the evaluation really started.'

This is an incumbent displacement situation, not a head-to-head competitive evaluation.
Customers with Luvexis already in their environment are not choosing Luvexis over
us — they are finding a reason to stay with Luvexis rather than add a new vendor.
These are structurally different loss mechanisms requiring structurally different
responses.

A Luvexis battle card is the correct intervention for a head-to-head feature
competition. It is the wrong intervention for an incumbent scenario, because the
customer is not comparing features — they are comparing vendor consolidation versus
new vendor evaluation. Framing the conversation as feature vs. feature may reinforce
the wrong question.

**Pass 1 recommendation:** Before generating a battle card, conduct discovery on
the next three Luvexis-competitive deals specifically to answer: Is Luvexis
already in the customer's environment? Who is making the 'single vendor vs. best
of breed' decision — IT or the CFO? The answer determines whether the intervention
is competitive positioning or executive-level business case and timing.

**Mechanism Confidence: Medium. Prevalence Confidence: Low.** One Tier 1 interview
supports the incumbent hypothesis for the Corvath Capital deal. It cannot establish how
broadly the incumbent dynamic explains the other four Luvexis losses — no comparison
rate across the five Luvexis-competitive deals is yet available. Mechanism confidence
will reach High or redirect after 2–3 more interviews; prevalence will strengthen
with additional closed deals and a denominator."

**[FEEDBACK POINT 1 — LOOP UPDATE]**

Two weeks later: New Luvexis deal closes (loss). Exit interview conducted.
Telvane Asset Group: "IT had a recommendation and leadership went with it. I don't
think the business case we were making got much air time internally." Second deal
closes (also Luvexis loss). No interview, but rep notes: "The customer said they
were standardizing on Luvexis — this wasn't really an evaluation."

---

### WITH LOOP — PASS 2

**New evidence entering the Loop:**
- Second Tier 1 interview (Pinnacle): confirms incumbent dynamic — IT recommendation
  was never elevated to a business case comparison
- Rep note from third deal: customer using language of "standardization," not evaluation

**Where the Loop updates:** Mechanism Confidence on Pattern 3 moves from Medium to
High. Two interviews now confirm the same mechanism: the evaluation is nominal, not
comparative. Prevalence Confidence moves to Medium — two interviews and one rep note
out of five Luvexis losses. The Loop has enough evidence to specify the correct
intervention type and deploy it as a diagnostic pilot.

**Pass 2 output:**

"Pattern 3 updated — Mechanism Confidence: High. Prevalence Confidence: Medium.

Two Tier 1 exit interviews and one rep note now confirm the same mechanism: in deals
where Luvexis is already in the customer's environment, the evaluation is driven by
IT with a prior vendor preference. The business case is not reaching CFO or COO level,
where a 'best-of-breed vs. consolidation' question could be decided on ROI rather than
relationship.

The battle card correctly addresses what Luvexis does vs. what we do. It does not
address the question that is actually being asked, which is 'why would we add a new
vendor when Luvexis is already here?' That question is answered by a different
document (executive-level business case on multi-vendor risk vs. capability advantage)
and a different person (CFO or COO, not IT Director).

**Pilot intervention recommended — Luvexis Incumbent Displacement Play:**

Prevalence Confidence is Medium — the mechanism is well-evidenced across two interviews
but confirmed in 2 of 5 Luvexis-competitive losses only. Deploy the following as a
diagnostic pilot; evaluate win rate after 3+ closed deals before treating this as
confirmed standard strategy.

First, build an incumbent displacement discovery question set for reps to use in
first calls with FS accounts. Goal: identify whether Luvexis is already in the
environment before Stage 2. If yes, trigger a different path — not the standard
evaluation track.

Second, develop an executive-level business case document (not a battle card)
addressing: total cost of vendor consolidation vs. capability advantage, specific
use case performance differences in regulated data environments, and why single-vendor
for all data workloads may increase compliance risk in fintech specifically.

Third, the target reader for this material is CFO or COO, not IT Director. Rep should
not use this document in a conversation with IT — it will read as circumventing their
recommendation, not addressing their concern.

Do not generate a standard competitive battle card for this motion."

---

### DELTA — SCENARIO 1

| Dimension | Without Loop | Loop Pass 1 | Loop Pass 2 |
|---|---|---|---|
| Pattern identified | Competitive loss to Luvexis | Possible incumbent displacement, insufficient data to confirm | Mechanism Confidence: High; Prevalence Confidence: Medium. Pilot intervention recommended. |
| Intervention recommended | Battle card + competitive training | Hold — conduct discovery on next 3 deals first | Incumbent displacement play: discovery questions + executive business case |
| Target audience for artifact | Rep (battle card) | Not yet generated | CFO/COO (business case), not IT |
| Sequencing | Generate artifact immediately | Diagnostic action first | Artifact generated after confirmation |
| What feedback changed | n/a | Corvath Capital interview reframes from "competitive" to "possible incumbent" | Two interviews confirm mechanism; battle card explicitly contraindicated |
| Cost of wrong intervention | 3 weeks enablement, win rate drops | Avoided by Loop holding artifact | n/a |

**Where in the Loop feedback mattered most:** Pass 1 → Pass 2. The first interview
(Corvath Capital) created a hypothesis. The second and third data points confirmed it. The
Loop held the battle card through both passes — the mechanism was different enough
from standard competitive loss that acting early would have produced the wrong artifact.

---

## Scenario 2 — When the Pattern Is Qualification, Not Execution

**Setup:** Same enterprise fintech scenario. Team has been trying to improve demo
quality and sales training for two quarters. Win rate is still declining. A prompt-
based analysis is run and attributed to rep performance. Meanwhile, the Loop has
been tracking champion profile data.

**The core question this scenario answers:** How does the Loop distinguish between
a qualification problem and an execution problem when the symptom (losses) looks the
same from the outside?

---

### WITHOUT LOOP

**Prompt given:**
"Our enterprise win rate in financial services dropped from 47% to 38% in 12 months.
We've tried improving demos and training. What's going wrong?"

**Output received:**
"A 9-point win rate decline despite training and demo improvement suggests the issue
may be deeper than presentation quality. Possible explanations:

1. Rep performance variance — some reps may be underperforming significantly. Review
   individual win rates and consider additional coaching for the bottom half.

2. Competitive shifts — competitor products may have improved. Review competitive
   intel and update battle cards.

3. Market saturation — you may have already captured the easiest deals in this segment.

4. Messaging drift — your ICP and messaging may no longer align with buyer priorities.
   Consider a messaging refresh.

We recommend a rep scorecard and a messaging audit."

**What the team did:** Ran a rep scorecard review. Marcus L. (8 months in) was flagged
as underperforming and placed on an informal performance plan.

**What was missed:** The scorecard did not control for deal source (Marcus's territory
skews outbound, which has lower baseline win rates for all reps). And it missed the
pattern visible in the data: 12 of 15 losses involved IT Directors as the sole
champion — across all three reps, not just Marcus.

---

### WITH LOOP — PASS 1

**Inputs provided:** Full 24-deal data set with champion title, economic buyer
engagement flag, deal source, and per-rep win rates.

**Where the Loop enters the feedback cycle:** The Loop observes the rep performance
gap (Marcus at 27% vs. 44-46% for others) but tests the confound hypothesis before
drawing a conclusion. It then cross-references champion profile across all reps —
and finds the real signal.

**Pass 1 output:**

"Win rate analysis identifies two active patterns and one confound requiring
investigation before acting.

Pattern 1 (High confidence): Champion profile is the strongest predictor of outcome
in this deal set. 12 of 15 losses involved IT Director or IT Manager as sole champion,
with no economic buyer engagement. 8 of 9 wins involved VP Engineering, CTO, Head
of Data, or CDO, with CFO or CEO engaged. This pattern appears across all three reps
— it is not unique to Marcus L.

Before attributing win rate differences to rep performance, test this question:
Of Marcus's 7 losses, how many had IT Director as sole champion with no economic
buyer? If the answer is 6 or 7, his underperformance is likely a qualification and
territory issue, not a skills issue. He may be running the same playbook as Priya
and Tom — but against a harder deal profile in an outbound-sourced territory.

Preliminary recommendation: Update Stage 2 qualification criteria to require VP-level
technical champion before committing Stage 3 resources. This applies to all reps.

Hold the performance management action on Marcus until the territory/deal-source
confound is controlled."

**[FEEDBACK POINT 2 — LOOP UPDATE]**

Manager pulls the data: Marcus's 7 losses. 6 of 7 had IT Director as sole champion.
1 had VP Engineering but lost to a compliance gap (Pattern 2). Marcus's outbound
deals (5 of 7 losses) are sourced from a cold list that targets IT decision-makers,
not VP Engineering. The other two reps have partner and referral sources that
naturally surface VP-level contacts.

---

### WITH LOOP — PASS 2

**New evidence entering the Loop:**
- Champion profile confound confirmed: Marcus's losses follow the same pattern as
  the rest of the team
- Deal source root cause identified: outbound list is targeting IT Director titles,
  not VP Engineering
- No rep execution issue confirmed

**Where the Loop updates:** Pattern 1 (champion profile) strengthens. The proposed
root cause for Marcus's underperformance flips from rep execution to outbound targeting.
Performance management action is explicitly contraindicated by the evidence.

**Pass 2 output:**

"Pattern 1 update — Champion Profile (High confidence, mechanism supported after evaluating the deal-source confound).

Marcus L.'s 7 losses follow the same champion profile pattern as the other 8 losses:
IT Director as sole champion, no economic buyer engagement. His lower win rate vs.
Priya and Tom is explained by deal source: his outbound list targets IT Director
titles, while partner and referral sources surface VP Engineering and above.

The available evidence — Marcus's champion profile matching the team pattern, and
his outbound list targeting IT Director titles — supports a targeting and territory
explanation over an execution explanation. A controlled comparison (Marcus's outbound
win rate vs. peers on comparable outbound deals) would confirm this. Placing Marcus
on a performance plan before that comparison is made would apply a performance
conclusion to evidence that does not yet support it.

Updated recommendations:

1. Qualification criteria change: Add 'VP-level or above technical champion identified
   by end of Stage 2' as a gate for Stage 3 entry. This is a team-wide change,
   not rep-specific.

2. Outbound list targeting: Revise Marcus's outbound list to target VP Engineering,
   Head of Data, and CDO titles in FS accounts. IT Director outreach is not disqualified
   — but the goal of that outreach should be to identify and reach the VP-level
   champion, not to run the full evaluation with the IT Director as the buyer.

3. The Loop recommends that sales leadership review the decision to place Marcus on
   an informal performance plan. The deal-source confound — not yet controlled for
   through a direct outbound win rate comparison — is the stronger current explanation
   for the outcome differential. A performance management action applied before this
   comparison is made would not be supported by the current evidence. The final
   decision on the plan rests with sales leadership, not the Loop.

Artifact flagged: Qualification criteria change — ready to generate for all three reps
and for SDR targeting."

---

### DELTA — SCENARIO 2

| Dimension | Without Loop | Loop Pass 1 | Loop Pass 2 |
|---|---|---|---|
| Root cause identified | Rep underperformance (Marcus L.) | Champion profile pattern (all reps); Marcus's territory as possible confound | Mechanism supported: champion profile + outbound targeting; Marcus's performance explicable by territory |
| Action recommended | Rep scorecard; informal performance plan for Marcus | Hold performance action; test confound hypothesis | Loop recommends sales leadership review performance plan; update qualification criteria and outbound targeting for all reps |
| Level of intervention | Rep-level (individual) | Systemic hypothesis forming | Systemic (team-wide qualification gate + SDR targeting) |
| What feedback changed | n/a | Champion data cross-referenced with deal source — confound identified | Deal-source confound evaluated; mechanism supported — outbound list targets IT Director titles, explaining the outcome differential without requiring an execution explanation |
| Risk of wrong intervention | Misattributed loss, morale damage, possible rep attrition | Avoided | Avoided |

**Where in the Loop feedback mattered most:** Between Pass 1 and Pass 2. The Loop's
Pass 1 diagnostic — "test the territory confound before acting" — prevented a
performance management decision that would have been made on the wrong evidence.
The manager's data pull (feedback) confirmed the confound and redirected the
intervention from individual to systemic.

---

## Scenario 3 — When New Evidence Reorders the Entire Priority Stack

**Setup:** Same team, one quarter later. Two patterns from the previous output have
been addressed (champion profile qualification criteria updated, compliance gap
flagged to product). A new deal closes in a different way. It changes what the Loop
thinks is the most important thing to focus on.

**The core question this scenario answers:** How does the Loop update when a new
closed deal doesn't fit the existing pattern model — and what does it do when the
new evidence suggests the pattern was more nuanced than initially understood?

---

### WITHOUT LOOP

**Prompt given (quarterly review):**
"We updated our qualification criteria last quarter to require VP-level champions.
Three deals closed this quarter in enterprise fintech — two lost, one won. What
should we look at?"

**Output received:**
"Despite improved qualification criteria, continued losses may indicate:

1. The ICP update needs more time to show results — pipeline built under old criteria
   is still closing.

2. Competitive pressure has increased. Consider additional competitive readiness.

3. Some deals may have slipped through the new qualification gate.

Recommendation: Give the new criteria two more quarters to work. Track the cohort
of deals qualified under the new criteria separately."

---

### WITH LOOP — PASS 1

**New evidence entering the Loop this quarter:**
- 3 losses in the quarter
- 2 had VP Engineering as champion (new criteria met) — both lost to compliance gap
- 1 had VP Engineering but won — deal source: customer referral into CISO, not VP
  Engineering initially

**Where the Loop enters the feedback cycle:** The Loop has a champion profile pattern
and a compliance gap pattern already active. New deals stress-test both. Two of three
losses confirm Pattern 2 (compliance gap). The one win surprises the Loop — it came
through a CISO relationship, not through a VP Engineering champion.

**Pass 1 output:**

"Pattern update: 3 new closed deals.

Pattern 1 (Champion profile): Two VP Engineering champions — but both lost. Reason
in both cases: compliance gap (Pattern 2). The qualification criteria update was
applied, but it cannot fix deals where the compliance feature is still missing.
Pattern 1 confidence holds at High; it is not contradicted. These losses are
attributable to Pattern 2, not Pattern 1 reverting.

Pattern 2 (Compliance gap): Confirmed again in both losses. Combined loss attribution
now 5 deals, $1.9M over two quarters. This escalation brief should now be treated
as urgent — the pattern is accelerating, not plateauing.

New observation — win via CISO entry: This quarter's win came through a CISO
relationship, not a VP Engineering champion. The CISO sponsor elevated the deal to
CFO within 3 weeks and drove procurement. This does not contradict Pattern 1 —
but it nuances it. The qualification criterion may need to be broader: 'VP Engineering
or equivalent decision-influencing stakeholder with C-suite access.' CISO in a
regulated FS environment has that authority.

**Recommended action:** Update the compliance escalation brief to Diane R. and
Darren W. — 5 deals, $1.9M attributed, pattern accelerating. This is no longer a
'flag for product' situation — it is a GTM-blocking product gap with a growing cost."

**[FEEDBACK POINT 3 — LOOP UPDATE]**

Product confirms: compliance feature will not ship until Q1 2027 — later than the
Q4 2026 estimate in the original context. One more deal closes: FS account,
VP Engineering champion, CISO also engaged. Compliance requirement confirmed in
Stage 2 discovery. Rep paused the deal to avoid a loss; deal flagged as "waiting
for product."

---

### WITH LOOP — PASS 2

**New evidence entering the Loop:**
- Compliance feature delayed to Q1 2027
- New deal paused (rep applied the qualification gate — this is intervention adoption
  evidence and a leading indicator, not a closed-deal outcome; it does not count
  toward prevalence confidence for Pattern 2)
- CISO entry pattern: 1 closed confirming deal (the won deal) + 1 paused deal with
  CISO engaged (leading indicator only — the paused deal is not a closed outcome)

**Where the Loop updates:** Pattern 2 urgency increases. The product delay changes
the intervention — it is no longer "flag for product review," it is "change ICP
scope for 2 quarters" and "build communication for active pipeline." Pattern 1
nuance (CISO as valid champion type) moves from "observation" to "qualification
criteria update candidate."

**Pass 2 output:**

"Pattern 2 update — Compliance Gap (urgent escalation).

Product delivery moved to Q1 2027. This extends the horizon over which we cannot win
regulated FS accounts with hard compliance requirements. The previous recommendation
(Stage 1 disqualification gate for compliance-required accounts) is now the correct
practice for the next two quarters — not a temporary hold. Reps should not invest
past Stage 2 in accounts with SEC 17a-4 or FINRA data residency requirements until
the feature ships.

The rep who paused the current deal applied the gate correctly. That deal should be
moved to a Q1 2027 pipe date and stayed warm through product update communications.

Updated leadership brief for Diane R. and Darren W.:
- 5 confirmed losses, $1.9M attributed to compliance gap over 6 months
- 1 active deal paused, $315K
- Product delivery: Q1 2027
- Recommended action: Explicitly exclude hard-compliance FS accounts from Q3–Q4 2026
  pipeline targets; adjust SDR prospecting criteria to exclude or defer these accounts;
  prepare customer communication for prospects currently in pipeline who have compliance
  requirements.

Pattern 1 qualification update (CISO addition):
Two data points now support CISO as a valid entry champion in regulated FS
(comparable decision influence to VP Engineering when compliance is a C-suite concern).
Recommend updating Stage 2 qualification criteria to include: 'VP Engineering, CTO,
Head of Data, CDO, or CISO with confirmed C-suite access.'

Confidence on CISO pattern: Low (1 closed confirming deal — the won deal via CISO
entry; the paused deal is intervention adoption evidence, not a closed outcome).
Adding to pattern log. Will reach Medium with 2 more closed confirming deals;
formal criteria update recommended at Medium with supporting Tier 1 interview."

---

### DELTA — SCENARIO 3

| Dimension | Without Loop | Loop Pass 1 | Loop Pass 2 |
|---|---|---|---|
| Pattern reading | Criteria may need time to show results | Pattern 2 accelerating; CISO entry observed | Pattern 2 now GTM-blocking for 2 quarters; CISO champion nuance forming |
| Recommended action | Wait 2 more quarters | Escalate to Diane + Marcus; note CISO observation | Explicit ICP scope change for Q3–Q4 2026; customer comms for active pipeline; CISO criteria update queued |
| Feedback effect | n/a | Product timeline + paused deal inform urgency | Product delay shifts from "flag" to "structural ICP exclusion"; rep applied gate correctly |
| Confidence update | n/a | Pattern 2: High, accelerating. Pattern 1 nuance: emerging | Pattern 2: urgent escalation. CISO: Low (1 closed confirming deal), tracking toward Medium |
| What the Loop preserved | n/a | Prior pattern state (P1, P2 active) | Pattern history across 2 quarters — escalation quantified to $1.9M |

**Where in the Loop feedback mattered most:** Product timeline update changed the
nature of the response entirely. "Flag for review" (Pass 1) became "adjust ICP scope
for two quarters and communicate to pipeline" (Pass 2) — not because the pattern
changed, but because the resolution timeline changed. The Loop preserved the pattern
state and the $1.9M evidence base across two quarters; the escalation brief in Pass
2 was quantified because the Loop had been tracking it since Pass 1.

---

## Summary: What the Loop Changes

Across three scenarios, three distinct feedback effects:

**Scenario 1:** Feedback reframes the competitive mechanism — incumbent displacement,
not feature competition. Battle card explicitly contraindicated. Different artifact,
different audience, different play.

**Scenario 2:** Feedback controls for a confound — rep underperformance attributed
to territory design, not execution. Performance management avoided. Systemic
intervention (qualification criteria + SDR targeting) replaces individual intervention.

**Scenario 3:** Feedback shifts the time horizon — product delay converts a monitoring
pattern into a GTM-blocking constraint for two quarters. "Flag for product" becomes
"adjust ICP scope and communicate." The Loop's two-quarter evidence base made the
escalation brief quantifiable.

In all three cases, the Loop's value was not in the first pass. It was in knowing
what it had already diagnosed, holding that state across feedback cycles, and deciding
how new evidence changed — or confirmed — what to do next.

---

## Appendix — Synthetic Future Update: Illustrative Intervention Evaluation

**This section demonstrates how the Loop would process a hypothetical post-deployment
evaluation result for Scenario 1 (Luvexis incumbent displacement). It does not
validate the fictional intervention or establish a real-world causal effect. It is
included to show what the evaluation design, evidence reporting, and confidence
language look like when applied correctly.**

---

### Setup

Following Pass 2 of Scenario 1, the team deployed an incumbent displacement play:
a discovery question set for reps (to identify Luvexis incumbency at Stage 1)
and an executive business case document targeting CFO and COO audiences with a
"best-of-breed vs. vendor consolidation" framing.

**Deployment date:** October 1, 2026
**Eligibility criteria:** Enterprise FS deals (500+ employees) where Luvexis is
confirmed as an incumbent in the account's environment, identified at Stage 1
through the new discovery question set

**Assignment method:** All eligible deals entering pipeline on or after October 1,
2026, in accounts where the rep confirms Luvexis incumbency at Stage 1

**Treated cohort:** Enterprise FS deals with confirmed Luvexis incumbency, entering
pipeline October 1, 2026+, where the rep applied the discovery question set and, if
applicable, the executive business case was delivered to CFO or COO

**Comparison cohort (same-period matched):** Enterprise FS deals in the same period
where Luvexis was present as a competitor but no prior Luvexis incumbency was
identified at Stage 1 (standard competitive motion, no displacement play applied)

**Matching variables (pre-treatment only):** Segment, geography, deal source, deal
value range, rep tenure at deal entry, initial stage at entry, product requirements.
Note: Whether the economic buyer (CFO/COO) was engaged is a mediating outcome of
the intervention, not a matching variable.

**Pre-treatment baseline:**
* Luvexis-incumbent deals (Q1–Q2 2026, pre-intervention): 0 of 5 won (0%)
* Luvexis-competitive non-incumbent deals (Q1–Q2 2026): 1 of 1 won (Meridian
  Capital — 100%, very small comparison sample)

**Observation window:**
* Start: October 1, 2026
* Minimum deal count: 10 closed eligible treated deals
* Planned end: June 30, 2027
* Leading indicator: % of eligible deals where CFO or COO was engaged before Stage 3

**Minimum threshold and concurrent changes:** The team set a minimum of 10 eligible
treated-cohort closures before interpreting results. During the observation window:
one product release (compliance feature shipped December 2026, increasing Databricks
competitive pressure in one adjacent sub-segment), no pricing or territory changes.

---

### Synthetic Observation Result (illustrative — not a real outcome)

As of June 30, 2027, observation window complete:

**Treated cohort (Luvexis-incumbent plays deployed):**
* Eligible deals opened: 14
* Eligible deals closed: 11 (above 10-deal minimum threshold)
* Won: 5 / Lost: 6 = 45% win rate
* CFO or COO engaged before Stage 3 in 8 of 11 (73%) — leading indicator met
* Adoption: 10 of 11 deals confirmed to have used discovery question set; 7 of 11
  delivered executive business case to CFO/COO (fidelity: partial — 3 deals advanced
  to Stage 3 before executive document was delivered)

**Same-period matched comparison cohort (Luvexis competitive, no incumbency flag):**
* Deals opened: 12
* Deals closed: 9
* Won: 3 / Lost: 6 = 33% win rate
* Matching criteria met for segment, geography, deal source, and deal value range.

**Concurrent change note:** The compliance feature shipped December 2026 and affected
2 deals in the comparison cohort (both lost to compliance-requirement accounts already
in pipeline). These 2 deals may have inflated the comparison cohort's loss rate for
a reason unrelated to the Luvexis intervention. Sensitivity check: excluding those
2 deals, comparison win rate is 3/7 = 43%.

**Leading indicator result:** 73% of treated deals had CFO/COO engaged before Stage 3,
vs. an estimated ~20–30% in the pre-intervention period. This is adoption evidence —
the play changed rep behavior in the expected direction.

---

### Loop Assessment

**Intervention confidence: Matched Evidence — single cohort**

The treated cohort (45%) outperformed the same-period matched comparison cohort (33%)
by 12 percentage points, compared to a pre-intervention baseline of 0% in Luvexis-
incumbent deals. The treated cohort result is directionally consistent with the
incumbent consolidation mechanism hypothesis.

This result does not confirm that the intervention caused the improvement. Specific
limitations:

* Non-random assignment: deals were self-selected into the treated cohort by rep
  identification of Luvexis incumbency. If reps applied the incumbency flag
  selectively to accounts they already assessed as more winnable, the comparison
  is biased.

* Partial fidelity: 3 of 11 treated deals did not receive the executive business
  case document before Stage 3. A fully-applied cohort (7 deals with complete
  delivery) shows a win rate of 4/7 (57%) vs. the partial-delivery cohort (1/4 = 25%).
  This suggests the document delivery timing may matter, but the sample is too small
  to conclude this.

* Sensitivity to concurrent change: the compliance feature shipment affected the
  comparison cohort in a way that may have elevated its loss rate. If excluded, the
  treated cohort's advantage narrows (45% vs. 43%). The conclusion is sensitive to
  this adjustment.

* Unobserved confounders: rep experience with the new play increased over the
  observation window. Later deals in the cohort may have benefited from rep learning
  rather than the play itself.

**Maturity state update:** Association observed → Mechanism supported → Intervention
testing → **Monitoring result**

The pattern moves to Monitoring result. Intervention confidence is Matched Evidence
(single cohort) with the limitations above stated. The pattern does not move to
Validated on a single cohort observation with known matching limitations and
fidelity gaps.

**What would support Validated:**
* Replication of the matched comparison result in a second independent cohort
  (different quarter, different region, or staggered rollout group)
* Higher fidelity rate (executive document delivered before Stage 3 in 9+ of 10
  eligible deals)
* A controlled comparison — a staggered rollout where some eligible deals randomly
  did not receive the play — would substantially strengthen the inference

**Loop recommendation:** Continue the play with improved fidelity tracking. Attempt
a staggered rollout in the next deployment period to create a cleaner comparison.
Conduct 2–3 exit interviews from the won deals in the treated cohort to test whether
the executive business case was the perceived pivoting factor.

Buyer-reported counterfactual example (hypothetical interview, Clearbrook Capital):
"Buyer reported that having the CFO conversation early in the process, before IT
made its recommendation, was a factor in keeping the evaluation open. Whether that
alone would have changed the outcome is hard to say."
This is a buyer-reported contributing factor. It is not a claim that the intervention
caused the win.

---

### What This Appendix Demonstrates

* The Loop reports early descriptive results without upgrading confidence before the
  threshold
* The Loop separates leading indicators (CFO/COO engagement rate) from final outcomes
  (win rate)
* The Loop explicitly limits confidence to Matched Evidence based on the comparison
  design — not Controlled Evidence, because assignment was not random
* The Loop notes the concurrent change (compliance feature) and performs a sensitivity
  check
* The Loop flags the fidelity gap and its possible effect on results
* The Loop labels buyer-reported responses correctly: "buyer reported that X was a
  factor" — not "X caused the win"
* The Loop declines to move to Validated on a single non-random cohort with known
  limitations
