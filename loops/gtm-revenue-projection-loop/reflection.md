# From Forecasting a Number to Governing Projection Integrity

*A first-person reflection on the design of the Revenue Projection Loop*

---

I approached the Revenue Projection Loop differently from the Annual GTM Strategy
and Goal Governance Loop.

By the time I began this work, I had already spent significant time defining the
deeper principles behind the broader GTM Loop system. I had worked through what
distinguishes a Loop from a one-time Skill, where the user's responsibility should
end and the system's analytical responsibility should begin, why state must persist
across runs, why evidence and judgment must remain distinguishable, and why a system
that does not evaluate its own prior outputs is not truly learning.

Because those foundations were already established, I did not need to rediscover
the philosophy from scratch.

The Revenue Projection Loop could move faster.

But moving faster did not mean simply producing a forecasting template. In some ways,
the familiarity of the problem made the design riskier. Revenue forecasting is a
process most companies already perform. There are established dashboards, CRM forecast
categories, stage-weighted models, manager calls, Finance forecasts, and rep commits.
It would have been easy to reproduce those existing practices in a cleaner format and
call it a Loop.

The real design question was:

*What is missing from the way revenue projections are normally produced and used?*

The answer was not another number.

It was projection integrity.

---

## The initial question: what does a field leader actually need?

The starting point was practical rather than theoretical.

I wanted to understand what a GTM or field leader actually knows, what information
they can credibly provide, and what they need in return.

A field leader is often asked:

- What are you committing to?
- How much will close this quarter?
- Is the annual target still achievable?
- Which deals are real?
- How much additional pipeline do you need?
- Can the team absorb more pipeline?
- What changed since the last forecast?
- Why should Finance believe the number?

Yet the field leader does not own the entire projection system.

They may know more than the CRM about the commercial reality behind an opportunity.
They know whether the buyer is genuinely engaged, whether procurement has begun,
whether a champion has authority, whether a product dependency is likely to slip,
whether a competitor has become the preferred vendor, whether a rep is overloaded,
or whether a customer deadline creates unusual urgency.

But they may not own:

- the historical conversion model;
- stage-to-stage progression data;
- slippage and push-rate history;
- pipeline-generation trends;
- forecast bias analysis;
- official recognition rules;
- or the source-of-record actuals.

RevOps and Finance own much of that evidence.

This meant the Loop could not be designed for a single isolated user. Its natural
operating unit became the Field Leader–RevOps pair, supported by Finance and GTM
Strategy.

RevOps supplies the quantitative commercial baseline. The field supplies
evidence-backed context that the system cannot observe. Finance defines what
officially counts. GTM Strategy provides the assumptions behind approved incremental
initiatives.

The Loop reconciles these inputs without pretending that one of them represents the
entire truth.

That became one of the most important distinctions in the design.

---

## The first major principle: project the engine first

The central idea behind the Loop is simple:

Project what the commercial engine can produce first. Compare it with the target
second.

This ordering matters because many commercial forecasts begin with the target.

Leadership sets a number. RevOps calculates the pipeline coverage required to reach
it. Initiative contributions are added. Stage weights are adjusted. Future pipeline
is assumed. A new campaign, product launch, or partner motion is positioned as the
source of the remaining gap.

Eventually the numbers are made to balance.

But that is not a projection. It is a target-justification exercise.

The Loop reverses the sequence.

It begins with:

- actual contribution already recognized;
- current pipeline;
- evidence-based conversion;
- cycle timing;
- remaining time;
- slippage;
- historical pipeline generation;
- future creation vintages;
- approved initiatives;
- field evidence;
- and capacity.

Only after the commercial engine has been projected does the target enter the
analysis.

The difference is subtle but consequential.

A target of $12 million does not cause the engine to produce $12 million. It simply
creates a comparison point.

If the engine supports $8 million, the result should be an explicit $4 million
unsupported gap — not a model whose assumptions have been stretched until the gap
disappears.

This became the governing rule of the entire Loop and the main distinction between
a credible projection and a plan that has been reverse-engineered to look achievable.

---

## The metric itself is a design parameter

Before the engine can be projected, the metric must be defined precisely.

This sounds obvious. It is routinely skipped.

