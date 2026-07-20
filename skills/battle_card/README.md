#Details about generating battle cards
# Competitive Battle Card Skill

A structured AI workflow for diagnosing competitive situations and generating deal-specific battle cards.

Unlike a traditional battle card generator, this Skill does **not** start with a feature comparison. It first diagnoses the competitive motion—developer preference, procurement leverage, or incumbent displacement—and then adapts the strategy, objection handling, and recommended next actions accordingly.

## Contents

* **SKILL.md** — Core workflow, decision logic, output structure, and guardrails
* **input-template.md** — Structured template for capturing deal context
* **example-input.md** — Fictional enterprise payments database evaluation
* **example-output.md** — Battle card generated from the example scenario

## How to Use

1. Load **SKILL.md** into Claude as an Agent Skill (or paste it into a conversation).
2. Complete **input-template.md** with your deal context.
3. Run the Skill using the completed input.
4. The Skill diagnoses the competitive motion before generating any recommendations. If critical information is missing, it flags the gap instead of inventing an answer.

## What the Skill Produces

* Competitive motion diagnosis
* Deal strategy and winnability assessment
* Buyer and stakeholder map
* Honest competitive positioning, including where the competitor genuinely wins
* Buyer-specific objection handling
* Landmine discovery questions
* "Do Not Say This" guidance
* Stage-specific next actions
* Evidence labels for every claim

## Design Principles

The workflow is built around four principles:

* Diagnose the situation before generating content.
* Adapt recommendations to the buyer, deal stage, and competitive motion.
* Distinguish verified evidence from assumptions.
* Make the reasoning transparent and inspectable.

## Repository

This repository also includes companion Skills for:

* Product Launch Planning
* Sales Enablement Briefs

All three follow the same design philosophy: package reusable GTM judgment into structured AI workflows rather than standalone prompts.

## Read More

**Beyond Prompting: How I Turned GTM Judgment Into a Reusable Claude Agent Skill**

*Link will be added once the article is published.*
