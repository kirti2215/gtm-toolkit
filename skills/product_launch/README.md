#Details about Product launch skill
# Product Launch Planner Skill

A structured AI workflow for building launch packages that field teams can actually use.

Unlike a generic launch-plan or messaging generator, this Skill starts by diagnosing why the launch matters now, which buyer pressures make it relevant, and what is changing in the market before producing any content.

## Contents

- **SKILL.md** — Core workflow, decision logic, output structure, and guardrails
- **input-template.md** — Structured template for capturing launch context
- **example-input.md** — Fictional enterprise AI platform launch for financial services in Southeast Asia
- **example-output.md** — Complete launch package generated from the example scenario

## How to Use

1. Load **SKILL.md** into Claude as an Agent Skill, or paste it into a conversation.
2. Complete **input-template.md** with your launch context.
3. Run the Skill using the completed input.
4. The Skill identifies the launch’s “why now” before developing messaging or enablement materials.

If the timing trigger, buyer context, or market rationale is missing, it flags the gap rather than producing a generic launch plan.

## What the Skill Produces

- Launch strategy brief
- Launch narrative
- Buyer personas with goals, pressures, and fears
- Messaging framework with internal rationale
- Seller enablement kit
- Technical or solutions-architect enablement kit, where relevant
- Buyer-specific objections and responses
- Cross-functional launch-readiness checklist
- Evidence labels for key claims

## Design Principles

The workflow is built around four principles:

- Diagnose the market and buyer context before creating messaging.
- Make the launch narrative answer “why now,” not only “what is launching.”
- Adapt enablement to the needs of sellers, technical teams, and buyers.
- Distinguish verified evidence from assumptions.

## Repository

This repository also includes companion Skills for:

- Competitive Battle Cards
- Sales Enablement Briefs

All three follow the same design philosophy: package reusable GTM judgment into structured AI workflows rather than standalone prompts.

## Read More

**Beyond Prompting: How I Turned GTM Judgment Into a Reusable Claude Agent Skill**

*Link will be added once the article is published.*
