# Revenue Projection Loop — Example Output

*This output was produced by running the loop-prompt against the Nexovane
FY2025 Month 7 Reforecast input (example-input.md).*

---

### REVENUE PROJECTION LOOP — RUN OUTPUT

**Organization:** Nexovane
**Projected metric:** New Enterprise ARR — net new annual recurring revenue from
new enterprise customer contracts executed in FY2025; excludes renewals,
expansions on existing contracts, and SMB-tier accounts (ACV < $50K)
**Metric inclusion rules:** New enterprise contracts, ACV ≥ $50K, recognized at contract execution
**Metric exclusion rules:** Renewals, upsells on existing contracts, SMB tier
**Recognition rule:** ARR recognized at contract execution date
**Projection horizon:** FY2025 — February 1, 2025 – January 31, 2026
**Run type:** Reforecast
**As-of date:** August 2, 2025
**Pipeline snapshot date:** August 2, 2025
**Projection version:** R03
**Model version:** M03 (updated this run: Stage 3 win rate 38% → 30%; cycle 90 → 94 days)

---

### PROJECTION BRIDGE

**Model parameters in effect (M03):**
- Stage 4 → closed-won (direct enterprise): 72%
- Stage 3 → closed-won (direct enterprise): 30% (updated from 38% per M03; Luvexis-adjusted)
- Stage 2 → closed-won (direct enterprise): 22% (no FY2025 data yet; retaining M01 rate)
- Channel Stage 2 → closed-won (Korval): 65%
- Median cycle Stage 3 → close: 94 days (updated from 90 per M03)
- Median cycle Stage 2 → close (channel): 32 days
- Stage 4 slippage: 20% push rate at 47 days average (model; observed Q2 rate was 50%
  on n=2 — too small to update; flagged for monitoring)

**Timing filter basis:**
- Fiscal year end: January 31, 2026
- Recognition lag: 0 days (contract execution = recognition)
- Contracting / legal: 21 days typical (from procurement approval to signed contract)
- Available window from August 2: 182 days
- Stage 4 close feasibility: Yes — median 28 additional days from Stage 4; all 4 within window
- Stage 3 close feasibility: Yes, if cycle holds at 94 days — Stage 3 entered June–July closes
  by September–November; within window; one account (Telvoran) at risk due to champion absence
- Stage 2 (direct): Marginal — Stage 2 entered July; 140+ days to close = December 19 at median;
  within window but subject to slippage
- Channel Stage 2: Yes — 32-day cycle; all 6 referrals close well within window if they qualify

