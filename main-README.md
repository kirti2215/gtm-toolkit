# GTM Toolkit

AI-powered GTM systems built by a practitioner, for practitioners.

This toolkit contains two types of systems — **Skills** and **Loops** — each designed for a different kind of GTM problem. Skills handle one-time workflows. Loops govern recurring commercial decisions over time.

> 📬 **Newsletter:** [Subscribe for GTM + AI insights →](YOUR_NEWSLETTER_LINK_HERE)

---

## What's in Here

```
gtm-toolkit/
├── loops/               ← Four stateful GTM systems (the deeper work)
├── skills/              ← Reusable one-time workflow prompts
└── universal-prompts/   ← Standalone prompts, no setup required
```

---

## Loops

Four stateful GTM systems. Each one preserves prior state, infers conclusions from new evidence, produces a decision or action output, and evaluates whether that output actually worked.

A Loop is not a prompt you run once. It is a system designed to govern a recurring commercial decision across an entire fiscal year or deal cycle.

| Loop | What it governs |
|------|----------------|
| [GTM Annual Strategy Loop](./loops/gtm-annual-strategy-loop/) | Whether the annual strategy still supports the commitment — and what decision is justified when it doesn't |
| [Revenue Projection Loop](./loops/gtm-revenue-projection-loop/) | What the commercial engine is likely to produce, why the projection changed, and what conditions the target requires |
| [Pipeline Risk Loop](./loops/gtm-pipeline-risk-loop/) | What the primary risk mechanism is in a live deal, whether it changed, and what the one next action is |
| [Win/Loss Pattern Loop](./loops/gtm-winloss-pattern-loop/) | What mechanism caused past wins and losses, whether that pattern is repeating, and whether interventions changed it |

→ **[Full loops README with visuals and artifact guide](./loops/)**

---

## Skills

Reusable AI skills for common GTM workflows. Each Skill diagnoses the business context before generating content. One skill per workflow, built to be repurposed.

| Skill | What it does |
|-------|-------------|
| [Competitive Battle Card](./skills/battle_card/) | Diagnoses the competitive motion and produces account-specific positioning, objection handling, and deal strategy |
| [Product Launch Planner](./skills/product_launch/) | Identifies the "why now" before building a launch package — messaging, personas, seller enablement, objection handling, and launch-readiness checklist |
| [Sales Enablement](./skills/sales_enablement/) | Builds account-specific materials for enterprise deals — value props by persona, discovery questions, pitch points, business case |

**Coming soon:** Messaging Framework Builder · Sales Play Creator

---

## Each Skill and Loop Includes

```
├── LOOP.md / README.md      ← Architecture or overview
├── loop-prompt.md           ← The runnable prompt (copy into Claude or any LLM)
├── input-template.md        ← Structured form for what to provide
├── example-input.md         ← Complete worked example input
├── example-output.md        ← Full output from the example input
└── before-after-evals.md    ← Side-by-side: naive approach vs. this system
```

---

## How to Use

**Claude / Cowork users**
Download the `.skill` file from the `skills/` folder and install it in your Cowork or Claude Code plugins. The skill triggers automatically when you describe the relevant workflow.

**Everyone else (ChatGPT, Gemini, Copilot, any LLM)**
Open the `loop-prompt.md` or skill prompt file. Copy it as your system prompt. Fill in the corresponding `input-template.md` and paste it as your first message. Works with any capable LLM.

**For Loops specifically:** Complete the initialization input once at the start of the fiscal year or deal cycle. At each recurring review, supply only what changed. The Loop carries the prior state forward — you are never starting from scratch.

---

## Design Principles

Every system in this toolkit follows the same principles:

- **Diagnose before generating.** The system reads the situation before producing an output.
- **Separate evidence from judgment.** What is known, what is inferred, and what is assumed are kept distinct.
- **Preserve state.** Prior beliefs are recorded so later outcomes can evaluate them.
- **Stop at the boundary.** These systems surface options and evidence. Binding decisions belong to the human.

---

## About

Built by **Kirti Gupta**, GTM leader with experience across North America, EMEA, APAC, and LATAM. Previously led worldwide GTM for Amazon DynamoDB at AWS.

This toolkit grew out of a question: what would it look like if AI could do more than generate content — if it could actually reason through a commercial decision the way an experienced operator would, and keep learning from what happened?

The Skills answer that question for one-time workflows. The Loops answer it for the decisions that recur every month and matter most at year-end.

> 📬 **Follow along:** [Newsletter →](YOUR_NEWSLETTER_LINK_HERE)
