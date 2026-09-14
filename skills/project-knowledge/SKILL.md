---
name: project-knowledge
description: Resolve authoritative project records and resume or persist work through the configured knowledge adapter.
---

# Project knowledge

Read the applicable `Project knowledge` section in AGENTS.md, contract version 1.
It identifies the primary store, entry point, adapter, explicit exceptions, and
resumption procedure. Each record has one authority; unspecified information types
use the primary store. Code and tests remain repository artifacts. A snapshot names
its source and captured state; it is not a second maintained authority.

Load only the adapter for the information concerned, using its supplied location.
An adapter may be a skill or complete inline instructions. Read linked instructions
when needed; do not reload unchanged material already in context or invoke an active
caller recursively. Missing configuration blocks authoritative persistence, not
useful discussion or drafting. Use [setup-project](../setup-project/SKILL.md) for setup.
A task-specific override does not silently rewrite project configuration.

## Read and resume

Retrieve current originals, not remembered thread content. Start at the configured
entry and active item, then follow relevant requirements, terms, decisions, and evidence.
Resolve ambiguity between active tasks. Inspect the actual working tree, including
new files; a commit alone misses uncommitted changes.

When continuity is needed, keep a short record with the work item:

- Objective and source IDs; decisions and open questions.
- Completed work, next step, and existing authority with its source.
- Outstanding human review and evidence tied to the checked content state.

Unknown authority stays unknown. A continuation summary cannot establish current
verification or human confirmation by itself. Interaction preferences belong in a
separate `Agent interaction` section in AGENTS.md, not project records.

## Write and reconcile

The method supplies content and decision status; the adapter supplies storage mechanics.
Search before creating, read current content before updating, preserve contributions,
and verify saved results. Surface conflicts and partial writes. Routine authorized
documentation needs no extra approval; saving it grants no new action permissions.

At handoff, check whether changed behavior affects requirements, terminology, decisions,
or references. Update supported descriptive facts and record unresolved discrepancies.
Never rewrite desired behavior to fit code. Use [reconcile-knowledge](../reconcile-knowledge/SKILL.md)
for a requested catch-up. Age alone does not prove drift. If access fails, report unsaved
work and continue whatever does not depend on that access.