```
Recognized actuals (Feb 1 – Jul 31, 2025):          $5.48M   [Certain]

+ Current-pipeline contribution:

  Stage 4 — direct enterprise (4 accounts, $2.03M):
    Base model (72% × $2.03M):               $1.46M
    Slippage adjustment (20% push at $1.46M
    → $0.29M pushed to Q1 FY2026):          -$0.29M
    Stage 4 net (model):                     $1.17M   [High — 4 accounts, procurement active or legal]

  Stage 3 — direct enterprise (5 accounts, $2.25M):
    Base model (30% × $2.25M):               $0.68M
    Timing filter: Telvoran Capital ($420K)
    — champion absent through Sep 1; deal
    progression stalled; moves to marginal:
    → Telvoran contribution: 10% × $420K = $0.04M
    (partial, not excluded — champion may return;
    flagged as marginal)
    Stage 3 net (model):                     $0.64M   [Medium — Luvexis present in 4 of 5;
                                                         cycle risk on Telvoran]

  Stage 2 — direct enterprise (2 accounts, $0.80M):
    Base model (22% × $0.80M):               $0.18M
    Timing filter: both entered Stage 2 in July;
    at 94-day cycle from Stage 3 entry (not yet
    in Stage 3), these deals require 140+ days
    from Stage 2 to close. Median close: December 19.
    Slippage risk at 20% push rate is material.
    Retained at model rate; flagged as low-confidence.
    Stage 2 net (model):                     $0.18M   [Low — timing marginal; slippage risk]

  Channel Stage 2 — Korval (6 accounts, $0.60M):
    Base model (65% × $0.60M):               $0.39M
    Capacity constraint: delivery team at 3.5
    onboards/quarter; Korval competes with direct
    for same slots. Maximum Korval contribution
    without displacing direct enterprise: 2 channel
    onboards in Q3, 2 in Q4 = 4 total × $100K ACV
    = $0.40M ceiling. Model rate ($0.39M) falls
    within capacity ceiling — no additional deduction
    required at base. Constraint binds only if both
    channel and direct enterprise volume exceeds 3.5/quarter.
    Channel net (model):                     $0.39M   [Medium-High — short cycle; capacity monitored]

  Total current-pipeline contribution (model):  $2.38M

+ Future-pipeline contribution (existing engine):

  Latest useful creation date calculation:
    Period end: January 31, 2026
    − Contracting/legal: 21 days
    − Sales cycle from Stage 3: 94 days
    − Stage 2 qualification: 21 days minimum
    Latest useful Stage 2 creation date: October 16, 2025

  August creation vintage (existing engine):
    Expected direct: $1.4M qualified (peak-season 1.4× factor × $1.1M base)
    Qualification rate: 70% → $0.98M to Stage 2
    Win rate (30% at Stage 3) × timing factor (full 94-day window available):
    Contribution: $0.98M × 30% × 0.95 timing = $0.28M
    Channel (Korval): 3 additional referrals expected × $100K × 65% = $0.20M
                      (capacity check: within 3.5/quarter ceiling with current pipeline)
    August vintage contribution:   $0.48M   [Medium-Low]

  September creation vintage:
    Expected direct: $1.3M qualified (seasonal slightly above average)
    Win rate × timing factor (94-day cycle from Stage 3; created Sep → closes by Dec):
    $1.3M × 70% × 30% × 0.85 timing = $0.23M
    Channel: 3 referrals × $100K × 65% × 0.90 timing = $0.18M
    September vintage contribution:  $0.41M   [Medium-Low]

  October creation vintage:
    Direct enterprise: October creation enters Stage 2 in October; Stage 3 in November;
    close by end of January requires exactly 94-day cycle with no slippage.
    Timing probability: 30%. Adjusted: $1.0M × 70% × 30% × 0.30 = $0.06M
    Channel: 32-day channel cycle means October channel creation can close by November.
    3 referrals × $100K × 65% = $0.20M (channel not affected by 94-day constraint)
    October vintage contribution:    $0.26M   [Low for direct; Medium for channel]

  Pipeline created after October 16 (direct enterprise):
    Excluded from current-period projection → next-period carryover.
    Estimated next-period carryover value: $0.8M–$1.2M.

  Total future-pipeline contribution (model):   $1.15M   [Medium-Low]

+ Approved-initiative uplift — Korval expansion:

  Korval initiative uplift above existing-engine channel projection:
    Existing engine already includes 3 referrals/month (base generation).
    Initiative represents incremental referrals beyond base, and the signed
    partnership structure (vs. ad-hoc introductions). Base-case initiative uplift
    above engine: $0.3M–$0.6M (the initiative's formalization and partner
    incentive structure drives incremental volume beyond what spontaneous
    introductions would have generated).
    Confidence: Medium (pipeline ahead of ramp; recognition not yet proven)
    Korval initiative uplift (labeled separately):  $0.3M–$0.6M   [Medium]

+ Field overlays (net, evidence-backed):
  OV01 Velstrom Asset Management:   +$0.12M (model $0.39M → field $0.51M)
  OV02 Telvax Investment Group:     -$0.11M (model $0.37M → field $0.26M)
  OV03 Pelantrix Advisors:          +$0.11M (model $0.11M → field $0.23M)
  Net overlay effect:               +$0.12M   [Evidence-backed — see Field Overlay Records]

− Capacity constraints:
  Delivery capacity constraint:
    3.5 onboards/quarter measured vs. 4.0 assumed.
    At base projection volumes, delivery is the binding constraint in Q4 if both
    direct enterprise Stage 3 accounts and Korval referrals close concurrently.
    Estimated current-period impact at base (not all scenarios breach this):
    -$0.10M (1 deal expected to be pushed to Q1 FY2026 due to capacity)   [Delivery]

− Timing and slippage (residual):
  Telvoran Capital champion absence:   -$0.04M (absorbed in Stage 3 calculation above;
                                        no additional deduction needed)
  Overall additional slippage buffer:  -$0.08M (residual; primarily Stage 3 and 4)

− Overlap and duplication:
  Alderix Capital Expansion ($490K in Stage 3) is an existing customer requiring
  a new contract for a new product. It qualifies under the metric inclusion rules.
  No double-counting with YTD actuals (Alderix Capital original contract already recognized).
  No deduction required.

= EVIDENCE-BACKED PROJECTION RANGE (model-only base):

  Actuals:                           $5.48M
  Current-pipeline (model):         +$2.38M
  Future-pipeline (model):          +$1.15M
  Initiative uplift (base):         +$0.30M
  Capacity constraint:              -$0.10M
  Residual slippage:                -$0.08M

  Model-only base projection:        $9.13M
  Model-only range:                  $8.7M – $9.5M
```

