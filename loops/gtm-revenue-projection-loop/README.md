# Revenue Projection Loop — Toolkit Release 1.0

| Component | Version | Purpose |
|-----------|---------|---------|
| LOOP.md | 1.0 | Architecture reference |
| loop-prompt.md | 1.0 | Runnable system prompt |
| input-template.md | 1.0 | Structured input form (MODULE I / R / C) |
| example-input.md | 1.0 | Nexovane FY2025 Month 7 Reforecast — full input |
| example-output.md | 1.0 | Nexovane FY2025 Month 7 Reforecast — full output |
| revenue-projection-before-after-evals.md | 1.0 | Four before/after evaluations |

---

## What This Loop Does

The Revenue Projection Loop determines what the current commercial engine is
likely capable of producing for a defined metric and time horizon. It does not
generate strategy. It does not own the official forecast. It projects the engine
first and compares it against the target second.

That ordering is the whole point.

When a projection starts from the target and works backward — adjusting pipeline
assumptions, stage weights, or initiative contributions until the math closes —
the output is a gap-closure argument dressed up as a forecast. It tells leadership
what they want to hear, and it collapses at the first sign of variance.

This Loop prevents that. It produces a versioned, evidence-backed range that
separates model-based expectation, field judgment, and initiative-dependent
uplift. It explains why the projection changed from the prior run. It identifies
the conditions required to reach the target, labeled by evidence status. It
calibrates every prior projection against actual outcomes at close.

---

## What Gets Produced

**Every Reforecast run produces:**

- A full projection bridge — actuals, current pipeline by cohort, future pipeline
  by creation vintage, approved-initiative uplift (labeled separately), and
  capacity constraints (attributed to source)
- Three projection views — model-only, field-adjusted, and official operating
  forecast — preserved separately and never blended
- Four scenario ranges — evidence-supported lower bound, base (model-only),
  recovery/upside case, and best credible ceiling — each with named conditions
  and joint-feasibility confirmation
- A projection movement bridge explaining what changed from the prior run and why,
  attributed to pipeline move, model update, overlay change, or actuals revision
- Gap analysis — unsupported gap between target and projection, with
  required-conditions statement labeled by evidence status
- Sensitivity analysis — which variable produces the greatest dollar impact and
  whether it is within near-term organizational control
- Field Overlay Records — every field judgment documented with scope, evidence,
  model value before override, and expiration date
- Latest useful pipeline creation date — the date after which new pipeline
  cannot close in the current period
- Evidence gaps and confidence limitations — what the model cannot see, and
  what evidence would most reduce uncertainty
- A version-stamped, immutable Projection Run snapshot

---

## What the Loop Does Not Do

The Revenue Projection Loop does not:

- Generate strategic bets, new segments, or motions to pursue
- Decide what the organization should do to close the gap
- Own or commit to the official operating forecast
- Evaluate root cause of strategy divergence
- Govern intervention deployment
- Revise model parameters to match actuals without versioning

Strategy decisions belong to the Annual GTM Strategy and Goal Governance Loop.
This Loop provides the capability view. The Annual GTM Loop makes the portfolio
decisions that follow from it.

---

## How to Use It

### Step 1 — Initialize (once per fiscal year)

Copy `input-template.md` and complete MODULE I: define the metric, recognition
rules, horizon, source of record, and historical model parameters. Establish
approved initiatives with explicit ramp dates and evidence. Set capacity by
source. This is the foundation against which every Reforecast and Calibration
will be compared.

### Step 2 — Run Reforecasts (monthly or quarterly)

At each operating review, complete MODULE R: update actuals, provide a fresh
CRM pipeline snapshot, report observed commercial metrics (win rate, cycle,
generation, ACV), submit field overlays with supporting evidence, and update
initiative progress and capacity. Run the prompt. Review the output before the
leadership operating review.

### Step 3 — Run Close and Calibrate at period end

Complete MODULE C: provide verified final actuals, deal-by-deal outcomes for
all modeled pipeline, field overlay outcomes, and official forecast history.
The calibration output will show projection accuracy by run, model parameter
accuracy, field overlay accuracy per overlay, and bias by team and region.
Use the findings to update model parameters for the next cycle.

### Step 4 — Hand off gap findings to the Annual GTM Loop

When the projection shows an unsupported gap — as it likely will at
initialization if the target is ambitious — supply the projection output to the
Annual GTM Strategy and Goal Governance Loop. The Revenue Projection Loop
identifies the gap and the required conditions. The Annual GTM Loop decides
whether to Hold, Reinforce, Reallocate, Revise Commitment, or Escalate.

