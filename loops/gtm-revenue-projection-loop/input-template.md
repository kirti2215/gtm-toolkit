# Revenue Projection Loop — Input Template

**Version:** 1.0

---

## How to Use This Template

This template has three modules corresponding to the three lifecycle stages.

**MODULE I — Initialize and Plan**
Complete once at the start of the fiscal year or projection horizon. Defines the
metric, establishes historical model parameters, and produces the first projection.
Do not skip MODULE I. The quality of the initialization determines the quality of
every subsequent Reforecast run.

**MODULE R — Reforecast**
Complete at each operating review. Supply only what has changed since the prior run;
the Loop carries forward all prior inputs. Update actuals, pipeline, observed metrics,
field overlays, and any events that affect the projection.

**MODULE C — Close and Calibrate**
Complete at period close. Supply verified actual outcomes and observed commercial
metrics. The Loop will compare all prior Projection Runs against actuals and
produce parameter-level calibration findings.

---

## MODULE I — Initialize and Plan

*Complete at the start of the fiscal year or projection horizon.*
*Mark each field `[init]` — required at initialization.*
*Mark `[opt]` — provide if available; Loop will flag the limitation if absent.*

---

### I.1 — Run Context `[init]`

```
Organization name:        [Your organization]
Fiscal year or horizon:   [e.g., FY2026: Feb 1, 2026 – Jan 31, 2027]
Planning run date:        [YYYY-MM-DD]
Prepared by:              [Role — e.g., VP Revenue Operations]
```

---

### I.2 — Metric Definition `[init]`

*(The Loop projects one primary metric per run. Define it exactly. Revenue,
bookings, ARR, and recognized revenue are not interchangeable. Secondary
metrics may be shown as implications but are not blended into the bridge.)*

```
Primary projected metric:          [e.g., New Enterprise ARR]
Metric definition:                 [e.g., Net new annual recurring revenue from new
                                   enterprise customer contracts, excluding renewals,
                                   expansions from existing customers, and SMB tier]
Inclusion rules:                   [What counts toward this metric]
Exclusion rules:                   [What is explicitly excluded]
Recognition rule:                  [When contribution is recognized — e.g., contract
                                   executed date, implementation start, billing start]
Projection horizon:                [Period start and end dates]
Source of record:                  [e.g., Salesforce SFDC, NetSuite, internal Finance]
Currency:                          [e.g., USD]
Bookings-to-revenue treatment:     [e.g., 1:1 — fully recognized at contract; or
                                   describe any lag between bookings and recognized ARR]
Annual leadership target:          [$X.XM]
Target owner and approver:         [e.g., CFO approved; CRO committed]
```

---

### I.3 — Historical Commercial Parameters `[init]`

*(These parameters form the model. The Loop applies them to project pipeline and
future generation. State the source, period covered, and sample size for each.
When cohort data is insufficient for a refined model, state that and supply
simple stage averages with the limitation noted.)*

**Stage conversion rates:**

| Stage | To closed-won | Cohort basis | Period covered | Sample size | Limitations |
|-------|--------------|-------------|---------------|-------------|-------------|
| `[Stage 2]` | `[X%]` | `[Segment / motion / source]` | `[e.g., FY2023–FY2024]` | `[n deals]` | `[e.g., excludes SMB; partner-sourced not separated]` |
| `[Stage 3]` | `[X%]` | | | | |
| `[Stage 4]` | `[X%]` | | | | |
| `[Channel / partner Stage 2]` | `[X%]` | `[Channel-qualified]` | | | |

*(Add rows for additional cohorts where data supports conditional conversion:
e.g., competitive deals, specific segments, inbound vs. outbound source.)*

**Sales cycle length:**

| Cohort | Median (days) | 75th percentile | Distribution note | Period covered |
|--------|--------------|-----------------|-------------------|---------------|
| `[Direct enterprise — Stage 3 to close]` | `[n]` | `[n]` | `[e.g., right-skewed; outliers above 150 days excluded]` | |
| `[Channel — Stage 2 to close]` | `[n]` | `[n]` | | |

*(Add rows for additional cohorts.)*

**Slippage and push rates:**

