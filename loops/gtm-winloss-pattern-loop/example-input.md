# Win/Loss Pattern Loop — Example Input

**Fictional scenario.** All companies, products, people, deal data, quotes, and outcomes in this file are fictional and created solely to demonstrate the Loop's analytical behavior. Any resemblance to real organizations, products, or individuals is unintentional.

---

## Part 1 — Baseline Context

**Segment scope:** Enterprise financial services (500+ employees), North America

**Time window:** Q1 and Q2 2026 — 6 months, 24 closed deals

**Win/loss ratio baseline:**
* Overall enterprise win rate: 38% (9 won, 15 lost)
* Previous year same segment: 47%
* Win rate decline: 9 percentage points over 12 months

**Primary concern:**
"We're losing more enterprise fintech deals than we were 12 months ago. The team
doesn't know if it's competitive, a product issue, a rep execution issue, or
something in how we're qualifying. We've tried improving demo quality and it hasn't
moved the number."

**Artifact generation authorized:**
* Competitive battle card
* Qualification criteria change
* Product signal / gap report
* Leadership escalation brief

**Escalation contacts:**
* VP of Sales: Diane R.
* Head of Product: Darren W.
* Regional GM (East): Tyler K.

**Observation thresholds:** 15 closed eligible deals or Q4 2026 end, whichever
is later (based on approximately 90-day average enterprise sales cycle).

**Deal velocity:** Approximately 70–120 days, enterprise fintech.

---

## Part 2 — Initial Deal Set — Q1 and Q2 2026

### Won Deals (9)

| Account | Value | Stage at Close | Champion Title | Economic Buyer Engaged | Competitor(s) | Source | Days |
|---|---|---|---|---|---|---|---|
| Telvoran Capital | $480K | Stage 5 | VP Engineering | Yes (CFO) | Luvexis (evaluated, not chosen) | Outbound | 87 |
| Pelantrix Advisors | $310K | Stage 5 | Head of Data | Yes (COO) | None | Partner referral | 64 |
| Aldrivex Trust | $560K | Stage 5 | CTO | Yes (CEO) | Databricks | Customer referral | 102 |
| Drevith Asset Management | $290K | Stage 5 | VP Data Engineering | Yes (CFO) | None | Inbound | 71 |
| Kelvane Wealth | $195K | Stage 4 | Director of Analytics | No | Tableau | Inbound | 58 |
| Orsane Equities | $740K | Stage 5 | Chief Data Officer | Yes (CEO, CFO) | Databricks, dbt | Outbound | 118 |
| Cadrova Financial | $225K | Stage 5 | VP Engineering | Yes (CTO) | None | Customer referral | 79 |
| Vestral Lending | $180K | Stage 4 | Analytics Manager | No | Looker | Inbound | 52 |
| Nexvath Capital Group | $410K | Stage 5 | Head of Platform | Yes (CFO) | Palantir | Partner referral | 94 |

### Lost Deals (15)

| Account | Value | Stage at Loss | Champion Title | Economic Buyer Engaged | Competitor Chosen | CRM Loss Reason | Source | Days |
|---|---|---|---|---|---|---|---|---|
| Corvath Capital | $620K | Stage 4 | IT Director | No | Luvexis | "Competitor offered better price" | Outbound | 91 |
| Velstrom Asset Management | $380K | Stage 3 | IT Director | No | Luvexis | "Competitor better fit" | Outbound | 43 |
| Telvax Investment Group | $510K | Stage 4 | IT Director | No | Databricks | "Product gap — compliance features" | Outbound | 77 |
| Kessval Financial | $290K | Stage 3 | IT Director | No | Luvexis | "No decision — budget freeze" | Inbound | 38 |
| Aldrevox Private Equity | $450K | Stage 4 | IT Director | No | Palantir | "Competitor relationship" | Partner referral | 84 |
| Vestrix Securities | $340K | Stage 2 | IT Manager | No | — | "Not the right fit" | Outbound | 22 |
| Telvane Asset Group | $670K | Stage 4 | IT Director | No | Luvexis | "Competitor better fit" | Outbound | 96 |
| Korvel Investments | $220K | Stage 3 | IT Director | No | None (no decision) | "No decision — priority shifted" | Inbound | 47 |
| Korsavel Fund Management | $480K | Stage 4 | IT Director | No | Databricks | "Product gap — compliance features" | Outbound | 88 |
| Valdrex Capital | $310K | Stage 3 | Data Engineer (IC) | No | — | "Not the right fit" | Outbound | 31 |
| Pelanthor Trust | $540K | Stage 4 | IT Director | No | Luvexis | "Competitor offered better price" | Inbound | 73 |
| Drevax Advisors | $185K | Stage 3 | IT Manager | No | — | "No decision — no budget" | Inbound | 29 |
| Nexvore Capital | $420K | Stage 4 | IT Director | No | Palantir | "Competitor relationship" | Partner referral | 81 |
| Velkorath Asset Management | $290K | Stage 3 | IT Director | No | Luvexis | "Competitor better fit" | Outbound | 44 |
| Orvana Wealth | $360K | Stage 4 | IT Director | No | Databricks | "Product gap — compliance features" | Outbound | 69 |

