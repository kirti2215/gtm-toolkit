# GTM Annual Strategy and Goal Governance Loop

**Toolkit Release: 1.0**

| Component | Version |
|-----------|---------|
| LOOP.md | v2.0 |
| input-template.md | v2.1 |
| loop-prompt.md | v1.0 |
| example-input.md | v1.0 |
| example-output.md | v1.0 |
| annual-strategy-before-after-evals.md | v1.0 |
| README.md | Toolkit Release 1.0 |

---

## What This Loop Does

The Annual GTM Strategy and Goal Governance Loop governs a portfolio of strategic
bets against a set of annual commitments from initial portfolio formation through
year-end learning.

It tracks the assumptions behind each bet — not just the actuals — so the
organization knows when a plan is failing before the results confirm it. It
separates execution failures from strategy failures, identifies cross-commitment
tradeoffs before they become blind spots, and evaluates whether deployed
interventions actually changed outcomes.

The Loop operates across four modes: Planning, Monitoring, Adaptation, and
Endgame and Learning. It infers mode from evidence. It does not accept mode
declarations from users.

---

## When to Use This Loop

Use this Loop when you need to know whether your annual GTM plan is still
credible — not just whether you are behind plan.

Specific use cases:

**Annual planning:** Pressure-test the portfolio before committing. Surface
unsupported assumptions, seasonal calendar gaps, contribution bridge shortfalls,
and dependency risks before the fiscal year starts.

**Monthly operating reviews:** Go beyond actuals-vs-plan. Understand whether the
assumptions behind each bet are holding, whether the seasonal window is still open,
and whether the organization is executing the right strategy or the wrong one well.

**QBR preparation:** Know whether the plan is supportable before the meeting, not
after. Arrive with a diagnosis, not just a summary.

**Assumption signals:** When a load-bearing assumption starts weakening, understand
immediately whether it warrants intensified Monitoring and a named decision deadline,
or full Adaptation.

**Upside capture:** When a bet is outperforming, evaluate whether to accelerate
investment before the seasonal window closes — and whether doing so creates
tradeoffs for other commitments.

**Non-negotiable commitment risk:** When a protected commitment is in question,
run the formal breach assessment before leadership needs to make the decision.

**Intervention follow-through:** After deploying a pivot or response, evaluate
whether it worked — and what to do next based on the result.

---

## Files in This Folder

| File | Purpose |
|------|---------|
| `LOOP.md` | Canonical architecture reference. The design principles, state model, health model, decision vocabulary, and operating rules. Read this to understand what the Loop is built to do and why. |
| `loop-prompt.md` | Runnable system prompt. Paste this into your AI system before providing the input template. This is what governs each Loop run. |
| `input-template.md` | Structured input form. Fill this in and provide it after the prompt. MODULE A is completed once at planning. MODULE B is completed on each review run. |
| `example-input.md` | A complete filled-in example input showing Nexovane's FY2025 Month 7 Operating Review. Use this as a reference when completing your own input. |
| `example-output.md` | The Loop's full output for the Nexovane example. Shows what a real Adaptation run looks like, including a non-negotiable breach notice, cross-commitment conflict detection, conditional recommendations, and an opened intervention evaluation record. |
| `annual-strategy-before-after-evals.md` | Five before-and-after evaluations showing what a generic response produces vs. what this Loop produces across Planning, Warning, Adaptation, Intervention evaluation, and a synthetic future update. |

---

## How to Run This Loop

**Step 1:** Read `LOOP.md` once to understand the architecture. You do not need
to reference it during each run — it is the design specification, not the runtime prompt.

**Step 2:** At the start of your fiscal year, complete MODULE A of `input-template.md`.
This is your planning-time initialization. Do not rush it. The quality of MODULE A
determines the quality of every subsequent run.

**Step 3:** Paste `loop-prompt.md` into your AI system as the system prompt.

**Step 4:** Provide your completed MODULE A (and MODULE B on recurring reviews)
as the user message.

**Step 5:** Read the output. The Loop infers operating mode, assesses all state
and health dimensions, diagnoses root cause, and recommends decisions in the
canonical vocabulary. Use the recommendations to make, approve, and record
explicit decisions — the Loop surfaces the options; the organization decides.

**Step 6:** When the Loop triggers Adaptation and recommends an intervention,
open an Intervention Evaluation record using the fields defined in the output.
Return in the next review with actual leading signal readings so the Loop can
assess whether the intervention worked.

**Step 7:** Any change to a plan value — assumption statement, commitment target,
threshold, seasonal window, contribution expectation — must be recorded in A9
(Version Ledger) with the original value, revised value, change type, and evidence.
The Loop cannot preserve plan integrity if values are changed without a record.

---

## How This Loop Relates to the Rest of the GTM Toolkit

The Annual GTM Strategy Loop sits at the top of the Loop hierarchy. It consumes
outputs from two subordinate Loops:

**Win/Loss Pattern Loop:** Findings about why deals win and lose in specific segments.
Win/Loss findings affect Bet 1-type assumptions about champion profile, competitive
dynamics, and product-market fit. Import Win/Loss findings with their full attribution
schema (mechanism confidence, prevalence confidence, cohort, denominator, period,
scope limitations) — do not summarize them.

**Pipeline Risk Loop:** Findings about pipeline health, velocity, and concentration
risk. Pipeline Risk findings affect Annual GTM Loop assumptions about pipeline
coverage, stage conversion, and deal velocity. Import with source-specific attribution
(portfolio scope, as-of date, risk definition, stage/cohort, concentration, timing).

Neither subordinate Loop replaces the Annual GTM Loop. They supply evidence to it.

---

## Design Principles

**Evidence in, diagnosis out.** The user supplies facts. The Loop determines mode,
status, health, root cause, and recommendations. No status judgment belongs in the
user's input.

**The plan is immutable.** The Loop may update the plan; it may never rewrite it.
Every change is preserved alongside its original in the Version Ledger. Formal target
accommodation is labeled as such — permanently.

**Warning is not Adaptation.** A Warning on a load-bearing assumption triggers a
named decision deadline and intensified monitoring. Adaptation triggers when Warning
combines with a compressed latest-useful window, when multiple related Warnings
produce material combined portfolio impact, or when an assumption is Invalidated.

**Root cause determines decision type.** Execution failures require execution
responses. Strategy failures require strategic responses. The Loop diagnoses before
recommending. Applying an execution response to a strategy failure wastes resources.

**The Loop closes the loop.** Every intervention receives a baseline, an expected
leading signal, a signal date, an observation window, and a formal result assessment.
The organization learns from what it does, not just from what the market does to it.

---

## Fictional Universe Used in Examples

All company names, account names, partner names, people, regulators, timelines,
market conditions, statistics, financial figures, deal data, and events referenced
in the example files are entirely fictional and created for illustrative purposes
only. They have been verified to have no real-world collision.

- **Organization:** Nexovane (compliance automation platform)
- **Competitor:** Luvexis
- **Partner:** Korval Advisory Partners
- **Accounts referenced:** Alderix Capital, Telvax Investment Group, Cadrova
  Financial, Velstrom Asset Management, Vestrix Securities, Korvel Investments,
  Pelanthor Trust, Telvoran Capital, Pelantrix Advisors, Kessval Financial

Any resemblance to real companies, people, market events, regulatory actions,
financial results, or deal outcomes is coincidental. The figures, timelines,
win rates, deal sizes, competitive dynamics, and regulatory scenarios in the
examples are constructed to illustrate Loop behavior — they do not represent
actual market conditions, real organizations, or factual data.
