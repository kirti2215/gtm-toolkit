# GTM Pipeline Risk Loop — Before/After Eval Results

**Purpose:** Show what changes when you move from a static risk prompt to a
feedback-driven Loop — and specifically, where in the Loop feedback enters
and how it shifts the output.

**Methodology note:** These are illustrative behavioral evaluations designed
to demonstrate the effect of GTM judgment, persistent state, and feedback
across passes. They are not a controlled benchmark isolating each component
independently. The comparison demonstrates the combined value of better
context, encoded GTM judgment, state continuity, feedback incorporation, and
action sequencing — not each component measured separately.

**Core thesis being tested:**
> A skill uses context to decide how to perform the work.
> A loop uses outcomes to decide what work should happen next.

**Method:** Same deal context fed to both. Three scenarios. Each scenario
shows: without-loop output → Loop Pass 1 → feedback input → Loop Pass 2.
The delta between Pass 1 and Pass 2 is where the Loop earns its name.

---

## How to Read This

Each test case has four sections:

- **WITHOUT LOOP** — output from a plain "which deals are at risk" prompt
- **WITH LOOP — PASS 1** — initial diagnosis and recommended action
- **[FEEDBACK POINT]** — what new evidence arrives after the action
- **WITH LOOP — PASS 2** — updated diagnosis and revised plan
- **DELTA** — what changed, where feedback shifted the output, and why it matters

---

---

## Scenario 1: The Silent Champion

**Deal context:**
- Account: Meridian Financial
- Stage 4 (Proposal), close date August 15 (3 weeks away)
- Deal value: $420K
- Rep sent revised proposal July 10. No reply in 18 days.
- CTO is the only contact engaged. Procurement not involved.
- Sales manager flagged this as a deal to watch.

---

### WITHOUT LOOP

**Prompt used:**
*"Meridian Financial is in Stage 4, closing August 15, $420K deal. Rep sent
a revised proposal 18 days ago with no reply. What should they do?"*

**Output:**

This deal shows signs of stalling. Recommended actions:
- Follow up with the CTO on the proposal
- Ask if there are any outstanding questions
- Consider offering a discount to accelerate the decision
- Loop in your manager if no response within the week

Risk level: Medium-High. Close date may be at risk.

---

**What is wrong with this output:**
- "Follow up on the proposal" is the one thing the rep has already tried
- "Consider offering a discount" is premature — we don't know why they're quiet
- No diagnosis of why the champion went silent
- No distinction between "deal is dead" and "something changed internally"
- No forecast implication
- No definition of success or failure for any recommended action
- Cannot incorporate any new evidence — the output is static

---

### WITH LOOP — PASS 1

**Initial context provided:**
- Meridian Financial, Stage 4, $420K, close August 15
- 18 days since rep-sent proposal with no buyer-initiated reply
- CTO is only contact — no economic buyer below or above engaged
- Procurement not started
- Sales manager's field note: "CTO has been harder to reach lately"

**Loop diagnosis:**

Primary risk: **Stakeholder risk**
The champion has gone quiet after a proposal. This is one of the two most
common pre-loss signals in enterprise deals. The risk is not that the CTO
dislikes the proposal — it is that something changed in their world that
has shifted their priorities, and the rep doesn't know what that is yet.

Secondary risk: **Process and timing risk**
Procurement has not started on a deal closing in 3 weeks. Financial
institutions often run procurement cycles of four to six weeks or longer —
though the precise timeline depends on company-specific benchmarks. If that
heuristic applies here, August 15 is not a supportable close date without
procurement already underway.

Recoverability: Recoverable — but the window is closing.

**Action (Pass 1):**
The rep should call the CTO — not email — and change the subject entirely.
Not: "Following up on the proposal." Instead: "Wanted to check in on your
priorities — I know you've had a lot going on. Is August still the right
timeline for you, or has something shifted?"

Goal: surface whether the deal is still active and whether something changed
internally. An honest answer — even "we need to push" — is more valuable
than silence.

**Success signal:** CTO picks up and gives a direct answer about timeline.
**What would change the plan:** If the CTO mentions a new stakeholder,
a budget review, or an internal priority shift — the risk type changes.
**Forecast implication:** Move out of Commit now. August 15 is not supportable
without procurement started.

---

