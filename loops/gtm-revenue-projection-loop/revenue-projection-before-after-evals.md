# Revenue Projection Loop — Before/After Evaluations

*Four evaluations illustrating the difference between a naive commercial
projection and a Revenue Projection Loop output. Each shows the same business
situation handled two ways.*

---

## Eval 1 — Planning-time projection

**Situation:** It is February 1, 2025. Nexovane is setting its FY2025 commercial
plan. The CRO has stated that the company's target is $12.0M in new enterprise ARR.
RevOps is asked to produce a projection.

---

### Before: Naive coverage math

> **Revenue plan — FY2025**
>
> Target: $12.0M
>
> Coverage model:
> We need $12.0M in ARR. Historical win rate is 38% at Stage 3. We therefore
> need $31.6M in qualified pipeline across the year. We currently have $3.2M in
> carryover and expect $1.1M/month in new qualified pipeline = $13.2M new
> generation = $16.4M total. At 38%, this gives us $6.2M from the existing engine.
>
> The Korval channel partnership is expected to add $1.2M–$1.8M. We plan to
> pursue the Basel IV compliance module launch to address a regulatory-driven
> demand spike in the second half. This is expected to close the remaining gap.
>
> We are comfortable with the $12.0M target.

**What is wrong with this:**

1. The projection starts from the target. It works backward from $12.0M to determine
   whether coverage "adds up," rather than projecting the engine forward and comparing
   it against the target. As a result, comfortable language is attached to a gap that
   has not been quantified.

2. All future pipeline is treated as a single undifferentiated annual pool.
   A deal created in January has 12 months to close. A deal created in November has
   2 months to close. Applying a single 38% win rate to both as if they contribute
   equally to the year overstates the value of late-created pipeline.

3. The module launch is described as expected to "close the remaining gap" without
   stating the size of the gap, the evidence basis for the launch contribution, or
   the conditions required for that contribution to materialize. This is not an
   approved initiative with a stated ramp — it is a circular placeholder.

4. Capacity is never mentioned. At 4 onboards per quarter, the delivery team can
   support 16 new enterprise customers in FY2025. If both Korval channel and direct
   enterprise close above the model volume, delivery becomes the binding constraint —
   and the projection ignores it.

5. No model parameters are stated or versioned. There is no way to know what the
   38% win rate is based on, which cohort it applies to, or how to revise it if
   FY2025 observed rates diverge.

---

### After: Revenue Projection Loop output — Initialize and Plan

> **REVENUE PROJECTION LOOP — RUN OUTPUT (R01)**
>
> **Run type:** Initialize and Plan | **As-of date:** February 1, 2025
> **Model version:** M01 (Stage 3 → win 38%; cycle 90 days; generation $1.1M/month;
> capacity 4 onboards/quarter; channel 65% via Korval)
>
> **PROJECTION BRIDGE**
>
> ```
> Recognized actuals (Feb 1):                          $0.00M  [Certain]
>
> + Current-pipeline contribution (carryover, $3.2M):
>     Stage 3 (4 accounts, $1.9M): 38% × $1.9M:       $0.72M  [Medium]
>     Stage 2 (3 accounts, $1.3M): 22% × $1.3M:       $0.29M  [Low]
>   Subtotal carryover:                                $1.01M
>
> + Future-pipeline contribution (existing engine):
>     Latest useful creation date: October 15, 2025
>     Feb–Oct creation (8 months × $1.1M base):
>       $8.8M qualified pipeline × 70% qual × 38%:    $2.34M  [Medium-Low]
>     Peak-season adjustment (Aug–Oct, 1.4×):         +$0.34M
>   Subtotal future pipeline:                          $2.68M
>
> + Approved-initiative uplift (Korval channel):
>     Ramp from August 2025; base case $1.2M–$1.8M
>     Confidence: Medium (signed agreement; 6 accounts
>     in early qualification; contribution not yet recognized)
>   Subtotal initiative:                    $1.2M–$1.8M  [Medium]
>
> − Capacity constraint:
>     16 maximum onboards at 4/quarter.
>     At base volumes: constraint does not bind.
>     If Korval upper range + direct enterprise exceed
>     16 concurrent closes: estimated push: -$0.2M      -$0.0M (base)
>
> = Model-only base projection (R01):          $4.69M + Korval base
> = Model-only range:              $5.6M – $6.3M
>
> Initiative-dependent range:       $6.8M – $8.1M
>   (Model base + Korval at $1.2M–$1.8M)
> ```
>
> **THREE PROJECTION VIEWS**
>
> View 1 — Model-only: $5.6M – $6.3M
> (Existing engine without Korval contribution)
>
> View 2 — Field-adjusted: Not applicable at initialization; no overlays yet
>
> View 3 — Official operating forecast: $12.0M (leadership target, not projected)
>
> **GAP ANALYSIS**
>
> Target: $12.0M
> Best credible initiative-inclusive range: $6.8M – $8.1M
>
> **Unsupported gap: $3.9M – $5.2M**
>
> This gap is unsupported by the current commercial engine, carryover, or the
> approved Korval initiative at its stated base case. The $12.0M target requires
> either: (a) a new contribution source not yet modeled; (b) a material model
> assumption change; or (c) the module launch producing $4M+ in net new ARR — a
> contribution range that has no evidence basis in this plan.
>
> *This finding is supplied to the Annual GTM Strategy Loop. Strategy decisions
> about what to change belong there, not here.*