---

## Part 3 — Exit Interview Data (4 interviews conducted, Q1–Q2 2026)

**Corvath Capital** (Lost to Luvexis)
Conducted by: post-sale CS team

"Honestly, Luvexis was already in our environment for another use case. IT was
going to have to evaluate a brand new vendor versus expanding a relationship we
already trusted. We never really got to a rigorous evaluation of your product — the
decision was made before the evaluation really started. Your product might have been
fine. We just couldn't justify adding another vendor."

Interviewer note: Buyer seemed candid. Luvexis was an incumbent, not a competitive
winner on merits. CRM loss reason ("competitor offered better price") does not match
the interview.

---

**Telvax Investment Group** (Lost to Databricks)
Conducted by: sales manager

"We have very specific data residency requirements. Your team told us that feature
was on the roadmap but couldn't commit to a timeline. Databricks had something
workable today. We can't make a compliance bet on a roadmap item."

Interviewer note: Rep was unaware of the compliance requirement until Stage 3.
Feature has been on the product roadmap for two quarters with no committed ship date.

---

**Telvane Asset Group** (Lost to Luvexis)
Conducted by: AE post-loss

"The IT team was really the one driving this. They'd used Luvexis at their previous
company. I don't think the business case we were making got much air time internally
— IT had a recommendation and leadership went with it."

Interviewer note: AE confirmed no CFO or COO ever engaged. CRM showed IT Director
as champion throughout.

---

**Korvel Investments** (No decision)
Conducted by: SDR post-loss

"We just couldn't get budget approved this cycle. Our COO was interested but it
never got to the CFO. Timing wasn't right."

Interviewer note: No champion above IT Director level was ever engaged. "COO was
interested" — no direct contact with COO confirmed in CRM.

---

## Part 3B — Rep Notes (selected)

**Vestrix Securities** (Lost — "not the right fit," Stage 2)
Rep: "I pushed for a second meeting but the IT Director kept saying they'd look at
it again next quarter. I couldn't get anyone else on the call. Not sure if it was
a real deal."

**Valdrex Capital** (Lost — "not the right fit," Stage 3)
Rep: "The data engineer I was talking to loved the product but kept saying he needed
to get his boss involved. Never happened. Deal died when he left the company."

**Kessval Financial** (No decision)
Rep: "Budget freeze was real, but I also felt like our champion didn't have the
authority to push this through. He was technically our main contact but I'm not sure
he ever put it in front of the actual decision-makers."

---

## Part 4 — Prior Intervention (deployed Q3 2026)

Following an initial analysis in late Q2 2026, the team deployed a qualification
criteria update. The Loop should treat this as an active Intervention testing pattern
and process the partial observation data below without upgrading Intervention
confidence until the predefined threshold is reached.

**Intervention deployed:** Stage 2 qualification criteria updated to require
identification of a VP-level or above technical champion (VP Engineering, CTO,
Head of Data, CDO, or CISO with confirmed C-suite access) before committing
Stage 3 resources. Reps are instructed that deals with IT Director or IT Manager
as sole champion should not advance past Stage 2 until a VP-level contact is
identified or the deal is disqualified.

**Deployment date:** July 7, 2026

**Eligibility criteria:** New enterprise FS opportunities entering pipeline on or
after July 7, 2026, in which a VP-level technical champion is identified and
confirmed at Stage 2 entry.

**Assignment method:** All eligible deals (no holdout control group). Same-period
comparison cohort: enterprise FS deals entering pipeline from July 7 onward with
IT Director or IT Manager as sole champion, not meeting the new criteria.

**Treated cohort (as defined):** Enterprise FS deals, 500+ employees, North America,
entering pipeline July 7, 2026 or later with VP-level champion confirmed at Stage 2.

**Comparison cohort:** Enterprise FS deals entering pipeline same period (July 7
onward) with IT Director or IT Manager as primary champion — business as usual.

