# Win/Loss Pattern Loop — Example Output

**Fictional scenario.** All companies, products, people, deal data, quotes, and outcomes in this file are fictional and created solely to demonstrate the Loop's analytical behavior. Any resemblance to real organizations, products, or individuals is unintentional. This output reflects the state of the Loop as of August 1, 2026.

---

## Pattern Analysis Summary

**Segment:** Enterprise financial services, North America (500+ employees)
**Period analyzed:** Q1–Q2 2026 (24 deals: 9 won, 15 lost)
**Baseline win rate:** 38% vs. 47% prior year — 9-point decline over 12 months
**Evidence available:** 24 closed deals, 4 exit interviews, 3 rep notes, product
and competitive context, partial intervention observation data (25 days post-deployment)

**Active patterns:** 3 at Mechanism supported; 1 under investigation

**Intervention in progress:** Pattern 1 qualification criteria update deployed
July 7, 2026. Observation threshold not reached (3 of 15 minimum eligible deals
closed). All partial intervention results in this output are early descriptive data
only — Intervention confidence remains Untested.

---

## Pattern Status Dashboard

| Pattern | Types | Maturity | Op. Status | Mech. Conf. | Prev. Conf. | Int. Conf. | Replication | Artifact |
|---|---|---|---|---|---|---|---|---|
| IT Director champion / no economic buyer | 2 + 8 | Intervention testing | Active | High | High | Untested | None | Recommended — observation threshold pending |
| Compliance capability gap | 10 | Mechanism supported | Active + Escalated | High | Medium | n/a | n/a | Escalation brief ready |
| Luvexis as incumbent | 4 + 7 | Mechanism supported | Active | High | Medium | n/a | n/a | Hold — evidence acquisition first |
| Rep performance vs. territory | Under investigation | Association observed | Active | Insufficient | Insufficient | n/a | n/a | None |

---

## Pattern 1 — Champion Profile and Stakeholder Breadth: IT Director Without Economic Buyer

**Pattern types:** Champion profile + Stakeholder breadth (Types 2 + 8)
**Pattern maturity:** Intervention testing
**Operational status:** Active
**Direction:** Loss pattern

### Two required causal statements

**Association statement:**
Two cohorts are defined from the Q1–Q2 2026 enterprise FS deal set (24 deals).

Exposed cohort — IT Director or IT Manager as sole champion, no economic buyer
engaged: 14 deals (0 won, 14 lost) — 0% win rate (12 IT Directors, 2 IT Managers).

Comparison cohort — VP Engineering, CTO, Head of Data, CDO, or equivalent senior
technical champion with direct economic buyer engaged (CFO, COO, CEO, or CTO):
7 deals (7 won, 0 lost) — 100% win rate.

Three deals fall outside both defined cohorts: Kelvane Wealth (Director of Analytics,
no economic buyer, won), Vestral Lending (Analytics Manager, no economic buyer, won),
and Valdrex Capital (Data Engineer IC, no economic buyer, lost). These deals are
not counted in the cohort comparison. The comparison cohort is small (7 deals) and
non-random; the 100% win rate reflects a strong directional signal but should be
interpreted with that limitation in mind.

**Mechanism hypothesis:**
We hypothesize that IT Director or IT Manager as sole champion may influence loss
outcomes through an authority limitation: the champion cannot elevate the business
case to C-suite decision-makers without an explicit internal mandate to do so, and
absent that mandate, the evaluation defaults to the path of least resistance — the
incumbent vendor, the existing relationship, or the vendor the IT team already knows.

**Alternative mechanisms evaluated:**
* IT Directors lack technical knowledge to evaluate effectively — contradicted by
  Pinnacle interview. The evaluation was not conducted rigorously enough for feature
  strengths or weaknesses to be the deciding factor.
* IT Directors prefer different product features — not supported; no deals reached
  the depth of evaluation where feature comparison was determinative.
* IT Director presence is a proxy for organizational treatment of data as an IT
  function rather than a business capability — plausible and not fully distinguishable
  from the stated mechanism with current evidence. Acknowledged limitation.

