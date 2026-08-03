# Revenue Projection Loop — Architecture Reference

**Version:** 1.0

---

## What This Loop Does

The Revenue Projection Loop produces a versioned, evidence-backed forward range for
a defined commercial metric and time horizon. It separates model-based expectation,
field judgment, and initiative-dependent uplift; explains why the projection changed;
identifies the conditions required to reach the target; and calibrates each
projection against actual outcomes.

This is more than prediction, but less than strategy.

It answers:

- What has already landed?
- What is likely to land from existing pipeline?
- What can still be created and converted within the period?
- What contribution depends on initiatives that have not yet proved themselves?
- What is the target gap?
- What would need to be jointly true to close it?
- Where was the previous projection wrong?

It does not decide which new segment, motion, channel, product bet, or strategic
change the organization should pursue. Those decisions belong to the Annual GTM
Strategy and Goal Governance Loop.

---

## The Primary State Object

A **Projection Run** is an immutable, evidence-backed view of what the commercial
engine is expected to produce at a specific point in time, under a defined metric,
horizon, and set of model parameters.

Each Projection Run carries:

- A version ID and as-of date
- A data snapshot date (the date of the CRM or pipeline source pull)
- The metric being projected, with its definition and recognition rules
- The projection bridge, broken down by contribution source
- Three projection views (model-only, field-adjusted, official operating forecast)
- Four scenario ranges
- Evidence gaps and confidence limitations

Projection Runs are never rewritten. A new run creates a new version. The sequence
of Projection Runs is what calibration compares against actual outcomes at period close.

---

## Three Supporting Records

**Field Overlay Record**
Documents each individual field judgment that changes the model-only projection.
Required fields for every overlay: scope (specific opportunity, cohort, or territory),
direction and dollar amount, owner, date, evidence, reason, model value before
override, field-adjusted value, expiration or review date.

Every overlay is preserved and compared against actual outcome at close. This is
how the Loop evaluates whether field judgment adds or removes forecast accuracy.

**Projection Version Ledger**
Documents changes to model parameters — conversion rates, cycle length assumptions,
pipeline generation rates, ACV estimates, capacity constraints, seasonality, or
initiative assumptions. Preserves: original value, revised value, revision date,
evidence, and prior Projection Runs calculated under the old parameters.

Model parameters may be updated when evidence justifies revision. They may never
be silently revised to match actuals after the period closes. A model that adjusts
its conversion assumption to match observed outcomes without preserving the prior
version is not learning — it is revising history.

**Calibration Record**
Produced at period close. Compares each prior Projection Run against actual outcomes
by source. Records model accuracy, field overlay accuracy, official forecast accuracy,
and parameter-level accuracy (conversion assumed vs. realized, cycle assumed vs.
realized, generation assumed vs. realized).

Calibration findings drive Projection Version Ledger updates for the next cycle.

---

## The Projection Bridge

```
Recognized actuals
  (already closed; source of record; excluded from projections)

+ Current-pipeline contribution
    applied by cohort where data supports:
      stage × segment × motion × source × deal size
      × age and time in stage
      × competitive status
      × procurement progress
      × remaining fiscal time
      × Pipeline Risk finding if available
    − timing filter: deals with insufficient remaining cycle time
      for current-period recognition → moved to next-period carryover
    − slippage and push adjustments by cohort

+ Future-pipeline contribution (existing engine)
    modeled by creation vintage:
      expected pipeline created in period t
      × qualification rate
      × conversion probability given remaining time after creation
      × expected cycle length for that vintage
      × expected ACV
      × capacity feasibility for that period
    pipeline created after the latest useful creation date
      → next-period carryover; excluded from current-period bridge

+ Approved-initiative uplift
    always labeled separately from the existing engine
    ramp date / evidence basis / dependencies stated explicitly
    confidence level stated; never pre-blended into the base

+ Field overlays
    labeled separately; each overlay requires evidence
    model value before override always remains visible

− Capacity constraints
    attributed to the source they affect:
      generation, progression, technical validation,
      contracting, implementation, or recognition
    stated with affected period and estimated dollar impact

− Timing and slippage effects

− Contribution overlap and duplication across sources

= Evidence-backed projection range

Target
− Projection range
= Supported or unsupported gap to target
```

