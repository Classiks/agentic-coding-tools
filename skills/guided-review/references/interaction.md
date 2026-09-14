# Review interaction

Defaults:

- Choose a coherent portion and adapt its size to feedback.
- Occasionally offer a comprehension question for subtle behavior. Explain first;
  do not quiz after every portion or require an answer.
- A declined offer ends offers for this session unless invited again.
- Explicit confirmation is still required for human-review coverage.

An optional, separate AGENTS.md section can override conversational defaults:

```markdown
## Agent interaction

- Review portions: small coherent units; adapt to feedback.
- Comprehension questions: only when I request them.
```

Current prompts override preferences for the session, subject to binding project rules.
Persist changes only when asked to update AGENTS.md, preserving unrelated content.
Never save interaction preferences in project knowledge or a separate user-profile file.

"Skip the quiz" does not waive confirmation. "Work longer on your own" does not reduce
review coverage. An explicit coverage change records the new mode and actual inspection.