"Revenue" can mean recognized revenue at cash collection, annual recurring revenue
at contract execution, net new ARR excluding renewals and expansions, bookings by
signature date, or billings at invoice. These are not the same number. They do not
move in the same direction at the same time. They do not respond to the same
commercial activities.

A projection built on the wrong metric definition will be compared against an actual
result measured on a different basis. The resulting accuracy analysis is meaningless.

The Loop therefore requires explicit definition at initialization:

- What is being projected — the specific commercial metric by name;
- What is included — contract types, segments, ACV thresholds, motion sources;
- What is excluded — renewals, expansions, SMB tier, non-standard deals;
- When contribution is recognized — contract execution, invoice, cash, or another
  defined event;
- Where the source of record lives — which system, which team confirms it.

This also means the Loop does not assume it is a revenue Loop.

The same architecture applies to new bookings, pipeline creation, customer count,
or any other commercial metric with a forward projection and an annual target. The
engine-first principle, the projection bridge, the three views, and the calibration
structure all transfer. Only the metric, recognition rules, and conversion assumptions
change.

Making the metric configurable rather than assumed prevents the Loop from being
applied to the wrong thing without anyone noticing.

---

## The projection bridge became the core analytical object

The Annual GTM Loop had strategic bets, assumptions, interventions, health
dimensions, and operating modes.

The Revenue Projection Loop needed a much narrower backbone.

Its central object became the projection bridge:

- Recognized actuals
- Expected contribution from current pipeline
- Expected contribution from pipeline not yet created
- Approved-initiative uplift
- Evidence-backed field overlays
- Capacity effects
- Timing and slippage
- Overlap and duplication
- Projected range
- Gap to target

This bridge matters because a projection number without source attribution tells
leadership very little.

Two projections can both show $18 million and have completely different risk
profiles.

One may consist of:

- $12 million recognized actuals;
- $4 million in late-stage pipeline;
- and $2 million in future generation.

The other may consist of:

- $5 million recognized actuals;
- $3 million in current pipeline;
- $6 million in pipeline that does not yet exist;
- and $4 million of unproven initiative uplift.

The headline number is the same. The evidentiary quality is not.

The projection bridge makes the composition visible.

It forces the system to answer:

- What has already happened?
- What is supported by current commercial inventory?
- What depends on future engine performance?
- What depends on a new initiative?
- What depends on field judgment?
- What is constrained by time or capacity?
- What has no current source?

That source-level visibility is more valuable than the final number alone.

---

## Confidence is labeled per source, not only in aggregate

The bridge produces a range. But a range without composition is still incomplete.

A projection of $9M–$10M built primarily from recognized actuals and late-stage
procurement-active pipeline is not the same commercial risk as $9M–$10M built
from early-stage pipeline and an unproved initiative — even when the total is
identical.

The Loop labels confidence at the source level in every Projection Run output,
using a defined ladder:

- **Certain** — recognized actuals; already closed and recorded at the source of
  record
- **High** — late-stage pipeline where the economic buyer is confirmed, procurement
  is active, and the deal is within its typical remaining cycle
- **Medium** — mid-stage pipeline progressing with sufficient remaining time and no
  blocking dependency
- **Low** — early-stage pipeline requiring multiple progressions and with marginal
  remaining time
- **Medium-Low** — future pipeline from the existing engine, not yet created
- **Low to Medium** — initiative-dependent uplift from a motion that has not yet
  proved itself

Field overlays with documentary evidence adjust the model-level confidence up or
down. Field overrides without evidence are not accepted.

Then the output reports the **confidence composition** of the total:

How much comes from Certain sources? How much from High? How much depends on
Medium-Low or initiative-dependent contribution?

A projection of $9.1M composed 60% of recognized actuals and 10% High-confidence
pipeline is a fundamentally different commercial situation from a projection of
$9.1M composed 65% of future pipeline and initiative uplift — even if the headline
number is the same.

Reporting composition rather than only the total prevents the range from being used
as false confidence. It makes the real uncertainty visible.

---

## The most important design choice: separate the three views

The strongest design decision in the Loop was preserving three projection views:

1. Model-only projection
2. Field-adjusted projection
3. Official operating forecast or commit

These numbers are often blended in real operating processes.

A CRM model produces one number. Managers adjust deals. Leadership applies judgment.
Finance chooses an operating forecast. By the time the number appears in a QBR,
no one can reliably determine which part came from the model, which came from the
field, and which came from leadership's risk appetite.