**The target is never the starting assumption.** The commercial engine is projected
first. The target is compared second. This prevents the projection from reverse-
engineering optimistic inputs until the gap disappears.

---

## Three Projection Views

**View 1 — Model-only projection**

Produced from actuals, pipeline, historical conversion (conditional cohort where
data supports it, simple stage rate where it does not), cycle distributions,
generation rates, capacity, and model parameters. No field judgment applied.

This is the evidence baseline. It shows what the commercial system produces without
human override.

**View 2 — Field-adjusted projection**

Model-only projection plus or minus evidence-backed field overlays. Every overlay
retains its Field Overlay Record fields. The model value before the override remains
visible alongside the field-adjusted value.

**View 3 — Official operating forecast or commit**

The number formally adopted by leadership, RevOps, or Finance as the operating
number for the period. Supplied as an organizational event. The Loop does not
calculate or own this number. If not supplied, it is absent — not substituted with
the field-adjusted view.

**These three views are never silently blended.** A model-only projection of $17M
with $4M of field overlays producing $21M is not the same as a model-only projection
of $21M. At close, all three are compared against actual outcomes independently.
This is what allows the organization to distinguish model error, field judgment
quality, and organizational forecast bias from one another.

---

## Source Confidence Model

Different contribution sources carry different confidence levels. The Loop labels
confidence per source in every Projection Run output.

| Contribution source | Confidence |
|---------------------|------------|
| Recognized actuals | Certain — already closed and recorded |
| Late-stage pipeline: economic buyer confirmed, procurement active, within typical cycle | High |
| Mid-stage pipeline: progressing, sufficient remaining time, no blocking dependency | Medium |
| Early-stage pipeline: needs multiple progressions, marginal remaining time | Low |
| Future pipeline — existing engine, not yet created | Medium-Low |
| Initiative-dependent uplift — initiative not yet demonstrated | Low to Medium |
| Field overlay with strong documentary evidence | Adjusts model level up or down |
| Field override without supporting documentation | Not accepted |

A total projection of $18M composed primarily of late-stage high-confidence
pipeline is not the same risk profile as $18M composed primarily of future pipeline
and initiative-dependent uplift — even when the headline number is identical.
The Loop reports the composition, not only the total.

---

## Lifecycle Stages

### Stage 1 — Initialize and Plan

Run once at the start of the fiscal year or projection horizon.

**Define:** projected metric and its definition; inclusion and exclusion rules;
recognition rules; horizon; source of record; currency; bookings-to-revenue or
ARR-to-revenue treatment where applicable.

**Establish:** historical model parameters — conversion by cohort (or by stage
where cohort data is insufficient), cycle length distributions, pipeline generation
rates by motion and segment, ACV, slippage and push rates, seasonality, capacity
by source, and historical forecast bias.

**Project:** what the existing engine plus approved initiatives can credibly produce
before the leadership target is set.

**Primary question:** Is the leadership target evidence-supported, partially
supported, or unsupported before the fiscal year begins?

### Stage 2 — Reforecast

Run at each operating review — monthly or quarterly, depending on the business.

**Update:** actuals, current pipeline state from a fresh CRM snapshot, observed
conversion vs. model parameters, observed pipeline generation vs. historical,
actual cycle lengths vs. historical, slippage observed, field overlays (new,
revised, or expired), initiative progress, capacity actuals, remaining time.

**Output:** updated projection range, projection movement bridge explaining what
changed and why, updated gap and required conditions, immutable Projection Run
snapshot preserved.

**Scenario analysis and required-conditions analysis run on every Reforecast.**
They are not a separate lifecycle stage.