| Stage | Push rate (deals that miss close date by >30 days) | Average push duration | Period |
|-------|---------------------------------------------------|----------------------|--------|
| `[Stage 3]` | `[X%]` | `[n days]` | |
| `[Stage 4]` | `[X%]` | `[n days]` | |

**Pipeline generation rates:**

| Motion / source | Qualified pipeline created per month | ACV range | Period covered | Seasonality |
|----------------|-------------------------------------|-----------|---------------|-------------|
| `[Outbound enterprise]` | `[$X.XM]` | `[$X–$XK]` | | `[e.g., higher in Q2 and Q3]` |
| `[Inbound / marketing]` | `[$X.XM]` | | | |
| `[Partner / channel]` | `[$X.XM]` | | | |
| `[Event-sourced]` | `[$X.XM]` | | `[post-event qualification rate: X%]` | |

**Qualification rate (Stage 1 → Stage 2):** `[X%]` of leads / initial conversations
reach qualified Stage 2. Period covered: `[dates]`. Source: `[e.g., CRM lead-to-
opportunity conversion]`.

**ACV distribution:**

| Segment | Median ACV | 25th–75th percentile range | Notes |
|---------|-----------|--------------------------|-------|
| `[Enterprise]` | `[$X]` | `[$X–$X]` | |
| `[Channel-sourced]` | `[$X]` | | |

**Historical forecast bias** `[opt]`:

| Team / region | Systematic direction | Average magnitude | Period |
|---------------|---------------------|------------------|--------|
| `[e.g., Enterprise East]` | `[Optimistic / Conservative / Neutral]` | `[+/-X%]` | |

*(If forecast history is not yet available, note that baseline will be established
in the first Close and Calibrate run.)*

---

### I.4 — Seasonality `[init]`

*(Describes when pipeline is typically created and when it typically closes.
The Loop uses this to estimate the viable creation and conversion window per month.)*

| Month | Pipeline creation index | Close concentration | Notes |
|-------|------------------------|---------------------|-------|
| `[Feb]` | `[1.0 = average]` | `[X% of annual closes]` | |
| `[Mar]` | | | |
| `[Apr]` | | | |
| `[May]` | | | |
| `[Jun]` | | | |
| `[Jul]` | | | |
| `[Aug]` | | | |
| `[Sep]` | | | |
| `[Oct]` | | | |
| `[Nov]` | | | |
| `[Dec]` | | | |
| `[Jan]` | | | |

**Calendar constraints:** `[Any hard dates — e.g., "No new enterprise contracts
execute in the last 5 business days of December," or "Quarter-end compression adds
an average 8% to Stage 4 close rate in the final 2 weeks of Q4"]`

---

### I.5 — Capacity `[init]`

*(State capacity by source. Apply constraints to the source they affect, not as
one generic deduction.)*

**Pipeline generation capacity:**

| Motion | Reps or resources | Expected pipeline output per resource per month | Constraint |
|--------|-----------------|------------------------------------------------|-----------|
| `[Outbound enterprise]` | `[n AEs]` | `[$X.XM qualified]` | `[e.g., SDR capacity is the binding constraint at 3 SDRs]` |
| `[Channel / partner]` | `[n partners]` | `[$X.XM]` | |

**Deal progression capacity (technical / solutions):**
```
Solutions engineering available per quarter:   [n SEs]
Max concurrent technical evaluations:          [n]
Known Q[n] bottleneck:                         [Description or None]
```

**Implementation / delivery capacity:**
```
New enterprise onboards supportable per quarter:    [n]
Current delivery team:                              [n implementation resources]
Contracted backlog (pre-committed delivery):        [n onboards / $X.XM ARR affected]
Capacity constraint affects recognition:            [Yes / No / Describe]
```

**Rep ramp and attainment:**
```
Fully ramped AEs (>6 months tenure):       [n]
Ramping AEs (1–6 months):                 [n] — expected attainment: [X%] of quota
New hires planned this period:             [n] — ramp date: [date] — first contribution period: [quarter]
```

---

### I.6 — Carryover Pipeline `[init]`