**Target:** $12.0M
**Supported or unsupported gap (model-only base):** $2.5M – $3.3M **[unsupported]**

---

**Confidence composition of model-only base projection ($9.13M):**
- Certain (recognized actuals): $5.48M (60%)
- High-confidence remaining: $0.88M (10%) — Stage 4 pipeline net of slippage
- Medium-confidence remaining: $1.64M (18%) — Stage 3 + channel at model rates
- Medium-Low / Low / initiative-dependent: $1.13M (12%) — future pipeline + initiative base

---

### THREE PROJECTION VIEWS

**View 1 — Model-only projection:** $8.7M – $9.5M
*(No field overlays. Actuals $5.48M + current pipeline at M03 conversion + future
pipeline at historical generation + Korval initiative at base-case ramp.
Model version M03 — Stage 3 win rate 30%, cycle 94 days.)*

**View 2 — Field-adjusted projection:** $8.8M – $9.6M
*(Model-only plus OV01 +$0.12M, OV02 -$0.11M, OV03 +$0.11M. Net field effect:
+$0.12M. Field overlays have modest net impact this run — two overlays partially
offset each other. The OCC deadline on Velstrom is the most material positive;
Telvax competitive risk is the most material negative.)*

**View 3 — Official operating forecast:** Not supplied this run.
*(RevOps will present projection to CRO and Finance on August 5; official commit
to be recorded as an organizational event in R04.)*

---

### FIELD OVERLAY RECORDS

| Overlay ID | Scope | Direction | Net effect | Owner | Date | Evidence summary | Model value | Adj. value | Expires |
|------------|-------|-----------|-----------|-------|------|-----------------|-------------|------------|---------|
| OV01 | Velstrom Asset Management — Stage 4, $540K | + | +$0.12M | Regional VP Sales NE | Aug 2, 2025 | OCC exam Jan 15; CFO verbal; procurement approved Jul 31; redlines expected Aug 8 | $0.39M | $0.51M | Sep 1, 2025 |
| OV02 | Telvax Investment Group — Stage 4, $520K | − | -$0.11M | Regional VP Sales NE | Aug 2, 2025 | Luvexis proposed 20% below ACV; champion preferred vendor stated; redlines in progress but competitive risk active | $0.37M | $0.26M | Sep 1, 2025 |
| OV03 | Pelantrix Advisors — Stage 3, $380K | + | +$0.11M | Regional VP Sales SE | Aug 2, 2025 | CISO security review started Aug 1, 6 weeks early; confirmed in writing; CFO in 2 calls; no Luvexis | $0.11M | $0.23M | Sep 15, 2025 |

