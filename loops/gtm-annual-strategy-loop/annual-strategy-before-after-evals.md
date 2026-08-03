# Annual GTM Strategy and Goal Governance Loop — Before and After Evals

This document evaluates the Loop against five scenarios representative of the
full operating range: Planning mode quality review, Warning without Adaptation,
Adaptation with cross-commitment conflict, Intervention evaluation, and a
synthetic future update showing the next review cycle.

Each eval shows what a generic LLM response produces without the Loop prompt,
followed by what this Loop produces. The gap between the two is the value the
Loop architecture delivers.

---

## Eval 1 — Planning Mode: Pressure-Testing an Annual Portfolio

**Scenario:** It is February 1, 2025. The Nexovane leadership team has submitted
its FY2025 plan for Loop review. The plan shows $12.0M New Enterprise ARR target
with three bets. The user asks: "Does this plan hold together?"

---

### BEFORE (Generic LLM, no Loop prompt)

> Great plan structure. A few observations:
>
> - The $12.0M target looks ambitious but achievable given your three bets totaling
>   $7.4M plus a $2.1M base. You're ~$2.5M short on paper, which typically gets
>   closed through upside performance or deals you haven't yet modeled.
>
> - Bet 1 (Basel IV) has strong timing logic — regulatory deadlines create urgency.
>   Make sure your team is ready with demo materials before the peak window.
>
> - Bet 2 (Korval channel) looks promising. One closed deal would validate the model.
>   Watch the partner margin carefully.
>
> - Bet 3 (NRR expansion) is a solid retention play. CSM capacity is your biggest
>   risk here — make sure the hires go well.
>
> Overall the plan is reasonable. Execution will be the key variable.

**What's wrong:** No gap to C1 is flagged ($9.0M forecast vs. $12.0M target). The
$3.0M planning gap is called "upside from deals not yet modeled" — that is not a
plan, it is a hope. Module GA dependency risk for Bet 1 is noted as "make sure your
team is ready" rather than identified as a load-bearing assumption with a defined
invalidation threshold. Procurement cycle length assumption is never challenged.
Luvexis competitive assumption is never probed. No contribution bridge is evaluated.
No seasonal calendar is verified. The output produces false confidence.

---

### AFTER (This Loop)

**Observed portfolio mode: Planning**

**Portfolio formation assessment:** The portfolio as submitted has a documented
$3.0M gap between the risk-adjusted portfolio forecast ($9.0M) and the $12.0M
non-negotiable target. The $9.0M reflects base contributions from each bet after
evidence-based deductions for assumption uncertainty, seasonal timing risk, and
dependency constraints — not merely the sum of nominal bet targets. This gap
requires explicit acknowledgment and either a plan to close it through one of
the three bets or a formal target revision before initialization.
Characterizing it as "upside from outperformance" is not a planning assumption —
it is a planning gap.

**Assumption quality review:**

> *A4 — Module GA date (Bet 1):* This is a load-bearing dependency. The seasonal
> calendar requires GA by June 15 to enable a six-week demo campaign before the
> August 1 peak. If GA slips past July 15 — the Invalidation threshold — the build
> window closes entirely and Bet 1 contribution falls from $5.2M to an estimated
> $1.5–2.5M (existing pipeline only, no new account generation). This assumption
> carries High owner confidence but no engineering delivery evidence. The Loop
> assigns Insufficient evidence. Evidence required before Planning mode closes:
> Engineering committed delivery date, QA plan, and at least one prior GA delivery
> track record for a module of comparable complexity.

> *A3 — Procurement cycle 60–90 days (Bet 1):* The plan assumes 75-day cycles.
> No historical evidence of procurement velocity at regional banks in this ACV range
> is provided. If cycles run 90–110 days — a common outcome for regulated financial
> institutions making new vendor commitments — deals sourced after August 1 cannot
> close by October 31. This is a single-point failure in the seasonal logic. Evidence
> required: Historical deal velocity from prior banking segment deals, or CRM data
> from similar accounts. Owner-stated High confidence; Evidence-assessed: Insufficient
> evidence.

> *A2 — Luvexis competitive position (Bet 1):* Plan assumes no Luvexis Basel IV
> module. This is a time-bounded assumption — if Luvexis releases partial coverage
> before October 31, buyers may accept partial compliance and choose the incumbent.
> A monitoring signal and Warning threshold must be defined. As submitted, there is
> no tripwire. Evidence required: Competitive intelligence update on Luvexis product
> roadmap; define Warning threshold (Luvexis announces partial release) and response.