That makes later learning almost impossible.

If the final forecast was wrong, what failed? The model? The data? The rep
judgment? The regional leader's override? The official commitment? Or an event
that occurred after the forecast?

The three-view structure preserves those distinctions.

**Model-only projection** — the evidence baseline: actuals, pipeline, historical
behavior, timing, generation, capacity, and initiative assumptions without
subjective field overlays.

**Field-adjusted projection** — the model-only view plus specific evidence-backed
commercial judgment. The original model value remains visible alongside the
adjustment. The model is not overwritten.

**Official operating forecast** — the number formally adopted by leadership, RevOps,
or Finance. The Loop records it if supplied. It does not calculate it. It does not
substitute the field-adjusted view when the official commit is absent.

This design respects the fact that models and people each know different things.

The model provides consistency and historical discipline. The field sees context not
encoded in the CRM. Leadership may consciously choose a more conservative or
aggressive operating number.

The Loop does not eliminate those differences. It makes them visible and measurable.

At close, all three are compared against actual outcomes independently. This is
what allows the organization to distinguish model error, field judgment quality,
and organizational forecast bias from one another.

---

## Field judgment had to become evidence, not opinion

My GTM experience shaped this part of the design directly.

A purely analytical forecasting system can easily become dismissive of field
judgment. It may assume the model is objective and the field is biased.

That is not commercially realistic.

A field leader may know that a statistically ordinary deal has already received
board approval, completed security review, and entered final redlines against a
fixed buyer deadline. The historical stage rate may understate that opportunity.

The reverse is also true. A rep may call a deal highly likely because the buyer
is friendly, while procurement has not begun, the economic buyer is absent, and a
competitor is preferred.

The answer was not to choose between model and field. It was to turn field judgment
into a structured, testable object: the **Field Overlay Record**.

Each overlay preserves:

- the opportunity, cohort, or territory affected;
- the direction and dollar amount of the adjustment;
- the owner;
- the date;
- the model value before the adjustment;
- the field-adjusted value;
- the supporting evidence;
- the reasoning;
- and the expiration or review date.

"This deal feels strong" is not accepted.

"Procurement approved, legal redlines exchanged, buyer deadline confirmed, and CFO
authority documented" is evidence.

Most importantly, every overlay is compared with the actual outcome at close.

This changes field judgment from an informal political input into a measurable
source of forecast information. Over time, the organization can learn which leaders
consistently improve model accuracy, which types of evidence are genuinely
predictive, where field judgment catches risks before the data does, and where
optimism systematically inflates the forecast.

That is a much more useful relationship between human judgment and quantitative
modeling than either blindly trusting the field or blindly trusting the system.

---

## Three supporting records serve three separate purposes

The Loop produces three record types. This matters because mixing them corrupts
the audit trail in ways that are difficult to detect until after something has gone
wrong.

**Field Overlay Record** — documents individual field judgments that adjust the
model-only projection. One record per overlay per run. Each is preserved and
compared against the actual deal outcome at close. This is how the organization
learns whether field judgment adds or removes forecast accuracy.

**Projection Version Ledger** — documents changes to model parameters: conversion
rates, cycle lengths, generation rates, ACV estimates, capacity assumptions,
seasonality factors, initiative ramp assumptions. Every parameter revision requires
a Ledger entry: original value, revised value, revision date, evidence justifying
the change, and which prior Projection Runs were calculated under the old parameters.
Prior runs are annotated, not rewritten.

**Calibration Record** — produced at period close. Compares every prior Projection
Run against verified actual outcomes. Records model-only accuracy, field-adjusted
accuracy, official forecast accuracy, and parameter-level accuracy by source.

These three records must be kept separate because they track different things:
Field Overlays track whether individual human judgments were correct. The Version
Ledger tracks whether the model assumptions changed and why. The Calibration Record
evaluates whether the projection system as a whole — model plus field plus official
commit — is learning.

If Field Overlay entries were logged inside the Projection Version Ledger, a
parameter revision and a one-time human judgment adjustment would look identical.
If calibration findings were folded into overlay records, it would be impossible to
separate deal-level accuracy from model-level accuracy.

Each record type exists because the question it answers cannot be answered by either
of the other two.

---