### [FEEDBACK POINT — WHERE THE LOOP ENTERS]

**What the action revealed:**
The rep calls. The CTO picks up. She says she is still interested, but a
new VP of Finance started two weeks ago and wants to review all vendor
commitments over $200K before signing. She is supportive but cannot move
forward without the VP's sign-off.

---

### WITH LOOP — PASS 2

**What changed:**
Stakeholder risk partially resolved — the champion is engaged and the deal
is still alive. But a new stakeholder appeared who was not part of the
original buying process, has not met the rep, and controls the decision.

**What feedback confirmed and what it revealed:**
Stakeholder risk was the initial hypothesis — the champion had gone quiet.
The call confirmed the champion is still engaged, resolving that uncertainty.
But it revealed the specific cause: a new VP of Finance entered the buying
process and controls the decision. Stakeholder risk is now specific rather
than suspected. Timing risk escalates from likely to confirmed — the buying
process has materially expanded and the current close date cannot hold.

**Updated action (Pass 2):**
Do not re-send the proposal. Do not push on the original timeline.
Ask the CTO to arrange a 30-minute briefing with the new VP of Finance —
framed not as a sales meeting but as a decision-support session: "I want
to make sure your VP has everything they need to feel confident."

This meeting needs to happen before August 8. If it doesn't, the deal
moves to Q4.

**Updated forecast implication:**
Remove from Q3 Commit immediately. Add to early Q4 pipeline with two
confirmed milestones required before re-entering Commit: (1) VP of Finance
meeting held, (2) procurement timeline confirmed in writing.

**What the second pass found that the first pass couldn't:**
The silence was not disengagement — it was the champion managing an internal
constraint she hadn't told the rep about. The call changed the entire
understanding of the deal. A system that couldn't incorporate that call
would have continued recommending "follow up on the proposal" indefinitely.

---

### DELTA

| Dimension | WITHOUT LOOP | LOOP PASS 1 | LOOP PASS 2 | What the feedback shift did |
|---|---|---|---|---|
| Risk diagnosis | "Signs of stalling" | Stakeholder risk suspected + timing risk | Stakeholder risk confirmed and made specific; timing risk escalated to confirmed | Feedback resolved uncertainty — revealed the specific cause, not a new risk type |
| Recommended action | "Follow up on the proposal" | Call, change subject to priorities | Arrange VP briefing, do not re-send proposal | Pass 1 action was the right move; feedback made Pass 2 possible |
| Forecast | Not addressed | Move out of Commit | Remove from Q3, milestone criteria for Q4 | Forecast implication became specific only after feedback |
| Deal status | Ambiguous | Alive but at risk | Alive, stakeholder constraint identified, different quarter | Feedback resolved the ambiguity — deal is real but the constraint is now known |
| What happens next | "Loop in your manager" | Defined success signal | Specific milestone-gated path | Without feedback, next step was generic; with it, next step is precise |

**Where feedback entered:** Between Pass 1 and Pass 2 — the CTO call.
**What it shifted:** Diagnostic confidence and specificity, timeline assessment, forecast category, and the specific action. The risk type did not change — stakeholder risk was the initial hypothesis. Feedback confirmed it and identified the precise cause.

---

---

## Scenario 2: The Competitive Deal the Rep Didn't Prepare For

**Deal context:**
- Account: Cascade Logistics
- Stage 3 (Evaluation), close date August 28
- Deal value: $180K
- Competitor: DataStax, introduced by the customer's data engineering team
- Rep has not run any competitive positioning
- No buyer-initiated contact in 9 days since last SA demo

---

### WITHOUT LOOP

**Prompt used:**
*"Cascade Logistics is in Stage 3, $180K deal, August 28 close. DataStax is
in the deal. The rep hasn't done any competitive positioning. What's the risk?"*

**Output:**

Competitive risk is present. Recommended actions:
- Build a competitive battle card comparing your product to DataStax
- Highlight your product's strengths in the next call
- Ask the customer what they like about DataStax
- Make sure the rep is aware of key differentiators

Risk level: Medium. Deal is winnable if the rep prepares.

---

**What is wrong with this output:**
- Does not diagnose *why* DataStax is in the deal — developer preference
  is a completely different problem from procurement leverage
- "Highlight your product's strengths" is the wrong move for a developer
  preference battle
