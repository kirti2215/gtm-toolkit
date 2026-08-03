# Annual GTM Strategy and Goal Governance Loop — Example Input

**Organization:** Nexovane
**Fiscal year:** FY2025 (February 1, 2025 – January 31, 2026)
**Run date:** August 2, 2025
**Review type:** Month 7 Operating Review

---

## MODULE A — Planning and Initialization

*Set at annual planning (February 1, 2025). Fields are immutable after initialization.
Any change to a value below must be recorded in A9 — Version Ledger.*

---

### A1 — Organization and Period Context

**Organization:** Nexovane
**Product:** NexovaneOS — compliance automation and regulatory intelligence platform
  for financial services firms
**Primary market:** Mid-market and enterprise financial services (banks, RIAs,
  advisory firms, asset managers)
**Key competitor:** Luvexis (compliance workflow platform)
**Fiscal year start:** February 1, 2025
**Fiscal year end:** January 31, 2026
**Planning date:** February 1, 2025
**Finance/RevOps forecast source:** Nexovane Revenue Operations, Salesforce CRM,
  confirmed by CFO sign-off February 1, 2025

---

### A2 — Commitment Portfolio

**Commitment summary:**

| C# | Commitment name | Metric | Target | Baseline | Owner | Protection level |
|----|----------------|--------|--------|----------|-------|-----------------|
| C1 | New Enterprise ARR | Net new enterprise ARR closed and booked | $12.0M | $0 (incremental) | CRO | Non-negotiable |
| C2 | Net Revenue Retention | NRR across all accounts at fiscal year-end | ≥108% | 103% (FY2024 actual) | VP Customer Success | Protected |
| C3 | New Enterprise Pipeline | Qualified pipeline in enterprise segment | ≥$48M | $0 (incremental) | VP Sales | Supporting |

---

**Commitment C1 — New Enterprise ARR** `[non-negotiable]`

Metric name: Net new enterprise ARR
Metric definition: ARR from new enterprise logos (≥$150K ACV) signed and booked
  in FY2025. Does not include upsell or expansion from existing logos unless
  executed as a new multi-entity contract.
Exclusion rules: Renewal ARR; expansion ARR from existing single-entity accounts;
  professional services revenue; pilot ARR until converted to full contract
Recognition rule: Contract signed, MSA executed, and first invoice issued
Time horizon: February 1, 2025 – January 31, 2026
Source of record: Salesforce CRM, confirmed by Finance at close
Currency: USD
Protection level: Non-negotiable. Breach notice required if evidence indicates
  target is unattainable under any credible scenario.
Revision authority: Board approval required for target revision

---

**Commitment C2 — Net Revenue Retention**

Metric name: Net Revenue Retention (NRR)
Metric definition: (Starting ARR + expansion ARR − contraction ARR − churn ARR)
  ÷ Starting ARR, measured at January 31, 2026 across all accounts
Exclusion rules: New logo ARR; professional services
Recognition rule: Measured at fiscal year-end against February 1, 2025 ARR base
  of $31.5M
Time horizon: Full fiscal year; measured at close
Source of record: Nexovane Revenue Operations
Currency: USD
Protection level: Protected. Formal review required if NRR falls below 105%.
Revision authority: CEO approval

---

**Commitment C3 — New Enterprise Pipeline**

Metric name: Qualified new enterprise pipeline
Metric definition: Opportunities ≥$150K estimated ACV in Stage 2+ (confirmed
  discovery complete, economic buyer identified) in the enterprise segment
Exclusion rules: Opportunities below $150K ACV; Stage 1 (prospecting only);
  expansion opportunities in existing accounts
Recognition rule: Salesforce stage and ACV as of measurement date
Time horizon: Measured monthly; target is portfolio balance at any point in H2
Source of record: Salesforce CRM
Currency: USD
Protection level: Supporting. Used as a leading indicator for C1.
Revision authority: CRO

---

### A3 — Evidence-Supported Base

**Definition:** Contribution from existing or established motions not attributed
to the incremental strategic bet portfolio, using the Finance/RevOps forecast
and the same metric as C1.

**Evidence-supported base (C1 metric):** $2.1M
Basis: Inbound and self-serve enterprise pipeline from pre-FY2025 activities;
  accounts in late-stage pipeline as of February 1, 2025 not attributed to any
  FY2025 bet; partner referrals from pre-existing agreements not covered by Bet 2