## Future pipeline required a different mental model

Another important design shift came from pipeline that does not yet exist.

At the beginning of a year — or even midway through it — a meaningful portion of
the eventual result may come from pipeline that has not yet been created.

A simplistic model may take the expected annual pipeline-generation rate, multiply
it by a conversion rate, and treat the entire pool as current-year contribution.

That ignores time.

Pipeline created in February does not have the same probability of closing within
the fiscal year as pipeline created in November.

The Loop therefore models future pipeline by **creation vintage**. For every month
or quarter, it asks:

- How much pipeline is likely to be created?
- What percentage will qualify?
- How much time will remain after creation?
- What conversion rate applies with that remaining window?
- What cycle time is required?
- Is capacity available?
- What ACV is expected?
- How much belongs in the current period?
- How much becomes next-period carryover?

This led to the **latest useful pipeline creation date**: the point after which
newly created pipeline can no longer reasonably progress, close, and be recognized
within the target period.

That date makes timing operational.

A leader may say: we need another $10 million in pipeline.

The Loop asks: by when?

Pipeline created after the useful date may still be strategically valuable, but it
cannot be used to justify the current-period revenue target. This protects the
forecast from one of the most common forms of false comfort: treating future
pipeline generation as though time does not exist.

---

## Capacity could not remain a generic deduction

Capacity is often handled poorly in forecast models.

A model may calculate the expected number of wins and then subtract a generic
capacity adjustment at the bottom. But different capacity constraints affect
different parts of the commercial engine.

- SDR capacity affects pipeline generation.
- AE capacity affects progression and deal concurrency.
- Solutions-engineering capacity affects technical evaluation.
- Security and legal capacity affect timing.
- Implementation capacity may determine when revenue is recognizable.
- Customer-success capacity may affect retention or expansion.

A delivery constraint should not reduce pipeline generation. A rep constraint
should not be treated as an implementation deduction.

The Loop therefore attaches each capacity constraint to the source and stage it
affects. It asks:

- What is constrained?
- In which period?
- At what point in the commercial process?
- Does the constraint affect generation, conversion, timing, or recognition?
- What is the estimated dollar impact?

This makes the projection more operationally useful because it reveals where the
commercial engine is actually binding. It also prevents a misleading scenario in
which the model projects more wins than the organization can onboard, recognize,
or support.

---

## Scenarios had to remain honest — and the lower bound is not a floor

The Loop produces four scenarios:

- Evidence-supported lower bound
- Base projection
- Recovery or upside case
- Best credible ceiling

The scenarios are not arbitrary optimism levels. Each names the conditions it
depends on and checks those conditions for joint feasibility.

But the **evidence-supported lower bound** deserves its own discussion, because it
is often misread.

The lower bound is what the evidence actually supports: recognized actuals plus
the highest-confidence remaining pipeline only. No model conversion applied to
early-stage accounts. No future creation assumptions. No initiative uplift. No
field overlays.

It is not a committed floor. It is not a sandbagged conservative number designed
to set expectations low and beat them. It is the literal evidence-based minimum —
the number that only requires the highest-confidence deals to close as documented.

This distinction matters because organizations sometimes resist reporting this
number honestly. It can feel aggressive to show leadership that the evidence-backed
minimum is well below the official forecast. But that distance is information.

A projection of $9.1M base with a $7.8M evidence-supported lower bound tells the
organization:
- The base requires model-rate conversion across multiple mid-stage accounts;
- The lower bound requires only current late-stage pipeline to perform;
- The spread of $1.3M represents the risk in mid-stage conversion.

That is operationally useful. A committed-floor dressed up to be more palatable
is not.

The **best credible ceiling** carries the complementary constraint. It is bounded by
what is both individually plausible and jointly feasible — not by adding every
optimistic assumption regardless of shared dependencies.

Forecasting systems often produce an "upside case" by stacking favorable conditions:
all major deals close, win rate improves, cycle time shortens, deal size rises, the
initiative ramps early, capacity remains available. Each condition may be possible
in isolation. Together, they may share the same implementation team, the same reps,
the same delivery slots.

The Loop tests joint feasibility. When the theoretical all-favorable ceiling
materially exceeds the best credible ceiling, both are shown with an explicit
explanation of why they diverge. This keeps scenario planning from becoming another
way of hiding the gap under a label.