- No sense of urgency about the 9-day silence
- Cannot update when the competitive situation changes
- Produces a document recommendation when the problem is a relationship problem

---

### WITH LOOP — PASS 1

**Initial context provided:**
- Cascade Logistics, Stage 3, $180K, August 28 close
- DataStax introduced by data engineering team (not procurement, not executive)
- Rep has not run competitive positioning
- 9 days since last contact, last activity was SA demo

**Loop diagnosis:**

Primary risk: **Competitive risk — developer preference motion**
DataStax entered through the engineering team, not through procurement or
executive mandate. This is a developer preference battle — in many technical
buying motions, one of the harder competitive situations to reverse, because
it is tied to workflow familiarity and technical identity, not only feature
comparison. Whether it is reversible here depends on the deal context. Attacking features in this situation typically backfires.

Secondary risk: **Engagement risk**
9 days of silence after a demo. Either the demo did not land, the team
is internally debating, or DataStax is pulling ahead.

Recoverability: Recoverable — but only with the right positioning. The wrong
positioning (feature comparison, price, generic differentiators) will
accelerate the loss.

**Action (Pass 1):**
Before producing any competitive content, call the champion to diagnose why
DataStax is gaining support: "Help me understand how the engineering team is
thinking about this decision — is it a technical preference, or are there
specific use case requirements driving it?"

The Loop sequences this diagnostic call before invoking the competitive
battle card Skill. If the call reveals that the evaluation has already
shifted — the engineering team has committed, a second demo happened, a
trial started — the battle card becomes the wrong artifact. The uncertainty
must be resolved before content is generated, not after.

Once the call completes and the competitive motion is understood, invoke the
competitive battle card Skill with the correct buyer, motivation, and
decision context.

**Success signal:** Customer articulates the specific technical concern, not
just "engineers like DataStax." That gives the rep something to address.
**What would change the plan:** If the customer says the engineering team has
already made a recommendation internally — the battle has moved to executive
override territory, which requires a different play.

---

### [FEEDBACK POINT — WHERE THE LOOP ENTERS]

**What the action revealed:**
The rep calls the champion before running the competitive positioning. In the
call, the champion says: "DataStax gave a really compelling demo last week
focusing on their developer tooling. Our engineering team is excited about it.
They've started prototyping with DataStax's trial account."

---

### WITH LOOP — PASS 2

**What changed:**
Two critical pieces of new information: (1) DataStax has already run a
second demo — the rep did not know this. (2) Engineers have started an
active trial. This is no longer an evaluation — it is a momentum shift.
DataStax is no longer in consideration; DataStax is ahead.

**Updated primary risk: Stakeholder risk**
The engineering team has moved from "considering DataStax" to "actively
using DataStax." The rep's primary problem is no longer competitive
positioning — it is that engineering is becoming a detractor and there is
no executive relationship to counterbalance them.

**Updated action (Pass 2):**
The next action is no longer a battle card. It is changing the stakeholder
and decision architecture of the deal.

Run a dual-thread strategy: maintain technical engagement to understand and
influence the evaluation criteria — abandoning that audience now deepens the
loss — while simultaneously building access to the business and risk
decision-makers who can broaden the decision beyond developer preference.

Ask the champion: "Who in your organization is thinking about the vendor
selection from a business and risk perspective, not just the technical
implementation? I'd like to make sure they have what they need to feel
confident in the decision."

The technical thread keeps the rep inside the evaluation. The business thread
is the path to a competitive upset — because the engineering team's prototype
enthusiasm and the business buyer's concerns about vendor risk, migration cost,
and long-term TCO are often very different conversations.

**If no business decision-maker exists or is willing to engage:** This deal
is likely lost at this stage. Reassess whether continued investment is
warranted.

**Updated forecast implication:**
Move from active pipeline to "monitor or reassess." Do not commit field
resources to a feature comparison — it is the wrong battle. Escalate to
manager if the champion cannot provide access to a business decision-maker
within 5 business days.

**What the second pass found that the first pass couldn't:**
DataStax had run a second demo that the rep did not know about, and the
engineers had already started a trial. The Loop's Pass 1 diagnostic action
was exactly the right move — it revealed that competitive positioning was no
longer the primary lever before the team spent time producing the wrong
artifact. What became obsolete was the anticipated battle card, not the
diagnostic call that preceded it.

