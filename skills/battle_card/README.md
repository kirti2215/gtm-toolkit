#Details about generating battle cards
**Competitive Battle Card Skill**

A structured AI workflow for diagnosing competitive situations and generating deal-specific battle cards.

This is not a feature comparison generator. Before producing any content, the Skill identifies the type of competitive motion — developer preference, procurement leverage, or incumbent displacement — and adapts the strategy, objection handling, and recommended next action accordingly.

**What's in this folder**

SKILL.md — the core skill: workflow, decision logic, output structure, and guardrails
input-template.md — structured input form to fill out before running the skill
example-input.md — fictionalized enterprise scenario (payments database evaluation)
example-output.md — battle card the skill produced for the example scenario

**How to use**

1. Copy SKILL.md into a Claude conversation or load it as an Agent Skill
2. Fill out input-template.md with your deal context
3. Paste the completed input and run

The skill will diagnose the competitive motion before generating any content. If critical context is missing, it will flag the gap rather than invent an answer.

**What the output includes**

Competitive motion diagnosis, deal strategy and winnability assessment, buyer and stakeholder map, honest competitive positioning (including where the competitor genuinely wins), objection handling tailored to the deal context, landmine discovery questions, a Do Not Say This section, a stage-specific next action, and evidence labels on every claim.

**Read more**

Full writeup on how this was built and what changed during testing: [Beyond Prompting: How I Turned GTM Judgment Into a Reusable Claude Agent Skill] — link to be added on publication.
