#Details about generating battle cards
Competitive Battle Card Skill
A structured AI workflow for diagnosing competitive situations and generating deal-specific battle cards.

This is not a feature comparison generator. Before producing any content, the Skill identifies the type of competitive motion — developer preference, procurement leverage, or incumbent displacement — and adapts the strategy, objection handling, and recommended next action accordingly.
What's in this folder
File
Description
SKILL.md
The core skill — workflow, decision logic, output structure, and guardrails
input-template.md
Structured input form to fill out before running the skill
example-input.md
Fictionalized enterprise scenario (payments database evaluation)
example-output.md
Battle card the skill produced for the example scenario

How to use
Copy SKILL.md into a Claude conversation or load it as an Agent Skill
Fill out input-template.md with your deal context
Paste the completed input and run

The skill will diagnose the competitive motion before generating any content. If critical context is missing, it will flag the gap rather than invent an answer.
What the output includes
Competitive motion diagnosis (developer preference / procurement leverage / incumbency)
Deal strategy and winnability assessment
Buyer and stakeholder map
Honest competitive positioning — including where the competitor genuinely wins
Objection handling tailored to the deal context
Landmine discovery questions
Do Not Say This section
Stage-specific next action
Evidence labels on every claim (verified / customer-reported / assumption)
Read more
Full writeup on how this was built, what was encoded, and what changed during testing: Beyond Prompting: How I Turned GTM Judgment Into a Reusable Claude Agent Skill

(Link will be updated on publication)