**What the Loop added:**

The engine is projected forward without the target as an input. The gap is
quantified as $3.9M–$5.2M — not hand-waved away with "the module launch will
cover it." Capacity is checked. The Korval initiative is labeled separately with
a confidence level. The official target is recorded as an organizational number,
not a projection. The required conditions to reach $12.0M are explicit and
evidence-labeled, not assumed.

---

## Eval 2 — Mid-year reforecast with field overlays

**Situation:** It is August 2, 2025 — Month 7 of FY2025. RevOps is running the
monthly reforecast. Three field overlays have been submitted by Regional VP Sales:
Velstrom is high-confidence (OCC deadline), Telvax is at competitive risk (Luvexis),
and Pelantrix has accelerated its security review.

---

### Before: Blended number with overlays absorbed into the total

> **August Reforecast — Nexovane FY2025**
>
> Based on pipeline review and field input:
>
> YTD actuals: $5.48M
> Remaining pipeline contribution: ~$4.2M (field-adjusted)
> Forecast: $9.7M
>
> Confidence: Medium-High. Sales leadership has reviewed active accounts.
> Velstrom is a strong close; Telvax has some risk but is expected to hold.

**What is wrong with this:**

1. The three projection views are blended into one. The $9.7M is presented as
   a single field-adjusted number. There is no model-only view, which means at
   close, it is impossible to determine whether the projection was accurate because
   the model was good or because the field overlay was good. When things go wrong,
   you cannot isolate which input failed.

2. "Telvax has some risk but is expected to hold" is not an evidence-based overlay.
   It asserts an outcome without stating the evidence — Luvexis proposed 20% below
   ACV and the champion confirmed Luvexis as their preferred vendor. That is specific
   information that belongs in a Field Overlay Record, not softened language in a
   paragraph.

3. "~$4.2M remaining pipeline contribution" is a blended total. The mix of
   Stage 4 high-confidence pipeline, Stage 3 medium-confidence pipeline, future-period
   creation, and the Korval initiative are all collapsed into one number. At close,
   there is no way to know which of those components over- or under-performed.

4. No movement bridge is provided. The prior projection in July was $10.4M. The
   August number is $9.7M. Why did it move down $0.7M? Was it a model parameter
   change (Stage 3 win rate revision)? A pipeline event (module ship delay)? A
   capacity constraint? The reader cannot tell.

---

### After: Revenue Projection Loop output — Reforecast (R03)

*(Abbreviated for illustration; full output in example-output.md)*

