---
name: guided-review
description: Guide confirmed human review of changes or hand off delegated verification.
---

# Guided review

Resolve mode from the task and project rules. Ask if unclear before claiming completion. Private or work use does not determine mode.

| Mode | Completion |
| --- | --- |
| Full ownership | Explicit inspection confirmation for every current changed line and artifact in scope |
| Focused review | Explicit confirmation for selected scope. Name omissions. |
| Delegated verification | Return AI evidence and limits only. |

- Work rhythm, coverage, and portion size are independent. Longer autonomy retains ownership obligations. Group behavior with its tests, then split into manageable portions without reshaping code. Follow [interaction settings](references/interaction.md).
- Verify intended behavior on the actual change before presenting it as ready. Run applicable repository checks, reuse current evidence, and rerun affected checks after edits. Disclose failed, missing, or unavailable checks before an informational tour.
- Use [coverage and resumption](references/coverage.md) to inventory the scoped baseline and dirty diff, including staged, unstaged, and new files. Account for tests, configuration, docs, deletions, renames, and non-text changes. Full ownership includes mechanical changes.

## Human review portions

- Give confirmed portions out of the planned total and a rounded estimate or range for effort completed and remaining. Weigh complexity, unfamiliar behavior, and discussion. Exclude the current portion until confirmed. Flag uncertain totals and re-estimate as scope, difficulty, or coverage changes.
- Explain purpose, behavior, consequential choices, and test support. Label inference. Use the actual diff and name the complete ranges to inspect. Link start lines where supported, using baseline lines for removals. Summaries and explanations establish no coverage.
- Name the portion and wait for explicit inspection confirmation before marking it reviewed or advancing. Resolve questions or edits first. "Reviewed, continue" suffices. Silence, praise, and quiz answers do not.
- Tie confirmation to inspected content. Reopen coverage when content or meaning changes. Refresh inventory and evidence after edits, on resumption, and before handoff. Keep AI checks separate from confirmations.

## Finish

Report mode, confirmed and pending scope, evidence, and gaps. Save progress only when continuity needs it. Review records reported inspection. It cannot prove comprehension or enforce inspection.

Explanation method adapted from [pstack teach](https://github.com/backnotprop/pstack/blob/18e0e908a13553b0e58d065ab26dbc9a972ec8ba/skills/teach/SKILL.md). MIT, see LICENSE.
