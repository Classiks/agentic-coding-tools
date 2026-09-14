---
name: plane-records
description: >-
  Read and maintain project knowledge in Plane when configured, using existing verified MCP or REST access.
---

# Plane records

Read [project-knowledge](../project-knowledge/SKILL.md) for the common persistence
contract. This adapter supplies Plane mechanics, not implementation eligibility,
review rhythm, or acceptance policy. Do not also load the old plane-work workflow
as a dependency: its fixed local-ADR, lifecycle, and outage rules can conflict.

## Start and select references

1. Read [configuration](references/configuration.md) to resolve the project, entry
   record, object mapping, and required backend values. Use the project's values,
   never the example deployment as an implicit target.
2. Read [transport](references/transport.md) before operations. Inspect the configured
   compatibility record and currently supplied tool signatures. Existing tool access
   and an existing tested helper are allowed; install nothing.
3. Read [record operations](references/records.md) for finding, reading, creating,
   updating, linking, and resuming records. It defines content fields and read-back.
4. For status, labels, archives, or acceptance-sensitive updates, also read
   [state mapping](references/states.md). The caller supplies the authorized semantic
   change; the adapter resolves and writes its Plane representation.
5. For an unavailable operation or an uncertain write, use
   [failures and capability checks](references/failures.md).

This adapter covers storage for requirements, tasks, glossary, ADRs, findings, evidence,
and continuation records. Use implement-change and verify-change for those methods. Capabilities depend on the
configured transport; a saved record or status label establishes no approval.