> *C3 — Implementation capacity (Bet 3):* Plan assumes 4 concurrent onboards/quarter
> after two CSM hires in Months 4 and 5. At planning time, the hires have not been
> made. The capacity assumption has no supporting evidence. If hires are delayed or
> take longer than expected to ramp, Bet 3 NRR contribution is directly constrained.
> Owner-stated Medium; Evidence-assessed: Insufficient evidence. Confirmation
> required: Candidates identified, offer timeline committed, ramp time estimated.

**Contribution bridge gap:**

The risk-adjusted portfolio forecast produces $9.0M against the $12.0M target.
The $3.0M gap must be documented in the Version Ledger as R01 (initial planning
gap acknowledgment). This is not a revision — it is the starting state.
Leadership must either:
a) Accept $9.0M as the evidence-supported planning ceiling and revise C1 accordingly, OR
b) Identify a specific fourth source of contribution (unmodeled upside from an
   evidence-supported source), OR
c) Accept $12.0M as a stretch commitment with a documented probability below 50%

**Planning mode does not close until:** A4 dependency evidence is provided, A3
cycle evidence is provided, C3 capacity evidence is provided, and the $3.0M gap
is formally dispositioned in the Version Ledger.

---

**What changed:** The Loop surfaces the $3.0M gap, challenges three load-bearing
assumptions with Insufficient evidence, identifies A4 as a single-point failure in
the seasonal logic, and defines conditions Planning mode must satisfy before
transitioning to Monitoring. The generic response validated false confidence in a
plan with structural gaps.

---

## Eval 2 — Warning Without Adaptation

**Scenario:** Month 4 (June 1). The Nexovane field team reports that Luvexis has
started doing demos in 4 of Nexovane's active Bet 1 accounts and is "offering
aggressive pricing." The user reports this as an assumption update.

---

### BEFORE (Generic LLM, no Loop prompt)

> This is a meaningful competitive signal. I'd recommend:
>
> 1. Immediately update your competitive battlecard.
> 2. Brief the field team on Nexovane's differentiation against Luvexis.
> 3. Consider whether you need to adjust your pricing to compete.
> 4. Flag this to leadership as a risk — you may want to review your Bet 1 target.
>
> This kind of competitive pressure is normal in a growth market. Stay focused on
> your differentiation and don't panic-react.

**What's wrong:** No assessment of whether A2's Warning threshold has been crossed.
No inference about what this means for the seasonal window. No named decision
deadline. No defined escalation trigger. "Consider adjusting pricing" is a
recommendation without a guardrail check (discount ceiling is 18%). "Review your
Bet 1 target" is vague — no distinction between a tactical tune and a formal target
revision. The response is generic advice, not a loop-governed assessment.

---

### AFTER (This Loop)

**Observed bet mode: Monitoring (not Adaptation)**

**A2 assessment — Luvexis competitive position:**

Current evidence: Luvexis is running demos in 4 of 11 active Bet 1 accounts.
Pricing reports are "aggressive" but unquantified. No confirmed Luvexis product
release has been announced.

A2 Warning threshold: *Luvexis announces a limited or partial Basel IV release.*
Current evidence does not cross this threshold — demos without a product announcement
indicate Luvexis may be demoing a roadmap or limited prototype, not a released module.
**A2 structural status: Held (Warning threshold not crossed)**

However, Luvexis competitive presence in 4 of 11 active accounts is a material
new signal that warrants elevated monitoring and a named decision deadline.

**Actions triggered (not Adaptation):**
- A2 monitoring frequency: increase to weekly. Specific evidence to collect: Luvexis
  demo content or materials from accounts where Nexovane has a champion; Luvexis
  pricing proposals; whether Luvexis is claiming Basel IV capability or demonstrating it.
- Field guidance: Do not adjust pricing without VP Sales approval. Discount ceiling
  is 18%; any competitive concession above this threshold requires escalation. This
  is a guardrail check, not a competitive panic.
- Named decision deadline: If by **June 20** (3 weeks) Nexovane has not received
  competitive intelligence confirming Luvexis's coverage depth, assume Warning
  threshold is at risk and prepare Adaptation materials.