> **REVENUE PROJECTION LOOP — RUN OUTPUT (R03)**
>
> **Run type:** Reforecast | **As-of date:** August 2, 2025
> **Model version:** M03 (Stage 3 win rate 38% → 30% per M02; cycle 90 → 94 days per M03)
>
> **THREE PROJECTION VIEWS**
>
> View 1 — Model-only: $8.7M – $9.5M
> (No field overlays. M03 parameters applied to full pipeline.
> Stage 3 win rate 30%; cycle 94 days; initiative at $1.4M–$2.0M base.)
>
> View 2 — Field-adjusted: $8.8M – $9.6M
> (Net overlay effect: +$0.12M)
> — OV01 Velstrom: +$0.12M (OCC deadline, procurement approved — adjusts up)
> — OV02 Telvax: -$0.11M (Luvexis preferred vendor, price competition — adjusts down)
> — OV03 Pelantrix: +$0.11M (early CISO security review, CFO engaged — adjusts up)
>
> View 3 — Official operating forecast: Not supplied this run.
> (RevOps will present to CRO and Finance on August 5; official commit to be
> recorded in R04.)
>
> **PROJECTION MOVEMENT BRIDGE (vs. R02 — July 1, 2025)**
>
> ```
> Prior R02 base:  $10.4M
> Current R03 base: $9.1M
> Change:           -$1.3M
>
> Module ship delay (44 days):        -$0.38M  [pipeline timing]
> Luvexis — Stage 3 win rate M02:     -$0.18M  [model update]
> Cycle time revision M03:            -$0.09M  [model update]
> Delivery capacity constraint:       -$0.10M  [capacity applied]
> Telvoran champion absence:          -$0.08M  [pipeline event]
> Korval referrals added:             +$0.39M  [pipeline addition]
> Alderix Expansion to Stage 3:       +$0.15M  [pipeline addition]
> Actuals outperformed R02:           +$0.10M  [actuals revision]
> Residual:                           -$0.21M
> ```

**What the Loop added:**

The three views are preserved separately. A leader reviewing this output can see
the model expects $8.7M–$9.5M, the field adjustments add $0.12M net, and the
official commit is not yet set. The movement bridge explains that $0.38M of the
decline came from the module delay, $0.18M from the model parameter revision, and
$0.39M was offset by new Korval referrals. These are attributable, auditable facts.
At close, each Field Overlay Record can be compared against the actual deal outcome
to determine whether field judgment improved or degraded accuracy.

---

## Eval 3 — Sparse data handling

**Situation:** It is early in Nexovane's use of the Revenue Projection Loop —
Month 3 of FY2025. Only 3 deals have closed in the fiscal year. The Stage 3 win
rate is uncertain; there are only 2 observations. RevOps is asked for a projection
and a confidence range.

---

### Before: Invented precision on thin data

> **March Reforecast — Nexovane FY2025**
>
> Model parameters: Stage 3 win rate 38% (historical FY2023–FY2024). Cycle: 90 days.
>
> Pipeline: $4.1M in active stages. Applying 38% to Stage 3 and 22% to Stage 2:
> projected contribution $1.3M. Adding YTD actuals ($1.4M) and future generation
> ($3.2M at 38%): Full-year projection P50: $7.8M, P75: $9.1M.

**What is wrong with this:**

1. "P50" and "P75" are labels for statistically calibrated distributions —
   the 50th and 75th percentile of a modeled distribution. With n=3 closed deals
   in the current year and no FY2025 calibration yet, there is no distribution.
   Applying percentile labels to a point estimate dressed up with a multiplier
   is false precision. It implies a rigorous probability model that does not exist.

2. The Stage 3 win rate of 38% is presented as certain. There are 2 observations
   in FY2025 — insufficient to validate or contradict the historical parameter.
   Whether FY2025 is tracking above or below the historical rate is unknowable at
   this sample size. The output does not flag this.

3. The projection does not distinguish between confidence tiers. "$1.3M pipeline
   contribution" combines Stage 3 and Stage 2 at different confidence levels
   without labeling them. At close, there is no way to know which tier drove
   over- or under-performance.

---

### After: Revenue Projection Loop output — sparse-data run

