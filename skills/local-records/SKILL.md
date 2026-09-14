---
name: local-records
description: Store and retrieve project knowledge in Markdown when local files are the configured authority; works without a tracker or MCP.
---

# Local records

Apply [project-knowledge](../project-knowledge/SKILL.md). Use the configured project path
and existing conventions. Resolve a missing destination before saving; drafts may stay
in chat. An unavailable external store does not authorize a local replacement.

Search by ID and content before creation and read current files before updates.
Without an established layout, use `spec.md` and, if decomposition helps, `tasks.md`
inside the chosen directory. Split files only when useful; create no empty template tree.

Give independently referenced records stable IDs unique within their storage scope.
Keep IDs through renames and reordering. Relative links and IDs identify records;
line numbers only navigate. Link tasks to their specification and actual blockers,
and new work from the entry point. Keep continuation with its work item. Glossaries
and ADRs follow the configured mapping, not a separate default folder.

Merge intended changes into the current content, preserving unrelated contributions
and decision status. Re-read if intervening edits are possible; surface conflicts.
Inspect saved content and affected links. Report paths, IDs, and partial writes.
A deliberately selected local draft of an external record keeps its source reference
and draft status; saving it does not establish synchronization.