**A2 is not at Warning yet. The Loop does not trigger Adaptation on competitive
presence alone. Adaptation triggers when Luvexis announces a release or wins deals
in the active pipeline.** The named decision deadline prevents the organization from
waiting indefinitely without acting.

---

**What changed:** The Loop correctly holds Monitoring mode while the Warning
threshold has not been crossed, defines exactly what evidence would cross it, sets a
named deadline, and applies the guardrail check before any pricing response. The
generic response recommended unstructured action — and would have triggered false
Adaptation on noise.

---

## Eval 3 — Adaptation with Cross-Commitment Conflict

**Scenario:** August 2 (Month 7). Bet 2 is outperforming. Six new Korval referrals
are available. The VP of Sales asks: "Should we accelerate Bet 2? Can we push all
six Korval accounts into active sales now?"

---

### BEFORE (Generic LLM, no Loop prompt)

> Yes, definitely pursue the Korval referrals — you have momentum and a proven model.
> I'd recommend:
>
> 1. Qualify all 6 referrals immediately — get first calls scheduled this week.
> 2. Assign a dedicated AE to the Korval channel to maintain relationship quality.
> 3. If deals close as expected, this could add $600K–$900K to your ARR total.
>
> This is a win — capitalize on it. The channel is working.

**What's wrong:** No guardrail check. Implementation capacity conflict is never
identified. The recommendation would trigger a delivery capacity breach that creates
churn risk in Tier 1 accounts — directly threatening C2, which is a protected
commitment. The cross-commitment conflict (Bet 2 acceleration vs. Bet 3 NRR) is
invisible. The response is enthusiastic and dangerous.

---

### AFTER (This Loop)

**Observed bet mode: Adaptation (upside)**

**Replacement-bet feasibility — Bet 2 acceleration:**

Before recommending Reinforce for Bet 2, 10 feasibility questions must be answered:

1. *Incremental addressable demand:* Yes — 6 new referrals from Korval are in
   qualification. Segment has not been saturated.
2. *Available pipeline:* Yes — 6 new referrals not yet attributed to Bet 2.
3. *Additional capacity:* **Partially** — implementation capacity is the constraint.
   Current: 3.5/quarter. Combined demand (Bet 3 H2 + Bet 2 acceleration): 6–7/quarter.
   Guardrail threshold: 4/quarter. **Capacity is not available without expansion.**
4. *Sales-cycle feasibility:* Yes — Korval deals close in 35 days; latest useful
   date is November 19 for January 31 close.
5. *Saturation risk:* Low — Korval has 40+ client firms; 7 total so far.
6. *Cannibalization:* Low — distinct segment from Bet 1 (advisory vs. banking).
7. *Pull-forward risk:* Low — Korval firms have recurring compliance needs; not
   pulling next-year deals.
8. *Shared dependency strain:* **YES — CRITICAL.** Implementation capacity is shared
   across Bets 1, 2, and 3. Adding Bet 2 volume strains the shared pool.
9. *Disruption to working bets:* **YES — HIGH RISK.** Bet 3 NRR expansion requires
   4 onboards/quarter in H2 to close the 1.8pp NRR gap and reach C2 target of 108%.
   Adding Bet 2 acceleration without expanding capacity will block Bet 3 pilots.
   Bet 3 is a protected commitment (C2). This bet is currently working.
10. *Maximum credible incremental contribution:* $600K–$900K if all 6 qualify and
    close; ceiling, not expectation.

**⚠ GUARDRAIL BREACH RISK — Delivery Capacity:**
Pursuing all 6 referrals simultaneously as proposed breaches the delivery capacity
guardrail (≤4 concurrent onboards/quarter) and creates direct risk to C2 (NRR ≥108%).
This is not a tradeoff to accept implicitly — it requires a named decision.

**Recommendation: Reinforce — conditional**
Bet 2 Reinforce proceeds only after one of three conditions is resolved:
a) COO approves services capacity expansion to ≥6 onboards/quarter, OR
b) Leadership explicitly accepts limiting Bet 3 H2 pilots to 3/quarter (accepting
   C2 risk mitigation instead of target attainment), OR
c) Korval referrals are staggered — no more than 2 new onboards/quarter alongside
   Bet 3 pilots

Decision owner: CRO. Approver: COO (owns services capacity).
Deadline: August 15. Korval referrals lapse if not progressed by then.