Data source: RevOps pipeline report, January 31, 2025
Finance confirmation: CFO-reviewed, February 1, 2025
Forecast risk: $0.3M of the $2.1M depends on two late-stage deals (Pelantrix
  Advisors and Telvoran Capital) expected to close Q1; if either slips, base
  reduces to $1.5–1.8M
Note: Evidence-supported base carries forecast risk. It is not guaranteed.

---

### A4 — Bet Portfolio

---

#### BET 1 — Basel IV Compliance Suite: Mid-Market Banks

**A4.1 — Hypothesis** `[init]`

Regional and mid-market banks (assets $2B–$50B) face a hard October 31, 2025
deadline to demonstrate Basel IV capital adequacy compliance. The majority of
these institutions are currently using manual spreadsheet processes or legacy
risk platforms that cannot generate the required reports. Nexovane's Basel IV
module — shipping GA June 15, 2025 — addresses all eight required regulatory
reporting areas. Luvexis does not have a competing Basel IV module.

The mandatory spend window created by this regulatory deadline, combined with
Nexovane's first-mover position, will yield 20–25% win rate in the addressable
~120-account mid-market bank segment, generating $5.2M New Enterprise ARR
(22 accounts at average ACV of $236K).

**Primary commitment effect:** C1 ($5.2M New Enterprise ARR)
**Secondary commitment effects:** C3 (pipeline positive), C2 (neutral to positive
  if accounts renew after regulatory deadline passes)

**A4.0 — Commitment Mapping and Guardrails** `[pvt]`

| Commitment | Effect | Expected contribution | Notes |
|------------|--------|----------------------|-------|
| C1 — Primary | Positive | $5.2M New Enterprise ARR | |
| C2 — Secondary | Neutral/Positive | Renewal likely post-compliance | Depends on customer success post-close |
| C3 — Supporting | Positive | ~$20M pipeline during peak | Pipeline builds in build window |

**Guardrail metrics:**

| Guardrail | Metric | Threshold | Evidence source | Consequence if breached |
|-----------|--------|-----------|-----------------|------------------------|
| CAC ceiling | CAC per new logo | ≤$42,000 | Finance / CRM | Bet must pause pending CFO review |
| Gross margin floor | Deal-level gross margin | ≥62% | Deal desk | Requires CFO approval before signing |
| Discount ceiling | Maximum discount rate | ≤18% | Deal desk | VP Sales approval required above 18% |
| Delivery capacity | Onboards per quarter | ≤8 enterprise onboards/quarter | Services capacity | Requires services capacity review before additional commits |
| Concentration ceiling | Single vertical as % of C1 | ≤50% of C1 from banking vertical | Finance | CFO review required |

**A4.2 — Assumptions** `[asm]`

> **A1 — Basel IV deadline creates mandatory spend before October 31, 2025**
> Assumption: EU Banking Authority and US OCC will hold the October 31, 2025
>   Basel IV implementation deadline, creating a non-discretionary buying window
>   for mid-market banks in Q2–Q3 FY2025 (June–October)
> Indicator: Regulatory confirmation of deadline; bank procurement signals
> Normal variance: Minor deadline clarifications or guidance updates
> Warning threshold: Deadline extended by more than 60 days, OR fewer than 40%
>   of target accounts begin procurement conversations by August 31
> Invalidation threshold: Deadline suspended indefinitely, OR global regulatory
>   consensus shifts away from October enforcement
> Restoration evidence: Deadline reinstated with sufficient lead time to capture
>   Q4 FY2025 close
> Owner-stated confidence at planning: High
> *(Owner-stated confidence is not treated as evidence by the Loop.)*

> **A2 — Luvexis has no competing Basel IV module at time of Nexovane GA**
> Assumption: Luvexis will not release Basel IV coverage before Nexovane's
>   June 15 GA date, giving Nexovane a competitive first-mover window
> Indicator: Luvexis product releases, conference announcements, customer intel
> Normal variance: Luvexis marketing activity without product substance
> Warning threshold: Luvexis announces a limited or partial Basel IV release
> Invalidation threshold: Luvexis releases a full 8-area Basel IV module GA
>   and wins 3+ competitive evaluations in the target segment
> Restoration evidence: Luvexis module shown to have material coverage gaps
>   in head-to-head evaluations
> Owner-stated confidence at planning: High