---

### SCENARIO RANGES

| Scenario | Range | Key conditions | Joint feasibility |
|----------|-------|----------------|-------------------|
| Evidence-supported lower bound | $7.8M – $8.2M | Actuals $5.48M + Stage 4 closes with OV01 and OV02 applied + Velstrom (OCC deadline) + Kessval only from Stage 3 + Korval channel 4 accounts at $100K = no new pipeline required | Confirmed — these are existing accounts with documented progress |
| Base projection (model-only) | $8.7M – $9.5M | M03 conversion applied to all stages; 3 creation vintages at historical rate; Korval initiative at base ramp; capacity at 3.5/quarter | Confirmed — conservative stage conversion and seasonal generation rates |
| Recovery or upside case | $9.8M – $10.6M | OCC guidance creates urgency (September) → 2 additional Stage 3 accounts accelerate; Telvax is retained despite Luvexis (competitive response effective); all 6 Korval referrals qualify; delivery capacity reaches 4.0/quarter in Q4 | Partially confirmed — OCC guidance is expected but not published; Korval referral volume confirmed; Telvax competitive outcome uncertain; capacity requires backfill confirmation |
| Best credible ceiling | $10.8M | All recovery conditions hold AND Luvexis does not expand coverage (keeps Stage 3 win rate at 35% vs. 30%) AND October channel vintage closes before year end | Capacity ceiling of 4.0/quarter must hold across Q3 and Q4 simultaneously — shared constraint between direct enterprise and channel closes; this is the binding joint constraint on the ceiling |

*Theoretical all-favorable ceiling: $11.5M — requires every deal in current pipeline to close
at 90%+ conversion AND all 3 creation vintages to outperform AND initiative at upper bound
AND capacity at 4.5/quarter. Delivery capacity at 4.5 requires both the backfill hire AND
no implementation extensions on any Q3 close. These conditions cannot all be jointly true
given current delivery team status.*

---

### PROJECTION MOVEMENT BRIDGE (vs. R02 — July 1, 2025)

```
Prior base projection R02 (Jul 1, 2025):      $10.4M
Current base projection R03 (Aug 2, 2025):     $9.1M   [midpoint of $8.7M–$9.5M]
Change:                                         -$1.3M

Drivers:
  Module ship delay (Jul 28 vs. Jun 15):
    3 Stage 3 accounts delayed ~4–6 weeks;
    2 of 3 expected to still close within window,
    but at lower conversion given timing pressure.
    Effect:                                     -$0.38M  [pipeline timing moved]

  Luvexis partial coverage announcement (Jul 22):
    Stage 3 win rate revised 38% → 30% per M03.
    Applied to $2.25M Stage 3 pipeline:
    Effect:                                     -$0.18M  [model parameter update M03]

  Cycle time revision 90 → 94 days per M03:
    Tighter timing window; October vintage
    contribution reduced:
    Effect:                                     -$0.09M  [model parameter update M03]

  Delivery capacity constraint identified:
    3.5/quarter vs. 4.0 assumed; caps channel
    and direct upside in Q4:
    Effect:                                     -$0.10M  [capacity constraint applied]

  Telvoran Capital champion absence:
    Deal progression stalled; contribution
    moved to marginal:
    Effect:                                     -$0.08M  [pipeline move — field event]

  New Korval referrals (6 accounts, $0.60M added):
    6 new Stage 2 channel accounts at 65%
    conversion within timing window:
    Effect:                                     +$0.39M  [pipeline addition]

  Alderix Capital Expansion entered Stage 3:
    $490K new Stage 3 at 30% = $0.15M added
    (not in R02 pipeline):
    Effect:                                     +$0.15M  [pipeline addition]

  Prior R02 actuals delta (actual vs. projected):
    R02 projected $5.38M YTD; actual $5.48M:
    Effect:                                     +$0.10M  [actuals revision]

  Other residual movements:                    -$0.21M  [slippage buffer adjustment,
                                                          minor stage changes]

Net change R02 → R03:                          -$1.30M
```