*(Pipeline already in the CRM at initialization. This is the starting inventory
for the current-period projection.)*

**CRM snapshot date:** `[YYYY-MM-DD]`

| Stage | Opportunity count | Total value | Median age (days) | Median time in stage (days) |
|-------|------------------|-------------|-------------------|-----------------------------|
| `[Stage 2]` | | | | |
| `[Stage 3]` | | | | |
| `[Stage 4]` | | | | |
| `[Channel Stage 2]` | | | | |

**Notable concentration:**
```
Largest single opportunity:     [Account name / ID — $X.XM — Stage N]
Segment concentration:          [e.g., "62% of Stage 4 is financial services"]
Source concentration:           [e.g., "4 of 8 Stage 3 deals are channel-sourced"]
Geographic concentration:       [e.g., "Stage 4 is 80% US"]
```

**Known dependencies in carryover pipeline:**
```
[e.g., "3 Stage 4 accounts pending OCC Basel IV guidance — expected September"]
[e.g., "2 Stage 3 accounts blocked on security review, internal process takes 45 days"]
```

---

### I.7 — Approved Initiative Assumptions `[init if applicable]`

*(Initiatives expected to produce incremental pipeline or ARR above the existing
engine. Always labeled separately from the base engine projection. Never pre-blended
into the historical model.)*

**Initiative:** `[Name]`
```
Type:                    [e.g., new partner motion / campaign / product launch / territory expansion]
Segment / motion affected: [Description]
Ramp date:               [When first contribution is expected]
Ramp curve:              [e.g., "Month 1: $0, Month 2: $200K, Month 3: $400K, steady state: $600K/month"]
Contribution range:      [$X.XM – $X.XM this period]
Evidence basis:          [What the range is grounded in — historical analogs, pilot, signed agreements]
Known dependencies:      [What must be true for the ramp to hold]
Confidence level:        [Low / Medium / High]
Approved by:             [Owner and approver]
```

*(Repeat block for each approved initiative.)*

---

### I.8 — Known Dependencies and Constraints `[init]`

```
Product / delivery dependencies: [e.g., "Module X required for Segment Y deals;
                                   currently scheduled Q2; delay affects X pipeline"]
Regulatory dependencies:         [e.g., "OCC guidance expected September; affects
                                   urgency in US enterprise pipeline"]
External market dependencies:    [e.g., "Partner contract renewal due April 1"]
Legal / procurement constraints: [e.g., "Average enterprise security review: 45 days"]
```

---

### I.9 — Version Ledger Initialization `[init]`

*(Create the first entry. This is the starting state, not a revision.)*

| Revision ID | Date | Parameter | Value | Notes |
|-------------|------|-----------|-------|-------|
| `M01` | `[YYYY-MM-DD]` | `[Model version initialized]` | `[Parameter set as defined in I.3]` | `[Initial model — no prior version]` |

---

## MODULE R — Reforecast

*Complete at each operating review. Supply only what changed or is new.*
*The Loop carries forward all MODULE I and prior MODULE R inputs.*
*Do not re-enter unchanged parameters.*

---

### R.1 — Run Context `[req]`

```
Organization:                     [Name]
Reforecast run date:              [YYYY-MM-DD]
Fiscal period:                    [e.g., Month 7 of 12 — July actuals complete]
Prior projection version:         [e.g., R02 — July 1, 2025]
Prepared by:                      [Role]
```

---

### R.2 — Actuals Update `[req]`

```
[Metric] recognized YTD as of [date]:    [$X.XM]
Source of record:                         [e.g., Finance / ERP system]
Period covered:                           [e.g., Feb 1 – Jul 31, 2025]
Notes or adjustments:                     [e.g., "Includes $X.XM reclassification from upsell"]
```

**Actuals vs. prior projection (optional, helpful):**
```
Prior projection for this period:    [$X.XM]
Actual recognized:                   [$X.XM]
Delta:                               [±$X.XM]
Primary driver of delta:             [Description]
```

---

### R.3 — Current Pipeline Snapshot `[req]`

**CRM snapshot date:** `[YYYY-MM-DD]`

