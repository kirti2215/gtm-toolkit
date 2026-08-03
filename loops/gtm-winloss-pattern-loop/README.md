# GTM Win/Loss Pattern Loop

A feedback-driven Claude agent loop for enterprise win/loss analysis.
Built for PMM, GTM strategy, RevOps, and sales leadership who need to understand
why they are winning and losing — and who need that understanding to stay current
as new deals close, not sit in a document from last quarter.

---

## What This Is

This is a prompt-driven prototype of a stateful GTM Loop. It uses a persistent
Claude conversation to maintain a living pattern model across deals — updating
hypotheses as new evidence arrives, calibrating confidence based on evidence quality,
and recommending artifacts only when the pattern is strong enough to act on.

Most win/loss analysis is a point-in-time exercise: pull the data, find the patterns,
write the summary, share it once. The patterns sit in a document. The next quarter's
losses don't update them. A new exit interview doesn't get incorporated. The battle
card goes out based on a pattern observed six months ago.

This Loop treats the pattern model as a living object. Each new closed deal is an
input. Each new interview is the highest-priority evidence update. The Loop tracks
what interventions it recommended, whether they were deployed, and whether win rate
in the targeted segment changed afterward — within the limits of what the evidence
actually supports.

**What a standard win/loss prompt produces:** a list of patterns ranked by frequency,
with generic recommendations.

**What this Loop produces:** a calibrated pattern model with evidence tiers, a three-
part confidence architecture, a five-level learning chain from association to validated
intervention, and a sequencing principle — diagnose the mechanism before generating
the artifact.

---

## Intended Users

This Loop is designed for:
* **PMM and GTM strategy** — pattern identification, artifact recommendations,
  competitive positioning decisions
* **RevOps** — evidence base, routing, measurement design, pipeline quality analysis
* **Sales leadership** — qualification decisions, enablement priorities, escalation
  decisions
* **Product leadership** — capability gap signals, escalation briefs

This Loop is **not** a rep-facing tool. Reps should not run this Loop on individual
deals in isolation — the statistical patterns are only meaningful across a deal set,
not a single account. It is retrospective (closed deals only), not predictive (open
deals). It should not be used for pipeline management — use the Pipeline Risk Loop
for that. Confirmed Win/Loss patterns may later inform the risk calibration in the
Pipeline Risk Loop, but the two Loops operate independently.

**Single-deal forensics vs. multi-deal analysis:** a single exit interview supplies
high-quality mechanism evidence — the best available explanation for what happened
in one deal. Multi-deal analysis tests whether mechanisms generalize across the
deal set. The Loop connects both, but treats them as separate evidence types with
different epistemic weight.

---

## When to Use This Loop

Use this Loop when:
* Win rate in a segment has declined and the team does not know why
* Multiple interventions have been tried and none have moved the number
* You want to distinguish a rep execution issue from a qualification, product, or
  competitive pattern before acting
* A new deal closes (won or lost) and you want to know if it confirms or contradicts
  the current pattern model
* A new exit interview is available and you want to know what it changes

Do not use this Loop as a pipeline management tool or as a real-time deal coaching
tool. For open deal risk, use the Pipeline Risk Loop.

---

## The Five-Level Learning Chain

The Loop operates through five levels. Each level requires specific evidence before
the next becomes accessible:

1. **Outcome** — what happened
2. **Association** — what variables co-occur disproportionately with this outcome
3. **Mechanism hypothesis** — what pathway may connect the variable to the outcome
4. **Counterfactual evidence** — buyer-reported evidence about what would have needed
   to change
5. **Intervention evaluation** — how the treated cohort performed relative to a
   credible comparison

Correlation identifies the pattern cohort. Mechanism explains what may be happening.
Counterfactual evidence strengthens the hypothesis but remains a buyer claim, not
experimental proof. Intervention evaluation tests whether addressing the mechanism
changed outcomes.

A pattern cannot move directly from association to strategy.

---

## Folder Structure

```
gtm-winloss-pattern-loop/
├── README.md               ← You are here
├── loop-prompt.md          ← The runnable prompt — copy this into Claude
├── input-template.md       ← How to structure your deal data before running
├── example-input.md        ← Fictionalized enterprise fintech scenario (reference)
├── example-output.md       ← Pattern output from the above input, demonstrating
│                              the full Loop: causal chain, confidence architecture,
│                              intervention evaluation, and evidence acquisition
├── LOOP.md                 ← Full Loop design document (architecture, five-level
│                              chain, pattern state model, evidence hierarchy,
│                              confidence thresholds, intervention evaluation design,
│                              routing table — read this to understand the system)
└── winloss-before-after-evals.md
                            ← Before/after evaluations across 3 scenarios showing
                               how feedback changes the pattern diagnosis, plus a
                               Synthetic Future Update appendix demonstrating
                               intervention evaluation design and confidence language
```