---

### GAP ANALYSIS

**Target:** $12.0M
**Current base projection (model-only):** $8.7M – $9.5M
**Unsupported gap:** $2.5M – $3.3M

**Required conditions to reach $12.0M (jointly, not independently):**

1. *$10.4M of qualified Stage 2 direct enterprise pipeline must be created and
   proceed through to close before January 31, 2026.* Given 94-day cycles and the
   latest useful creation date of October 16, this requires peak monthly generation
   of approximately $3.5M/month in qualified pipeline — more than 3× the historical
   rate. **Evidence status: No evidence basis. This condition is not achievable with
   the existing commercial engine.**

2. *Stage 3 win rate must recover to 55%+ (from current observed 33% and model 30%).* 
   This would require winning the majority of competitive deals in which Luvexis is
   present. **Evidence status: No current evidence basis; Luvexis announced partial
   coverage July 22; no competitive wins against Luvexis in FY2025 yet.**

3. *Delivery capacity must expand to 6+ onboards per quarter.* Current capacity is
   3.5. Even at 4.0, the ceiling on recognizable ARR from delivery constraints limits
   upside. Reaching $12.0M would require delivery at approximately 6 concurrent
   onboards — a 70%+ increase from current capacity. **Evidence status: No basis.
   The backfill hire is not confirmed.**

**Conclusion:** The $12.0M target is not achievable under any jointly feasible scenario.
The unsupported gap of $2.5M–$3.3M cannot be closed through execution improvement
alone. The commercial engine's realistic ceiling is $10.8M (best credible ceiling)
under jointly feasible conditions.

*This finding should be supplied to the Annual GTM Strategy and Goal Governance
Loop. The strategy decision — whether to revise the commitment, identify a new
contribution source, or formally acknowledge the gap — belongs there, not here.*

---

### LATEST USEFUL PIPELINE CREATION DATE

**Date: October 16, 2025**

**Basis:**
- Period end: January 31, 2026
- Contracting / legal from procurement approval: −21 days
- Sales cycle median (Stage 3 → close, M03): −94 days
- Stage 2 qualification minimum (before entering Stage 3): −21 days
- Total: January 31 − 136 days = **September 17** for Stage 3 entry
- Working backward: Stage 2 creation must precede Stage 3 entry by 21 days minimum
- **Latest useful Stage 2 creation date: October 16, 2025** for direct enterprise
- **For Korval channel:** January 31 − 32-day cycle = December 30, 2025 (channel creation
  date much later due to shorter cycle; channel pipeline created through December is viable)

**Pipeline created in direct enterprise motions after October 16:**
Excluded from current-period projection. Estimated next-period carryover:
$0.8M–$1.2M in qualified pipeline expected to be created in November–January
for FY2026 coverage.

---

### SENSITIVITY ANALYSIS

| Variable | Unit | Dollar impact (base) | Within near-term control? |
|----------|------|---------------------|--------------------------|
| Stage 3 win rate | +1 pp (e.g., 30% → 31%) | +$0.023M | Partially — competitive response may improve rate |
| Stage 4 win rate | +1 pp (e.g., 72% → 73%) | +$0.020M | Partially — limited to 4 accounts in pipeline |
| Median cycle time | +/−10 days | ±$0.09M (through vintage timing effects) | No — market-driven; financial services procurement pace |
| Pipeline generation rate | +$1M qualified Stage 2 | +$0.30M (at 30% win rate, before timing filter) | Yes — within Q3 effort; limited by October 16 useful creation date |
| ACV | +10% across current pipeline | +$0.33M | No — deal size is buyer-budget-driven |
| Delivery capacity | +1 onboard/quarter | +$0.10M–$0.15M | Yes — backfill hire in August enables this |
| Latest useful creation date | pipeline slips 30 days | −$0.12M in direct enterprise vintage | No — time-bound; cannot be extended |

