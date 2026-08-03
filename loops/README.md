# GTM Loops

Four stateful GTM systems built on top of Claude. Each Loop preserves prior state,
infers analytical conclusions from new evidence, produces a decision or action
output, and evaluates whether that output actually worked.

> **Related article:** *From Skills to Loops: What Building Four Stateful GTM Systems Taught Me*
> → [Link to be added on publication]

---

## What Is a Loop?

Most AI-assisted GTM work is stateless. You supply context, get an output, and
start over next time. A Prompt answers the current request. A Skill applies
reusable domain logic. Neither one remembers what it believed last time, and
neither evaluates whether its prior output proved correct.

A Loop is designed around a different job: governing an evolving state over time.

![Prompt vs. Skill vs. Loop](https://raw.githubusercontent.com/kirti2215/gtm-toolkit/main/loops/assets/ChatGPT%20Image%20Aug%203%2C%202026%20at%2002_55_37%20PM%20(1).png)

The distinction that matters most is in **core reasoning**. A Prompt responds to
the situation. A Skill applies a repeatable workflow. A Loop asks: *does this new
evidence confirm or change what I previously believed?* That question requires
persistent state — and it's the question that recurring GTM decisions actually need
answered.

---

## The Four-Loop Evidence System

The four Loops are designed to work as a connected evidence system, each feeding
the next.

![The Four-Loop Evidence System](https://raw.githubusercontent.com/kirti2215/gtm-toolkit/main/loops/assets/ChatGPT%20Image%20Aug%203%2C%202026%20at%2002_55_41%20PM%20(10).png)

The flow is:

**Win/Loss Pattern Loop** → identifies the mechanisms behind past wins and losses.
Why did deals close or fail, by segment, motion, and competitive context?

**Pipeline Risk Loop** → takes those mechanisms and asks: is this mechanism active
right now in live opportunities? What is the primary risk in each deal, and what
is the one next action?

**Revenue Projection Loop** → aggregates pipeline, actuals, field judgment, and
initiative assumptions into a forward commercial range. What can the current engine
produce, and how did that change since the last run?

**Annual GTM Strategy and Goal Governance Loop** → governs whether the strategy
still supports the annual commitments. If projection falls short of target, what
decision is justified: Hold, Reinforce, Reallocate, Revise, or Escalate?

Decisions and outcomes from the Annual GTM Loop feed future evidence — closing the
learning cycle into the next year.

---

## How a Loop Thinks

Every Loop follows the same underlying process, regardless of which domain it
covers.

![How the Loop Thinks](https://raw.githubusercontent.com/kirti2215/gtm-toolkit/main/loops/assets/ChatGPT%20Image%20Aug%203%2C%202026%20at%2002_55_38%20PM%20(5).png)

The nine steps:

1. **Prior recorded state** — what the Loop last believed: the plan, the diagnosis,
   the projection, or the mechanism hypothesis
2. **New evidence and formal events** — what changed: actuals, pipeline, dates,
   calls, market signals, organizational decisions
3. **Evidence quality and timing assessment** — is this evidence strong enough to
   change the state, or is it a weak or immature signal?
4. **Does this confirm or change the state?** — the core inference step; the system
   does this, not the user
5. **Execution problem or strategy problem?** — separating a gap that better
   execution can close from one that requires a strategy change
6. **What options remain feasible?** — the decision set, gated by operational
   feasibility, not just plausibility
7. **Human decision and intervention** — the Loop produces options; a human
   decides and acts
8. **Did the intervention work?** — outcome evaluation against a documented
   baseline and expected signal
9. **Updated state** — the record that carries forward into the next run

A Loop is not repetition. It is a system that preserves what it believed,
interprets what changed, supports a decision, and learns from outcomes.

---

## The Annual GTM Loop — The Deepest Case

The Annual GTM Strategy and Goal Governance Loop is the most architecturally
complex of the four. It is also the one that required the most design iteration
before it worked.

### Why a target was not enough

The first version of the Loop tracked a single number: the annual target. It
showed variance and recommended a corrective action. That was insufficient because
a number being behind plan doesn't tell you whether to fix the team, the strategy,
or nothing at all.

![Why a Target Was Not Enough](https://raw.githubusercontent.com/kirti2215/gtm-toolkit/main/loops/assets/ChatGPT%20Image%20Aug%203%2C%202026%20at%2002_55_38%20PM%20(3).png)

The final state model runs from Commitment down through Strategic Bets, Assumptions
and Dependencies, Initiatives, Indicators, Evidence, to Decision. A bet underneath
a target can be redesigned, reallocated, or replaced. A target on its own can only
be missed.

### Users report facts. The Loop infers state.

An early design asked users to declare the system's state: select whether an
assumption is Held, Warning, or Invalidated; select whether the plan is in
Monitoring or Adaptation.

That was wrong. If the user has already concluded the plan is in crisis, the Loop
is just formatting a conclusion they already reached. That's not diagnosis.

![Users Report Facts. The Loop Infers State.](https://raw.githubusercontent.com/kirti2215/gtm-toolkit/main/loops/assets/ChatGPT%20Image%20Aug%203%2C%202026%20at%2002_55_38%20PM%20(4).png)

The redesigned input asks only for facts: what changed, what evidence supports it,
when did it happen, is the date confirmed or tentative, what organizational decision
was formally made. The Loop infers assumption status, operating mode, attainability,
and required transition. Users provide evidence and formal events. The Loop
performs the inference.

### When monitoring becomes adaptation

Not every warning should trigger action. But waiting too long can close the window
where action is still useful.

![When Monitoring Becomes Adaptation](https://raw.githubusercontent.com/kirti2215/gtm-toolkit/main/loops/assets/ChatGPT%20Image%20Aug%203%2C%202026%20at%2002_55_40%20PM%20(6).png)

The four levels:

- **Weak or immature signal** → Continue Monitoring
- **Mature warning + sufficient recovery window** → Monitor with explicit trigger
  and deadline
- **Warning + closing useful window** → Prepare Adaptation
- **Confirmed binary dependency miss beyond latest useful date** → Immediate
  Adaptation; no waiting for a second signal

A warning alone does not trigger Adaptation. A warning combined with a closing
decision window does. State transitions require timing-aware rules — not generic
red/yellow/green scoring.

### Three kinds of change — three separate records

For a while, all changes lived in one record. That meant a plan revision, the
Loop's change of assessment, and an intervention's result all looked identical.
The audit trail became meaningless.

![Three Kinds of Change](https://raw.githubusercontent.com/kirti2215/gtm-toolkit/main/loops/assets/ChatGPT%20Image%20Aug%203%2C%202026%20at%2002_55_40%20PM%20(7).png)

Three separate record types:

- **Version Ledger** — formal changes to the plan itself (commitment revised,
  bet parameters updated)
- **State Transition History** — changes in the Loop's own assessment (assumption
  moved from Held to Warning)
- **Intervention Evaluation Record** — what was tried and whether it worked
  (partner reallocation was partially effective)

Plan changed ≠ diagnosis changed ≠ intervention worked. Mixing any two corrupts
the audit trail in a way you won't notice until you need it.

### Plain review vs. the Annual GTM Loop

The same underlying fact — a product delivery slip — produces two very different
outputs.

![Plain Review vs. Annual GTM Loop](https://raw.githubusercontent.com/kirti2215/gtm-toolkit/main/loops/assets/ChatGPT%20Image%20Aug%203%2C%202026%20at%2002_55_40%20PM%20(8).png)

A plain review treats it as an execution delay and says to keep monitoring.
The Loop distinguishes the strategic thesis from current-horizon feasibility,
identifies the specific timing threshold, evaluates Hold alongside alternatives,
and moves the affected bet from Monitoring to Adaptation.

The window may already be closed. The Loop says so. A plain review doesn't know
the window exists.

### The six iterations that changed the architecture

![The Six Iterations That Changed the Architecture](https://raw.githubusercontent.com/kirti2215/gtm-toolkit/main/loops/assets/ChatGPT%20Image%20Aug%203%2C%202026%20at%2002_55_37%20PM%20(2).png)

| First design | What failed | What replaced it |
|---|---|---|
| Target tracking | Showed variance but not what failed | Commitment → Bet → Assumptions → Evidence → Decision |
| User-declared status | The user performed the diagnosis | Users report evidence; Loop infers state |
| Uniform warning logic | Either overreacted or acted too late | Mechanism- and timing-specific transitions |
| One combined history | Mixed diagnosis, plan changes, and results | Three separate record types |
| Plausible recommendations | Ignored operational feasibility | Feasibility-gated option set |
| Repeated recommendations | No evidence that anything was learned | Intervention and outcome evaluation |

---

## How to Use the Loops

![How a GTM Team Uses the Loop](https://raw.githubusercontent.com/kirti2215/gtm-toolkit/main/loops/assets/ChatGPT%20Image%20Aug%203%2C%202026%20at%2002_55_40%20PM%20(9).png)

**Step 1 — Initialize once (at fiscal year start or period start)**

Open the `input-template.md` for the relevant Loop and complete the initialization
module. For the Annual GTM Loop: commitments, strategic bets, assumptions,
dependencies, timing, capacity, thresholds, and guardrails. For the Revenue
Projection Loop: metric definition, recognition rules, model parameters, carryover
pipeline. For Win/Loss: the outcome dataset and initial mechanism hypotheses. For
Pipeline Risk: the opportunity and its prior diagnosis context.

Don't rush initialization. Everything downstream depends on the starting state
being real.

**Step 2 — Update each review (only what changed)**

At each recurring review, complete the Reforecast or Update module. Supply only
what changed: actuals, pipeline movement, dates, evidence, interventions deployed,
formal organizational decisions. You are not re-entering the entire plan — you are
reporting what the plan encountered.

**Step 3 — Run the loop-prompt**

Copy `loop-prompt.md` into Claude (or any capable LLM). Paste in your completed
input. The Loop returns: current state assessment, attainability or diagnosis,
operating mode or risk level, feasible options including Hold, evidence gaps, and
the updated records to carry into the next review.

**Step 4 — Start the next review from preserved state**

The Loop's output includes updated records. These become the prior state for the
next run. You are never starting from scratch. The goal is to focus each review
on what changed, not to reconstruct the entire plan from memory.

---

## Artifact Guide

Every Loop folder contains the same seven file types. Here is what each one is
for and when to use it.

### `LOOP.md` — Architecture Reference

The design specification for the Loop. Read this to understand the full
architecture: what state the Loop preserves, what transitions it recognizes, what
output it produces, what record types it maintains, and what it explicitly does not
do. Not a runnable prompt — a reference document.

**Read this first** if you want to understand why the Loop is designed the way
it is, or if you are evaluating whether it fits your use case.

### `loop-prompt.md` — Runnable System Prompt

The prompt you actually run. Copy this into Claude as the system prompt, then
supply your completed input template as the user message. The prompt contains
the full processing sequence, inference rules, output format, and prohibitions.

**Use this** when running the Loop against a real input. It is version-controlled —
if the architecture changes, this is where the change appears first.

### `input-template.md` — Structured Input Form

The form you fill in before each run. Organized into modules: an initialization
module (filled once at the start of the period) and a recurring update module
(filled at each review). Fields are labeled with what to supply and what evidence
standard applies.

**Copy and fill this in** before each run. The template tells you exactly what the
Loop needs and in what format. Incomplete or undifferentiated inputs produce weaker
outputs.

### `example-input.md` — Complete Worked Example Input

A fully completed input template using a consistent fictional scenario (Nexovane
for the GTM and Revenue loops; analogous fictionalized scenarios for Win/Loss and
Pipeline Risk). Every field is filled in with realistic commercial data, including
actuals, pipeline, evidence, overlays, dependencies, and capacity.

**Read this** to understand what a well-formed input looks like before writing your
own. The example is designed to exercise the Loop's full reasoning — not a minimal
or simplified case.

### `example-output.md` — Complete Worked Example Output

The full Loop output produced from the example input. Shows every section of the
output format: state assessment, attainability, diagnosis, operating mode, option
set, evidence gaps, record updates, and next review notes.

**Read this** to understand what to expect from a run, how the Loop reasons from
the evidence, and what a high-quality output contains. The before/after evals file
shows the contrast with a naive approach on the same situation.

### `[loop-name]-before-after-evals.md` — Before/After Evaluations

Four side-by-side evaluations comparing a naive approach to the same situation
against the Loop's output. Each evaluation shows the same underlying business
situation handled two ways, followed by a diagnosis of what the naive approach got
wrong and what the Loop added.

**Read this** to understand the practical difference the Loop makes — not in
abstract terms but in specific outputs on specific situations. Useful for explaining
the system to stakeholders or evaluating whether it's worth the initialization
investment.

### `reflection.md` — Design Reflection

A first-person account of how the Loop was designed: what failed, what was rebuilt,
and what each architectural decision is actually for. Not documentation — a design
journal.

**Read this** if you want to understand the reasoning behind the architecture, are
adapting the Loop for a different context, or are building something analogous and
want to learn from the design process rather than just the final output.

---

## Folder Structure

```
loops/
├── README.md                          ← You are here
│
├── gtm-annual-strategy-loop/
│   ├── LOOP.md
│   ├── loop-prompt.md
│   ├── input-template.md
│   ├── example-input.md
│   ├── example-output.md
│   ├── annual-strategy-before-after-evals.md
│   ├── reflection.md
│   └── README.md
│
├── gtm-pipeline-risk-loop/
│   ├── LOOP.md
│   ├── loop-prompt.md
│   ├── input-template.md
│   ├── example-input.md
│   ├── example-output.md
│   ├── pipeline-risk-before-after-evals.md
│   ├── reflection.md
│   └── README.md
│
├── gtm-revenue-projection-loop/
│   ├── LOOP.md
│   ├── loop-prompt.md
│   ├── input-template.md
│   ├── example-input.md
│   ├── example-output.md
│   ├── revenue-projection-before-after-evals.md
│   ├── reflection.md
│   └── README.md
│
├── gtm-winloss-pattern-loop/
│   ├── LOOP.md
│   ├── loop-prompt.md
│   ├── input-template.md
│   ├── example-input.md
│   ├── example-output.md
│   ├── winloss-before-after-evals.md
│   ├── reflection.md
│   └── README.md
│
└── assets/
    └── [11 visual diagrams referenced throughout this README]
```

---

## Which Loop to Start With

**If you want to understand the full architecture:** Start with `LOOP.md` in the
Annual GTM folder. It is the most complete and the one that required the most
design iteration. The others are simpler once this one makes sense.

**If you want to run something immediately:** Start with the Revenue Projection
Loop. The problem it solves (revenue forecasting is broken) is immediately
recognizable, the input template is straightforward, and the output is directly
useful at a monthly or quarterly review.

**If you want to understand how Win/Loss feeds everything downstream:** Start
with the Win/Loss Pattern Loop. It sits at the top of the evidence chain — its
mechanism findings affect conversion assumptions in the Projection Loop and
competitive handling in the Pipeline Risk Loop.

**If you are managing live deals:** Start with the Pipeline Risk Loop. It takes
the smallest update (new call notes, a stakeholder change, a legal update) and
produces a specific next action rather than a generic risk flag.

---

## How the Loops Were Evaluated

![How the Loops Were Evaluated](https://raw.githubusercontent.com/kirti2215/gtm-toolkit/main/loops/assets/ChatGPT%20Image%20Aug%203%2C%202026%20at%2002_55_41%20PM%20(11).png)

Each Loop was tested against eight criteria and mapped to the stakeholder it
serves.

**Eight tests:**

- **State continuity** — Did it preserve what was previously believed?
- **Inference quality** — Did it diagnose rather than repeat a user-provided label?
- **Transition discipline** — Did it change state at the correct threshold?
- **Evidence attribution** — Can every conclusion be traced to evidence?
- **Temporal realism** — Did timing and remaining windows affect the result?
- **Decision usefulness** — Did it produce a feasible next decision?
- **Learning integrity** — Can the prior decision be evaluated without rewriting
  history?
- **Authority discipline** — Did it stop before making a binding organizational
  decision?

**Stakeholder mapping:**

- **CRO / GTM leadership** → Execution problem or strategy failure?
- **RevOps** → Does forecast movement change commitment attainability?
- **Finance** → Which contribution is evidence-supported?
- **Product** → Has a dependency crossed its useful contribution date?
- **Regional leader** → Should the motion be reinforced, redesigned, or stopped?
- **Bet owner** → Has confidence diverged from the available evidence?

---

## What These Systems Are (and Are Not)

These are designed and tested prototypes, not production deployments.

They do not autonomously access CRM, financial, or product systems — someone
supplies the update each run. A real implementation would connect the state model
to live data sources. The architecture is designed with that wiring in mind; the
files here are the logic layer, not the infrastructure layer.

The example files use a consistent fictional universe (Nexovane, Luvexis, Korval
Advisory Partners, and a set of fictional accounts) built to demonstrate the full
reasoning of each Loop. They are not measured outcomes from a real enterprise.

The Loops do not make binding organizational decisions. Forecast category changes,
commitment revisions, resource reallocations, performance actions — all of these
are named explicitly with the evidence and the person who has to decide. The Loop
stops there.

---

## Fictional Scenario Consistency

All examples across the four Loops use a shared fictional universe for consistency:

- **Company:** Nexovane (compliance automation platform, financial services)
- **Competitor:** Luvexis
- **Partner:** Korval Advisory Partners
- **Accounts:** Alderix Capital, Telvax Investment Group, Cadrova Financial,
  Velstrom Asset Management, Vestrix Securities, Korvel Investments,
  Pelanthor Trust, Telvoran Capital, Pelantrix Advisors, Kessval Financial

Any resemblance to real organizations, people, or commercial outcomes is
coincidental. All deal values, win rates, market conditions, regulatory timelines,
and competitive dynamics are invented for demonstration purposes.

---

*Built with Claude. Architecture by KT.*
