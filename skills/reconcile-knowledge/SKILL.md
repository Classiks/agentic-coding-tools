---
name: reconcile-knowledge
description: On request, reconcile documentation with current code after other contributors or suspected drift, without redefining intended behavior.
---

# Reconcile knowledge

Use [project-knowledge](../project-knowledge/SKILL.md) to retrieve the relevant records.
Establish the requested area and compare its requirements, terminology, ADRs, references,
and evidence with current code, including uncommitted and new files. Use a prior
checkpoint only if it covers that scope; disclose an absent baseline.

Check both undocumented code changes and outdated documented claims:

| Finding | Action |
| --- | --- |
| Supported descriptive drift, such as a renamed file | Update and check references |
| Code contradicts confirmed requirements | Record a possible bug; do not redefine intent or infer permission to fix |
| An unresolved domain choice | Present the decision needed |
| Code contradicts an old ADR | Record the discrepancy; invent no historical rationale or accepted successor |
| Stale test evidence or changed reviewed content | Mark affected evidence or review for reassessment |

Age and missing access do not prove drift. Persist in-scope updates through the adapter,
link existing findings, and report checked scope, code state, observations, and gaps.
A partial reconciliation establishes neither project-wide freshness nor runtime correctness.
