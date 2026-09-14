---
name: to-tickets
description: Split substantial requirements into verifiable behavioral tasks and real dependencies in the configured store; avoid needless tickets for small changes.
---

# To tickets

Use [requirements](../requirements/SKILL.md) and [project-knowledge](../project-knowledge/SKILL.md).
Read the current specification and existing tasks; link the specification rather than
copy it. Prefer behavioral slices containing the layers and tests they need over
separate database, API, and UI tasks. Tests may follow implementation.

Each task names its outcome, specification, acceptance criteria, and actual blockers.
Match size to coherent implementation and the requested rhythm. Wide mechanical
refactors may need expand/migrate/contract sequencing; identify verifiable boundaries
without adding unrelated preparatory refactors.

Check missing and cyclic dependencies. Let the adapter handle IDs, layout, and tracker
relationships. Save proposals as proposals; ask about consequential scope decisions,
not each routine write. Do not incidentally close or change the parent. Technical
independence and an approved breakdown add no implementation authority; preserve any
implementation mandate already given.

Adapted from [Matt Pocock](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/to-tickets/SKILL.md). MIT, see LICENSE.