**Proxy variable check:**
IT Director title may be a proxy for "IT-led buying motion" at organizations where
data is operationally managed rather than strategically governed. The proposed
intervention (require VP-level champion identification) addresses the decision-
authority pathway. If the underlying variable is organizational data maturity,
the intervention may not generalize to all account types in the segment. This is
a scope limitation to monitor in the observation window.

**Confounders evaluated:**
Deal source: pattern holds across inbound, outbound, and partner referral. Rep
identity: pattern appears across all three reps. Competitive presence: pattern holds
regardless of which competitor appeared.

### Evidence base

* Exposed cohort (IT Director/Manager, no economic buyer): 14 deals — 0 won,
  14 lost — 0% win rate (12 IT Directors, 2 IT Managers)
* Comparison cohort (VP+ technical champion, economic buyer engaged): 7 deals —
  7 won, 0 lost — 100% win rate
* Outside both defined cohorts: Kelvane Wealth (won), Vestral Lending (won),
  Valdrex Capital (lost) — excluded from cohort comparison
* Contradiction count: 0 within the defined exposed cohort
* Note: Comparison cohort is small (7 deals) and non-random. The 100% comparison
  win rate reflects strong directional separation; it should not be taken as a
  precise population-level estimate.
* Highest tier: Tier 1 — Pinnacle interview confirms IT recommendation followed
  without elevation to CFO or COO; Korvel interview confirms COO awareness
  without direct CFO engagement, producing the same outcome as no senior awareness.

**Mechanism confidence: High**
Both required statements written. Alternative mechanisms and proxy variable evaluated.
Tier 1 evidence supports the authority-limitation pathway through two independent
deals with different failure modes (recommendation followed without question at
Pinnacle; active COO interest that never reached CFO at Korvel).

**Prevalence confidence: High**
14 of 14 exposed-cohort deals (IT Director/Manager, no economic buyer) are losses —
0% win rate. The defined comparison cohort (VP+ champion with economic buyer) shows
7 of 7 wins — 100% win rate. The outcome differential between cohorts is complete
and consistent across all three reps and multiple deal sources. Tier 1 evidence
directly supports the mechanism in 2 of the 14 exposed-cohort confirming deals.

Note: Prevalence confidence is High based on the cohort outcome differential — not
based on interview count. The interviews raise Mechanism confidence; the complete
differential across the defined cohort establishes Prevalence confidence. The
comparison cohort is small (7 deals); the differential is directionally unambiguous
but the exact win rate estimate should be treated with that limitation.

**Intervention confidence: Untested**
Intervention deployed July 7. Observation threshold not yet reached (3 of 15
minimum eligible deals closed as of August 1, 2026).

### Intervention evaluation design (active)

```
Intervention: Stage 2 qualification criteria requiring VP-level or above technical
  champion (VP Engineering, CTO, Head of Data, CDO, or CISO with C-suite access)
  before Stage 3 commitment
Deployment date: July 7, 2026

Eligibility: Enterprise FS, 500+ employees, North America, VP+ champion confirmed
  at Stage 2

Assignment: All eligible deals (no holdout)

Exposure:
  Fidelity: Unknown — CRM audit pending
  Adoption rate: Unknown pending audit

Treated cohort:
  Eligible deals opened since July 7: 8
  Closed: 3 (below 15-deal minimum threshold)
  Exclusions / attrition: None identified yet

Comparison cohort:
  Type: Same-period (IT Director sole champion, same segment, July 7 onward)
  Matching variables (pre-treatment only): segment, geography, deal source,
    deal value range, competitor presence, rep tenure, product requirements
  Note: Economic buyer engagement is the intervention target behavior — it is
    tracked as a leading indicator, not a matching variable
  Deals opened: 5
  Closed: 2

Baselines:
  Treated cohort segment prior rate: 38% (Q1–Q2 overall)
  IT Director sole-champion prior rate in competitive conditions: 0–15%

Observation window:
  Start: July 7, 2026
  Minimum deal count: 15 closed eligible deals
  Planned end: December 31, 2026 or 15 minimum, whichever is later

Leading indicator: % of new Stage 3 entries with VP+ champion AND economic buyer
  (CFO, COO, CEO) contacted at least once
Final outcome metric: Win rate of eligible treated cohort at close
Unit: Deal
Analysis population: Intention-to-treat + actually treated

Concurrent changes: No product, pricing, territory, or rep changes since July 7.
  Luvexis Q1 promotional campaign appears to have concluded.

Confounders not controlled: Deal source mix may shift as reps adjust outbound
  prospecting toward VP+-accessible accounts.
Unobserved: Seasonal effects, buyer urgency variation by quarter.
```