> **A3 — Mid-market bank procurement cycles run 60–90 days**
> Assumption: The procurement cycle from first meeting to signed contract at
>   target accounts will average 60–90 days, allowing deals sourced in June–July
>   to close before the October 31 deadline
> Indicator: Deal velocity in active pipeline; days from Stage 2 to signed
> Normal variance: Individual deal variance of ±15 days
> Warning threshold: Median cycle exceeds 90 days across 5+ active deals
> Invalidation threshold: Median cycle exceeds 120 days, making October 31
>   close infeasible for deals sourced after August 1
> Restoration evidence: N/A — if cycles consistently exceed 120 days, this
>   structural fact cannot be reversed for current-year deals
> Owner-stated confidence at planning: High

> **A4 — Nexovane Basel IV module ships GA June 15, 2025**
> Assumption: The NexovaneOS Basel IV module will be generally available by
>   June 15, 2025, enabling pre-peak pipeline build and demo capability in
>   the May–July build window
> Indicator: Engineering delivery milestone; QA sign-off; GA announcement
> Normal variance: Up to 2 weeks variation in ship date
> Warning threshold: GA date slips beyond July 1
> Invalidation threshold: GA date slips beyond July 15 (compresses pre-peak
>   readiness window to zero)
> Restoration evidence: N/A — a slipped GA date cannot be unslipped
> Owner-stated confidence at planning: High

**A4.3 — Seasonal Calendar** `[init]`

| Window | Dates | Activities required |
|--------|-------|---------------------|
| Pre-season | Feb 1 – Apr 30 | Module development, sales enablement, prospect list build |
| Build | May 1 – Jul 15 | Pipeline generation, demo campaigns, RFP responses |
| Pre-peak | Jul 16 – Jul 31 | All demos complete, proposals submitted, procurement started |
| Peak | Aug 1 – Oct 15 | Contract negotiations, close activity |
| Post-peak | Oct 16 – Oct 31 | Final close push; deadline-driven urgency |
| Off-season | Nov 1 – Jan 31 | Carry-forward; next-year positioning |

**Implementation lead time:** 5 days (contract execution to kickoff)
**Field/partner ramp:** 0 (existing field team)
**Pipeline/demand build:** 30 days (outreach to first qualified meeting)
**Sales/qualification cycle:** 75 days (median, per A3 assumption)
**Procurement/realization:** 10 days (legal review and signature)
**Recognition lag:** 0 (recognized at signature)
**Total timing chain:** 120 days from decision to close

---

#### BET 2 — Korval Advisory Partners Channel

**A4.1 — Hypothesis** `[init]`

Korval Advisory Partners is a financial advisory consultancy with 40+ mid-market
financial advisory clients (including Alderix Capital). These firms are
NexovaneOS prospects — they face compliance requirements similar to larger
enterprise accounts but operate at $80–150K ACV. Nexovane's direct enterprise
field cannot serve this segment cost-effectively at current headcount.

A co-sell and referral arrangement with Korval will generate qualified,
pre-validated opportunities with a compressed 30–45 day sales cycle (Korval's
existing trust relationship eliminates early-stage discovery friction). The
channel will produce $1.8M New Enterprise ARR in FY2025.

**Primary commitment effect:** C1 ($1.8M New Enterprise ARR)
**Secondary commitment effects:** C3 (positive pipeline), C2 (neutral)

**A4.0 — Commitment Mapping and Guardrails** `[pvt]`

| Commitment | Effect | Expected contribution | Notes |
|------------|--------|----------------------|-------|
| C1 — Primary | Positive | $1.8M New Enterprise ARR | Lower ACV than Bet 1; higher volume |
| C2 — Secondary | Neutral | Minimal effect | Small accounts; NRR measured at portfolio level |
| C3 — Supporting | Positive | ~$7M pipeline | Korval referrals qualify quickly |

**Guardrail metrics:**