---

## False precision became an explicit design concern

Forecasting encourages numerical confidence.

A model produces percentages, weighted values, ranges, and often labels such as P50
or P75. Those labels can create an impression of statistical rigor even when the
organization has too little data to support them.

The sparse-data handling made this issue explicit.

If a company has three closed deals and two Stage 3 observations in the current
period, it does not have a newly calibrated probability distribution. The Loop
therefore refuses to treat limited data as precision.

When evidence is sparse, it:

- preserves the prior model version;
- states that current evidence is insufficient to revise it;
- widens the range;
- reports the confidence composition;
- names the limitations explicitly;
- and avoids probabilistic labels that the model has not earned.

Missing evidence does not cause the system to fabricate certainty. It causes the
range to remain wider.

This is important for smaller companies or newer motions that may not have enough
historical data for sophisticated cohort models. The Loop should still be useful.
It can use simple stage averages when necessary, provided it clearly states the
limitation. Sophistication comes from honesty about evidence quality — not from
using more mathematical language than the data can support.

---

## The movement bridge made the projection useful in operating reviews

A projection number matters, but a changing projection is often more important.

If last month's base projection was $10.4 million and this month's is $9.1 million,
leadership needs to know why.

The **projection movement bridge** decomposes that change into attributable drivers:

- actuals revision;
- pipeline added;
- pipeline removed;
- stage progression;
- slippage;
- model parameter revision;
- capacity change;
- initiative change;
- field overlay added or removed;
- or data-quality correction.

This answers a question that is frequently obscured in forecast conversations:

*Did the commercial reality change, or did someone change the model?*

A projection can move because a major opportunity slipped, conversion evidence
deteriorated, more pipeline was created, the sales cycle lengthened, a field overlay
expired, or RevOps revised a historical assumption. Those events should not be
blended.

The movement bridge creates a narrative that is both quantitative and operational:

*The projection fell by $1.3 million. $0.8 million came from three deals moving into
the next period. $0.6 million came from a conversion-rate revision. New partner
pipeline added $0.4 million. A capacity constraint removed $0.5 million.*

This is the kind of output that can actually improve a forecast call. It gives
leadership something more useful than "the number is down." It explains the system
movement.

---

## Required conditions created the boundary between projection and strategy

The Loop needed to be actionable without becoming another strategy system.

The solution was the required-conditions analysis.

When the target is above the projection, the Loop identifies what would mathematically
need to be true:

- how much qualified pipeline must be created;
- by what date;
- what conversion rate must hold;
- what cycle time is required;
- how quickly an initiative must ramp;
- what ACV is necessary;
- and which capacity constraint must be resolved.

It then classifies each condition:

- Supported by current evidence
- Plausible but unconfirmed
- No current evidence basis

This is not a recommendation.

The Loop may say: to reach $20 million, the organization needs $12 million in
qualified pipeline created by June 15, a 28% win rate, median cycle below 95 days,
and the partner initiative producing by May. It does not say: enter healthcare,
hire eight reps, or launch a new partner channel.

Those are strategic choices.

The Revenue Projection Loop states what the current target requires. The Annual
GTM Strategy and Goal Governance Loop decides what to change in response.

This boundary prevents the systems from duplicating one another. It also prevents
the Projection Loop from generating strategy recommendations disguised as
mathematical requirements.

---

## The Projection Run became the primary state object

The Loop needed memory, but not the multidimensional state model of the Annual GTM
Loop.

Its primary state object became the **Projection Run**.

Every run preserves:

- version ID;
- as-of date;
- data snapshot date;
- metric and horizon;
- pipeline population;
- model version;
- historical parameters in use;
- initiative assumptions;
- field overlays;
- three projection views;
- scenario ranges;
- latest useful creation date;
- and evidence limitations.

A new run never overwrites the previous one.

This is essential because CRM data is not static. Opportunities change stage, values
are edited, close dates move, and outcomes become known. If the organization later
evaluates a prior forecast using the updated CRM record rather than the data visible
at the time, it can create artificial forecast accuracy.

The Loop freezes what was actually known. On August 2, this opportunity was in
Stage 3, had been there 28 days, had no procurement started, and carried a
particular model value. At close, the organization compares the actual result with
that historical snapshot — not with a retroactively cleaned record.

