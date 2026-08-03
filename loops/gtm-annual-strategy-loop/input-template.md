# Annual GTM Strategy and Goal Governance Loop — Input Template

**Version:** 2.1

---

## How This Template Works

**The user/Loop boundary is strict and applies everywhere in this template.**

The user supplies evidence, facts, timelines, and organizational context.
The Loop infers operating mode, assumption status, seasonal position, readiness,
dependency confidence, guardrail status, and all recommendations. No status or
confidence judgment appears in the user-supplied sections.

**Module guide:**

| Module | Use when |
|--------|----------|
| **A — Planning and Initialization** | Annual planning, or when adding a new bet mid-year |
| **B — Recurring Update** | Monthly operating reviews and QBRs |
| **C — Adaptation Annex** | When a pivot decision is required |
| **D — Endgame and Year-End Annex** | Year-end review or when results are verified closed |

**State carry-forward:**
The Loop carries forward all state from the prior run. In Module B, supply only
what has changed. Do not resubmit unchanged data from Module A.

**Field labels used throughout this template:**

- `[init]` — Required to initialize the Loop. Omitting these produces unreliable output.
- `[asm]` — Required before the Loop can assess assumption status or infer signal trajectory.
- `[pvt]` — Required before the Loop can recommend a pivot or intervention.
- `[opt]` — Optional enrichment that improves analytical precision but is not required to begin.

**Minimum viable initialization:**

Submit these fields to receive a Planning mode output. Complete `[asm]` fields before
the first Monitoring review. Complete `[pvt]` fields before any Adaptation
recommendation is needed. `[opt]` fields improve precision and should be completed
as evidence arrives.

*Required at initialization `[init]`:*
- A1: Review type, review date, fiscal year dates, organizational events
- A2: All commitments with metric definitions, targets, and protection levels
- A3: Evidence-supported base and gap calculation
- A4 per bet: Hypothesis, target, owner, commitment mapping, load-bearing assumptions
  with planning-time evidence and indicators, seasonal peak window,
  required readiness gates, known dependencies
- A5: Forecast contribution bridge

*Required before assumption assessment `[asm]`:*
- A4.2: All assumption fields — thresholds, signal windows, restoration evidence
- A4.6: Indicator table

*Required before pivot recommendation `[pvt]`:*
- A4.0: Guardrail metrics and thresholds
- A4.7: Available intervention levers
- A9: Version ledger (so the Loop tracks what is being changed and from what original value)
- C2: Replacement-bet feasibility evidence

*Optional enrichment `[opt]`:*
- A6: Prior-year learning
- A7: Imported Loop findings
- A8: External market signals
- A4.5: Full dependency detail beyond minimum evidence
- A4.3: Full seasonal curve beyond peak window

**Version integrity rule:**
The Loop may revise the plan. It must never rewrite what the organization originally
believed. Every revision to a commitment target, assumption, threshold, seasonal
window, or contribution expectation must be recorded in A9 alongside the original
value. Prior assessments calculated under the old version remain visible.

---

## MODULE A — Planning and Initialization

*Complete at Annual planning and when initializing the Loop for the first time or
adding a new bet mid-year. At subsequent reviews use Module B and carry forward
unchanged state.*

---

### A1 — Review Context `[init]`

**Review type:**
```
[ ] Annual planning
[ ] Monthly operating review
[ ] QBR
[ ] Urgent reassessment
[ ] Executive decision review
[ ] Year-end review
```

**Review date:** `[YYYY-MM-DD]`

**Fiscal year:** `[FY20XX — YYYY-MM-DD to YYYY-MM-DD]`

*(The Loop computes days elapsed and remaining from the review date and fiscal year
boundaries. You do not calculate these.)*

**Organizational events to report:** `[init]`
*(Facts the Loop cannot observe from signal data: board decisions, executive changes,
budget reallocations, external events, competitive moves, leadership directives.
Undisclosed organizational events are the most common source of incorrect mode inference.)*

```
[Event 1 — Date: YYYY-MM-DD — Description: ]
[Event 2 — Date: YYYY-MM-DD — Description: ]
[Event 3 — Date: YYYY-MM-DD — Description: ]
```

---

### A2 — Commitment Portfolio `[init]`

*(An annual GTM plan typically carries multiple simultaneous commitments across
different metrics. Each commitment is independent. A strategic bet may contribute
positively to one commitment and negatively to another. The Loop tracks each
commitment separately and flags cross-commitment conflicts before recommending
any intervention. Carry forward unchanged commitments at subsequent reviews.)*

**Commitment summary table:**

| C# | Commitment name | Metric | Target | Baseline | Owner | Protection level |
|----|----------------|--------|--------|----------|-------|-----------------|
| C1 | `[Name]` | `[Metric]` | `[Target]` | `[Prior period actual]` | `[Role]` | `[See below]` |
| C2 | `[Name]` | `[Metric]` | `[Target]` | `[Prior period actual]` | `[Role]` | `[See below]` |
| C3 | `[Name]` | `[Metric]` | `[Target]` | `[Prior period actual]` | `[Role]` | `[See below]` |

*(Add rows for each commitment. Common commitments include: New Enterprise ARR,
Expansion ARR, Net Revenue Retention, Pipeline Created, Partner-Sourced Pipeline,
Product Adoption Rate, Gross Margin, CAC Ratio, Consumption Revenue.)*

---

**For each commitment, complete the definition block below.**

*(Repeat once per commitment. The metric definition governs inclusion/exclusion rules
for that commitment's contribution bridge, evidence-supported base, and bet attribution.
If two commitments share a metric, they must still be defined separately with their
own inclusion/exclusion rules.)*

---

**Commitment `[C_]` — `[Name]`** `[init]`

Metric name: `[Full metric name]`

Metric definition:
*(Precise statement of what is being measured.)*
```
[
]
```

Inclusion rules:
```
[What counts toward this commitment metric]
```

Exclusion rules:
*(Critical for preventing double-counting across commitments. If C1 is New Enterprise
ARR, expansion and renewal ARR must be explicitly excluded here.)*
```
[What does not count]
```

Recognition rule:
*(When does an outcome count — contract signature, revenue recognition, adoption
milestone, activation threshold?)*
```
[
]
```

Time horizon: `[This fiscal year / Calendar year / Rolling 12 months]`

Source of record: `[CRM / Finance system / Data warehouse / Other]`

Reporting currency: `[USD / EUR / GBP / Other]`

