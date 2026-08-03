---
name: gtm-pipeline-risk-loop
description: >
  A goal-driven agentic Loop that diagnoses pipeline risk across active deals,
  recommends stage-appropriate GTM interventions, and updates its plan when
  new field or customer evidence arrives. Use when a GTM leader, sales manager,
  or PMM wants to know which deals are at risk, why, what to do, and whether
  the last action worked. Unlike a Skill, this Loop does not end with a
  deliverable — it ends when the risk is resolved, the deal permanently
  exits, or the next decision is handed to an authorized human process.
  A reforecasted deal moves to a new monitoring horizon with its state
  preserved — it is not a closed deal.
---

# GTM Pipeline Risk Loop

---

## The Core Distinction

**The Skill contains the GTM judgment. The Loop owns the commercial journey.**

A Skill uses context to perform a unit of work. You give it the deal, the
buyer, the competitor — it applies encoded GTM judgment and produces an output.
Someone could rerun that Skill with updated context and get a better output.
But the Skill does not remember the previous run, does not know what action
was taken, and does not know whether the action worked.

A Loop owns the continuity between runs. It preserves the previous diagnosis,
knows which action it recommended, waits for or detects a defined feedback
signal, compares the outcome with the expected success signal, updates the
deal state, and selects the next action. It continues until an exit condition
is reached.

The difference is not that a Skill cannot use new information. It is that
a Skill must be told everything each time. A Loop remembers.

| Skill | Loop |
|---|---|
| Needs context to produce the right output | Needs context to begin; preserves state to continue |
| Applies GTM judgment once per invocation | Reapplies judgment each time new evidence arrives |
| Can be rerun with updated context | Owns the continuity between runs — remembers what happened |
| Ends with a deliverable | Ends when the risk is resolved, the deal permanently exits, or handed to a human — a reforecasted deal continues in a new horizon |
| Quality depends on input context | Quality depends on context, state, and feedback signals |

---

## Goal

> Reduce preventable pipeline slippage and improve forecast confidence by
> continuously identifying opportunity risks, diagnosing their causes,
> recommending stage-appropriate actions, and updating the commercial plan
> when new field or customer evidence changes the picture.

The Loop is not asking: *Is this deal risky?*

It is asking: *What is blocking this deal, is the risk recoverable, what
should the GTM team do next, and did the last action change anything?*

---

## Step 1: Initial Context

The Loop needs this before its first pass. More context produces a more
accurate first diagnosis — but the Loop will update its understanding
regardless of how complete the starting point is.

### Required

- **Pipeline snapshot** — active deals with at minimum:
  - Deal name / account
  - Stage
  - Expected close date
  - Deal value
  - Last meaningful activity (not auto-emails)
  - Assigned rep

- **Time horizon** — what period are you trying to protect?

- **Definition of success** — what does "resolved" look like?
  Close this quarter / protect forecast integrity / identify what to reforecast

### Optional but materially improves the first pass

- **Historical benchmarks** — average time in stage, win rate by stage and
  deal size, typical procurement timeline. Without these, the Loop applies
  general thresholds that may not match your business.

- **Competitive context** — named competitors in any deal

- **Rep context** — new hire, covering two territories, deal size vs. history

- **Field intelligence not in CRM** — what reps have said in reviews, calls,
  or Slack that does not appear in the system

### Evidence hierarchy

The Loop weights evidence in this order. Contradictions between tiers are
flagged explicitly — never silently resolved.

1. Direct customer statement (exit interview, direct buyer feedback, written commitment)
2. Observed buyer behavior (call transcript, email patterns, response timing,
   product usage, meeting attendance)
3. Multi-source corroboration (same signal appearing across rep notes + CRM + field intel)
4. CRM field data (stage history, close dates, contact records, forecast category)
5. Rep notes (recent and specific outweigh weeks-old and vague)
6. Inferred from pattern alone (ratio or trend without explanation)

Confidence level cannot exceed what the evidence supports. A deal with only Tier 5–6
evidence gets Low confidence even if the risk signal looks strong.

---

## Deal State Model