---

### DELTA

| Dimension | WITHOUT LOOP | LOOP PASS 1 | LOOP PASS 2 | What the feedback shift did |
|---|---|---|---|---|
| Risk diagnosis | "Competitive risk" | Competitive risk (developer preference motion) | Stakeholder risk — engineering is now a detractor | Feedback revealed the deal had moved further than CRM showed |
| Recommended action | "Build a battle card" | Diagnostic call first; Skill invoked only after motion is confirmed | Dual-thread: maintain technical engagement, open business decision-maker path | Loop sequences uncertainty-reducing actions before artifact generation |
| Competitive motion understood | No | Yes — developer preference, but unconfirmed | Yes — evaluation had already shifted past the competitive stage | Call revealed what the CRM could not: the trial had started |
| Deal viability | "Winnable if rep prepares" | Recoverable with right positioning | Likely lost unless executive path exists | Feedback surfaced the real deal status |
| Next action logic | Generic prep | Diagnostic call before Skill | Dual-thread technical and business decision strategy | Each pass produced a different action because the situation changed |

**Where feedback entered:** The champion call after Pass 1.
**What it shifted:** Risk type, deal viability assessment, recommended action, and resource allocation. The rep was about to spend time on a competitive battle card for a deal that had already moved past the competitive evaluation stage.

---

---

## Scenario 3: The Deal That Looked Healthy

**Deal context:**
- Account: Ironclad Manufacturing
- Stage 5 (Negotiation), close date August 8
- Deal value: $680K
- Legal redlines exchanged, CFO signed off, active engagement
- Loop Pass 1 classified this deal as: Healthy

---

### WITHOUT LOOP

**Prompt used:**
*"Ironclad Manufacturing is in Stage 5, $680K deal, legal redlines exchanged,
CFO approved. Close date August 8. Any risks?"*

**Output:**

This deal looks well-positioned. Legal is in progress, executive buy-in
confirmed. Key things to monitor:
- Ensure legal redlines are resolved quickly
- Confirm implementation timeline with the customer
- Lock down signing logistics ahead of August 8

Risk level: Low. On track to close.

---

**What is wrong with this output:**
- Takes CRM signals at face value with no evidence weighting
- Has no mechanism to incorporate new information from legal review
- "Low risk" is a point-in-time assessment with no update trigger
- A product gap surfacing in legal review would not change this output

---

### WITH LOOP — PASS 1

**Initial context provided:**
- Ironclad Manufacturing, Stage 5, $680K, August 8 close
- Legal redlines in progress, CFO signed off
- Strong engagement throughout evaluation
- No competitive pressure, no procurement delays flagged

**Loop diagnosis:**

Primary risk: **None currently identified — Healthy**
This deal has executive buy-in, legal in progress, and strong engagement.
All signals positive.

Observation: $680K deal in Stage 5 with 10 days to close. Legal redlines
exchanged but not resolved. At this deal size and stage, the primary risk
going forward is anything legal surfaces that was not anticipated in the
evaluation — product capability gaps, compliance requirements, data handling
terms. The Loop cannot assess this without seeing the redlines.

**Action (Pass 1):**
No field intervention needed. Monitor legal progress. Flag to the Loop
when legal review is complete or if any new requirements surface.

**Success signal:** Redlines resolved, contract signed by August 8.
**What would change the plan:** Any new technical, compliance, or
commercial requirement that emerges from the legal review.

---

### [FEEDBACK POINT — WHERE THE LOOP ENTERS]

**What the action revealed:**
Legal comes back with a new requirement: Ironclad's counsel has flagged
a data residency clause requiring all customer data to be stored within
the United States with quarterly third-party audit reports. The rep's
product team confirms this requirement is not fully supported in the
current product version. A workaround exists but is not documented and
has not been tested at scale.

---

### WITH LOOP — PASS 2

**What changed:**
A product capability gap has surfaced at Stage 5 on the highest-value deal
in the pipeline. This is the most dangerous risk type because it appears
late, when the customer has already committed emotionally and commercially,
and a "no" or a delay destroys trust rapidly.

**Updated primary risk: Technical risk — product gap in legal review**
The data residency requirement is a hard blocker. It cannot be managed
with messaging or competitive positioning. It requires a confirmed,
documented product answer before the next customer conversation.