Protection level:
```
[ ] Board commitment — cannot be revised without board action
[ ] Leadership commitment — can be revised with CRO / CFO / CEO agreement
[ ] Operating target — can be revised through standard operating review
[ ] Reference only — not a binding commitment
```

Revision authority: `[Role or body that can authorize a revision to this commitment]`

---

*(Repeat commitment definition block for each commitment.)*

---

### A3 — Portfolio Accounting `[init]`

*(Gap calculation. References commitment IDs from A2. The Loop tracks attainability
separately for each commitment, but the primary commitment drives portfolio mode inference.)*

**Primary commitment for portfolio attainability tracking:** `[C_ from A2]`

**Evidence-supported base for primary commitment:**
*(The portion of the primary commitment target expected from the base business
regardless of whether any strategic bet succeeds. Must use the same metric and
exclusion rules defined for that commitment in A2.)*

Amount: `[$X.XM]`
Derivation: `[How this was reached — finance model, prior-year expansion rate,
known renewal uplift, base territory historical performance]`

**Gap to be covered by strategic bets:** `[$X.XM]`
*(Primary commitment target minus evidence-supported base)*

**Active bets in this portfolio:** `[n]`

**Non-negotiable commitment designations:**
*(Non-negotiability attaches to the commitment, not automatically to a specific bet.
A failed bet only breaches a non-negotiable commitment if no credible alternative
path to fulfilling the commitment remains.)*

| Commitment | Protection level | Consequence if breached | Alternative paths if primary bet fails |
|------------|-----------------|------------------------|---------------------------------------|
| `[C_]` | `Non-negotiable / Protected / Leadership expectation` | `[What follows]` | `[Other bets or mechanisms that could fulfill this commitment]` |

---

### A4 — Strategic Bets `[init]`

*(One block per active bet. In Module B, bets unchanged since the last review may
be summarized as "No change since [date]." Complete the full block for all bets
at initialization and for any new bet added mid-year.)*

---

#### Bet `[ID]` — `[Bet Name]`

**Bet owner:** `[Name / Role]` `[init]`
**Executive sponsor:** `[Name / Role]` `[init]`