This makes the projection history trustworthy.

---

## Calibration transformed a forecast process into a Loop

The most important difference between this system and an ordinary forecast template
appears at period close.

Without calibration, the process resets. The team explains what happened, updates
the win rate, changes the cycle assumption, and starts again next year. But the
organization does not know:

- which projection run was most accurate;
- whether the model improved during the year;
- whether field overlays helped;
- whether leadership's official commit was systematically optimistic;
- which conversion assumptions failed;
- whether pipeline generation was modeled correctly;
- which initiative ramp assumptions were wrong;
- and when the error became observable.

The Close and Calibrate stage compares every prior Projection Run against actual
outcomes.

It evaluates:

- model-only projection accuracy;
- field-adjusted accuracy;
- official forecast accuracy;
- source-level accuracy;
- conversion assumed versus realized;
- cycle assumed versus realized;
- generation assumed versus realized;
- field overlay performance per overlay;
- initiative performance versus stated range;
- and bias by team, region, segment, manager, and forecast category.

This changes the question from *why did we miss?* to *what did each version of the
projection believe, which component created the error, and what should the model
learn?*

Model updates are then recorded in the Projection Version Ledger.

The original parameter is preserved. The revised value is recorded with the evidence
that justified it. Prior runs remain associated with the model version that produced
them.

This reflects the same principle that became central in the Annual GTM Loop: the
system may learn, but it may not rewrite what it previously believed.

Without this, a model can always make itself look accurate by adjusting its
assumptions after the result is known. That is not calibration. It is hindsight.

---

## What makes this Loop useful for actual GTM teams

The Loop is not only for data scientists or forecasting specialists. It supports
several real commercial workflows.

**Annual target setting.** Before leadership commits to a target, RevOps can project
the existing commercial engine plus approved initiatives. The output may show an
existing-engine projection of $16–18 million, a leadership target of $24 million,
and an unsupported gap of $6–8 million. That does not automatically mean the target
is wrong. It means the strategic gap is visible before the commitment is finalized.

**Monthly and quarterly forecast reviews.** The team can see where the projection
currently stands, what changed since the prior review, which sources carry the most
uncertainty, how field judgment changed the model, and what must happen next.

**Field and Finance reconciliation.** Instead of debating one blended number, the
conversation becomes: the model says $9.1 million, the field overlays add $0.1
million net, leadership has not yet set an official commit, the largest uncertainty
is initiative ramp, and the latest useful date for new direct pipeline is October 16.
That is a much more disciplined conversation than arguing over a single number.

**Capacity and hiring discussions.** A rep hired in August may increase next-year
pipeline but is unlikely to materially affect current-year recognized revenue after
hiring, ramp, creation, and conversion time are included. The Loop makes timing
explicit so that capacity decisions are grounded in realistic contribution windows.

**Initiative evaluation.** The system shows initiative-dependent uplift separately
from the base engine. This prevents an unproved partner motion or product launch
from being treated as though it were part of the established revenue model.

**Forecast-bias analysis.** Over time, the organization can understand which teams
commit conservatively, which are consistently optimistic, where field overlays add
value, and which forecast categories are poorly calibrated. This is useful
operational learning, not just reporting.

---

## How my GTM experience shaped the design

My contribution to this system was not simply knowing that a forecast should use
pipeline, conversion rates, and sales cycles. Those mechanics are widely understood.

The GTM lens mattered in recognizing where the formal data is incomplete and where
human context is genuinely valuable.

A field person knows things the model may not:

- an economic buyer is present but not documented;
- the buyer has an external deadline;
- a competitor is preferred despite the opportunity stage;
- the account has approved procurement;
- the champion has lost influence;
- a partner referral is lower quality than its stage suggests;
- a rep is carrying too many complex evaluations;
- a territory is saturated;
- or a product dependency is weakening an entire cohort.

The solution was not to replace that judgment with a generic model. It was to make
the judgment explicit, attributable, evidence-backed, and measurable.

That is where the design uses GTM experience rather than merely forecasting theory.

A technically elegant model may produce a number. A commercially useful Loop must
understand why people in the field may disagree with it, what evidence would justify
that disagreement, and whether those disagreements proved useful over time.

---

## How this Loop fits into the broader GTM system

The Revenue Projection Loop occupies a clear middle layer.