| Guardrail | Metric | Threshold | Evidence source | Consequence if breached |
|-----------|--------|-----------|-----------------|------------------------|
| Gross margin floor | Deal-level gross margin | ≥58% (lower than direct due to partner fee) | Deal desk | Requires VP Finance approval |
| Delivery capacity | Onboards per quarter | ≤8 enterprise onboards/quarter (shared with Bet 1) | Services capacity | Must coordinate with Bet 1 delivery pipeline |
| Partner fee ceiling | Korval referral fee | ≤12% of ACV | Finance | CFO approval required above 12% |

**A4.2 — Assumptions** `[asm]`

> **B1 — Korval has genuine influence over software decisions at client firms**
> Assumption: Korval's advisory relationship with its clients extends to
>   technology stack decisions; its referral carries decision-maker weight,
>   not just brand familiarity
> Indicator: Win/close rate on Korval-referred opportunities vs. cold outbound;
>   economic buyer engagement rate in Korval-sourced deals
> Normal variance: Standard variation in individual deal outcomes
> Warning threshold: Win rate on Korval-referred deals falls below 25% after
>   10+ opportunities; economic buyer not engaged in 40%+ of referrals
> Invalidation threshold: Win rate below 15% after 15+ opportunities
> Restoration evidence: Win rate recovers to 30%+ over subsequent quarter with
>   consistent economic buyer engagement
> Owner-stated confidence at planning: Medium (Korval relationship is new;
>   Alderix Capital is the only prior collaboration)

> **B2 — Nexovane deal desk can support partner-sourced deals at $80–150K ACV
>   with acceptable margin**
> Assumption: The economics of smaller Korval-sourced deals (lower ACV, partner
>   fee deducted) still produce acceptable gross margin after partner fee
> Indicator: Gross margin on Korval-sourced deals vs. floor; deal desk capacity
> Normal variance: Deal-level variation in implementation complexity
> Warning threshold: Two or more Korval deals close below gross margin floor
> Invalidation threshold: Structural margin analysis confirms Korval-segment
>   economics are below floor at the required partner fee
> Restoration evidence: Partner fee renegotiated to restore margin, OR deal
>   desk finds efficiency gains to offset
> Owner-stated confidence at planning: High

> **B3 — Korval client firms can authorize purchase without extended procurement**
> Assumption: Advisory firms in the $500M–$5B AUM range can make software
>   decisions at the Managing Partner or COO level without multi-quarter procurement
> Indicator: Days from Korval referral to signed contract; procurement escalations
> Normal variance: ±10 days variance per deal
> Warning threshold: Average cycle exceeds 50 days across 5+ Korval deals
> Invalidation threshold: Average cycle exceeds 75 days; procurement escalations
>   required in majority of deals
> Restoration evidence: Cycle compresses below 45 days over subsequent quarter
> Owner-stated confidence at planning: High (Alderix confirmed this pattern)

**A4.3 — Seasonal Calendar** `[init]`

| Window | Dates | Activities required |
|--------|-------|---------------------|
| Ramp | Feb 1 – May 31 | Partner agreement, co-sell training, first referrals |
| Active | Jun 1 – Jan 31 | Referral pipeline active year-round |
| Off-season | None | Channel is active throughout FY2025 |

**Implementation lead time:** 3 days
**Field/partner ramp:** 0 (Korval manages the relationship; deals arrive pre-qualified)
**Pipeline/demand build:** 0 (Korval-sourced; Korval does the generation)
**Sales/qualification cycle:** 35 days (median; compressed by Korval relationship)
**Procurement/realization:** 5 days
**Recognition lag:** 0
**Total timing chain:** 43 days from Korval referral to close

---

#### BET 3 — NRR Module Expansion: Tier 1 Accounts

**A4.1 — Hypothesis** `[init]`

Nexovane's 22 Tier 1 accounts (≥$500K ACV) currently have an average of 2.1 of
6 available NexovaneOS modules deployed. A dedicated CSM-led expansion motion —
with two additional CSM hires in H1, targeted 90-day pilots, and executive sponsor
engagement — will drive adoption of 1–2 additional modules per account in FY2025,
generating NRR of ≥108% against the $31.5M starting ARR base.

**Primary commitment effect:** C2 (NRR ≥108%)
**Secondary commitment effects:** C1 ($0.4M positive — subsidiary upsells that
  qualify as new enterprise logos at related entities)

**A4.0 — Commitment Mapping and Guardrails** `[pvt]`