### Stage 3 — Close and Calibrate

Run at period close.

**Compare:** all prior Projection Run snapshots against verified actual outcomes.
Model-only projection vs. actual. Field-adjusted projection vs. actual. Official
operating forecast vs. actual. Each Field Overlay Record against the actual deal
outcome.

**Calibrate:** conversion parameters by cohort, cycle parameters, pipeline
generation parameters, slippage parameters, field override accuracy, forecast
bias by team and region.

**Update:** parameter changes that calibration justifies are recorded in the
Projection Version Ledger with original and revised values, revision date, and
evidence. Prior Projection Runs calculated under old parameters are annotated,
not rewritten.

---

## Latest Useful Pipeline Creation Date

For future pipeline, the Loop calculates the date after which new pipeline can
no longer be expected to convert and recognize within the current period:

```
Latest useful creation date =
  Period end date
  − recognition lag
  − procurement / realization time
  − qualification / sales cycle
  − (minimum pipeline progression to Stage 2 from creation)
```

Pipeline created after this date is modeled as next-period carryover. It may still
be valuable for building the following period's coverage, but it is excluded from
the current-period projection.

This date is recalculated on every Reforecast as remaining time compresses.

---

## Projection Movement Bridge

Every Reforecast produces a movement bridge that explains what changed from the
prior Projection Run and why:

```
Prior base projection (Month N):     $X.XM
Current base projection (Month N+1): $X.XM
Change:                              ±$X.XM

Drivers:
  [Item]   [Amount]   [Attribution: pipeline move / model update / overlay change / actuals revision]
  [Item]   [Amount]   [Attribution]
  ...
```

Each driver is attributed to its source: a pipeline change in the CRM, a model
parameter revision, a field overlay added or removed, or an actuals revision.

This is one of the highest-value outputs for operating reviews. Leaders should be
able to see whether the projection moved because the commercial situation changed
or because someone changed a number in the model or override list.

---

## Required-Conditions Analysis

When a gap exists between the projection and the target, the Loop produces a
required-conditions statement:

*To reach [Target], the following conditions must be jointly true:*
- [Volume of pipeline] must be created and qualified by [latest useful creation date]
- [Win rate] must hold at or above [value]
- Median cycle time must remain at or below [value]
- [Initiative] must ramp by [date] and produce [contribution range]
- [Capacity constraint] must be resolved by [date]

*Of these conditions:*
- *Supported by current evidence:* [list]
- *Plausible but not yet confirmed:* [list]
- *No current evidence basis:* [list]

This is not a strategy recommendation. It is a statement of what the math requires.
The Annual GTM Strategy Loop decides what, if any, strategic action to take.

---

## Scenario Structure

**Evidence-supported lower bound**
Recognized actuals plus contribution from the highest-confidence remaining pipeline
only — late-stage opportunities with confirmed economic buyers, procurement active,
within typical cycle range, no material outstanding dependencies. Nothing that
requires an additional progression stage to close.

**Base projection**
Applies conditional cohort conversion (or simple stage conversion where cohort data
is insufficient) to the full current pipeline, plus credible existing-engine future
generation through the latest useful creation date. Model-only. No field overlays.

**Recovery or upside case**
Adds conditions that are plausible based on available signals: field overlays with
documentary evidence, an initiative ramping at the upper end of its range, a pipeline
cohort converting above its recent historical average. Every condition named. Shared
dependencies and capacity requirements checked for joint feasibility.

**Best credible ceiling**
Maximum outcome under conditions that are both individually plausible and jointly
feasible given shared constraints — capacity, dependencies, timing. Not the
theoretical all-favorable ceiling, which adds every optimistic assumption regardless
of joint feasibility. When these differ materially, both are shown with an
explanation of why they diverge.

---

## Sensitivity Analysis

The Loop reports which variable produces the greatest dollar impact per unit of change:

