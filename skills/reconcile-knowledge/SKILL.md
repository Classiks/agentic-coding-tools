---
name: reconcile-knowledge
description: Reconcile suspected documentation drift on request while preserving intended behavior.
---

# Reconcile knowledge

- Retrieve records through [project-knowledge](../project-knowledge/SKILL.md). Within requested scope, compare requirements, terms, ADRs, references, and evidence with current code, including uncommitted and new files.
- Use only scope-matching checkpoints. Disclose a missing baseline. Look for undocumented changes and outdated claims. Age and missing access alone prove no drift.

| Finding | Action |
| --- | --- |
| Supported descriptive drift | Update and check references |
| Code contradicts confirmed requirements | Record a possible bug. Keep requirements. Fix only with existing authority. |
| Unresolved domain choice | Present decision needed |
| Code contradicts old ADR | Record discrepancy. Never invent rationale or an accepted successor. |
| Stale test evidence or changed reviewed content | Flag for reassessment |

- Save authorized updates at configured Markdown paths through project knowledge. Link existing findings.
- Report checked scope, code state, observations, and gaps. Partial reconciliation establishes neither project-wide freshness nor runtime correctness.