| Commitment | Effect | Expected contribution | Notes |
|------------|--------|----------------------|-------|
| C2 — Primary | Positive | ≥108% NRR | Core purpose of this bet |
| C1 — Secondary | Small positive | $0.4M from subsidiary upsells | New logos at subsidiary entities |
| C3 — Supporting | Neutral | No effect on enterprise pipeline | Expansion motion is account-specific |

**Guardrail metrics:**

| Guardrail | Metric | Threshold | Evidence source | Consequence if breached |
|-----------|--------|-----------|-----------------|------------------------|
| Churn floor | Gross retention across all accounts | ≥97% | CS platform | Immediate escalation to CRO + CCO |
| Delivery capacity | Concurrent expansion onboards | ≤4 per quarter (shared pool with Bets 1 & 2) | Services capacity | New expansion commits paused pending review |
| Pilot conversion rate | 90-day pilot to full contract | ≥60% | CS platform | Pilot program reviewed for redesign |

**A4.2 — Assumptions** `[asm]`

> **C1 — Existing champions have budget and authority to expand module footprint**
> Assumption: Tier 1 account champions (typically VP-level or above in compliance,
>   risk, or finance functions) have or can obtain budget authority for module
>   expansion without a new procurement cycle
> Indicator: Budget confirmation rate in discovery; time from pilot proposal to
>   pilot start
> Normal variance: Standard variation in budget timing
> Warning threshold: Budget confirmation takes more than 45 days in 30%+ of accounts
> Invalidation threshold: Budget confirmation takes more than 60 days in majority
>   of accounts; procurement escalation required in 40%+
> Restoration evidence: Budget processes simplify (e.g., finance policy change)
> Owner-stated confidence at planning: High

> **C2 — Module value is demonstrable within 90-day pilot**
> Assumption: NexovaneOS modules deliver measurable compliance improvement within
>   90 days that the champion can present to internal stakeholders to justify
>   full deployment
> Indicator: 90-day pilot completion rate; champion satisfaction score; pilot-to-
>   contract conversion rate
> Normal variance: Individual account variation
> Warning threshold: Pilot-to-contract conversion below 55% over rolling quarter
> Invalidation threshold: Pilot-to-contract conversion below 40% over two
>   consecutive quarters
> Restoration evidence: Conversion rate recovers to 60%+ following product or
>   CS process improvement
> Owner-stated confidence at planning: High

> **C3 — Implementation team can support up to 4 concurrent expansion onboards
>   per quarter**
> Assumption: The CS/implementation team, after two new hires (Months 4 and 5),
>   will have capacity to onboard up to 4 new expansion projects per quarter
>   without degrading existing account quality
> Indicator: Onboards per quarter; CSM utilization; customer health scores during
>   active onboards
> Normal variance: ±0.5 onboards per quarter
> Warning threshold: Capacity utilization reaches 90% (3.6+ onboards/quarter)
>   while new expansion demand exceeds 4 per quarter
> Invalidation threshold: CS team cannot complete 4 onboards/quarter without
>   measurable degradation in existing account health scores
> Restoration evidence: Additional CS hire or onboarding process efficiency
>   restores capacity to 4+ per quarter
> Owner-stated confidence at planning: Medium (CSM hires planned but not yet made)

**A4.3 — Seasonal Calendar** `[init]`

| Window | Dates | Activities required |
|--------|-------|---------------------|
| H1 Ramp | Feb 1 – Jul 31 | CSM hires, pilot designs, first expansion proposals |
| H2 Expansion | Aug 1 – Jan 31 | Active pilots, conversion to full contracts |
| Year-end | Nov 1 – Jan 31 | Final pilot conversions; NRR measured at Jan 31 |

**Implementation lead time:** 0 (expansion starts immediately after sign)
**Field/partner ramp:** 60 days (new CSM hires to full productivity)
**Pipeline/demand build:** 30 days (discovery to pilot proposal)
**Adoption cycle:** 90 days (pilot period)
**Realization:** 0
**Recognition lag:** 0 (measured at Jan 31)
**Total timing chain:** 180 days from new hire to full NRR impact

---

### A6 — Dependencies