**Strategic hypothesis:** `[init]`
*(Complete: "We believe that [market / customer / product premise] will allow us to
generate [contribution] by [mechanism] in [timeframe].")*
```
[Full hypothesis statement]
```

**Target contribution:** `[$X.XM in the primary commitment metric]` `[init]`

**Bet priority classification:** `[init]`
```
[ ] Strategically protected — core to long-term positioning; maintain even under pressure
[ ] Leadership required — CRO / CEO has directed this bet proceed
[ ] Contractually required — external commitment requires this bet's execution
[ ] Experimental — testing a hypothesis; not load-bearing for portfolio attainability
[ ] Discretionary — can be deprioritized if resource pressure demands
```

**Initiatives linked to this bet:** `[opt]`

| Initiative | Owner | Start date | Budget allocated | Status |
|-----------|-------|-----------|-----------------|--------|
| `[Description]` | `[Owner]` | `[YYYY-MM-DD]` | `[$X.XM]` | `Active / Planned / Blocked` |

**Decision rights:** `[pvt]`

| Decision type | Decision maker | Approver | Escalation path |
|--------------|----------------|----------|----------------|
| Bet launch or activation | `[Role]` | `[Role]` | `[Role]` |
| Pivot or intervention | `[Role]` | `[Role]` | `[Role]` |
| Escalation brief issued | `[Role]` | `[Role]` | `[Role]` |
| Portfolio Adaptation required | `[Role]` | `[Role]` | `[Role]` |
| Non-negotiable breach response | `[Role]` | `[Role]` | `[Role]` |

---

##### A4.0 — Commitment Mapping and Core Guardrails `[init]`

*(Required at initialization. The Loop cannot perform Planning mode assessment
without knowing which commitments each bet affects, in which direction, and what
core quality and capacity constraints apply. A plan approved without this section
has not been pressure-tested.)*

**Commitment effects:** `[init]`
*(List every commitment this bet touches — positively or negatively. A pivot that
improves C1 contribution while breaching C2's retention floor should not be
recommended without surfacing the tradeoff. That detection depends on this table.)*

| Commitment | Effect | Expected contribution or impact | Metric | Notes |
|------------|--------|-------------------------------|--------|-------|
| `[C_]` — Primary | `Positive contribution` | `[$X.XM]` | `[Same metric as C_]` | `[Primary commitment this bet is designed to fulfill]` |
| `[C_]` — Secondary | `Positive / Neutral / Negative` | `[$X.XM or qualitative]` | `[Metric]` | `[Describe how this bet affects the secondary commitment]` |
| `[C_]` — Risk | `Potential negative` | `[Description]` | `[Metric]` | `[e.g., "Aggressive discounting may harm gross margin commitment"]` |

**Core guardrail metrics:** `[init]`
*(Floors and ceilings that must not be violated in pursuit of this bet's primary
contribution. Guardrails protect portfolio health, organizational durability, and
long-term commitment quality. They are required at initialization — not after the
plan is approved. Remove rows that do not apply; add guardrails specific to this
bet's mechanism.)*

| Guardrail | Metric | Threshold | Evidence source | Consequence if breached |
|-----------|--------|-----------|----------------|------------------------|
| `[CAC ceiling]` | `[Customer Acquisition Cost]` | `[≤ $X,XXX per logo]` | `[Finance / CRM]` | `[Bet must pause pending margin review]` |
| `[Gross margin floor]` | `[Deal-level gross margin]` | `[≥ X%]` | `[Deal desk / Finance]` | `[Deals below threshold require CFO approval]` |
| `[Discount ceiling]` | `[Maximum discount rate]` | `[≤ X%]` | `[Deal desk]` | `[Above ceiling requires VP approval; affects NRR forecast]` |
| `[Delivery capacity ceiling]` | `[New enterprise onboards per quarter]` | `[≤ n per quarter]` | `[Services capacity model]` | `[Exceeding capacity creates churn risk and commitment drag]` |
| `[Churn floor]` | `[Gross retention rate]` | `[≥ X%]` | `[CS platform / Finance]` | `[Indicates growth is unsustainable; triggers CCO review]` |
| `[Concentration ceiling]` | `[Single-customer share of bet contribution]` | `[≤ X%]` | `[CRM / Finance]` | `[Revenue quality risk; triggers portfolio risk review]` |
| `[Brand or regulatory restriction]` | `[Description]` | `[Description]` | `[Legal / Compliance]` | `[Legal exposure or reputational risk]` |

**Pivot-specific guardrail analysis:** `[pvt]`
*(When Adaptation is triggered, supply additional guardrail analysis specific to
the options under evaluation — including options that may interact with guardrails
not tested in normal operations. The Loop checks every option against all guardrails
in this section before surfacing a recommendation.)*

---

##### A4.1 — Bet Timing `[init for peak window; pvt for full chain]`

*(The Loop uses these inputs to compute: latest useful decision date, latest useful
launch or deployment date, and the Endgame threshold for this specific bet.
Different bets have different timelines. Supply what you know; the Loop computes
derived dates and reports what is missing.)*

**Desired commercial outcome or recognition date:** `[YYYY-MM-DD]` `[init]`

**Known contractual or operational deadlines:** `[YYYY-MM-DD]` `[init if applicable]`

**Fixed external event dates that constrain this bet:** `[opt]`

**Implementation lead time:** `[n days]` `[init]`
*(From decision to first pipeline or demand impact.)*

**Time to first leading signal:** `[n days]` `[asm]`

**Pipeline or adoption build time:** `[n days]` `[pvt]`

**Average sales, procurement, or realization cycle:** `[n days]` `[pvt]`

**Revenue, adoption, or recognition lag:** `[n days]` `[pvt]`

**Pivot-specific time to impact:** `[opt]`
*(If a redirect is deployed, does time-to-impact change from the initial bet? Describe
if known. The Loop will request this when Adaptation is triggered.)*
```
[
]
```

---

##### A4.2 — Assumptions `[asm]`

*(Every assumption that must hold for this bet to generate its target contribution.
The Loop infers structural status and current-horizon status from the evidence you
supply. Do not assign statuses. Supply the facts; the Loop determines the status.)*

*(One block per assumption.)*

---

**Assumption `[B_-A_]`**

**Statement:** `[init]`
*(The specific, falsifiable claim that must be true.)*
```
[
]
```

**Assumption type:** `[asm]`
```
[ ] Market — about customer behavior, demand, or segment dynamics
[ ] Product — about product availability, capability, or adoption pattern
[ ] Competitive — about competitor behavior or positioning
[ ] Organizational — about internal capacity, execution, or alignment
[ ] External — about regulatory, macroeconomic, or partner environment
[ ] Operational — about delivery, implementation, or process performance
```

**Load-bearing or marginal:** `[init]`
```
[ ] Load-bearing — if this assumption fails, the bet fails at target contribution
[ ] Marginal — if this fails, contribution is reduced but the bet can still deliver
```

**Controllability:** `[asm]`
```
[ ] Fully controllable — bet owner can directly determine the outcome
[ ] Partially controllable — bet owner can influence but not determine the outcome
[ ] Not controllable — external; bet owner can only observe and respond
```

**Internal or external:** `[asm]`
```
[ ] Internal — depends on decisions and actions within the organization
[ ] External — depends on market, customer, partner, regulator, or competitor
```

**Commitments affected if this assumption fails:** `[asm]`
`[Which commitments from A2 would be materially affected]`

**Evidence at planning time:** `[init]`
*(What evidence supported this assumption when the bet was established?
Include source, date, and known limitations.)*
```
[
]
```

**Owner-stated confidence at planning:** `[init]`
`[High / Medium / Low / Insufficient to assess]`

*(This is the bet owner's judgment at planning time. The Loop separately infers
Evidence-Assessed Confidence and will report divergence between the two. Owner-stated
confidence is not treated as evidence by the Loop.)*

**Leading indicator:** `[asm]`
*(The specific, observable signal that will confirm or challenge this assumption.)*
```
[What is measured, how it is measured, and from which source]
```

**Expected signal window:** `[asm]`
```
[When should this indicator produce a meaningful reading?]
```

**Normal variance:** `[asm]`
*(Expected noise in the indicator that does not constitute a signal.)*
```
[
]
```

**Warning threshold:** `[asm]`
```
[Indicator value or event that triggers heightened attention]
```

**Invalidation threshold:** `[asm]`
```
[Indicator value or event that invalidates this assumption]
```

**Restoration evidence:** `[asm]`
*(What would need to be true to restore a weakened or invalidated assumption?
Note if restoration is structurally impossible.)*
```
[
]
```

**Hard seasonal or fiscal constraints:** `[init if applicable]`
*(Any date after which current-year contribution from this assumption becomes impossible
regardless of structural recovery.)*
```
[
]
```

---

**Current-period evidence update `[B]`:**
*(In recurring updates, supply only new evidence. The Loop carries forward prior status.
Do not declare whether a threshold was crossed — the Loop infers status from indicator
values and your defined thresholds. Supply the raw readings so the Loop can compare them.)*

| Evidence field | New entry |
|----------------|-----------|
| Supporting evidence | `[Source and date — or none]` |
| Contradicting evidence | `[Source and date — or none]` |
| Indicator result | `[Current value with units, e.g. "win rate: 34%" or "3 deals cited competitor as reason"]` |
| Signal date | `[YYYY-MM-DD]` |
| Threshold comparison notes | `[Optional context to help the Loop compare this reading against defined thresholds, e.g. "Win threshold is 40%; this reading covers Q2 closed deals only"]` |
| Organizational events relevant to this assumption | `[Description]` |

---

*(Repeat assumption block for each assumption.)*

---

##### A4.3 — Seasonal Operating Curve `[init for peak window; opt for full curve]`

*(Supply the expected seasonal profile for this bet. The Loop uses this curve and
the current date to infer Season Position and Season Readiness, and to determine
whether actuals are on pace against the seasonally expected path. Do not state
current position — supply the calendar and evidence.)*

**Seasonal calendar for this bet:**

| Window | Start | End | Description |
|--------|-------|-----|-------------|
| Preparation | `[Date]` | `[Date]` | `[What must complete before pipeline build begins]` |
| Pipeline build | `[Date]` | `[Date]` | `[When outbound, partner, or demand-gen produces qualified opportunities]` |
| Qualification / evaluation | `[Date]` | `[Date]` | `[When prospects are typically in active evaluation]` |
| Procurement / implementation | `[Date]` | `[Date]` | `[When signed deals go through legal, procurement, or deployment]` |
| Peak conversion / adoption | `[Date]` | `[Date]` | `[Primary contribution recognition window]` `[init]` |
| Post-peak tail | `[Date]` | `[Date]` | `[Residual contribution; significantly lower volume]` |
| Off-season / blackout | `[Date]` | `[Date]` | `[Window when demand is structurally absent]` |

**Expected contribution by period:** `[opt]`

| Period | Expected contribution | Cumulative expected | Notes |
|--------|-----------------------|---------------------|-------|
| `[Month or Quarter 1]` | `[$X.XM]` | `[$X.XM]` | |
| `[Month or Quarter 2]` | `[$X.XM]` | `[$X.XM]` | |
| `[Month or Quarter 3]` | `[$X.XM]` | `[$X.XM]` | |
| `[Month or Quarter 4]` | `[$X.XM]` | `[$X.XM]` | |

**Known next-year carryover behavior:** `[opt]`
```
[Does late-cycle pipeline typically slip to the following year?]
```

**Historical evidence for this seasonal curve:** `[asm]`
```
[Prior-year win data, industry patterns, or prior campaign results.
If this is a first-year bet, state that explicitly.]
```

**Confidence in the curve:** `[asm]`
`[High / Medium / Low / First-year bet — no historical baseline]`

*(This is user-supplied confidence in the curve itself, not an assessment of current
readiness. The Loop infers readiness from gate evidence.)*

---

##### A4.4 — Readiness Gates `[init for required gates; opt for supporting]`

*(Seven general gates apply to every bet. Supply evidence for each applicable gate.
The Loop infers gate status and overall season readiness from that evidence. Do not
assess readiness yourself.)*

---

**Gate 1 — Market Readiness**
*Is the target market ready to purchase, adopt, or engage with what this bet requires?*

Applicability: `[ ] Required  [ ] Supporting  [ ] N/A` `[init]`

Required condition: `[init]`
`[What must be true]`

Evidence: `[asm]`
```
[Current state evidence with source and date]
```

Owner: `[pvt]` `[Role]`
Deadline: `[init if Required]` `[Date]`
Recovery option if missed: `[pvt]`
Consequence if missed: `[pvt]`

---

**Gate 2 — Product Readiness**

Applicability: `[ ] Required  [ ] Supporting  [ ] N/A` `[init]`

Required condition: `[init]`

Evidence: `[asm]`
```
[Product milestone status, committed dates, gaps, and timeline risk]
```

Owner: `[pvt]`
Deadline: `[init if Required]`
Recovery option if missed: `[pvt]`
Consequence if missed: `[pvt]`

---

**Gate 3 — Field Readiness**

Applicability: `[ ] Required  [ ] Supporting  [ ] N/A` `[init]`

Required condition: `[init]`

Evidence: `[asm]`
```
[Training, certification, capacity evidence. Champion quality and economic-buyer
engagement evidence appear here as sub-gate evidence where relevant to this bet.]
```

Owner: `[pvt]`
Deadline: `[init if Required]`
Recovery option if missed: `[pvt]`
Consequence if missed: `[pvt]`

---

**Gate 4 — Partner Readiness**

Applicability: `[ ] Required  [ ] Supporting  [ ] N/A` `[init]`

Required condition: `[init if Required]`

Evidence: `[asm]`
```
[Agreement status, enablement, capacity, pipeline evidence]
```

Owner: `[pvt]`
Deadline: `[init if Required]`
Recovery option if missed: `[pvt]`
Consequence if missed: `[pvt]`

---

**Gate 5 — Pipeline or Demand Readiness**

Applicability: `[ ] Required  [ ] Supporting  [ ] N/A` `[init]`

Required condition: `[init]`

Evidence: `[asm]`
```
[Pipeline count and value by stage, coverage ratio, new pipeline rate, demand signals]
```

Owner: `[pvt]`
Deadline: `[init if Required]`
Recovery option if missed: `[pvt]`
Consequence if missed: `[pvt]`

---

**Gate 6 — Operational Delivery Readiness**

Applicability: `[ ] Required  [ ] Supporting  [ ] N/A` `[init]`

Required condition: `[init]`

Evidence: `[asm]`
```
[Capacity model, current utilization, planned additions, delivery track record]
```

Owner: `[pvt]`
Deadline: `[init if Required]`
Recovery option if missed: `[pvt]`
Consequence if missed: `[pvt]`

---

**Gate 7 — Economic Readiness**

Applicability: `[ ] Required  [ ] Supporting  [ ] N/A` `[init]`

Required condition: `[init]`

Evidence: `[asm]`
```
[Pricing approval, budget release, deal desk capacity, discount authority]
```

Owner: `[pvt]`
Deadline: `[init if Required]`
Recovery option if missed: `[pvt]`
Consequence if missed: `[pvt]`

---

##### A4.5 — Dependencies `[init for known dependencies; asm for full evidence]`

*(A roadmap item without a committed date and a named owner is not a planning-grade
dependency. Record it under the relevant assumption's evidence instead.)*

---

**Dependency `[D_]` — Product** `[init for existence; asm for full evidence]`

Description: `[What is required and from which team]`
Required by: `[Date]`

Evidence:
- Committed delivery date confirmed in writing: `[Yes — source / No / Pending]`
- Named engineering or delivery owner: `[Name / Role — or "Not assigned"]`
- Intermediate milestones and status: `[List milestones with dates and status]`
- Beta or UAT plan: `[Yes — describe / No]`
- Resourcing confirmed: `[Yes / No / Partial]`
- Second-order dependencies: `[Closed / Open — list unresolved]`
- Prior delivery reliability: `[Yes / No / Mixed — evidence]`
- Executive sponsor committed: `[Written / Public / Not committed]`
- Schedule buffer: `[n days / None]`

---

**Dependency `[D_]` — Headcount** `[init for existence; asm for full evidence]`

Description: `[Role(s) and count needed]`
Required in seat and producing by: `[Date]`

Evidence:
- Approved requisition: `[Number and date — or "Not approved"]`
- Recruiting status: `[Not started / In progress / Offer extended / Accepted]`
- Start date confirmed: `[YYYY-MM-DD — or "Not confirmed"]`
- Ramp time to productivity: `[n days]`
- Impact if delayed: `[Which bet activity is blocked]`

---

**Dependency `[D_]` — Partner** `[init for existence; asm for full evidence]`

Description: `[What the partner must deliver]`
Required by: `[Date]`

Evidence:
- Agreement status: `[Unsigned / In negotiation / Signed — date]`
- Enablement completion: `[Not started / In progress / Complete]`
- Confirmed partner capacity: `[n reps / n deals / n activations — or "Not confirmed"]`
- First registered opportunities: `[Count and value — or "None yet"]`
- Partner commitment to timeline: `[Written / Verbal / Not confirmed]`

---

**Dependency `[D_]` — Budget** `[init for existence; asm for full evidence]`

Description: `[What spend is required]`
Required available by: `[Date]`

Evidence:
- Approval status: `[Approved / Pending / Not yet submitted]`
- Approval authority: `[Role]`
- Expected release date: `[Date]`
- Procurement lead time: `[n days]`
- Activity blocked if not approved: `[Description]`

---

**Dependency `[D_]` — External or Regulatory** `[init for existence; asm for full evidence]`

Description: `[Regulatory change, certification, or external event]`
Required by: `[Date]`

Evidence:
- Authoritative confirmation source: `[Regulator / Standards body / Legal — document or URL]`
- Effective date: `[Confirmed / Estimated — date and basis]`
- Scope on this bet: `[Which deals or segments are affected]`
- Confidence in confirmation: `[Official / Draft / Anticipated — basis]`

---

**Dependency `[D_]` — Operational** `[init for existence; asm for full evidence]`

Description: `[Internal process, system, or capacity]`
Required by: `[Date]`

Evidence:
- Named owner: `[Role]`
- Milestone plan: `[Yes — summarize / No]`
- Current capacity: `[Quantify]`
- Required capacity: `[Quantify]`
- Delivery track record: `[Yes / No / Mixed — evidence]`

---

##### A4.6 — Indicators and Thresholds Summary `[asm]`

*(Consolidated reference for the Loop across all assumptions for this bet.
Detailed fields live in each assumption block in A4.2.)*

| Assumption ID | Indicator | Source | Frequency | Normal range | Warning | Invalidation |
|---------------|-----------|--------|-----------|-------------|---------|-------------|
| `[B_-A_]` | `[What is measured]` | `[Source]` | `[Frequency]` | `[Expected range]` | `[Warning trigger]` | `[Invalidation trigger]` |

---

##### A4.7 — Available Intervention Levers `[pvt]`

*(List interventions feasible for this bet. Used by the Loop in Adaptation to generate
the option set. Feasibility constraints from A3 and decision rights from A4 apply.
All levers are checked against guardrails in A4.0 before the Loop surfaces them.)*

| Lever | Description | Time to first impact | Time to contribution | Resource required | Reversibility | Guardrail risk |
|-------|-------------|---------------------|---------------------|-------------------|---------------|----------------|
| `[Name]` | `[What this lever does]` | `[n days]` | `[n days]` | `[Resource]` | `Fully / Partially / Irreversible` | `[Which guardrail this might breach and under what conditions]` |

---

##### A4.8 — User Assessment `[opt]`

*(Qualitative view. The Loop compares user assessment against signal data.
Divergence between the two is analytically relevant and will be noted.)*

**What is working:**
```
[
]
```

**What is not working:**
```
[
]
```

**What has changed since the last review:**
```
[
]
```

**Organizational facts specific to this bet not reflected elsewhere:**
```
[
]
```

---

*(End of Bet `[ID]` block. Repeat A4 for each additional bet.)*

---

### A5 — Portfolio Contribution Bridge — Forecast `[init]`

*(Use during Planning, Monitoring, Adaptation, and Endgame triage before fiscal close.
Adaptation requires an updated forecast bridge to show how a pivot changes portfolio
attainability. Do not switch to Year-End Actual Reconciliation until results are
verified closed. See Module D.)*

*(If the portfolio has multiple commitments from A2, the forecast bridge applies to
the primary commitment. Separate tracking for secondary commitments is noted in A4.0.)*

| Line item | Amount | Notes |
|-----------|--------|-------|
| Evidence-supported base | `$[X.XM]` | `[In primary commitment metric from A2]` |
| `B_` — `[Bet name]` expected contribution | `$[X.XM]` | |
| `B_` — `[Bet name]` expected contribution | `$[X.XM]` | |
| `[Additional bets]` | `$[X.XM]` | |
| **Gross forecast** | **`$[X.XM]`** | |
| Capacity deduction | `($[X.XM])` | `[Which constraint]` |
| Dependency-risk adjustment | `($[X.XM])` | `[Which dependency, current status]` |
| Seasonal concentration adjustment | `($[X.XM])` | `[Which bets, which window]` |
| Probability adjustment | `($[X.XM])` | `[Which bets, rationale]` |
| Contribution overlap deduction | `($[X.XM])` | `[Which bets share addressable accounts]` |
| **Risk-adjusted forecast** | **`$[X.XM]`** | |

---

### A6 — Prior-Year Carry-Forward Learning `[opt]`

*(Not required at first use. Required on every subsequent annual initialization.)*

**What worked — by bet:**

| Bet | What worked | Evidence |
|-----|------------|----------|
| `[B_]` | `[Mechanism or decision]` | `[Outcome evidence]` |

**What did not work — by bet:**

| Bet | What failed | Root cause | Signal that was missed or misread |
|-----|------------|------------|-----------------------------------|
| `[B_]` | `[What failed]` | `[Why]` | `[Retrospective signal identification]` |

**Assumption outcomes:**

| Assumption ID | Final outcome | Implication for this year |
|---------------|--------------|---------------------------|
| `[B_-A_]` | `[Held / Weakened / Invalidated — what happened]` | `[How this informs the current portfolio]` |

**Seasonal curve refinements:**
```
[Updates to expected windows or contribution distributions based on prior actuals]
```

**Bets carried forward with updated hypotheses:**
```
[What changed in the hypothesis or assumptions]
```

---

### A7 — Imported Loop Findings `[opt]`

*(Findings from the Win/Loss Pattern Loop or Pipeline Risk Loop that affect assumptions
or strategy in this portfolio. Every finding must be attributed, scoped, and linked
to the specific assumptions it affects.)*

**Win/Loss Pattern Loop findings:**

| Finding | Source (version / date) | Mech. confidence | Prev. confidence | Cohort | Period | Denominator | Scope and limitations | Last validated | Assumptions affected |
|---------|------------------------|-----------------|-----------------|--------|--------|-------------|----------------------|----------------|---------------------|
| `[Pattern]` | `[v_, YYYY-MM-DD]` | `High/Med/Low` | `High/Med/Low` | `[Segment]` | `[Period]` | `[n deals]` | `[Limitations]` | `[Date]` | `[B_-A_ list]` |

**Pipeline Risk Loop findings:**

| Finding | Source (version / date) | Risk type | Confidence | Cohort | Period | Denominator | Scope | Last validated | Assumptions affected |
|---------|------------------------|----------|------------|--------|--------|-------------|-------|----------------|---------------------|
| `[Risk]` | `[v_, YYYY-MM-DD]` | `[Type]` | `High/Med/Low` | `[Segment]` | `[Period]` | `[n]` | `[Limits]` | `[Date]` | `[B_-A_ list]` |

---

### A8 — External Market and Industry Signals `[opt]`

| Signal | Source | Date | Geography / segment | Type | Reliability | Materiality | Assumptions affected | Last refreshed | Contradictory evidence |
|--------|--------|------|---------------------|------|-------------|-------------|---------------------|----------------|----------------------|
| `[Description]` | `[Source]` | `[YYYY-MM-DD]` | `[Scope]` | `Fact / Forecast / Opinion / Data` | `High/Med/Low` | `High/Med/Low` | `[B_-A_ list]` | `[YYYY-MM-DD]` | `[Conflicts]` |

---

### A9 — Version Ledger `[pvt — required before any revision is recorded]`

*(The Loop may revise the plan. It must never rewrite what the organization originally
believed. Every revision to a commitment target, assumption statement, threshold,
seasonal window, latest useful date, contribution expectation, metric definition, or
intervention success criterion must be recorded here alongside the original value.
Prior assessments calculated under the old version remain visible and are never
overwritten. A revised assumption that makes the plan appear healthy again is not
the same as evidence that the plan is healthy.)*

*(Add one row per revision. Revisions may occur at any review.)*

| Revision ID | Date | Item revised | Original value | Revised value | Change type | Evidence prompting revision | Decision owner | Approver | Impact on contribution bridge | Prior assessments under old version |
|-------------|------|-------------|---------------|---------------|-------------|----------------------------|----------------|----------|------------------------------|-------------------------------------|
| `[R01]` | `[YYYY-MM-DD]` | `[e.g., B1-A2 warning threshold / C1 target / B2 seasonal peak end date]` | `[Exact original value]` | `[Exact revised value]` | `New learning / External change / Execution correction / Formal target accommodation` | `[Evidence: source, date, what it showed]` | `[Role]` | `[Role]` | `[How this changes the forecast bridge and by how much]` | `[Loop-maintained: prior status, prior contribution estimate, prior attainability assessment under old value]` |

**Change type definitions:**

| Type | Meaning |
|------|---------|
| New learning | Evidence has arrived that genuinely changes what the organization knows |
| External change | An external event has changed the facts the assumption was based on |
| Execution correction | The original value contained a factual error now corrected |
| Formal target accommodation | The target or threshold is being revised to match changed expectations, not changed evidence |

*(Formal target accommodation is the most consequential change type. It means the
organization is revising down what it expects rather than discovering new information.
The Loop must preserve the original commitment and track cumulative revision history.)*

---

## MODULE B — Recurring Update

*Use at monthly operating reviews, QBRs, and routine Monitoring passes.
The Loop carries forward all prior state. Supply only what has changed.
If nothing has changed for a bet, note the Bet ID and "No change since [date]."*

---

### B1 — Review Context `[ALL]`

**Review type:**
```
[ ] Monthly operating review
[ ] QBR
[ ] Urgent reassessment
[ ] Executive decision review
```

**Review date:** `[YYYY-MM-DD]`

**Organizational events since last review:**
```
[Event 1 — Date: YYYY-MM-DD — Description: ]
[Event 2 — Date: YYYY-MM-DD — Description: ]
```

**Commitment-level progress (optional — for commitments with independent tracking):**

| Commitment | Actual to date | Plan to date | Variance |
|------------|---------------|-------------|---------|
| `[C_]` | `[$X.XM or X%]` | `[$X.XM or X%]` | `[+/- amount]` |

---

### B2 — Per-Bet Signal Update

*(One block per bet with new information. Omit unchanged bets.)*

---

**Bet `[ID]` — `[Bet Name]`**

**Actuals this period:**
- Closed / recognized contribution: `[$X.XM in primary commitment metric]`
- Period: `[Month or Quarter]`
- Source: `[CRM / Finance / Other]`
- Cumulative contribution to date: `[$X.XM]`

**Guardrail readings (if any guardrail metric has moved):**

| Guardrail | Current reading | Threshold | Movement since last review |
|-----------|----------------|-----------|---------------------------|
| `[CAC / Margin / Discount / etc.]` | `[Value]` | `[Threshold]` | `[Direction and magnitude]` |

**Pipeline snapshot:**

| Stage | Count | Value | Change since last review |
|-------|-------|-------|--------------------------|
| `[Stage 2]` | | | `[+/- n deals or $X.XM]` |
| `[Stage 3]` | | | |
| `[Stage 4]` | | | |
| `[Stage 5 / Commit]` | | | |

**New pipeline added this period:** `[$X.XM from n opportunities]`

**At-risk open opportunities (new or changed):**

| Opportunity | Value | Stage | Change or risk |
|-------------|-------|-------|----------------|
| `[Name]` | `[$X.XM]` | `[n]` | `[What changed]` |

---

**Assumption evidence updates:**
*(New evidence only. The Loop carries forward prior status and updates it from the delta.
Do not declare whether a threshold was crossed — supply indicator readings and the Loop
will compare them against defined thresholds. Add threshold comparison notes if the
reading requires context to interpret correctly, e.g. cohort scope or coverage period.)*

| Assumption ID | New supporting evidence | New contradicting evidence | Indicator result | Signal date | Threshold comparison notes | Org. events relevant |
|---------------|------------------------|---------------------------|------------------|-------------|---------------------------|-----------------------|
| `[B_-A_]` | `[Source, date — or none]` | `[Source, date — or none]` | `[Value with units]` | `[YYYY-MM-DD]` | `[Optional: context for comparing this reading to defined thresholds]` | `[Description]` |

---

**Dependency updates (changed status only):**

| Dependency ID | What changed | Evidence | Date |
|---------------|-------------|---------|------|
| `[D_]` | `[Description]` | `[Evidence]` | `[YYYY-MM-DD]` |

---

**Readiness gate evidence updates (new evidence only):**

| Gate | New evidence | Owner update | Date |
|------|-------------|-------------|------|
| `[Gate name]` | `[Evidence]` | `[Change if any]` | `[YYYY-MM-DD]` |

---

**Revisions to record in A9 (if any values changed this period):**

| Item revised | Original value | Revised value | Change type | Evidence |
|-------------|---------------|---------------|-------------|---------|
| `[Description]` | `[Original]` | `[Revised]` | `[Type]` | `[Evidence]` |

---

**User assessment update (only if view has changed):**
```
[What changed and why]
```

---

*(Repeat B2 for each bet with new information.)*

---

### B3 — Cross-Portfolio Signal Update

**New shared dependency risks:** `[Description, bets affected, timeline impact]`

**Resource conflicts that have emerged:** `[Description, bets competing for same resource]`

**Cross-commitment conflicts identified:**
*(Has any bet's actual performance revealed a tradeoff between commitments that was
not visible at planning? e.g., aggressive discounting improving C1 ARR while
eroding C2 retention?)*
```
[
]
```

**Contribution overlap newly identified:** `[Deals at risk of multi-bet attribution]`

**Portfolio-level upside signal:** `[Bet outperforming — reallocation opportunity?]`

**Portfolio-level risk signal:** `[Multiple bets below pace or shared dependency failing]`

---

### B4 — Updated Contribution Bridge

*(Submit only if the numbers have changed. List only changed lines.)*

| Line item | Previous | Updated | Change driver |
|-----------|----------|---------|-------------|
| `[Line]` | `$[X.XM]` | `$[X.XM]` | `[What changed]` |

---

## MODULE C — Adaptation Annex

*Complete when the Loop or the user believes a pivot decision is required.
The Loop evaluates Hold as Option 0 — with explicit costs, benefits, and guardrail
impact — before evaluating any alternative.*

---

### C1 — Trigger and Context

**What evidence triggered consideration of Adaptation:**
```
[
]
```

**Type of trigger:**
```
[ ] Failure-side — a bet is falling short and an intervention is needed
[ ] Upside-side — a bet is outperforming and reallocation may be warranted
[ ] Both
```

**Bets under consideration:**

| Bet ID | Reason |
|--------|--------|
| `[B_]` | `[What you have observed]` |

**Cross-commitment concern (if applicable):**
*(Is there evidence that a pivot to improve one commitment would harm another?
State what you've observed; the Loop will evaluate.)*
```
[
]
```

---

### C2 — Replacement-Bet Feasibility Evidence

*(Required when evaluating reallocation. The Loop evaluates all ten feasibility
questions from this evidence. It also checks each option against guardrails in A4.0
before surfacing a recommendation.)*

**Candidate bet receiving reallocation:** `[Bet ID and name]`
**Gap to be absorbed:** `[$X.XM from which failing bet]`

| Question | Evidence to supply |
|----------|-------------------|
| 1 — Incremental addressable demand | `[Market size, whitespace analysis, saturation indicators]` |
| 2 — Available pipeline | `[Pipeline outside current bet coverage]` |
| 3 — Additional capacity | `[Capacity model, utilization, available additions and timing]` |
| 4 — Sales-cycle feasibility | `[Cycle length, days remaining, implementation lag]` |
| 5 — Saturation and diminishing returns | `[Win rate trend, deal size trend, competitive density]` |
| 6 — Cannibalization | `[Overlap with other bets or existing accounts]` |
| 7 — Pull-forward versus incremental | `[Pipeline vintage, customer purchase cycle]` |
| 8 — Shared dependencies | `[Shared product, headcount, partner, or delivery constraints]` |
| 9 — Disruption to working bets | `[Resource conflict across all active bets]` |
| 10 — Maximum credible incremental contribution | `[Conservative ceiling with derivation]` |

---

### C3 — Decision Constraints

**Budget available for interventions:** `[$X.XM — approval required from: Role]`

**Headcount reallocation limits:** `[What can and cannot be moved]`

**Partner or channel constraints:** `[Partner capacity, agreement restrictions]`

**Executive appetite for formal target revision:** `[Yes / No / Uncertain]`

**Board or commitment constraints:** `[What requires external approval]`

**Guardrail constraints on available options:**
*(Are there guardrails from A4.0 that rule out certain intervention types entirely?
e.g., "CAC ceiling rules out mid-market volume play")*
```
[
]
```

**Decisions that must be made before the next review:**
```
[
]
```

---

### C4 — Options Under Consideration

*(List options you are considering. The Loop evaluates Hold as Option 0 with explicit
costs, benefits, and guardrail impact before evaluating alternatives. Every option is
evaluated against the guardrail metrics in A4.0 before the Loop recommends it.)*

| Option | Description | Expected effect on primary commitment | Expected guardrail effects | Guardrail breach risk | Your initial view |
|--------|-------------|--------------------------------------|---------------------------|-----------------------|------------------|
| Hold | Continue current course | `[Estimated contribution shortfall]` | `[Effect on CAC, margin, etc.]` | `[Which guardrails are at risk if you hold]` | `[Your view of the cost of holding]` |
| `[Option A]` | `[Description]` | `[$X.XM change to commitment metric]` | `[Guardrail effects]` | `[e.g., "Discount ceiling at risk"]` | `[Your view]` |
| `[Option B]` | `[Description]` | `[$X.XM change]` | `[Guardrail effects]` | `[e.g., "No guardrail risk identified"]` | `[Your view]` |

*(Do not omit the "Expected guardrail effects" column. A recommendation that improves
the primary commitment while breaching a guardrail must surface the tradeoff, not
hide it.)*

---

## MODULE D — Endgame and Year-End Annex

*Use at the formal year-end review, or when actual results are sufficiently closed
and verified. An Endgame review in October or November still uses the forecast bridge
from Module A5. Do not switch to the Year-End Actual Reconciliation prematurely.*

---

### D1 — Year-End Actual Reconciliation Bridge

*(Forecast-risk adjustments do not appear here. Only verified deductions: confirmed
overlap, attribution disputes, metric-scope exclusions. Reducing a prior forecast
deduction that was larger than actual overlap is not additional contribution — it is
a smaller negative.)*

**Verification status:**
```
[ ] Verified closed — fiscal year closed, results confirmed by Finance
[ ] Substantially closed — [n]% closed; open items: [describe]
[ ] Not yet closed — use forecast bridge in Module A5
```

| Line item | Amount | Notes |
|-----------|--------|-------|
| Evidence-supported base (actual) | `$[X.XM]` | |
| `B_` — `[Bet name]` actual contribution | `$[X.XM]` | `[Decompose by mechanism if multiple contributed]` |
| `B_` — `[Bet name]` actual contribution | `$[X.XM]` | |
| `[Additional bets]` | `$[X.XM]` | |
| **Gross actual contribution** | **`$[X.XM]`** | |
| Verified overlap / attribution deduction | `($[X.XM])` | `[Specific deals counted in multiple bets]` |
| Metric-scope exclusion | `($[X.XM])` | `[ARR not qualifying under metric definition in A2]` |
| **Unique `[primary commitment metric from A2]`** | **`$[X.XM]`** | `[Reportable result]` |

**Secondary commitment actuals (if tracked):**

| Commitment | Target | Actual | Notes |
|------------|--------|--------|-------|
| `[C_]` | `[Target]` | `[Actual]` | `[Attribution or deduction notes]` |

---

### D2 — Learning Record

*(Seeds Module A6 in next year's initialization.)*

**What worked — by bet:**

| Bet | What worked | Evidence | Transferable? |
|-----|------------|----------|--------------|
| `[B_]` | `[Mechanism or decision]` | `[Evidence]` | `Yes / No / Modified` |

**What did not work — by bet:**

| Bet | What failed | Root cause | Earlier signal missed |
|-----|------------|------------|----------------------|
| `[B_]` | `[What failed]` | `[Why]` | `[Retrospective signal]` |

**Assumption outcomes:**

| ID | Structural outcome | Horizon outcome | Key learning |
|----|--------------------|-----------------|--------------|
| `[B_-A_]` | `Held / Weakened / Invalidated` | `Active / Deferred / Invalidated` | `[Learning]` |

**Guardrail performance:**

| Guardrail | Was it breached? | Contributing bets | Learning for next year |
|-----------|-----------------|-------------------|------------------------|
| `[Guardrail name]` | `Yes / No / At risk only` | `[B_]` | `[What to adjust in next year's thresholds or levers]` |

**Version ledger retrospective:**
*(How many revisions were made during the year? What change types dominated?
What does this reveal about planning accuracy?)*
```
[
]
```

**What the Loop surfaced that would have been missed without it:**
```
[
]
```

**What the Loop missed or got wrong — and what inputs would have corrected it:**
```
[
]
```

---

## Loop Output Fields — Do Not Fill In

*(The Loop populates all fields below in its response.)*

```
=== PORTFOLIO ===

Observed Portfolio Mode:              [Planning / Monitoring / Adaptation /
                                       Endgame and Learning]
Transition trigger:                   [Evidence that caused a mode change, if any]
Primary commitment attainability:     [On track / At risk — recoverable /
                                       Below threshold — intervention required /
                                       Non-recoverable / Endgame]
Secondary commitment status:          [Per C_ from A2: On track / At risk / Breached]
Guardrail status — portfolio level:   [Any guardrail breached or at risk across bets]
Missing organizational events:        [What the Loop needed but was not supplied]
Portfolio-level recommendations:      [Mode-appropriate actions]

=== PER BET ===

Bet [ID] — [Name]
  Observed bet-level mode:            [Planning / Monitoring / Adaptation / Endgame]
  Bet maturity:                       [Hypothesis / Signal acquisition /
                                       Mechanism supported / Intervention testing /
                                       Established]
  Bet operational status:             [Active / Escalated / Formally at risk /
                                       Recovery / Discontinued / Carry-forward]
  Season position (inferred):         [Pre-season / Build / Pre-peak / Peak /
                                       Post-peak / Off-season]
  Season readiness (inferred):        [Not started / In progress on track /
                                       In progress at risk / Ready /
                                       Missed recoverable / Missed unrecoverable]
  Commitment contribution:            [Expected contribution to each commitment from A4.0]
  Commitment conflict:                [Any detected tradeoff between commitments]
  Guardrail status — this bet:        [Any guardrail metric at or approaching threshold]
  Latest useful decision date:        [YYYY-MM-DD — Loop-computed]
  Latest useful launch date:          [YYYY-MM-DD — Loop-computed]
  Calculation basis:                  [Timeline chain used]
  Bottleneck:                         [Constraining element in the chain]
  Confidence in dates:                [High / Medium / Low — and why]
  Missing inputs for date calc:       [What the user did not supply]
  Date last recalculated:             [YYYY-MM-DD]
  User override (if supplied):        [YYYY-MM-DD — with recorded reason]

=== PER ASSUMPTION ===

  [B_-A_]:
    Owner-stated confidence:          [From A4.2 — user-supplied at planning]
    Evidence-assessed confidence:     [Loop-inferred from available evidence]
    Confidence divergence:            [Gap between owner-stated and evidence-assessed,
                                       with reason — e.g., "Owner: High. Evidence: Low.
                                       Reason: supported by one external forecast, no
                                       internal demand evidence, no committed product
                                       milestone."]
    Structural status:                [Held / Weakened / Warning / Invalidated / Restored]
    Structural rationale:             [Evidence basis]
    Current-horizon status:           [Active / Deferred / Invalidated (current year) /
                                       Restored]
    Horizon rationale:                [Evidence and date constraints]

=== PER READINESS GATE ===

  Gate [1–7] — [Name]:
    Inferred status:                  [Met / In progress / At risk / Not started /
                                       Missed recoverable / Missed unrecoverable / N/A]
    Key evidence considered:          [What the Loop used]
    Gap to Met:                       [What must happen and by when]

=== PER DEPENDENCY ===

  [D_]:
    Inferred confidence:              [High / Medium / Low / Insufficient]
    Evidence gaps:                    [What was missing]

=== DECISION AND INTERVENTION LAYER ===

Recommendations:                      [Mode-appropriate decisions with rationale,
                                       confidence, and guardrail impact for each option]
Decision owners:                      [From A4 decision rights]
Approvers required:                   [From A4 decision rights]
Observation windows set:              [Start / end / trigger condition per intervention]
Next review trigger:                  [Date or event]

Non-negotiable breach notice:         [Issued only if evidence indicates a commitment
                                       designated non-negotiable is unattainable under
                                       any credible scenario. The Loop surfaces the
                                       breach — it does not decide what to do.]

Version ledger update:                [Any values that changed this period, recorded
                                       with original value, revised value, change type,
                                       and prior assessments under the old version]
```
