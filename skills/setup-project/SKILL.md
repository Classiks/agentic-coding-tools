---
name: setup-project
description: Configure project knowledge in AGENTS.md on request, preserving existing conventions and selecting a resolvable adapter.
---

# Set up project knowledge

Inspect applicable instructions and existing requirements, glossaries, ADRs, and indexes.
Preserve established mappings. A file's existence alone does not establish authority;
resolve conflicting sources without implicitly migrating or deleting content.

Ask in chat only for missing consequential choices:

- Primary source and concrete entry point.
- Available adapter skill or complete inline access instructions.
- Any explicit exceptions by information type.
- How a fresh agent locates active work and continuation records.

Read the selected adapter for its required backend configuration. Use the
[section template](references/agents-section.md), populated with confirmed values.
Check available reads and mark unverified access honestly; configuration alone does
not prove access. Inline instructions must satisfy [project-knowledge](../project-knowledge/SKILL.md).
Keep credentials out of the file. Install no tools or host configuration.

Edit only the relevant knowledge section, preserving unrelated instructions. Resolve
contradictory sections in scope. Report the saved location and unresolved prerequisites;
placeholders must not look like an operational setup. External test writes require an
authorized test area.

Only on request, configure a separate `Agent interaction` section using the
[review settings](../guided-review/references/interaction.md). Do not add preference
questions to ordinary knowledge setup.
