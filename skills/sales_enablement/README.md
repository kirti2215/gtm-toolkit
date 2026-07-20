#Details about sales enablement skill
# Sales Enablement Skill

A structured AI workflow for building account-specific sales materials for enterprise deals.

Unlike a generic pitch deck or sales-content generator, this Skill starts by diagnosing the account context, buyer pressures, competitive situation, and external market forces before producing any content.

## Contents

- **SKILL.md** — Core workflow, decision logic, output structure, and guardrails
- **input-template.md** — Structured template for capturing deal and account context
- **example-input.md** — Fictional enterprise database modernization opportunity in UK financial services
- **example-output.md** — Complete sales enablement package generated from the example scenario

## How to Use

1. Load **SKILL.md** into Claude as an Agent Skill, or paste it into a conversation.
2. Complete **input-template.md** with your account and deal context.
3. Run the Skill using the completed input.
4. The Skill diagnoses the account, buyer priorities, competitive dynamics, and market context before generating sales materials.

If important information is missing—such as buyer priorities, competitive context, or business drivers—the Skill flags the gaps rather than producing generic enablement content.

## What the Skill Produces

- Account snapshot
- Buyer personas and priorities
- Persona-specific value propositions
- Discovery questions
- Account-specific pitch points
- Objection handling with follow-up questions
- Business case with assumptions clearly labeled
- Recommended next steps by commitment level
- Evidence labels for key claims

## Design Principles

The workflow is built around four principles:

- Understand the account before recommending a sales strategy.
- Adapt messaging to each buyer's priorities instead of using one generic pitch.
- Distinguish verified evidence from customer signals and assumptions.
- Produce materials that help advance a specific opportunity, not just describe the product.

## Repository

This repository also includes companion Skills for:

- Competitive Battle Cards
- Product Launch Planning

All three follow the same design philosophy: package reusable GTM judgment into structured AI workflows rather than standalone prompts.

## Read More

**Beyond Prompting: How I Turned GTM Judgment Into a Reusable Claude Agent Skill**

*Link will be added once the article is published.*