For the Loop to be a genuine Loop — not a Skill rerun with more context —
it must carry forward a state object for each deal. Without this, Pass 2
is just another fresh analysis. With it, Pass 2 is a state transition.

The Loop maintains the following for each deal across runs:

```
Deal state
  - Account name and deal ID
  - Current stage and forecast category
  - Current primary risk type
  - Current secondary risk type (if any)
  - Evidence supporting each risk (with tier from hierarchy)
  - Confidence in diagnosis: High / Medium / Low
  - Previous diagnosis (what changed and when)
  - Last recommended action
  - Action owner and deadline
  - Expected success signal
  - Actual outcome observed
  - New evidence received
  - Last state-change timestamp
  - Number of consecutive unsuccessful interventions
  - Current escalation status
  - Lifecycle status (active / monitoring / deferred / escalated / won / lost / disqualified / resolved)
```

The core operation on each feedback cycle:

```
Previous state
+ new evidence
+ result of prior action
→ updated state
→ revised priority across portfolio
→ next action or exit condition
```

This is what separates a Loop from a sophisticated one-shot prompt. The
Skill asks: *given this context, what should happen?* The Loop asks: *given
what has already happened and what just changed, what should happen next?*

---

## Step 2: How the Loop Reasons

The Loop runs as a continuous cycle:

> **Observe → Diagnose → Prioritize → Act → Measure → Update State → Observe Again**

The initial run moves through all six stages. When feedback arrives — a call
transcript, a customer reply, a stage change, a legal finding — the Loop
measures the outcome, updates the stored deal state, and reruns Observe
through Act using the new evidence. It does not only "measure and update."
It reassesses from the top, because new evidence can change the observed
signals, the diagnosis, the severity, the recoverability, the portfolio
priority, and the recommended action.

Scenario 3 in the eval document demonstrates this: a deal classified as
Healthy becomes the highest-priority deal in the portfolio when a legal
review surfaces a product gap. That is not an update — it is a full
re-diagnosis triggered by new evidence.

---

### Pass 1 — Observe

Scan all deals and collect signals. Group into:
- **High concern** — multiple signals present
- **Watch** — one or two signals
- **Healthy** — no significant signals

Signals the Loop looks for:

| Signal | What it suggests |
|---|---|
| Close date within 6 weeks, no stage progression in 14+ days | Deal is stalling |
| No buyer-initiated contact in 21+ days | Champion may have gone quiet |
| Late stage, no procurement or legal involvement | Process not started |
| Competitor named, no competitive activity logged | Field is unprepared |
| Deal size 2x+ rep's average | Complexity likely underestimated |
| New stakeholders added late | Decision process expanding |
| Last activity: rep email, no reply | Buyer has gone cold |
| Stage regression | Something went wrong |
| Close date moved more than once | Deal repeatedly slipping |
| Forecasted as Commit, no economic buyer documented | Forecast integrity risk |

---

### Pass 2 — Diagnose

For each high-concern deal, identify the **primary risk type**. This is the
most important pass — the right diagnosis determines the right action.
A deal with the wrong diagnosis gets the wrong intervention.

**Qualification risk**
The problem, urgency, budget, or success criteria are unclear.
Signals: generic use case, no quantified impact, no compelling event, stage
advanced without sufficient discovery.
Intervention type: requalify, not advance.

**Stakeholder risk**
The team has not built enough internal support.
Signals: one contact engaged, no economic buyer, champion has low influence,
key stakeholder has gone silent.
Intervention type: expand access, not produce content.

**Value risk**
The customer understands the product but not why acting now matters.
Signals: feature discussions dominate, no business case, initiative described
as important but not urgent, no quantified outcome.
Intervention type: business case, not feature proof.

**Technical risk**
The solution has not been proven in the customer's environment.
Signals: architecture questions unresolved, POC stalled, migration effort
unclear, security or compliance requirements open.
Intervention type: SA involvement, not sales pressure.

**Competitive risk**
An incumbent or alternative is threatening the deal.
Signals: competitor in evaluation, incumbent has executive relationships,
switching cost is high, differentiation is not connected to use case.
Intervention type: competitive positioning, not product comparison.