### Early descriptive result (observation threshold NOT reached)

As of August 1 — 3 of 15 minimum deals closed. Do not upgrade Intervention
confidence from Untested.

Treated cohort: 2 won / 1 lost (67% win rate — 3 deals)
Comparison cohort: 0 won / 2 lost (0% win rate — 2 deals)

The 1 treated-cohort loss (Fortbridge, $410K) is attributable to Pattern 2
(compliance capability gap). The VP+ champion criteria were met. This is not a
contradiction of Pattern 1; it confirms that Pattern 1 and Pattern 2 can co-occur
independently. Addressing the champion profile does not compensate for a
disqualifying product gap.

Results are directionally consistent with the hypothesis. With 3 treated and 2
comparison deals closed, any observed difference falls within normal sampling
variation. Intervention confidence remains Untested pending the predefined threshold.

### Recommended actions

* Continue Stage 2 VP+ criteria requirement. Complete CRM audit for adoption and
  fidelity rates. Flag any deals that advanced to Stage 3 without VP+ confirmation.
* Begin tracking economic buyer engagement as a leading indicator on all new Stage
  3 entries.
* SDR targeting review: Revise outbound prospecting to include VP Engineering, CTO,
  Head of Data, CDO, and CISO in the primary title set. IT Director outreach remains
  appropriate for initial discovery — the goal is to identify the VP-level contact
  through IT, not to run the full evaluation with IT as the buyer.
  Decision owner: VP Sales (Diane R.) + SDR leadership. Approver: Diane R.

**Routing:** Insight: PMM / GTM. Decision: VP Sales. Intervention: Sales enablement +
SDR leadership. Measurement: RevOps. Approver: Diane R. (VP Sales).

---

## Pattern 2 — Product / Capability Gap: Compliance Features Unavailable for Regulated Accounts

**Pattern types:** Product / capability (Type 10)
**Pattern maturity:** Mechanism supported
**Operational status:** Active + Escalated
**Direction:** Loss pattern — activates in SEC 17a-4 and FINRA-regulated accounts

### Two required causal statements

**Association statement:**
In enterprise FS deals closing Q1–Q2 2026, loss reason coded as "product gap —
compliance features" appears in 3 of 15 lost deals (Cardinal $510K, Elara $480K,
Orvana $360K), totaling $1.35M. A fourth compliance-attributed loss (Fortbridge
$410K) occurred in Q3 2026. No won deal involved a compliance-requirement objection.
Combined: 4 confirmed compliance losses, $1.76M, over 7 months.

**Mechanism hypothesis:**
We hypothesize that the absence of data residency and compliance features may influence
loss outcomes in SEC 17a-4 and FINRA-regulated accounts through a hard technical
requirement: accounts operating under those regulatory standards cannot adopt a product
that does not meet the compliance condition, regardless of other product strengths,
pricing, or sales effort. This is a disqualifying gap, not a persuadable objection.

**Alternative mechanisms evaluated:**
* Reps failing to discover compliance requirements early — supported by Cardinal
  evidence (rep unaware until Stage 3). This is a process compounding factor. Even
  with earlier discovery, the product still cannot meet the requirement.
* Compliance cited as rationalization for a decision made on other grounds — less
  supported. Cardinal interview named the specific regulatory standard (SEC 17a-4)
  and the specific product limitation. Databricks had a workable solution at the time.
  The buyer's alternative was not unavailable; it was the product that was unavailable.

