---
name: project-knowledge
description: Configure and maintain local Markdown project records or resume work from them.
---

# Project knowledge

- Read the applicable `Project knowledge` section of `AGENTS.md`. Resolve paths relative to that file. Use the configured directory, explicit mappings, and existing conventions.
- Maintain one source per record. Label snapshots with their source and captured state.

## Configure on request

- Inspect instructions and records first. Preserve established conventions and unrelated instructions. Ask about conflicting sources or consequential choices. Configuration changes leave records in place.
- Verify paths, report gaps, and explain where active work starts, even in a single file. Map glossary and ADR paths only when useful. Preserve existing mappings.

```markdown
## Project knowledge

- Path: `docs/project/`
- Active work: Start at `docs/project/tasks.md` and follow links to specs and continuation notes.
- Glossary: `GLOSSARY.md`
- ADRs: `docs/decisions/`
```

Resolve unknown destinations before saving. Discussion and drafts can proceed without setup.

## Resume and write

- Start at the configured entry point. Identify the intended work item and follow its specs, terms, decisions, and evidence. Inspect the working tree, including staged, unstaged, and untracked changes.
- For continuity, note the objective, source IDs, decisions, open questions, completed work, next step, and pending human review. Tie evidence and confirmations to the covered state. A summary establishes no verification, confirmation, or authority. Keep preferences in the separate `Agent interaction` section of `AGENTS.md`.
- Search by ID and content before creating. Read current content before editing. Preserve unrelated contributions and decision status. Surface conflicts.
- Without an established layout, start with `spec.md` and add `tasks.md` only if useful. Create only needed records.
- Give independently referenced records stable, scope-unique IDs across renames and reordering. Use relative links and IDs. Link new work from the entry point, and tasks to specs and actual blockers.
- Read back writes, check links, and report paths, IDs, and partial or unsaved work.
- At handoff, check for stale descriptions and links. Update supported facts within scope and record unresolved discrepancies. Never rewrite desired behavior to fit code. Age alone proves no drift. Use [reconcile-knowledge](../reconcile-knowledge/SKILL.md) for requested catch-up.