| Dep # | Description | Owner | Committed date | Type |
|-------|-------------|-------|---------------|------|
| D1 | NexovaneOS Basel IV module GA | Engineering / CPO | June 15, 2025 | Internal product |
| D2 | Deal desk capacity for partner-sourced deals | VP Finance | Feb 1, 2025 | Internal ops |
| D3 | CSM hires (2 FTEs) for Bet 3 expansion motion | VP People | Month 4 and 5 (May/Jun) | Headcount |
| D4 | Korval Advisory Partners co-sell agreement signed | VP Partnerships | March 31, 2025 | External partner |

---

### A7 — Contribution Bridge (Planning-Time Forecast)

*Forecast bridge as of February 1, 2025. This is not a guarantee.*

| Component | Amount | Notes |
|-----------|--------|-------|
| Evidence-supported base | $2.1M | Pre-FY2025 pipeline; Finance-confirmed |
| Bet 1 — Basel IV Mid-Market | $5.2M | 22 accounts × $236K avg ACV |
| Bet 2 — Korval Channel | $1.8M | 18 accounts × $100K avg ACV |
| Bet 3 — Subsidiary upsells (C1 effect) | $0.4M | New logos at related entities |
| Overlap deduction | ($0.3M) | Estimated account overlap between Bet 1 outreach and base pipeline |
| Dependency-risk adjustment | ($0.2M) | D1 slip risk applied to Bet 1 at 10% probability |
| **Forecast total (C1)** | **$9.0M** | vs. $12.0M target; gap = $3.0M |

*Note: $3.0M planning gap was acknowledged at planning as a stretch assumption
requiring upside from Bet 1 outperformance. Version Ledger R01 records this gap.*

**NRR bridge (C2):**
| Component | NRR impact |
|-----------|-----------|
| Baseline NRR (no action) | ~103% (extrapolated from FY2024) |
| Bet 3 module expansion (22 Tier 1 accounts, 1.5 modules avg) | +5pp |
| Expected NRR at plan | 108% |

---

### A9 — Version Ledger

| Rev ID | Date | Item | Original value | Revised value | Change type | Evidence | Owner | Bridge impact |
|--------|------|------|---------------|---------------|-------------|----------|-------|---------------|
| R01 | Feb 1, 2025 | Planning gap acknowledgment | N/A — first entry | $3.0M gap to C1 target documented | N/A — initial record | Finance bridge model | CFO | Documented as known stretch |

---

## MODULE B — Recurring Update

*Provided on this run. August 2, 2025 — Month 7 Operating Review.*

---

### B1 — Review Context

**Review type:** Monthly operating review
**Review date:** August 2, 2025
**Fiscal period:** Month 7 of 12; Q3 opens August 1
**Reviewer:** CRO-led revenue leadership team
**Organizational events this period:**
- Luvexis announced limited Basel IV module availability at FinCompliance Summit,
  July 15, 2025 (partial coverage: 3 of 8 required regulatory reporting areas)
- EU Banking Authority confirmed October 31, 2025 Basel IV deadline, July 1, 2025
- US OCC guidance expected September 2025; current OCC position supports Oct 31
- D3 CSM hires completed: Month 5 (June) and Month 6 (July). Both in role.
- D4 Korval co-sell agreement signed March 28, 2025 (on schedule)

**No operating mode declared by this input. The Loop infers mode from evidence.**

---

### B2 — Actuals and Indicators

#### B2.1 — Commitment Actuals (Month 7 YTD)

| Commitment | Target | YTD actual | Expected YTD per plan | Variance |
|------------|--------|------------|----------------------|----------|
| C1 New Enterprise ARR | $12.0M (FY) | $5.48M | $5.25M | +$0.23M (+4%) |
| C2 NRR (annualized) | ≥108% (year-end) | 106.2% (annualized) | 107.0% expected | −0.8pp |
| C3 Pipeline | ≥$48M | $38.2M | $42.0M expected | −$3.8M (−9%) |

*C1 note: $5.48M YTD includes $4.1M base + Bet 1 ($0.9M) + Bet 2 ($0.34M) +
  Bet 3 subsidiary ($0.14M). Aggregate looks near plan but bet-level composition
  is significantly off — Bet 1 is well behind its $2.8M expected YTD contribution.*

---

#### B2.2 — Bet-Level Actuals

