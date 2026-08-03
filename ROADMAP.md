# GTM Toolkit — Roadmap

This toolkit packages GTM judgment into two types of systems: **Skills** for one-time
workflows and **Loops** for recurring commercial decisions. This document tracks what
is live, what is in progress, and where the toolkit is heading.

---

## Live

### Loops

Four stateful GTM systems. Each Loop preserves prior state, infers conclusions from
new evidence, produces a decision or action output, and evaluates whether that output
actually worked.

**Annual GTM Strategy and Goal Governance Loop**
Governs whether the annual strategy still supports the commitment. Infers operating
mode (Monitoring vs. Adaptation), evaluates interventions, and produces a
feasibility-gated option set including Hold at every decision point.

**Revenue Projection Loop**
Projects what the commercial engine is capable of producing — not what the target
requires. Separates model-based expectation, field judgment, and initiative-dependent
uplift. Explains why the projection changed. Identifies the conditions the target
requires. Calibrates every projection against actual outcomes at close.

**Pipeline Risk Loop**
Diagnoses the primary risk mechanism in a live opportunity. Determines whether new
evidence changes the mechanism or just confirms it. Produces one specific next action
rather than a generic risk flag. Evaluates whether that action resolved the risk.

**Win/Loss Pattern Loop**
Builds and maintains a mechanism hypothesis for why deals close or fail — by
segment, motion, and competitive context. Withholds a pattern finding until the
mechanism is supported, not merely observed. Evaluates whether interventions changed
outcomes in the next deal cohort.

---

### Skills

Reusable one-time workflow prompts. Each diagnoses the business context before
generating content.

**Competitive Battle Card**
Handles developer preference, procurement leverage, and incumbent displacement
scenarios to produce account-specific battle cards, objection handling, and deal
strategy.

**Product Launch Planner**
Identifies the "why now" before building a launch package. Produces a launch
strategy brief, narrative, buyer personas, messaging framework, seller and technical
enablement, objection handling, and launch-readiness checklist.

**Sales Enablement**
Builds account-specific materials for enterprise opportunities. Produces buyer-specific
value propositions, discovery questions, pitch points, objection handling, business
cases with assumptions clearly labeled, and recommended next steps.

---

## In Progress

**Launch Readiness Skill**
Evaluates whether a product, team, and market motion are actually ready for launch —
not just whether the date has arrived. Produces a readiness assessment by dimension
(product, field, market, partner, comms) with explicit gap identification and a
recommended launch vs. delay recommendation.

**Renewal and Expansion Brief**
Diagnoses why an account is at risk — or ready to expand — before producing a
renewal or growth strategy. Key question: what has changed in this account since
the customer bought?

**Pipeline Review Brief**
Helps sales leaders and account teams evaluate deal health across an opportunity
pipeline. Key question: which deals have the conditions to close, and which are
stalled for a fixable reason?

---

## Considering

**Analyst and Press Briefing Prep**
Builds structured briefing materials for analyst and media conversations. Encodes
narrative sequencing, supporting evidence, anticipated questions, and topics to
avoid.

**Partner GTM Brief**
Builds a joint go-to-market plan for a partner opportunity. Encodes the combined
value proposition, partner responsibilities, field motion, and success criteria.

**QBR Preparation Brief**
Structures a quarterly business review for a named account or territory. Separates
what went to plan, what didn't, root cause by category, and what is committed for
the next quarter.

**Territory and Segment Planning Loop**
A recurring Loop for how a territory or segment is performing against its coverage
model — pipeline generation, conversion, and expansion — with operating mode
inference and intervention tracking across the year.

---

## Where This Is Heading

The Skills layer packages repeatable GTM judgment into structured workflows. The
Loops layer adds stateful reasoning — systems that remember what they previously
believed, interpret what changed, support a decision, and evaluate whether it worked.

The next layer is production deployment: connecting the Loop state model directly
to CRM, financial, and product systems so that the update arrives automatically
rather than through a structured input form. The architecture is already designed
for this. The files in this repository are the logic layer. The infrastructure
layer — storage, orchestration, and live data access — is what makes them fully
autonomous operating systems.

That is the direction this toolkit is built toward.