> **REVENUE PROJECTION LOOP — RUN OUTPUT (R02 — April 1, 2025)**
>
> **Run type:** Reforecast | **Model version:** M01 (unchanged — insufficient
> FY2025 data to justify parameter revision)**
>
> **Data limitation statement:** This run is based on 3 closed FY2025 deals
> (n=3) and 2 Stage 3 exits (n=2). The sample is insufficient to validate or
> revise the M01 model parameters. Projected ranges are wider than they will
> be in later-period runs. Do not apply percentile labels to these ranges —
> the data does not support a calibrated distribution.
>
> **PROJECTION BRIDGE**
>
> ```
> Recognized actuals (Feb 1 – Mar 31):            $1.40M  [Certain]
>
> + Current-pipeline contribution:
>     Stage 3 (3 accounts, $1.4M): 38% × $1.4M:  $0.53M  [Medium — M01; insufficient
>                                                           FY2025 data to revise;
>                                                           range widened ±12 pp]
>     Stage 2 (4 accounts, $1.8M): 22% × $1.8M:  $0.40M  [Low — no FY2025 S2 exits yet]
>
> + Future-pipeline contribution:
>     April–October vintages (existing engine):   $2.34M  [Medium-Low]
>     Korval initiative (ramp beginning Aug):     $1.2M–$1.8M  [Medium]
>
> − Capacity constraint:
>     4 onboards/quarter — not binding at current volume  $0.0M
>
> = Model-only projection:              $5.5M – $6.7M
>   [Range widened: M01 win rate applied with ±12 pp
>    uncertainty band given FY2025 n<5 at Stage 3]
>
> Initiative-inclusive range:          $6.7M – $8.5M
> ```
>
> **THREE PROJECTION VIEWS**
>
> View 1 — Model-only: $5.5M – $6.7M
> *(M01 parameters, widened range due to thin FY2025 data)*
>
> View 2 — Field-adjusted: Not applicable this run — no overlays with evidence
> submitted.
>
> View 3 — Official operating forecast: $12.0M (leadership target)
>
> **CONFIDENCE COMPOSITION:**
> Certain (actuals): $1.40M (21%)
> Medium (pipeline): $0.93M (14%)
> Low-Medium (future pipeline + initiative): $4.37M–$6.17M (65%)
>
> *65% of this projection comes from future pipeline and initiative — neither
> has yet proved itself in FY2025. Range will compress as actuals accumulate.*

**What the Loop added:**

The thin data is named and its effect on the range is stated explicitly. "P50"
and "P75" labels are not used because no calibrated distribution exists. The range
is widened appropriately ($5.5M–$6.7M vs. a false-precision point estimate of
$7.8M). The confidence composition shows that 65% of the projection depends on
future events — a material statement for leadership. As the year progresses and
actuals accumulate, the range will compress and the model parameters can be
validated or revised. The reader knows exactly what they are looking at.

---

## Eval 4 — Calibration output at close

**Situation:** January 31, 2026. FY2025 is closed. Final new enterprise ARR came
in at $9.2M. The Loop is asked to produce a calibration output.

---

### Before: No structured calibration

> **FY2025 Year-end review**
>
> We came in at $9.2M vs. $12.0M target — a $2.8M miss.
>
> What happened: Pipeline was lighter than expected. Win rates were affected by
> Luvexis entering the market. The Korval channel initiative took longer to ramp.
> Delivery capacity was tighter than planned.
>
> For FY2026: We will revise our win rate assumptions down to 30% and add
> more aggressive channel targets.

**What is wrong with this:**