**Commercial risk**
The customer wants the product but the transaction is blocked.
Signals: pricing objection, budget not confirmed, procurement not engaged,
legal delayed, discount expectations misaligned.
Intervention type: commercial path, not messaging.

**Process and timing risk**
The sales plan does not match the customer's buying process.
Signals: no mutual action plan, close date is seller-created, procurement
timeline exceeds close date, deal slips by exactly one quarter repeatedly.
Intervention type: mutual action plan, not pipeline pressure.

**Engagement risk**
Customer momentum is declining.
Signals: meetings postponed, response times increasing, key contact
disengaged, no new stakeholders, POC usage declining.
Intervention type: re-engage differently, not follow up again.

**Forecast integrity risk**
The deal is incorrectly staged or forecasted.
Signals: Commit without economic buyer, large deal with minimal engagement,
stage advanced before a forecast call, no confirmed customer decision date.
Intervention type: reforecast, not more activity.

---

### Pass 3 — Prioritize

Not all risky deals deserve the same attention. The Loop assesses two
dimensions for each high-concern deal:

**Risk severity** — how likely is this deal to slip, shrink, or be lost?
**Recoverability** — can the GTM team realistically change the outcome?

| Severity | Recoverability | What to do |
|---|---|---|
| High | High | Intervene immediately — specific action, 48-hour window |
| High | Low | Reforecast, deprioritize, or escalate — stop investing |
| Low | High | Monitor, strengthen, do not over-resource |
| Low | Low | Maintain normal cadence |

The Loop ranks recoverable deals by:

> **Revenue at risk × probability of loss × probability intervention helps × urgency**

Where urgency *increases* as the intervention window shrinks. In practice,
scored bands (1–5 per factor) work better than false precision:
Priority = impact × severity × recoverability × urgency.

The principle: prioritize deals where meaningful revenue is at risk, the
window is closing, and an intervention can still change the outcome. A large
deal with plenty of time and low recoverability ranks below a smaller deal
closing in two weeks that one call could save.

These scores begin as GTM heuristics. They become more accurate when
calibrated against the company's own historical patterns — stage conversion
rates, typical procurement timelines, win rates by deal size.

The output is ranked by **action urgency**, not risk score. Risk without
action is noise. A sales manager needs to know what to do today, not just
what to worry about.

---

### Pass 4 — Act

For each high-concern deal, the Loop recommends one specific next action
matched to the primary risk type. Not a list. Not "follow up." One action,
with a reason, a timeline, and a success signal.

**If qualification risk:** Revalidate the problem. Ask the champion what
changes if they do nothing for 6 months. If the answer is vague, the deal
is not real yet.

**If stakeholder risk:** Do not produce more content. Ask the champion to
introduce you to the economic buyer. If they won't, they may not have
enough influence to move the deal.

**If value risk:** Build the business case with the champion — not for them.
A case they co-built is more persuasive internally than one you deliver.

**If technical risk:** Bring in the SA before the customer asks. Waiting for
the customer to surface a technical concern is too late.

**If competitive risk:** Diagnose why the competitor is in the deal before
responding. Developer preference, procurement leverage, and incumbency are
three completely different problems.

**If commercial risk:** Engage procurement this week. Every week of delay adds
one week to the close date — at minimum.

**If process and timing risk:** Build a mutual action plan and get the customer
to own milestones. A close date no one on the customer side has signed off
on is not a forecast — it is a wish.

**If engagement risk:** Change what you are offering before you follow up
again. Another email on the same topic confirms you have nothing new to say.

**If forecast integrity risk:** Move the deal category before the next
forecast review. A Commit deal without an economic buyer is not a Commit.

---

### Pass 5 — Measure *(feedback enters here)*

After the recommended action is taken — or after a defined time window
passes without action — the Loop checks:

- Was the action completed?
- What did it reveal?
- Did the customer signal change (positively or negatively)?
- Did the primary risk type change?
- Is the close date more or less credible than before?
- Did a new risk surface?