**Bet 1 — Basel IV Compliance Suite:**
- Closed YTD: $0.9M (3 accounts; average ACV $300K)
- Expected YTD: $2.8M (per seasonal curve, 12 accounts by Month 7)
- Gap to YTD expected: −$1.9M (−68%)
- Active pipeline: $4.1M in 11 qualified opportunities (Stage 2–4)
- Pipeline by stage: Stage 2 (7 accounts, $2.4M), Stage 3 (3 accounts, $1.2M),
  Stage 4 (1 account, $0.5M)
- Average cycle length observed: 94 days (vs. 75-day plan; 3 closed deals)
- Demos delivered: 18 (target was 22 by July 31)
- Basel IV module status: GA shipped July 28, 2025 (was June 15 plan; 6-week slip)
- Competitive losses YTD: 2 accounts lost to Luvexis (Vestrix Securities, Korvel
  Investments); 1 no-decision (Pelanthor Trust)

**Bet 2 — Korval Advisory Partners Channel:**
- Closed YTD: $0.34M (1 account: Alderix Capital, $340K ACV, Month 6)
- Expected YTD: $0.525M (per seasonal curve)
- Gap to YTD expected: −$0.185M (−35%); but deal quality is high
- Active pipeline: $0.89M in 3 active Korval-referred opportunities
- Additional Korval referrals in qualification: 6 new firms expressing interest
  (Korval channel survey, June 30; estimated ACV $80–150K each)
- Average cycle length observed: 32 days (Alderix closed in 32 days; below 35-day plan)
- Win rate: 1/1 on qualified Korval deals (100%; small sample)
- Gross margin on Alderix deal: 64% (above 58% floor)
- Note: Implementation team is onboarding Alderix Capital concurrently with 2
  other accounts. Utilization is at 3.5 concurrent onboards/quarter.

**Bet 3 — NRR Module Expansion:**
- NRR annualized: 106.2% (vs. 107.0% expected at Month 7)
- Expansions closed H1: 3 (2 Fraud Detection module, 1 Audit Trail module)
- Active pilots in H2: 4 accounts (in 90-day pilot periods)
- Pilot-to-contract conversion rate: 3/4 = 75% (above 60% floor)
- CSM utilization: 3.5 concurrent onboards/quarter (at Warning threshold)
- Champion satisfaction scores: 8.4/10 average across active pilots
- C1 subsidiary upsells: $0.14M (1 account: Kessval Financial subsidiary)

---

#### B2.3 — Assumption Indicator Readings

**Bet 1 assumptions:**

> **A1 (Basel IV deadline):**
> Structural indicator: EU Banking Authority press release, July 1, 2025 — deadline
>   confirmed at October 31, 2025. US OCC expected to align September 2025.
> Reading vs. thresholds: Normal variance (no extension signaled)
> Current structural status: Held

> **A2 (Luvexis competitive position):**
> Structural indicator: Luvexis FinCompliance Summit announcement, July 15, 2025.
>   Luvexis confirmed Basel IV module with coverage of 3 of 8 required regulatory
>   areas (Pillar 1 capital requirements, credit risk, market risk only). Areas
>   not covered: liquidity reporting, operational risk, reporting disclosure,
>   remuneration, and supervisory review.
> Additional indicator: 2 competitive losses to Luvexis in Bet 1 pipeline
>   (Vestrix Securities, Korvel Investments). Loss reasons from exit interviews:
>   Luvexis offered a 25% price discount and existing relationship; buyers
>   accepted partial coverage as "good enough for now."
> Reading vs. thresholds: Warning threshold crossed (Luvexis has released limited
>   module; partial coverage is real)
> Current structural status: Warning

> **A3 (Procurement cycle length):**
> Structural indicator: 3 closed deals averaged 94-day cycle. 11 active pipeline
>   deals: median estimated cycle based on progression = 88 days.
> Reading vs. thresholds: Warning threshold crossed (median exceeds 90 days in
>   active deals; 94-day actuals in closed deals)
> Current structural status: Warning

> **A4 (Module GA date):**
> Structural indicator: Module shipped July 28, 2025 (44 days after June 15 plan)
> Reading vs. thresholds: Invalidation threshold crossed (shipped after July 15)
> Current structural status: Invalidated (but now resolved — module is available)
> Current-horizon status: Invalidated (current year) — the pre-peak build window
>   required GA by June 15 to complete demo campaigns before August 1 peak.
>   Module arrived after peak started.

**Bet 2 assumptions:**