**Highest-leverage variable this run:**
**ACV** at +$0.33M per 10% increase — but not within near-term control. Among
controllable variables, **delivery capacity** (backfill hire) is the fastest path
to protect upside: +$0.10–$0.15M and unblocks channel acceleration for Q4.
**Pipeline generation rate** in August has diminishing impact because October 16
is the useful creation date cutoff — there are approximately 10 weeks of productive
direct enterprise pipeline creation remaining.

---

### EVIDENCE GAPS AND CONFIDENCE LIMITATIONS

1. **Stage 3 win rate on small sample.** M03 win rate of 30% is based on 9 deals
   through the funnel in FY2025 — 3 wins, 6 losses. The Luvexis pattern is clear,
   but the non-competitive win rate (75%) and competitive win rate (0%) suggest
   the blended rate is highly sensitive to the share of pipeline with Luvexis present.
   Currently 7 of 11 active pipeline accounts have Luvexis present. If Luvexis expands
   to additional regulatory areas, the competitive win rate could deteriorate further.

2. **Stage 4 slippage on very small sample.** Observed Q2 slippage was 50% (n=2).
   Model retains 20% slippage from FY2024 historical data. If the higher slippage
   rate reflects a structural shift in financial services procurement cycles, Stage 4
   contribution could be $0.1M–$0.2M lower than modeled.

3. **Korval channel qualification rate unobserved.** 6 referrals in qualification;
   qualification calls begin August 5. If qualification rate is below 65% (e.g.,
   50%), channel contribution drops by approximately $0.09M.

4. **OCC guidance timing.** OCC Basel IV guidance expected September 2025. If guidance
   is delayed to Q4 or published with unexpected scope, urgency in Stage 3 accounts
   may not materialize as modeled in the recovery/upside case.

5. **Telvoran Capital champion return.** If champion does not return from leave before
   September 1, deal may need to be re-engaged from the economic buyer — adding
   60–90 days and making current-period close unlikely. Contribution from Telvoran
   ($420K) is currently modeled at a marginal 10% — risk is downside.

---

### PROJECTION VERSION LEDGER UPDATES THIS RUN

| Revision ID | Date | Parameter | Original value | Revised value | Evidence | Prior runs affected |
|-------------|------|-----------|---------------|---------------|---------|---------------------|
| M02 | Aug 2, 2025 | Stage 3 direct enterprise win rate | 38% | 30% | 3 FY2025 closed deals; 4 losses with Luvexis present; consistent pattern | R01, R02 annotated |
| M03 | Aug 2, 2025 | Median cycle time (Stage 3 → close) | 90 days | 94 days | 3 FY2025 closed deals; consistent; procurement cycles longer than FY2024 | R01, R02 annotated |

---

### NEXT REVIEW

**Next scheduled run:** September 1, 2025
**Run type:** Reforecast (R04)

**Priority data to collect before September 1:**
- OCC Basel IV guidance publication (if published in August — accelerate review)
- Velstrom Asset Management: signed redlines or delay signal by August 15 (OV01 expiry check)
- Telvax Investment Group: competitive outcome by September 1 (OV02 expiry)
- Korval channel: qualification outcomes for all 6 August referrals
- Delivery capacity: backfill hire decision and timeline
- Telvoran Capital: champion return status and deal re-engagement timeline
- August pipeline creation actuals (direct enterprise): compare to $1.4M expectation

**Standing triggers that would accelerate a run before September 1:**
- OCC guidance published in August (creates urgency signal; may warrant upside-case revision)
- Luvexis announces expanded coverage (5+ of 8 Basel IV areas) → immediate Stage 3
  win rate reassessment required
- Velstrom Asset Management closes early → positive signal; reassess ceiling
- Any Stage 4 loss to Luvexis → downside scenario becomes base; breach communication
  to Annual GTM Strategy Loop required
- Delivery backfill hire confirmed → capacity constraint lifted; upside scenario becomes viable