---

**What changed:** The Loop surfaces the delivery capacity conflict, applies the
10-question feasibility test, identifies the cross-commitment risk to C2 before
recommending acceleration, and converts "yes, go" into a conditional decision with
a named owner and deadline. The generic response would have accelerated into a
protected commitment breach.

---

## Eval 4 — Intervention Evaluation

**Scenario:** September 5 (5 weeks after Intervention 01 was deployed). The
competitive response battlecard was distributed to the field team on August 2.
The user reports: "We ran the competitive response play. We won two more accounts
in the Bet 1 pipeline — Telvax Investment Group ($280K) and Cadrova Financial
($195K). We lost one — Velstrom Asset Management — to Luvexis on price. Win rate
in competitive deals is now 4W/3L (57%)."

---

### BEFORE (Generic LLM, no Loop prompt)

> Good news — two more wins! That's $475K in new ARR.
>
> Losing Velstrom to Luvexis on price is frustrating but probably unavoidable
> if they're willing to heavily discount. Keep running the coverage differentiation
> message — it's clearly working for some accounts. Focus on the 8 remaining
> pipeline accounts and push for close before October 31.

**What's wrong:** No formal evaluation of whether the intervention worked. No
comparison to baseline. No assessment of whether the result is Effective, Partially
effective, or Inconclusive. No confounder analysis. No follow-on decision in the
canonical vocabulary. The $475K wins are accepted as intervention success without
examining whether the mechanism activated as intended. This produces a feeling of
progress without a structured learning.

---

### AFTER (This Loop)

**Intervention 01 Evaluation — Bet 1 Competitive Response**

Deployed: August 2, 2025
Observation window closed: September 5, 2025
Baseline: Win rate in competitive evaluations = 50% (2W/2L)
Expected leading signal: Win rate in competitive evaluations recovers to ≥70%
Expected magnitude: 2–3 accounts retained; $0.3–0.6M protected

**Actuals:**
- Win rate: 4W/3L = 57% (vs. 70% expected signal; vs. 50% baseline)
- Accounts won: Telvax Investment Group ($280K), Cadrova Financial ($195K)
- Accounts lost: Velstrom Asset Management (Luvexis, price-led displacement)
- Total contribution protected/generated: $475K

**Confounder analysis:**
The two wins occurred in accounts where the economic buyer had already been engaged
for 60+ days (Telvax) and where Nexovane had an existing relationship through a
prior services engagement (Cadrova). The Velstrom loss occurred in an account where
Luvexis had a prior relationship with the CFO predating the current deal. These
factors suggest the competitive battlecard contributed to the wins, but relationship
asymmetry was also a factor. It is not clear whether the battlecard alone would have
won Telvax and Cadrova without the prior relationship context.

**Result: Partially effective**

Win rate improved from 50% to 57% — directionally correct but below the 70% signal
threshold. The mechanism (full-coverage differentiation) is resonating in some
accounts but is not consistently overcoming Luvexis's pricing and relationship
advantage. The intervention is partially working; refining the execution elements
that are underperforming is the appropriate next step.

**Follow-on decision: Tune**

What to tune: The pricing-defense element of the competitive response. Velstrom
was lost on price — the coverage argument did not offset the discount Luvexis
offered. The battlecard needs a sharper economic argument: quantifying the cost of
non-compliance in the 5 areas Luvexis does not cover, converted into an ROI
comparison against the pricing delta. This is not a strategic change — it is a
sharpening of the execution element that underperformed.

What to preserve: The coverage differentiation argument (working in 2 of 3
competitive accounts where messaging was deployed). Executive sponsor protocol
(deployed in both wins).

New expected signal: Win rate in remaining competitive deals ≥65% in next 4 weeks
New signal date: October 3, 2025
Updated observation window: 4 weeks (through October 3)
Decision owner: VP Sales
Approver: CRO

**Version Ledger — Intervention 01 result:**
| Rev ID | Date | Item | Original | Revised | Change type | Evidence |
|--------|------|------|----------|---------|-------------|---------|
| R05 | Sep 5, 2025 | Intervention 01 result | Pending | Partially effective | New learning | 4W/3L win rate; Velstrom loss to price |
| R06 | Sep 5, 2025 | A2 competitive status | Warning | Warning (maintained) | New learning | Luvexis still at 3/8 areas; displacement is pricing-led not product-led |