---

## How to Run It

**Step 1 — Structure your deal data**
Use `input-template.md`. At minimum you need a closed deal log covering the last
3–6 months with: outcome, segment, deal value, champion title, economic buyer
engaged, competitor(s), loss reason code, and deal source. The more context you
provide (exit interviews, rep notes, product and competitive changes), the more
precise the first pattern model will be.

If a prior intervention has already been deployed, fill out the Prior Interventions
section of the input template so the Loop can continue tracking the evaluation
rather than starting from scratch.

**Step 2 — Copy `loop-prompt.md` into Claude**
Paste the loop prompt as your first message. Then paste your deal data below it.

**Step 3 — Review the pattern dashboard**
The Loop produces: a pattern status dashboard (with Pattern Maturity and Operational
Status), a pattern breakdown for each Medium or High Prevalence pattern (including
causal chain, evidence base, confidence assessments, and evidence acquisition plan),
and a portfolio observation.

**Step 4 — Feed back new evidence**
When a new deal closes, paste the deal record into the conversation. When a new
exit interview is available, paste it in — the Loop treats it as the highest-
priority evidence update. When an artifact has been deployed, note it and include
the intervention evaluation design fields from the input template.

---

## The Feedback Mechanism

| Evidence type | What the Loop does |
|---|---|
| New closed deal | Confirms or contradicts existing patterns; may cross a confidence threshold |
| Exit interview | Highest-priority update; may reframe the pattern type; elevates Mechanism confidence |
| Artifact deployed | Loop records evaluation design; tracks early results; does not upgrade confidence until observation threshold is reached |
| Contradicting deal | Pattern confidence recalibrated based on evidence-weighted contradiction assessment |

The Loop does not regenerate the full analysis on every update. It updates affected
patterns, states what changed, and flags if the portfolio observation has shifted.

---

## Pattern Taxonomy

Eleven pattern types the Loop monitors:

1. **Qualification** — wrong deals entering the pipeline
2. **Champion profile** — who drives the decision correlates with outcome
3. **Value** — specific use cases or value props landing or falling flat
4. **Competitive** — win rate shifts when a specific competitor is present
5. **Process / stall** — deals dying at a specific stage for process reasons
6. **Commercial** — pricing or packaging causing losses
7. **Timing / entry** — when in the buying cycle engagement begins affects outcome
8. **Stakeholder breadth** — single vs. multi-threaded deals behave differently
9. **Segment / vertical** — win rates differ systematically by segment or geography
10. **Product / capability** — product cannot meet a required capability or regulatory
    condition for a subset of buyers
11. **Sales execution / coverage** — outcome differences that persist after controlling
    for territory, source, deal size, and champion profile

---

## Three-Part Confidence Architecture

The Loop tracks three independent confidence dimensions — never collapsing them into
one score:

**Mechanism confidence (High / Medium / Low)** — how well evidenced is the proposed
pathway from variable to outcome?

**Prevalence confidence (Insufficient / Low / Medium / High / Contradicted)** — how
broadly does this mechanism operate across the deal set? Based on denominators and
outcome differentials, not interview count.

**Intervention confidence (Untested / Directional / Matched Evidence / Controlled
Evidence)** — how validated is the recommended intervention? Plus a separate
Replication status (None / Partial / Replicated).

A pre/post improvement in the treated cohort without a same-period comparison
produces Directional confidence only. Matched Evidence requires a same-period
comparison cohort matched on pre-treatment variables. Validated pattern maturity
requires Matched or Controlled Evidence, or Replicated Directional across independent
cohorts.

---

## Designed by

Kirti Gupta — GTM & Product Marketing, AWS
[LinkedIn](https://www.linkedin.com/in/kirtigupta) | [The Strategy Lens](https://www.linkedin.com/newsletters/the-strategy-lens)

Part of a series on Claude Agent Loops for GTM workflows. For the full architecture,
five-level learning chain, pattern state model, evidence hierarchy, confidence
thresholds, and routing table, see `LOOP.md`. For before/after evaluations and
a worked intervention evaluation example, see `winloss-before-after-evals.md`.