1. The "calibration" is retrospective narrative. None of the claims ("pipeline was
   lighter," "win rates were affected") are compared against a documented prior
   projection. There is no baseline to measure against — what did the projection
   say in February? In August? Were those projections accurate or optimistic?

2. The win rate is revised from 38% to 30% based on final observation — without
   preserving the original parameter, noting when the revision became visible in
   the data, or annotating prior projections. This is revising history rather than
   learning. If the win rate was already declining in Month 4, the organization
   missed 6 months of acting on an observable signal.

3. Field overlays are not evaluated. Were the field overlays submitted by RevOps
   and Sales leadership accurate? Did OV01 (Velstrom, +$0.12M) improve accuracy?
   Did OV02 (Telvax, -$0.11M) correctly call the Luvexis displacement? Overlay
   accuracy determines whether field judgment should be trusted, constrained, or
   recalibrated — and this output ignores it.

4. The Korval initiative is described as having "taken longer to ramp" — but what
   did the initiative contribute, and how did that compare with the $1.4M–$2.0M
   range in the August reforecast? Without that comparison, the organization cannot
   build a better initiative-ramp model for FY2026.

---

### After: Revenue Projection Loop — Close and Calibrate output

> **REVENUE PROJECTION LOOP — CALIBRATION RECORD (C01)**
>
> **Run type:** Close and Calibrate | **As-of date:** February 1, 2026
> **Metric:** New Enterprise ARR FY2025 | **Actual:** $9.2M
>
> **PROJECTION ACCURACY BY RUN**
>
> | Run | As-of | Model-only | Field-adj | Official | Actual | Model error | Field error |
> |-----|-------|-----------|-----------|----------|--------|-------------|-------------|
> | R01 | Feb 1 | $5.6M–$6.3M | n/a | $12.0M | $9.2M | Model: −$3.0M to −$2.9M at midpoint | — |
> | R02 | Apr 1 | $5.5M–$6.7M | n/a | $12.0M | $9.2M | Model: −$3.1M at midpoint | — |
> | R03 | Aug 2 | $8.7M–$9.5M | $8.8M–$9.6M | n/a | $9.2M | Model: +$0.2M at midpoint | Δ: +$0.3M vs. actual |
>
> *R01 and R02 projected $5.6M–$6.7M at midpoint for the full year, vs. $9.2M
> actual. The model undershoots were driven primarily by the Korval initiative
> contributing at the upper end of its range and by actual pipeline creation
> running above the base-case model. These were not errors in the existing-engine
> model — they were correct uncertainty statements about the initiative at
> initialization. R03 (August) was accurate to within $0.3M.*
>
> **PARAMETER ACCURACY**
>
> | Parameter | M03 assumed | Realized | Bias |
> |-----------|------------|---------|------|
> | Stage 3 win rate | 30% | 31% (revised M02 was accurate; actual rate confirms Luvexis impact) | +1 pp — negligible |
> | Cycle time (Stage 3 → close) | 94 days | 96 days median | +2 days — model nearly accurate |
> | Pipeline generation (direct) | $1.1M/month | $1.08M/month | On model |
> | Delivery capacity | 3.5/quarter | 3.3/quarter (one additional push-out in Q4) | Slightly optimistic |
>
> **FIELD OVERLAY ACCURACY**
>
> | ID | Scope | Model value | Field-adjusted | Actual | Field judgment |
> |----|-------|-------------|----------------|--------|----------------|
> | OV01 | Velstrom Asset Mgmt | $0.39M | $0.51M | $0.54M | Improved — OCC deadline signal accurate |
> | OV02 | Telvax Investment Group | $0.37M | $0.26M | $0.00M (lost to Luvexis in October) | Improved — competitive risk correctly identified |
> | OV03 | Pelantrix Advisors | $0.11M | $0.23M | $0.38M (closed full ACV; accelerated cycle confirmed) | Improved — security review signal accurate |
>
> **PARAMETER UPDATES FOR FY2026 (Projection Version Ledger)**
>
> | Rev ID | Parameter | Old value | New value | Evidence |
> |--------|-----------|----------|----------|---------|
> | M04 | Stage 3 win rate (competitive) | 30% blended | 12% competitive, 72% uncontested | FY2025 closed data confirms bimodal distribution; n=12 now sufficient |
> | M05 | Delivery capacity | 4.0/quarter | 3.5/quarter | FY2025 actual average; backfill hire resolved in Q1 FY2026 — monitor |
> | M06 | Korval channel ramp model | $1.2M–$1.8M (base) first year | $2.0M–$2.8M (Year 2+ ramp, post-proved) | Korval closed at $1.95M FY2025; Year 2 penetration rate established |
>
> **BIAS ANALYSIS**
>
> | Segment | Direction | Magnitude | Pattern |
> |---------|-----------|-----------|---------|
> | Northeast field overlays | Optimistic then accurate | OV02 moved to 0 vs. $0.26M field-adj | One displacement not caught; field adjustment underestimated Luvexis competitive win |
> | Southeast field overlays | Accurate to slightly conservative | Pelantrix closed full ACV vs. $0.23M field-adj | Fast-track signal underweighted |
> | Initiative contribution | Conservative at R01/R02; accurate at R03+ | R01 model-only missed Korval upper range; R03 field-adj was within $0.2M | Early-stage initiative uncertainty appropriately handled |

**What the Loop added:**

Every prior Projection Run is compared against the actual outcome with its
own accuracy line. Field overlays are evaluated individually — OV02 correctly
called the Luvexis displacement; OV03 correctly read the accelerated security
review. Model M03 parameters were accurate to within a few percentage points.
The calibration produces specific, versioned parameter updates for FY2026 (M04,
M05, M06) with evidence for each revision. These are not retroactive revisions —
they are forward-looking updates, traceable to specific observed data. The
organization enters FY2026 with a better model, documented field overlay accuracy
by team, and a proved Korval ramp model — none of which were available without
structured calibration.