**Proxy variable check:**
Not applicable. The compliance requirement is a direct, binary product condition —
it either meets the regulatory standard or it does not. The intervention is product-
level (build the feature) and GTM-level (qualify accounts with hard compliance
requirements out of the pipeline until the feature ships).

**Confounders evaluated:**
Databricks' compliance-ready release (Q4 2025) increases the opportunity cost of
the product gap by providing a viable alternative. It did not create the gap. The
gap exists independent of Databricks' offering.

### Evidence base

* Confirming deals: 3 of 15 lost deals Q1–Q2 (Cardinal, Elara, Orvana) + Fortbridge
  in Q3 = 4 confirmed
* Revenue: $1.35M Q1–Q2, $1.76M through Q3
* Contradiction count: 0
* Highest tier: Tier 1 — Cardinal exit interview directly confirms the mechanism,
  names the regulatory standard, and confirms the buyer chose based on available
  compliance documentation, not a roadmap commitment

**Mechanism confidence: High**
Cardinal interview directly explains the mechanism. Specific regulatory standard
named. Product deficiency confirmed by product team.

**Prevalence confidence: Medium**
Three Q1–Q2 confirming deals with one Tier 1 interview is below the High threshold.
The compliance-required account population is self-selecting — not all 15 losses
had this barrier. Prevalence of the specific mechanism across the broader segment
is unknown. Another exit interview would corroborate the mechanism and better define
its boundary. Additional eligible closed deals and a comparison rate for compliance-
required versus non-compliance-required accounts are needed to strengthen Prevalence
confidence.

Note: Mechanism confidence is High. Prevalence confidence is Medium. These are
separate assessments. High Mechanism confidence with Medium Prevalence confidence
means: we understand the mechanism well from one deal. We do not yet have a
sufficiently sized cohort comparison to establish persistent segment-level prevalence.

### Evidence acquisition plan

* **Priority interview target — Korsavel Fund Management ($480K):** Same loss code as
  Cardinal, similar deal size, different rep. Tests whether the mechanism is rep-
  specific or structural.
  Mechanism question: "Can you describe the specific compliance requirement that the
  product did not meet at the time?"
  Counterfactual question: "If the data residency feature had been available and
  compliant with your regulatory requirements at that time, do you think your decision
  might have been different?"
  Conductor: Sales manager or CS team.

* **Priority interview target — Orvana Wealth ($360K):** Third rep, additional
  confirmation of the mechanism across the team.

* **Won deal check:** Confirm that Telvoran Capital and Drevith Asset Management did
  not have a compliance requirement. This would tighten the boundary: compliance-
  required accounts lose; non-required accounts are not blocked.

### Recommended interventions

1. **Stage 1 compliance qualification gate (recommended, awaiting approval):**
   Add a compliance requirement check to Stage 1 discovery. If the account has SEC
   17a-4 or FINRA data residency requirements, flag as blocked pending feature
   availability. Do not invest Stage 3 or 4 resources until the feature ships. This
   is the Loop's recommendation — the decision rests with VP Sales.

2. **Leadership escalation brief (recommended — ready to generate):**
   For Diane R. (VP Sales) and Darren W. (Head of Product):
   * Confirmed compliance losses: 4 deals, $1.76M over 7 months
   * Compliance feature delivery estimate: Q4 2026 (no committed date)
   * Competitive context: Databricks has a workable compliance solution available now
   * Decision required: committed product timeline to communicate to active pipeline;
     whether to explicitly exclude hard-compliance FS accounts from Q3–Q4 pipeline
     targets; customer communication for prospects currently in pipeline with known
     compliance requirements
   * The roadmap and exclusion decisions belong to product and sales leadership.
     The Loop recommends escalating — not deciding.

**Routing:** Insight: PMM + RevOps. Decision: VP Product (roadmap), VP Sales (GTM
policy). Intervention: Product (roadmap); GTM (qualification gate). Measurement:
Product analytics + RevOps. Approver: VP Product (Darren W.) + VP Sales (Diane R.).

