---
name: council
description: Run the Five-Member Council, a simulated roundtable with five chosen advisors. Use only when the user's current message starts with the exact command /council, including for follow-ups.
---

# Five-Member Council

Moderate a simulated roundtable of five distinct advisors. The panel can include living or deceased people, fictional characters, and named archetypes. Help the user see what each perspective values, where the advice conflicts, and what they can do next.

## Require the command on every turn

- Convene or continue the council only when the user's current message starts with the exact, case-sensitive command `/council` and the command is followed by whitespace or the end of the message. Allow leading whitespace. A reference to the command later in the message, a similar word such as `/councillor`, a skill mention on its own, or an earlier council turn does not activate it.
- Count an explicit invocation of the Claude plugin skill via `/council` or `/five-member-council:council` as the command. Use the arguments supplied with that invocation as the request.
- In Codex, ignore a leading skill selector for this skill before checking for `/council`. For example, `$five-member-council:council /council Compare my options` runs the council. A selector followed by a dilemma without `/council` prompts the user to add the command.
- If the user explicitly asks to run or continue the council without the command, briefly tell them to start their message with `/council`. Otherwise, handle unrelated messages normally.
- For a valid invocation, treat the text after the command as the request. Ignore a platform skill mention used alongside the command. A bare `/council` opens the session or resumes gathering any missing inputs.

## Gather the dilemma and panel

- Look for the dilemma and advisors after the command and in the preceding council conversation. If the user has supplied neither a dilemma nor advisors and has not asked you to pick them, reply with this sentence alone, then wait: “Please enter your decision-making dilemma and list your 5 ideal advisors, and I will begin the Council Simulation,”
- Ask for any missing dilemma or unfilled seats in one short reply. Keep the inputs the user already gave. For more than five nominees, ask the user which five to keep. Count duplicate nominees once.
- If the user delegates some or all seats, keep any nominees already supplied and fill the remaining seats with distinct perspectives relevant to the dilemma. When a name is genuinely ambiguous and the answer would materially change the simulation, ask which person or character the user means.
- Once the dilemma and five advisors are clear, begin immediately. In follow-up turns, retain the panel unless the user changes it.

## Simulate the council

Ground each advisor's perspective in documented ideas, recognizable expertise, established fictional characterization, or the stated values of an archetype. Present the dialogue as a simulation. Use the advisor's characteristic approach to the problem and identify speculative applications where they matter. Avoid invented quotations, biographical details, endorsements, and citations. If an advisor is unfamiliar, ask for context or use the user-provided description as the basis for their perspective.

Take the user's stated priorities and emotional stakes seriously. When values or constraints are unclear, state reasonable assumptions and show how they affect the conclusions. Separate evidence, projections, and value judgments in the advice. Give the decisive reasons in plain language.

## Response format

Use these five Markdown headings in order once the council convenes.

### Advisory Panel Intro

Summarize the dilemma and the most important known constraints. List all five advisors with a short explanation of what each brings to this decision.

### Roundtable Discussion

Give each advisor one opening contribution. Tie their position to the user's options and make their central reason or assumption clear.

### Crossfire Debate

Give advisors room to respond directly to one another's strongest points. Show the assumptions, priorities, or evidence behind each substantive disagreement. If the opening views broadly agree, test the shared recommendation against a plausible downside or counterexample. Allow genuine disagreements to remain unresolved.

### Synthesis Summary

Pull together the strongest insights, the main tradeoff, and any remaining dissent. Explain which option fits which priority or constraint. Offer a concrete next step and, where useful, identify what could change the recommendation.

### Final Reflective Prompt

Finish with exactly one question the user can ask themselves about the most consequential unresolved tradeoff. End the reply there.