**Matching variables (pre-treatment):** Segment (enterprise FS), geography (North
America), deal source (inbound / outbound / partner / referral), deal value range,
competitor or incumbent presence, rep tenure, initial product requirements. Economic
buyer engagement is the target behavior of the intervention — it is tracked as a
leading indicator, not a matching variable.

**Pre-intervention baseline win rate (treated cohort segment, Q1–Q2 2026):** 38%
overall enterprise FS. For deals with VP+ champion specifically: 7 of 9 won deals
(78%) had VP+ champion. Baseline comparison for VP+ cohort will be estimated at
approximately 70%+ given Q1–Q2 data; note sample is small and precise segmented
baseline has not been separately calculated.

**Pre-intervention baseline, comparison (IT Director cohort, Q1–Q2 2026):** 0 of
15 lost deals closed won when IT Director was sole champion and no economic buyer
was engaged (0%). The two exceptions — Kelvane Wealth and Vestral Lending — had
IT Director-equivalent champions but at lower deal values in non-competitive
conditions. Estimated IT Director sole-champion win rate in competitive enterprise
FS: approximately 0–15%.

**Observation window:**
* Start: July 7, 2026
* Minimum deal count before interpretation: 15 closed eligible deals
* Planned end: Q4 2026 close (approximately December 31, 2026) or 15 minimum closed
  deals, whichever is later

**Leading indicator:** Percentage of new Stage 3 entries with VP-level champion
identified and economic buyer (CFO, COO, or CEO) contacted at least once.

**Final outcome metric:** Win rate of the eligible treated cohort at close.

---

**Partial observation data — as of August 1, 2026 (25 days post-deployment)**

This is early descriptive data only. The observation threshold has not been reached.
No Intervention confidence upgrade is warranted from these results.

Treated cohort (VP+ champion, July 7 onward):
* Deals opened: 8
* Deals closed: 3 (below the 15-deal minimum threshold)
  * Won: Clearbrook Capital ($340K) — VP Engineering + CFO engaged; Stage 5 close
  * Won: Morehouse Analytics ($280K) — CTO + COO engaged; Stage 5 close
  * Lost: Fortbridge Securities ($410K) — VP Engineering champion; lost at Stage 4.
    Loss reason: compliance feature gap. Note: this loss is consistent with Pattern 2
    (compliance capability gap), not a contradiction of the champion profile pattern.
    The qualification criteria change cannot compensate for a disqualifying product gap.
* Current treated cohort win rate (3 closed deals): 2 / 3 = 67%

Comparison cohort (IT Director sole champion, same period):
* Deals opened: 5
* Deals closed: 2
  * Lost: Telvex Trust ($390K) — IT Director, no economic buyer; lost to Luvexis
  * Lost: Redwood Capital ($255K) — IT Manager, no economic buyer; no decision
* Current comparison cohort win rate (2 closed deals): 0 / 2 = 0%

Adoption / fidelity: Unknown pending CRM audit. Reps have been informed of the new
criteria. No formal fidelity check has been completed. At least one deal (Fortbridge)
appears to have met criteria correctly.

Control-group contamination: Low likelihood. Comparison group deals are proceeding
under prior process. No cross-contamination observed.

Concurrent changes since July 7:
* No major product releases
* No pricing changes
* No territory changes
* Luvexis promotional campaign from Q1 appears to have concluded
* No new rep hires or departures

**Loop instruction:** The early treated cohort result (67% win rate, 3 deals) and
comparison result (0%, 2 deals) are directionally consistent with the champion
profile hypothesis. They do not constitute sufficient evidence to upgrade Intervention
confidence. Do not upgrade from Untested until the 15-deal minimum is reached or
the Q4 2026 observation window closes. Label all current results as "early descriptive
result — observation threshold not yet reached."

---

## Part 5 — Context and Confounders (Q1–Q2 2026)

**Product changes:** Data residency / compliance feature set has been "in progress"
for two quarters. Internal estimate is Q4 2026 delivery. Currently not available for
financial services customers with specific SEC 17a-4 or FINRA data residency
requirements.

**Competitive landscape:** Luvexis ran a promotional pricing campaign targeting
financial services accounts in Q1 2026. Databricks released a compliance-ready data
lakehouse offering in late Q4 2025 with SOC 2, ISO 27001, and initial SEC 17a-4
compliance documentation.

**Rep context:** Three AEs. Marcus L. joined 8 months ago and carries 7 of the 15
lost deals. Priya K. and Tom S. each carry 4 of the 15 losses. Win rates: Marcus L.
27%, Priya K. 44%, Tom S. 46%. Marcus's territory skews toward outbound-sourced deals.