**Updated action (Pass 2):**
Escalate to product and SA leadership today — not this week. Coordinate
the next response through legal, product, and solutions leadership. Do not
make a product or compliance commitment until the supported path is
documented in writing. The rep should not respond to the customer's legal
team unilaterally. The next customer communication needs to come from the
right people with the right answer on one of three paths:
1. The requirement is supported — here is the documentation
2. The requirement can be met via a confirmed workaround — here is the
   implementation plan and timeline
3. The requirement cannot currently be met — what is the product roadmap
   and what commercial accommodation can the company offer?

Do not let legal ping-pong continue while the product answer is unclear.
Each exchange without resolution erodes the customer's confidence.

**Updated forecast implication:**
Move from Commit to Best Case until the product question is resolved with
documented evidence. If the product team cannot confirm a path within 48
hours, notify the sales manager and move to Pipeline. A $680K deal closing
in 10 days with an unresolved product gap is not a Commit — it is a risk.

**What the second pass found that the first pass couldn't:**
The deal was genuinely healthy through evaluation. The risk only appeared
in legal review — which is precisely why the Loop needed a feedback trigger
for when legal surfaced something new, rather than simply classifying the
deal as "healthy" and closing the analysis.

---

### DELTA

| Dimension | WITHOUT LOOP | LOOP PASS 1 | LOOP PASS 2 | What the feedback shift did |
|---|---|---|---|---|
| Risk diagnosis | "Low risk, on track" | Healthy — monitor legal | Technical risk — product gap | Feedback revealed a risk that did not exist in the evaluation signals |
| Recommended action | "Lock down signing logistics" | Monitor, flag if legal surfaces something | Escalate cross-functionally today; coordinate next customer response, prevent unsupported commitments | Action went from passive to urgent in one feedback cycle |
| Forecast | "On track to close" | Commit — valid | Move to Best Case or Pipeline | Forecast changed from Commit to at-risk in one pass |
| Deal narrative | "Well-positioned" | Positive with one open watch item | Product gap in legal — highest urgency deal in portfolio | The healthiest-looking deal became the highest-urgency deal |
| Escalation | Not triggered | Not triggered | Triggered immediately | Without the feedback loop, escalation never happens — the deal closes as "lost in legal" with no intervention |

**Where feedback entered:** Legal review outcome — a requirement the CRM and prior conversations could not have surfaced.
**What it shifted:** Everything. A deal classified as Healthy became the highest-priority intervention in the pipeline based on a single piece of feedback the system was designed to watch for.

---

---

## Cross-Loop Pattern: What Feedback Does Every Time

These patterns appeared across all three scenarios:

| What changes between passes | What that means |
|---|---|
| **Risk type changes** | The first diagnosis was right for the information available — new evidence revealed a different underlying problem |
| **Action changes** | Pass 1 action was often the correct next step; feedback made Pass 2 possible by revealing what Pass 1 uncovered |
| **Forecast implication becomes specific** | Without feedback, forecast implications are hedged. With it, they are precise and actionable |
| **Deal status resolves** | Ambiguous deals (healthy? stalling?) get a real answer from feedback, not from analysis of static signals |
| **Escalation triggers correctly** | Without a feedback loop, escalation either never happens or happens too generically. With it, escalation is triggered by specific evidence |

---

## Key Insight for the Blog

The three scenarios each show a different type of feedback shift:

**Scenario 1:** Feedback resolved an ambiguous signal. The silence was not
disengagement — it was the champion managing an internal change. The Loop
needed the call to know that.

**Scenario 2:** Feedback made the initial recommended action obsolete. The
situation had already moved past where the action was useful. The Loop needed
the feedback to know it was now fighting the wrong battle.

**Scenario 3:** Feedback surfaced a risk that did not exist in the prior
signals. No amount of analysis of the evaluation-phase data would have
predicted a data residency requirement in legal review. The Loop was designed
to watch for exactly that moment.

Three different feedback types. Three different ways the plan changed.

The article claim this supports:
> **A GTM Skill makes an individual action context-specific. A GTM Loop
> connects those actions across time, preserves what has been learned, and
> changes the plan as the deal changes.**

And the cleaner one-line version:
> **The Skill contains the GTM judgment. The Loop owns the commercial journey.**