The Loop does not simply mark the task complete. It asks what the outcome
revealed about the deal — because the outcome is more informative than the
action itself.

Evidence the Loop looks for after an action:

| Action taken | What success looks like | What a different signal means |
|---|---|---|
| Economic buyer meeting | Buyer confirms budget and decision timeline | Buyer says no budget this quarter → commercial risk confirmed |
| SA brought in for technical review | Architecture questions resolved | New requirement surfaced → technical risk elevated |
| Competitive positioning applied | Customer asks about differentiators | Customer says "we've already decided" → engagement risk |
| Mutual action plan proposed | Customer accepts milestones | Customer ignores or delays → process risk confirmed |
| Champion introduced to procurement | Procurement meeting scheduled | Champion says "let me check" → stakeholder risk elevated |

---

### Pass 6 — Update State → Observe Again *(the loop)*

When new evidence arrives, the Loop updates the stored deal state and
immediately re-enters the Observe pass with the new evidence active.
It does not re-run the same analysis — it runs a new analysis from a
different starting point.

One additional design principle governs this cycle: **the Loop sequences
uncertainty-reducing actions before artifact generation.** If the right
intervention depends on information that does not yet exist, the first
action should resolve that uncertainty — not produce content that may be
obsolete once the information arrives. In the competitive scenario in the
eval document, the Loop chose a diagnostic champion call before invoking
the battle card Skill. The call revealed the evaluation had already shifted;
a battle card produced before that call would have been the wrong artifact.

This is also where the Loop's relationship to Skills becomes explicit:
**the Loop decides whether and when to invoke a Skill, supplies it with
the correct context, evaluates what happened after its output was used,
and decides whether to invoke it again or choose a different intervention.**
The Skill encodes quality. The Loop controls sequencing.

Three possible updates:

**Risk type changes**
The intervention addressed one risk, revealing a different underlying risk.
Example: stakeholder risk resolved (economic buyer meeting held), but buyer
confirms no budget until Q2. New primary risk: commercial timing. New action:
reforecast and explore phased path. Old action (get executive access) is
no longer the right move.

**Risk severity changes**
Same risk type, but the level of urgency has shifted.
Example: engagement risk flagged because champion went quiet. After outreach,
champion responds — deal is still active but champion explains a reorg is
happening. Risk type stays the same (stakeholder) but severity increases.
New action: get to the new decision owner before the reorg settles.

**Forecast implication changes**
The deal's forecast category needs to change based on what was learned.
Example: deal in Commit, POC revealed a product gap. Deal should move to
Pipeline until the gap is confirmed solvable. The Loop recommends the
forecast update explicitly — it does not leave that judgment to the rep.

---

## Step 3: Output Structure

### Per-deal risk brief

**[Account Name]**

- **Current risk type:** [primary type from taxonomy] — [one sentence why]
- **Severity:** High / Medium / Low
- **Recoverability:** Recoverable / Recoverable with escalation / Unlikely / Reassess
- **Evidence:** [specific signals that drove this diagnosis — traceable to tier in hierarchy]
- **Action:** [one specific action, person-specific, time-bound]
- **Success signal:** [the specific thing that tells you the risk decreased]
- **What changes the plan:** [the specific evidence that would shift the diagnosis]
- **Escalation trigger:** [when to involve management or stop investing]

### After each feedback cycle

- **What the action revealed:** [what new evidence changed]
- **Updated risk type:** [same / changed — explain]
- **Updated action:** [revised recommendation or confirmation]
- **Forecast implication:** [does the deal category need to change?]

### Portfolio-level pattern

One paragraph: the most common risk type across the pipeline, what it implies
about the team or motion, and the one systemic action most likely to protect
the quarter.

---

## What the Loop Will Not Do

- Invent deal context. Missing information is flagged and weighted
  accordingly in the evidence hierarchy.
- Call a deal unrecoverable on CRM data alone. CRM is a lagging indicator.
  The Loop asks whether field intelligence contradicts the system before
  drawing a conclusion.