---

**What changed:** The Loop produces a structured result classification (Partially
effective), a confounder analysis that prevents incorrectly attributing the full
result to the intervention, a specific follow-on decision (Tune, not Reinforce or
Revise Bet), and a new observation window with updated signal. The generic response
accepted wins as validation and produced no structured learning.

---

## Eval 5 — Synthetic Future Update: October 3 Review

**Scenario:** October 3 (Month 9). OCC guidance confirmed September 15: US Basel IV
deadline aligned with EU at October 31. Intervention 01 (Tune) has now been in
effect for 4 weeks. Six Korval referrals: 4 qualified as Stage 2+, 2 did not
qualify. COO approved services capacity expansion (2 contractors) on August 20.
Bet 1 pipeline: 5 of original 11 accounts have closed; 3 accounts remain in Stage 4.

**This eval shows how a future update flows through the Loop — not before/after
but a complete synthetic run at Month 9.**

---

### SYNTHETIC LOOP OUTPUT (Abbreviated) — Month 9

**Observed portfolio mode: Adaptation → Monitoring (closing Adaptation cycle)**

Mode rationale: The capacity conflict that triggered Portfolio Adaptation has been
resolved (COO capacity approval August 20). Intervention 01 (Tune) has produced
a follow-on Tune that is now in observation. The remaining Bet 1 accounts are in
final-stage close activity. No new threshold triggers are present. The Loop transitions
back to Monitoring with three named triggers for re-escalation.

---

**Commitment attainability (updated):**

**C1 — New Enterprise ARR:**
YTD actual: $8.12M (Month 9)
Expected remaining from active pipeline: Bet 1 (3 Stage 4 accounts, ~$720K);
  Bet 2 (3 active Korval accounts + 2 contractors onboarding, ~$780K);
  Bet 3 subsidiary (~$0.15M); base (~$0.3M)
Revised full-year forecast: $9.85–10.55M
Attainability: **Structurally at risk** (C1 revision decision by Board still
  pending; $12.0M target not formally revised)
Note: The non-negotiable breach notice issued August 2 remains active. Board
  decision on target revision was deferred to November board meeting.

**C2 — NRR:**
YTD actual: 107.1% annualized (improved from 106.2% in Month 7)
With 2 new pilots launched (September, enabled by contractor capacity):
  Forecast at January 31: 108.2–108.6%
Attainability: **On track** — capacity resolution enabled additional pilots;
  trajectory now above target

**C3 — Pipeline:**
YTD actual: $44.1M
Forecast at year-end: $46–49M depending on Q4 Korval qualification rate
Attainability: **At risk — recoverable**

---

**Intervention 02 result (Tune — competitive pricing ROI argument):**

Deployed: September 5. Observation closed: October 3.
Actuals: Win rate in competitive evaluations in observation period: 3W/1L = 75%.
  The ROI argument (cost of non-compliance in 5 uncovered Luvexis areas)
  was decisive in 2 of 3 wins per post-close buyer debrief.
Result: **Effective**
Follow-on: **Hold** — mechanism is working; no changes to Bet 1 execution approach.
  Focus shifts to closing 3 remaining Stage 4 accounts by October 31.

---

**Version Ledger — Month 9 additions:**

| Rev ID | Date | Item | Original | Revised | Change type | Evidence |
|--------|------|------|----------|---------|-------------|---------|
| R07 | Oct 3, 2025 | Intervention 02 result | Pending | Effective | New learning | 75% win rate; buyer debriefs confirm ROI argument |
| R08 | Oct 3, 2025 | Delivery capacity | 3.5/quarter | 5.5/quarter | External change (contractor approval) | COO approval August 20 |
| R09 | Oct 3, 2025 | A1 US OCC alignment | Pending US guidance | Confirmed — aligned with Oct 31 | New learning | OCC press release September 15 |

---

**What this update demonstrates:** The Loop traces from the Month 7 non-negotiable
breach notice through two intervention cycles to a Month 9 state where C2 has
recovered to On track, C1 remains structurally at risk but at a much tighter range
($9.85–10.55M), and two interventions have been formally evaluated and closed. The
plan did not reach $12.0M but the organization made evidence-based decisions at every
step, preserved what was learned, and has accurate visibility into where it will close.
That is what governance looks like.