> **B1 (Korval influence):**
> Indicator: Alderix Capital close (32 days; economic buyer engaged Day 4). Win rate 1/1.
> Reading vs. thresholds: Normal variance (small sample; within expected range)
> Current structural status: Held

> **B2 (Deal desk margin):**
> Indicator: Alderix gross margin 64% (above 58% floor)
> Reading vs. thresholds: Normal variance
> Current structural status: Held

> **B3 (Procurement speed):**
> Indicator: Alderix closed in 32 days (below 35-day expected)
> Reading vs. thresholds: Normal variance (favorable)
> Current structural status: Held

**Bet 3 assumptions:**

> **C1 (Champion budget authority):**
> Indicator: Budget confirmation rate in active pilots: 4/4 confirmed within 30 days
> Reading vs. thresholds: Normal variance
> Current structural status: Held

> **C2 (90-day pilot value):**
> Indicator: Pilot-to-contract conversion: 3/4 = 75% (above 60% floor)
> Reading vs. thresholds: Normal variance
> Current structural status: Held

> **C3 (Implementation capacity):**
> Indicator: CS team at 3.5 concurrent onboards/quarter. Warning threshold is 3.6.
>   Current demand: Bet 3 needs 4/quarter in H2 to hit NRR target. If Bet 2
>   accelerates (6 new Korval referrals in qualification), combined demand may
>   reach 5–6 onboards/quarter.
> Reading vs. thresholds: Warning threshold nearly reached (3.5 vs. 3.6 threshold)
> Current structural status: Warning

---

### B3 — External Evidence

> **EX-01 — Luvexis Basel IV module announcement**
> Source: FinCompliance Summit industry press coverage + Luvexis product blog,
>   July 15, 2025; Tier 2 (public announcement, no independent verification)
> Segment: Mid-market compliance platform buyers
> Geography: US and EU
> Nature: Fact (confirmed product announcement)
> Reliability: High (corroborated by two competitive loss exit interviews)
> Materiality: High — directly affects A2 (Luvexis competitive position). Luvexis
>   has partial Basel IV coverage. Pricing-led displacement is occurring.
> Assumptions affected: A2 (Bet 1)
> Expected duration: Structural — Luvexis module exists and will be developed further
> Contradictory evidence: None
> Last refresh: July 15, 2025

> **EX-02 — EU Banking Authority Basel IV deadline confirmation**
> Source: EBA press release, July 1, 2025; Tier 1 (official regulatory communication)
> Segment: All EU-regulated banks and their US affiliates
> Geography: EU primary; US (OCC alignment expected)
> Nature: Fact
> Reliability: Very high (official source)
> Materiality: High positive — confirms A1 deadline is intact. Buying window is real.
> Assumptions affected: A1 (Bet 1)
> Expected duration: Fixed deadline; not subject to further extension per EBA statement
> Contradictory evidence: None
> Last refresh: July 1, 2025

> **EX-03 — Korval partner channel survey**
> Source: Korval Advisory Partners pipeline update, June 30, 2025; Tier 2
>   (partner-provided, unverified by Nexovane)
> Segment: Mid-market financial advisory firms, $500M–$5B AUM
> Geography: US domestic
> Nature: Forecast (Korval's assessment of client interest; not confirmed buyer intent)
> Reliability: Medium (partner has incentive to project optimistic pipeline)
> Materiality: Medium — 6 additional referrals at $80–150K ACV = potential
>   $480K–$900K additional C1 if qualified and closed
> Assumptions affected: B1 (Korval influence), B3 (procurement speed)
> Expected duration: Current opportunity window; not a structural market shift
> Contradictory evidence: None; however, expressed interest ≠ qualified opportunity
> Last refresh: June 30, 2025

---

### B4 — Intervention Status

No formal interventions have been deployed with a defined baseline and observation
window as of August 2, 2025.

**Informal activity noted (not a formal intervention):**
Bet 1 field team initiated incremental outreach to Basel IV contacts in June 2025
following the module delay. No baseline was set, no expected signal was defined,
and no observation window was established. This activity cannot be formally
evaluated. If a structured intervention is deployed, it must be initialized with
a baseline, intended mechanism, expected leading signal, signal date, observation
window, and comparison method.

---

*End of input. Modules C and D not supplied — Loop to determine if Adaptation
annex is required.*