*(Provide the current pipeline population. The Loop applies model conversion and
timing filters. Do not apply conversion judgments here — that is the Loop's job.
Supply factual pipeline state and any known deal-level facts that affect conversion.)*

**Pipeline summary by stage:**

| Stage | Count | Total value | Median age (days in stage) | Notable characteristics |
|-------|-------|-------------|--------------------------|------------------------|
| `[Stage 2 — direct]` | | | | |
| `[Stage 3 — direct]` | | | | |
| `[Stage 4 — direct]` | | | | |
| `[Channel / partner Stage 2]` | | | | |

**Deal-level detail for Stage 3 and Stage 4** `[req for Stage 3+]`:

| Opportunity | Value | Stage | Days in stage | Segment | Source | Competitive status | Procurement status | Known dependencies |
|-------------|-------|-------|--------------|---------|--------|-------------------|-------------------|-------------------|
| `[Account name]` | `[$X.XM]` | `[n]` | `[n]` | `[Seg]` | `[Source]` | `[None / Competitor present]` | `[Not started / Active / Redlines / Final]` | `[Description or None]` |

**Pipeline additions since prior snapshot:** `[$X.XM from n new opportunities]`

**Pipeline removals since prior snapshot:** `[$X.XM — reason: [lost / disqualified / pushed to next period]]`

---

### R.4 — Observed Commercial Metrics `[req]`

*(Actuals for the commercial parameters the model depends on. The Loop compares
these with model assumptions to assess whether parameters remain valid.)*

```
Observed win rate (period):            [X% — cohort: segment/stage/source — n deals]
Observed median cycle time:            [n days — cohort: stage range — n closed deals]
Observed pipeline generation:          [$X.XM in new qualified Stage 2 — period: dates]
Observed average deal size (ACV):      [$X.XM — n closed deals — segment]
Observed slippage rate:                [X% of Stage 4 missed committed close date — average push: n days]
```

**Material deviations from model parameters:**
```
[e.g., "Win rate 27% vs. 38% model — Luvexis present in 4 of 7 losses"]
[e.g., "Cycle time 94 days median vs. 90 days model — consistent across 3 closed deals"]
[e.g., "Stage 4 slippage 35% vs. 20% model — procurement delays in financial services"]
```

---

### R.5 — Field Overlays `[opt — evidence required for each]`

*(Field overlays are the field leader's evidence-backed adjustment to the model
projection on specific deals, accounts, or cohorts. The Loop applies them as
View 2 only. Every overlay must supply the evidence behind it. An assertion that
a deal will close is not an overlay — it is a prediction. Supply the observable
facts that change the probability assessment.)*

*(New overlays this run:)*

**Overlay:** `[OV-n]`
```
Scope:                    [Specific opportunity / account name or cohort]
Direction:                [Increase / Decrease]
Model value (before):     [$X.XM — the Loop's model-only contribution for this scope]
Field-adjusted value:     [$X.XM]
Net effect:               [±$X.XM]
Owner:                    [Role and name]
Date:                     [YYYY-MM-DD]
Evidence:                 [e.g., "Board budget approval confirmed per email Aug 1;
                            procurement department engaged; signed NDA complete"]
Reason:                   [Why this evidence changes the probability assessment]
Expiration / review date: [YYYY-MM-DD — date to reassess if deal has not progressed]
```

*(Revised overlays this run — reference prior overlay ID and state what changed.)*

*(Expired or closed overlays this run — reference prior overlay ID and state outcome.)*

---

### R.6 — Initiative Progress Update `[opt if initiatives active]`

*(For each approved initiative from MODULE I, supply current progress.
Do not adjust the initiative's base assumptions here — that is a Projection
Version Ledger update if warranted.)*

**Initiative:** `[Name]`
```
Status:                   [On track / Behind ramp / Ahead of ramp / Stalled]
Contribution to date:     [$X.XM — period: dates]
Expected vs. actual ramp: [e.g., "Expected $200K by July; actual $140K"]
Updated range (if changed): [$X.XM – $X.XM — change reason: description]
Known dependency update:  [e.g., "Partner contract now signed; ramp confirmed"]
```

---

### R.7 — Capacity Update `[opt — supply if changed since prior run]`