- Conversion rate: each +/−1 percentage point produces approximately $X change
- Cycle length: each 10-day extension or compression produces approximately $Y
- Pipeline generation rate: +/−$1M of additional qualified pipeline produces $Z at current conversion
- ACV: each +/−10% ACV change produces approximately $W
- Capacity: the current binding capacity constraint is worth approximately $V in contribution
- Latest useful creation date: pipeline creation that slips by 30 days loses approximately $U in
  current-period contribution

This identifies which lever has economic relevance and which sounds useful but
produces minimal impact at current volumes and conversion rates.

---

## What This Loop Does Not Do

The Revenue Projection Loop does not:

- Generate strategic bets, segments, motions, or channels
- Decide what the organization should do to close the gap
- Own or commit to the official operating forecast
- Assess whether the annual strategy is still supportable
- Evaluate root cause of strategic divergence
- Govern intervention deployment or evaluation
- Revise model parameters to match actuals after close without versioning

It surfaces what the commercial engine can produce and what conditions the target
requires. The Annual GTM Strategy Loop makes the portfolio decisions that follow.

---

## Relationship to Other Loops

**Win/Loss Pattern Loop**
Provides mechanism evidence — why deals win and lose by segment, motion, and
competitive context. Win/Loss findings affect the conversion assumptions used
in the projection, particularly conditional cohort conversion rates by competitive
status and segment. Import Win/Loss findings with their attribution schema; do
not average them into a generic win rate without preserving the scope limitations.

**Pipeline Risk Loop**
Diagnoses which current opportunities and pipeline cohorts are fragile and why.
Pipeline Risk findings directly inform the current-pipeline contribution section
of the projection bridge — specifically, which Stage 3 and Stage 4 opportunities
should carry lower-than-historical conversion confidence due to identified risk
factors (dependency not started, economic buyer absent, competitive displacement).

**Annual GTM Strategy and Goal Governance Loop**
Consumes the Revenue Projection Loop output when a strategic decision about
commitments is required. The Projection Loop provides the capability view:
what the commercial engine can produce and what the gap is. The Annual GTM Loop
makes the portfolio decisions: Hold, Reinforce, Tune, Reallocate, Revise Bet,
Revise Commitment, Stop, or Escalate.

The clean handoff: Revenue Projection stops at identifying the gap and the
required conditions. Annual GTM Strategy decides what to do about it.

---

## Operating Rules

1. **Project the engine first. Compare it with the target second.** The target
   must never be the model's starting assumption.

2. **Preserve three views separately.** Model-only, field-adjusted, and official
   operating forecast are never blended into one number.

3. **Require evidence for every field override.** A field judgment without
   supporting evidence is not accepted. "This deal will close" is not evidence.
   Procurement status, confirmed economic buyer, signed redlines, or a buyer
   deadline is evidence.

4. **Model future pipeline by creation vintage.** Do not project unbuilt pipeline
   as one undifferentiated annual pool. Each creation period has a different
   remaining-time probability.

5. **Apply capacity constraints to the source they affect.** One generic capacity
   deduction at the bottom of the bridge does not distinguish between a generation
   constraint, a progression constraint, and a delivery constraint.

6. **Require jointly feasible scenarios.** The best credible ceiling is bounded by
   shared dependencies and capacity — not by adding every optimistic assumption
   independently.

7. **Snapshot every run immutably.** Calibration must compare actuals against what
   was known at the time of the projection, not against retroactively updated stages.

8. **Version model parameters.** Parameter changes must preserve the original value
   and annotate prior projections. A model that quietly updates to match actuals
   is revising history, not learning.

9. **State the confidence composition.** Report the source breakdown of the
   projection — how much comes from each confidence tier — not only the total.

10. **Widen the range when evidence is thin.** When data supports only a simple
    stage conversion rate rather than a conditional cohort model, state the
    limitation and widen the confidence range accordingly. Do not invent precision
    that the data does not support.