---

## Pattern 3 — Competitive Entry: Luvexis as Incumbent, Not Feature Competitor

**Pattern types:** Competitive + Timing / entry (Types 4 + 7)
**Pattern maturity:** Mechanism supported
**Operational status:** Active
**Direction:** Loss pattern — specific to accounts where Luvexis is already in
the customer environment

### Two required causal statements

**Association statement:**
In enterprise FS deals closing Q1–Q2 2026 where Luvexis was the named competitor,
5 of 5 Luvexis-competitive deals were lost. No Luvexis-competitive deals were
won in this period. (Telvoran Capital evaluated and did not choose Luvexis, but
the deal dynamic was a head-to-head evaluation — Luvexis was not an incumbent.)

**Mechanism hypothesis:**
We hypothesize that Luvexis's presence as a competitor in these accounts may
influence loss outcomes not through feature comparison but through an incumbent
consolidation dynamic: accounts already using Luvexis for another workload are
not running a rigorous comparative evaluation — they are seeking justification to
extend an existing relationship or consolidate vendors rather than add a new one.
The decision is substantially formed before the nominal evaluation begins.

**Alternative mechanisms evaluated:**
* Luvexis wins on product features — contradicted by Corvath Capital interview ("we never
  really got to a rigorous evaluation"). Features were not compared.
* Luvexis wins on price — Corvath Capital CRM code reads "competitor offered better price,"
  but the interview directly contradicts this. CRM loss codes for Luvexis losses
  may be rationalizations rather than buyer-stated reasons.
* Luvexis's Q1 promotional campaign created pricing pressure — plausible for
  Velstrom, Velkorath, Titan. Not confirmed through interview evidence. If true,
  this is a different mechanism (commercial / promotional) requiring a different
  response (commercial play) rather than an incumbent displacement play.

**Proxy variable check:**
"Luvexis present" is not a proxy — but the mechanism depends on whether Luvexis
was incumbent vs. entering as a net new competitor. The current evidence only confirms
the incumbent sub-pattern in one deal (Corvath Capital). The other four Luvexis losses may
contain a mix of mechanisms.

**Confounders evaluated:**
Luvexis Q1 promotional campaign may have affected price sensitivity across some
accounts in this period. Not controlled for.

### Evidence base

* Mechanism confirmed (incumbent sub-pattern): 1 via Tier 1 interview (Corvath Capital)
* Deals in Luvexis-competitive scope: 5 total losses
* Mechanism confirmed across: 1 of 5 Luvexis losses
* Contradiction count: 0 confirmed; 4 losses unclassified (not confirming, not
  contradicting — no interview data)
* Highest tier: Tier 1 (Corvath Capital) — CRM code contradicted by interview

**Mechanism confidence: High (for the Corvath Capital deal)**
Corvath Capital interview directly confirms: "Luvexis was already in our environment...
the decision was made before the evaluation really started." CRM code is wrong.
One strong Tier 1 interview for one deal.

**Prevalence confidence: Medium**
One confirmed instance out of 5 Luvexis losses. The 4 remaining Luvexis losses
have no interview data and may represent different mechanisms. Cannot establish
that the incumbent consolidation dynamic explains the other 4 losses. Medium is the
appropriate prevalence confidence — meaningful pattern signal, insufficient cohort
confirmation.

### Why no battle card is generated

A standard competitive loss → battle card is the right response.
An incumbent consolidation loss → different response: executive-level business case
reaching the CFO or COO with a "best-of-breed vs. vendor consolidation" question,
at an earlier stage before the IT recommendation is formed.

A feature comparison battle card in an incumbent consolidation scenario reinforces
the wrong question. The buyer is not asking "which product is better technically?"
They are asking "why would we add a new vendor when Luvexis is already here?"
Those questions require different artifacts, different audiences, and different entry
timing. Generating a battle card now would be acting on 1 of 5 confirmed deals
before the mechanism is established across the cohort.

### Evidence acquisition plan

* **Priority interview target — Velstrom Asset Management ($380K):** Stage 3 exit,
  outbound source. Early stage exit may indicate incumbent effect (evaluation never
  fully engaged).
  Mechanism question: "Was Luvexis already deployed in your environment before
  you started this evaluation, or was it a net new comparison?"
  Counterfactual question: "If Luvexis had not already been in your environment,
  do you think the evaluation might have proceeded differently?"

* **Priority interview target — Pelanthor Trust ($540K):** Stage 4 exit, inbound source,
  high value. Tests whether the incumbent dynamic appears in inbound deals (which
  would suggest the dynamic is not source-specific).

* **Won deal reference:** Telvoran Capital ($480K) — Luvexis was evaluated and
  not chosen. What made this a real comparative evaluation when others were not?
  Was Luvexis not an incumbent in that account?

After 2–3 more interviews confirming the mechanism, the Loop will move to High
Prevalence confidence and generate an incumbent displacement play (discovery question
set + executive business case framing). Until then, no Luvexis artifact is generated.

**Routing:** Insight: PMM. Decision: PMM + VP Sales. Intervention: PMM (artifact);
Sales leadership (deployment). Measurement: Sales leadership + RevOps. Approver:
VP Sales + PMM.

---

## Pattern Under Investigation — Rep Performance vs. Territory Confound

**Pattern types:** Not yet classifiable (potential Type 11 or structural confound)
**Pattern maturity:** Association observed
**Operational status:** Active

### Association

Marcus L. (8 months tenure) has a 27% win rate vs. Priya K. (44%) and Tom S. (46%).
Marcus carries 7 of 15 losses. This is an observed outcome differential. It is not
yet a classifiable pattern.

### Why Type 11 classification is premature

Before this can be classified as a Sales execution / coverage pattern, two confounders
must be tested:

1. Marcus's territory skews toward outbound-sourced deals. Outbound enterprise deals
   have lower baseline win rates across all reps in this dataset. If Priya and Tom
   carry more inbound and referral-sourced deals, the win rate differential may
   reflect territory composition rather than execution difference.

2. Marcus is 8 months into an enterprise sales role. Early-tenure reps commonly carry
   pipeline from a period before their ramp was complete.

### What is required before classification

Pull Marcus's 7 losses by deal source. Compare Marcus's outbound win rate to Priya and
Tom's outbound win rate on comparable deal values and segments. If his outbound win
rate matches peers working the same deal type and source, his outcome differential
is explained by territory composition.

### What the Loop cannot conclude

Whether Marcus's differential is caused by execution, territory, ramp timing, or a
combination. No performance or coaching recommendation is generated until the
territory confound is evaluated.

No artifact is generated for this pattern.

---

## Portfolio Observation

The team's instinct — improving demo quality — made sense as a response to losses.
If the problem were late-stage persuasion, demo quality would be the lever. The
data suggests the problem is earlier in the deal, and structural in two different ways.

In 14 of 15 lost deals, the evaluation was run with champions who lacked the
authority to close or elevate the decision. In 3 of those 15, the product cannot
meet a mandatory regulatory requirement — making the evaluation outcome predictable
before the demo happens. In 5 of 15, the competitive situation may have been resolved
before the nominal evaluation began, because the incumbent was already embedded.

Improving the demo does not address an authority limitation, a compliance product
gap, or an incumbent consolidation dynamic. These are qualification, product, and
market-entry problems.

The most urgent action is Pattern 2: $1.76M in confirmed losses in 7 months is a
pattern with a known mechanism, a named product cause, and a growing cost as
Databricks' compliant alternative gains traction. The decision about product timing
and GTM exclusion policy needs to be made explicitly by product and sales leadership
— and the evidence now supports presenting it.

Pattern 1 is in flight. The intervention is deployed. The question now is not what
to do — it is whether the qualification criteria change, combined with SDR targeting
adjustment, moves the treated cohort win rate by Q4 2026.

Pattern 3 needs two more interviews before an artifact is appropriate. Getting those
interviews is the next concrete action for the Luvexis pattern.
