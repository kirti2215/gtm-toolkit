# GTM Pipeline Risk Loop

A feedback-driven Claude agent loop for enterprise sales pipeline management.
Built for GTM and sales leaders who need to know which deals to prioritize, why,
and what to do about it — and who need that answer to update as new evidence comes in.

---

## What This Is

A Claude Loop is not a prompt. It is a structured cycle that maintains deal state
across multiple passes, updates its diagnosis when new evidence arrives, and decides
when a pattern has shifted enough to change the recommended action.

The Pipeline Risk Loop:
- Classifies each deal by risk type (9-type taxonomy)
- Prioritizes across the portfolio by revenue at risk × probability of loss × urgency
- Recommends specific next actions with owners, deadlines, and success signals
- Updates its diagnosis when feedback arrives (call transcripts, new stakeholders,
  rep notes, stage changes)
- Decides when to invoke downstream Skills (e.g., competitive battle card) vs. when
  to run a diagnostic action first

What a generic pipeline review prompt produces: a list of at-risk deals, sorted by
close date. What this Loop produces: a sequenced intervention plan with explicit
reasoning about which deal deserves the most attention and why.

---

## When to Use This Loop

Use this Loop when:
- A sales manager needs to prioritize attention across 6–20 active deals
- A deal's situation has changed and the previous recommendation may be stale
- You want to understand why the pipeline is at risk, not just which deals are at risk
- You need to know which cross-functional escalations are warranted (product, legal,
  executive) and which ones can wait

Do not use this Loop as a deal-level forecasting tool. It is a diagnostic and
intervention prioritization tool, not a prediction engine.

---

## Folder Structure

```
gtm-pipeline-risk-loop/
├── README.md               ← You are here
├── loop-prompt.md          ← The actual Loop prompt — copy this into Claude
├── input-template.md       ← Structured input format (fill this out before running)
├── example-input.md        ← Fictionalized 8-deal scenario (reference)
├── example-output.md       ← Example output from the above input (reference)
├── LOOP.md                 ← Full Loop design document (architecture, taxonomy,
│                              state model, feedback mechanism — read this to
│                              understand what the Loop is doing and why)
└── pipeline-risk-before-after-evals.md
                            ← Before/after evaluations across 3 scenarios showing
                               how feedback changes the output
```

---

## How to Run It

**Step 1 — Fill out the input template**
Use `input-template.md` to structure your pipeline data. At minimum you need:
- Pipeline snapshot (deals, stages, close dates, deal values, last activity)
- Time horizon and quarter end date
- Your definition of "at risk" for this review
- Rep context (any coverage gaps, new reps, territory changes)
- Recent field intelligence not captured in CRM

The more context you provide, the more precise the output. Optional fields (historical
win rates, competitive context, exit interview data) meaningfully improve diagnosis.

**Step 2 — Copy `loop-prompt.md` into Claude**
Paste the loop prompt as your system prompt or as the first message in a new Claude
conversation. Then paste your filled-out input below it.

**Step 3 — Review Pass 1 output**
The Loop will produce: an executive summary, a prioritized deal dashboard, deal-by-
deal breakdowns with specific actions, and a portfolio pattern observation.

**Step 4 — Feed back new evidence**
When a deal changes — new stakeholder added, call transcript available, rep shares an
update, stage or close date moves — paste that update into the conversation. The Loop
will update its diagnosis, revise the priority stack if needed, and tell you what
changed and why.

---

## The Feedback Mechanism

The Loop is designed to be used over time, not once. Each new piece of evidence is
an input:

| Evidence type | What the Loop does with it |
|---|---|
| Call transcript / meeting notes | Updates engagement signal, revises risk assessment |
| New stakeholder added | Evaluates champion risk; may change priority |
| Stage or close date change | Recalculates urgency; may trigger escalation |
| Rep update / field intel | Incorporates as evidence (weighted by tier) |
| Customer response to outreach | Confirms or contradicts the intervention hypothesis |
| Action deadline passes with no response | Triggers escalation or reforecast |

---

## Risk Taxonomy

The Loop classifies deals across 9 risk types:

1. **Qualification risk** — The deal may not be a real opportunity
2. **Stakeholder / champion risk** — The champion is weak, gone, or losing influence
3. **Value risk** — The business case is not landing or has not been made
4. **Technical risk** — Product gaps, integration concerns, or security review blockers
5. **Competitive risk** — A competitor is actively displacing or has incumbent advantage
6. **Commercial risk** — Pricing, terms, or contracting is causing stall or regression
7. **Process / timing risk** — Procurement, legal, or security has not started with
   insufficient time to close
8. **Engagement risk** — Buyer has gone silent or contact frequency has declined
9. **Forecast integrity risk** — The deal is in forecast but the signals do not support it

---

## Designed by

Kirti Gupta — GTM & Product Marketing, AWS
[LinkedIn](https://www.linkedin.com/in/kirtigupta) | [The Strategy Lens](https://www.linkedin.com/newsletters/the-strategy-lens)

Part of a series on Claude Agent Loops for GTM workflows. For the full architecture,
design rationale, and before/after evaluations, see `LOOP.md` and
`pipeline-risk-before-after-evals.md`.
