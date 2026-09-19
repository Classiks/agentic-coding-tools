---
name: guided-review
description: Walk through changes in small confirmed portions for full code ownership or focused review, tracking coverage separately from AI verification.
---

# Guided review

## Set coverage and rhythm

Resolve the mode from the task and project instructions. Ask if coverage is unknown
before claiming review completion; private versus work use does not determine it.

| Mode | Completion means |
| --- | --- |
| Full ownership | User confirmed inspection of every changed line and artifact in scope |
| Focused review | User confirmed selected scope; omitted changes remain outside human coverage |
| Delegated verification | AI supplied evidence; no human inspection is claimed |

Work rhythm, coverage, and portion size are independent. Longer autonomous work retains
full-ownership obligations. Group by behavior and associated tests, then split into
manageable portions. Do not distort implementation architecture for smaller review units.
Read [interaction settings](references/interaction.md) for defaults and optional
`Agent interaction` overrides in AGENTS.md. Prompt changes apply to the session.

## Validate and establish scope

Use [verify-change](../verify-change/SKILL.md) before presenting work as ready, reusing
current evidence. Report failed or unavailable checks. An informational tour can proceed
with disclosed gaps, but human confirmation cannot repair missing AI verification.
In delegated mode, return that evidence without starting a tour or human coverage ledger.

Read [coverage and resumption](references/coverage.md) to inventory the complete diff
and track confirmations against actual content. Include tests, configuration, docs,
new/deleted/renamed files, and non-text changes; full ownership has no mechanical-code
exemption.

## Present one portion

Start each portion with a brief progress estimate: confirmed portions out of the current
planned total, plus roughly how much review effort is complete and what remains.
Weight conceptual complexity, unfamiliar behavior, and discussion so far, not just line
or portion counts. Use a rounded estimate or range; flag an uncertain total rather than
invent precision. For example: "2/5 portions confirmed, roughly 25-35% of review effort
complete; the state machine and its tests are still ahead." Exclude the current portion
until confirmed. Re-estimate when scope, difficulty, or reopened coverage changes; this
estimate never substitutes for actual coverage.

Explain purpose, behavior, consequential choices, and how tests support it. Distinguish
observations and documented rationale from inference. Navigate with actual `file:line`
or `file:line-range` references, using clickable start-line links where supported.
Refer to the user's diff instead of repeating whole code blocks; use baseline-side
references for removals. Name complete inspected ranges. A function summary alone does
not establish inspection of its body.

Offer comprehension questions selectively under the interaction settings. They are
optional learning aids, never a gate or substitute for coverage confirmation.
For human review, identify the portion and wait for explicit confirmation before marking
it reviewed or moving on. A clear "reviewed, continue" suffices; silence, an explanation,
or unrelated praise does not. Resolve questions or edits first.

## Resume and finish

Refresh scope and affected evidence/confirmations after edits as the coverage reference
describes. Persist progress through project-knowledge only when continuity is needed.
Report the mode, confirmed and pending scope, evidence, and gaps. Full ownership requires
no unaccounted changes and confirmation for every portion.

This records the user's inspection; it cannot prove comprehension or observe their eyes.
It is an instruction-based workflow, not a technical enforcement gate.

Explanation method adapted from [pstack teach](https://github.com/backnotprop/pstack/blob/18e0e908a13553b0e58d065ab26dbc9a972ec8ba/skills/teach/SKILL.md). MIT, see LICENSE.