- Mark an action complete without asking what it revealed. Completion is
  not the point — what the action surfaced is.
- Produce the same recommendation after negative evidence. If the first
  action did not move the deal, the second recommendation must be different.
- Recommend an action that is outside the seller's authority without flagging
  the escalation required (pricing exception, product commitment, executive
  sponsorship).

---

## Feedback Triggers

The Loop reassesses a deal when any of the following occur:

- The recommended-action deadline passes (with or without action taken)
- A call transcript or seller note is added
- The customer responds to any outreach
- A stakeholder is added or removed from the opportunity
- Stage, close date, deal value, or forecast category changes in CRM
- Procurement, legal, security, or technical review status changes
- Product usage or trial activity materially changes
- A defined time-based risk threshold is crossed (e.g. 21 days without buyer contact)

These triggers make the transition from conceptual framework to buildable
system explicit. Without defined triggers, the Loop has no mechanism for
knowing when to wake up.

---

## Recommendation vs. Authority

The Loop recommends. It does not execute management decisions.

The Loop can recommend:
- A forecast-category change, with the evidence and the required approver named
- Pricing escalation, executive sponsorship, or product review
- Removal of a deal from the forecast

The Loop cannot finalize or execute:
- Forecast-category changes (management decision)
- Pricing exceptions or commercial accommodations
- Product roadmap commitments
- Legal positions or compliance statements
- Resource allocation decisions

When a recommendation requires authority the Loop does not have, it names
the specific decision, the evidence supporting it, and the person who needs
to approve it. It then waits for confirmation before updating the deal state.

---

## Deal Exit Conditions

Not all exits are permanent. The Loop distinguishes:

**Current-cycle exits** — the deal leaves the current protection window
but the commercial journey continues:
- Removed from current-quarter forecast → monitor status
- Deferred to next horizon → reactivates at defined date
- Moved to nurture → low-cadence monitoring

**Permanent exits** — the Loop closes the deal state:
- Won
- Lost
- Disqualified
- Risk resolved (no further intervention needed)
- Handed to an authorized human process (legal, executive, product)

A reforecasted deal is not a closed deal. It carries forward its state —
previous diagnoses, intervention history, evidence — into the next horizon.

---

## Escalation and Human Handoff

The Loop stops and hands off to a human when:

- Evidence contradicts itself materially and cannot be resolved
- A large strategic deal is deteriorating rapidly
- The recommended action requires pricing authority, product commitment,
  or executive relationship
- The Loop cannot diagnose the primary risk with available evidence
- A seller is not acting on recommendations — the problem may be coaching,
  not deal strategy
- The deal should be removed from the forecast — that is a management call,
  not an agent call

Escalation is not a failure. It is part of the design.

---

## Real Example (Two-Pass)

**Deal:** $420K enterprise deal, Stage 4 (Proposal), 3 weeks to close.
Rep sent revised proposal 18 days ago. No reply.

**Pass 1 — initial diagnosis:**
Primary risk: Stakeholder risk (champion has gone quiet).
Action: Rep should call — not email — the champion. Change the subject from
the proposal to the champion's current priorities. Goal is to learn whether
the deal is still active and whether something changed internally.
Success signal: Champion picks up and confirms deal is moving.

**Feedback input:**
Champion picks up. She says she is still interested but a new VP of Finance
started 2 weeks ago and wants to review all vendor commitments over $200K
before signing.

**Pass 2 — updated diagnosis:**
Stakeholder risk partially resolved — champion is still engaged.
New primary risk: Process and timing risk. The deal now requires a new
stakeholder who did not exist in the original buying process. Close date
in 3 weeks is no longer realistic.
Updated action: Do not re-send the proposal. Ask the champion to include
the new VP of Finance in a 30-minute business case review — framed not as
a sales call but as a briefing so the VP can feel confident in the
decision. Simultaneously, move the deal out of this quarter's Commit and
reforecast to next quarter unless the VP meeting is confirmed within 5 days.
Forecast implication: Remove from Commit. Add to early next-quarter pipeline
with specific milestone: VP meeting + procurement timeline confirmed.