```
Delivery capacity change:     [e.g., "Delivery team capacity measured at 3.5 onboards
                               per quarter; prior run assumed 4.0"]
Rep headcount change:         [e.g., "2 AE departures; 1 replacement hired Aug 1"]
SE bottleneck update:         [Description or No change]
```

---

### R.8 — External Events and Dependencies `[opt]`

*(Events outside the model that affect pipeline, conversion, timing, or capacity
this period. The Loop cannot see these without your input.)*

```
[e.g., "OCC Basel IV guidance expected September — creates urgency in US pipeline"]
[e.g., "Competitor announced full coverage of Basel IV — 3 Stage 3 accounts have
        requested competitive comparison"]
[e.g., "Partner contract pending renewal — no new introductions since July 15"]
[e.g., "Key champion departed at Telvoran Capital — deal at risk"]
```

---

### R.9 — Version Ledger Update `[opt — required if model parameters changed]`

*(If observed metrics in R.4 indicate that a model parameter should be revised,
record the revision here. Do not silently update model parameters.)*

| Revision ID | Date | Parameter | Original value | Revised value | Evidence | Prior runs affected |
|-------------|------|-----------|---------------|---------------|---------|---------------------|
| `[M0n]` | `[YYYY-MM-DD]` | `[e.g., Stage 3 direct win rate]` | `[38%]` | `[30%]` | `[3 closed deals at 27%; Luvexis present in all losses]` | `[R01, R02 annotated]` |

---

## MODULE C — Close and Calibrate

*Complete at period close after verified actuals are available.*
*The Loop will compare all prior Projection Runs against these actuals.*

---

### C.1 — Run Context `[req]`

```
Organization:                   [Name]
Period closed:                  [e.g., FY2025: Feb 1, 2025 – Jan 31, 2026]
Close and Calibrate run date:   [YYYY-MM-DD]
Verified actuals as of:         [YYYY-MM-DD — source of record close date]
Prepared by:                    [Role]
```

---

### C.2 — Verified Actual Outcomes `[req]`

```
Total [metric] recognized:               [$X.XM]
Source of record:                        [e.g., Finance / ERP — finalized]
Reconciliation notes:                    [Any material accounting adjustments]
```

**Contribution by source (actual):**

| Source | Actual contribution | Notes |
|--------|---------------------|-------|
| `[Direct enterprise — pipeline at initialization]` | `[$X.XM]` | |
| `[Direct enterprise — pipeline created during year]` | `[$X.XM]` | |
| `[Channel / partner]` | `[$X.XM]` | |
| `[Initiative uplift — specify]` | `[$X.XM]` | |
| `[Field overrides — aggregate]` | `[$X.XM]` | |

---

### C.3 — Observed Commercial Parameters (full year) `[req]`

```
Win rate (full period — direct enterprise):   [X% — n total Stage 2+ opportunities]
Win rate (channel-sourced):                   [X% — n]
Median cycle (Stage 3 to close):              [n days — n deals]
Median cycle (Stage 2 to close, channel):     [n days — n deals]
Actual pipeline generation (full year):       [$X.XM qualified — by motion if available]
Actual ACV (closed-won enterprise):           [$X.XM median — n deals]
Stage 4 slippage rate:                        [X% — average push: n days]
```

---

### C.4 — Field Overlay Outcomes `[req if overlays were active]`

*(For each field overlay issued during the period, state the actual outcome.)*

| Overlay ID | Scope | Model value | Field-adjusted value | Actual outcome | Field judgment: improved / degraded / neutral |
|------------|-------|-------------|---------------------|---------------|----------------------------------------------|
| `[OV01]` | `[Scope]` | `[$]` | `[$]` | `[$]` | `[Assessment]` |

---

### C.5 — Official Forecast History `[opt]`

*(If official operating forecasts were set during the period, list them here
to enable official-forecast accuracy analysis.)*

| Date | Official forecast | Period covered | Actual | Error |
|------|-----------------|----------------|--------|-------|
| `[YYYY-MM-DD]` | `[$X.XM]` | `[period]` | `[$X.XM]` | `[±$X.XM / ±X%]` |