These are not duplicates. They do different things. Running one does not
replace the other.

---

## The Three Projection Views — Why They Must Stay Separate

The most common failure mode in commercial forecasting is blending the three
views into one number and presenting that number as the forecast.

A model-only projection of $8.7M with $0.12M of net field overlays producing
a field-adjusted view of $8.8M is not the same as a model-only projection of
$8.8M. At close, if the actual is $9.2M, the organization needs to know:

- Was the model right?
- Did field judgment improve accuracy?
- Was the official forecast biased?

If the three views are blended, none of these questions can be answered. The
calibration becomes noise. The organization cannot distinguish model error,
field judgment quality, and organizational forecast bias — and it will make the
same mistakes next cycle.

The Loop preserves all three. Each is compared against actual outcomes independently.
This is what produces learning.

---

## Field Overlays — Evidence Required

A field overlay is a named, documented adjustment to the model projection for a
specific opportunity, cohort, or territory. It is not a rep's opinion that a deal
will close. It is not pipeline management optimism.

Every overlay must state: scope, direction and dollar amount, owner, date,
evidence (procurement status, confirmed buyer authority, signed redlines, buyer
deadline), reason, model value before adjustment, and an expiration or review date.

Overlays without evidence are not accepted. "This deal feels strong" is not evidence.
"Procurement approval received July 31; OCC exam deadline January 15; CFO stated
contract must be in place before exam" is evidence.

At close, every overlay is compared against the actual deal outcome. Field
judgment accuracy is tracked by overlay and by team. Over time, this determines
whether field overlays improve forecast accuracy — and it makes overlay quality
a measurable operational discipline rather than an assertion.

---

## Model Parameters — Version Everything

Model parameters — conversion rates, cycle lengths, generation rates, ACV,
slippage rates, capacity — are not fixed. They are calibrated against observed
data and updated when evidence justifies revision.

But they are never silently updated. Every revision requires a Projection Version
Ledger entry: original value, revised value, revision date, evidence, and prior
runs affected. Prior Projection Runs are annotated, not rewritten.

This matters because a model that quietly updates its conversion assumption to
match observed outcomes after the period closes is not learning. It is revising
history. The organization cannot ask "were our projections accurate?" if the model
is retroactively adjusted to match actuals.

The version ledger preserves the record. Calibration uses it. Next-cycle
parameter decisions are grounded in documented evidence rather than intuition.

---

## Relationship to Other Loops

**Annual GTM Strategy and Goal Governance Loop**
Consumes Revenue Projection output when a strategic decision about commitments
is required. Receives the capability view (what the engine can produce, what the
gap is) and makes portfolio decisions: Hold, Reinforce, Tune, Reallocate, Revise
Bet, Revise Commitment, Stop, Escalate. The clean handoff: Revenue Projection
stops at the gap and the required conditions. Annual GTM Loop decides what to do.

**Win/Loss Pattern Loop**
Provides mechanism evidence — why deals win and lose by segment, motion, and
competitive context. Win/Loss findings inform conditional cohort conversion rates.
Import findings with their attribution scope; do not average them into a generic
win rate that strips the context needed to apply them correctly.

**Pipeline Risk Loop**
Diagnoses which current opportunities and pipeline cohorts are fragile and why.
Pipeline Risk findings directly improve the current-pipeline contribution section
of the projection bridge — identifying which Stage 3 and Stage 4 accounts should
carry lower-than-historical confidence due to missing dependencies, absent economic
buyers, or competitive displacement.

---

## Fictional Disclaimer

All organizations, accounts, competitors, partners, and individuals named in the
example files (example-input.md and example-output.md) are entirely fictional and
created for illustration purposes only.

This includes: Nexovane, Luvexis, Korval Advisory Partners, Alderix Capital,
Telvax Investment Group, Cadrova Financial, Velstrom Asset Management, Vestrix
Securities, Korvel Investments, Pelanthor Trust, Telvoran Capital, Pelantrix
Advisors, and Kessval Financial. All deal values, ARR figures, win rates, cycle
times, market conditions, regulatory timelines, competitive dynamics, and
commercial outcomes described in these files are invented for demonstration
purposes.

Any resemblance to real companies, real people, real market conditions, or actual
commercial results is coincidental. These examples are not intended to represent
or imply anything about any real organization, product, or market.
