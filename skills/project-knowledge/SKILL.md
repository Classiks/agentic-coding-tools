---
name: project-knowledge
description: Configure, find, and maintain project records in local Markdown, including resuming active work.
---

# Project knowledge

Use the local Markdown paths in the applicable `Project knowledge` section of
`AGENTS.md`. Keep records under the configured path unless the section maps them
elsewhere. Use the project's conventions for filenames and structure. Each record has
one maintained source. A snapshot should identify its source and captured state.

## Configure on request

Inspect applicable instructions and existing records before writing or updating the
section. Preserve established conventions and unrelated instructions. Ask about
conflicting sources or missing consequential choices. Changing the configuration
does not move records. Verify any existing paths you reference and identify gaps.

A short section can look like this. Resolve paths relative to the containing
`AGENTS.md`. Include glossary and ADR paths only when an explicit mapping helps.

```markdown
## Project knowledge

- Path: `docs/project/`
- Active work: Start at `docs/project/tasks.md` and follow its links to specs and continuation notes.
- Glossary: `CONTEXT.md`
- ADRs: `docs/decisions/`
```

Use actual paths and describe how to find active work, even if the project keeps it all
in one file. If the destination is unknown, resolve it before saving. Discussion and
drafting can continue without setup.

## Read and resume

Read the current records, starting where the section directs you. Identify the
intended work item and follow relevant specs, terms, decisions, and evidence. Inspect
the actual working tree, including staged, unstaged, and untracked changes.

When continuity matters, save a short note with the work item. Include the objective,
source IDs, decisions and open questions, completed work, the next step, and any
outstanding human review. Tie evidence and confirmations to the state they cover. A continuation
summary alone cannot establish verification, confirmation, or authority. Keep
interaction preferences in the separate `Agent interaction` section of `AGENTS.md`.

## Write and check

Search by ID and content before creating a record. Read the current file before
updating it, preserve unrelated contributions and decision status, and surface
conflicts. For new specification work without an established layout, start with
`spec.md` and add `tasks.md` if a separate task list helps. Create only files with
content the task needs.

Give independently referenced records stable IDs unique within their scope and keep
those IDs through renames and reordering. Use relative links and IDs for references.
Link new work from the configured starting point and tasks to their specs and actual
blockers. Read back saved content, check affected links, and report paths, IDs, and
any partial or unsaved work.

At handoff, check whether the change leaves descriptive facts or references stale.
Update supported descriptions within scope and record unresolved discrepancies.
Never rewrite desired behavior to fit code. Age alone is insufficient evidence of
drift. Use [reconcile-knowledge](../reconcile-knowledge/SKILL.md) for requested catch-up.