**Win/Loss Pattern Loop** explains the mechanisms behind historical wins and losses.
Its findings may justify different conversion assumptions for particular segments,
motions, or competitive contexts — specifically, conditional cohort conversion rates
by competitive status, segment, and motion.

**Pipeline Risk Loop** diagnoses which current opportunities and cohorts are fragile
and why. Its findings adjust how much confidence current pipeline should carry in
the projection bridge.

**Revenue Projection Loop** aggregates actuals, current pipeline, future generation,
initiatives, capacity, timing, and field evidence into a forward commercial range.
It explains the gap and the required conditions.

**Annual GTM Strategy and Goal Governance Loop** decides whether that projected
capability still supports the annual commitments and what strategic or portfolio
decision should follow.

The clean system flow: Win/Loss explains historical mechanisms. Pipeline Risk
diagnoses live commercial fragility. Revenue Projection estimates what the engine
will produce. Annual GTM Strategy decides what the organization should change.

Keeping these boundaries clean prevents each Loop from becoming a generic
business-analysis system that duplicates every other.

---

## Why this Loop was simpler to build

The Revenue Projection Loop was materially less complex than the Annual GTM Loop.

That was not because revenue projection is trivial. It was because the previous work
had already established the design fundamentals:

- evidence in, analysis out;
- preserve historical state;
- separate human judgment from system inference;
- version changes;
- do not invent precision;
- model timing and capacity;
- maintain clean system boundaries;
- evaluate prior outputs;
- and carry learning into the next cycle.

I did not need to challenge every foundational choice again. Instead, I could ask:
*What is the smallest architecture that preserves these principles for a
revenue-projection problem?*

The result was one primary state object, three projection views, three lifecycle
stages, a movement bridge, a calibration loop, and a small set of supporting
records.

This was an important design lesson in itself. Not every Loop needs the same
complexity. The goal is not to reuse the Annual GTM architecture everywhere. The
goal is to reuse the reasoning principles and build only the state and governance
structure the specific decision requires.

---

## What I learned from building it

The first lesson was that a projection is not a number. It is a set of claims about
current commercial inventory, future pipeline generation, conversion, timing, deal
size, capacity, initiatives, and field judgment. A forecast is credible only when
those claims remain visible.

The second lesson was that human judgment should neither be hidden inside the model
nor excluded from it. It should exist beside the model, with evidence and
accountability.

The third lesson was that forecast accuracy cannot be evaluated retrospectively
without immutable snapshots. Once the CRM has been updated, the organization no
longer sees what it genuinely knew at the time.

The fourth lesson was that projection quality is not only measured by how close
the final number was. A projection range may correctly express uncertainty even if
its midpoint is not exact. A model may be directionally right but miss an
initiative's upside. A field adjustment may improve one deal's estimate and reduce
overall accuracy elsewhere. An official forecast may knowingly sit above the
evidence. The Loop needs to preserve those distinctions.

The fifth lesson was that annual target setting should begin with commercial
capability, not leadership aspiration. Leadership may choose to set a target above
the evidence-backed projection. But it should know the size and nature of the gap.
A stretch target is a leadership choice. An unsupported projection presented as
though it were evidence is a modeling failure.

---

## What the Revenue Projection Loop has become

What began as a relatively simple idea — use historical context to project revenue —
became a system for separating commercial evidence, field judgment, organizational
commitment, and learning.

Its purpose is not to eliminate forecasting judgment. It is to make that judgment
transparent.

It is not designed to guarantee a correct number. It is designed to make the
projection explainable, versioned, comparable, and capable of improving.

It tells the organization:

- what the engine is currently capable of producing;
- which sources support that view and at what confidence;
- what remains uncertain and where the range is widest;
- how field judgment changes the model — and whether it helps;
- what leadership has formally committed to;
- what conditions the target requires;
- what changed since the prior run and why;
- and what the prior projection got wrong.

Most commercial forecast processes ask:

*What is the number?*

This Loop asks a more useful set of questions:

*What produces the number? What part of it is evidence? What part is judgment? What
part is aspiration? What changed? What would have to be true for the target to hold?
And when the period closes, what did we learn?*

That is what makes it a Loop.

---

*This version serves as the full design journey. A shorter version for the
repository README can be extracted from the principle headings.*
