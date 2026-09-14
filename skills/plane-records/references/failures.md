# Failures and capability checks

## Preserve knowledge and avoid duplicate writes

Retrieve immediately before replacing a body. Where supported and verified, use the
backend's revision precondition. The inspected MCP signatures and existing REST helper
supply no compare-and-swap parameter; read-before-write is not atomic. Keep the window
small, preserve unrelated content, and stop on a detected mismatch rather than overwrite.
Read-back can detect some conflicts but cannot guarantee no concurrent write was lost.

After timeout, connection loss, or malformed write response, do not immediately repeat
creation or switch transport. Search using the same title/context and retrieve candidate
records to determine whether the operation took effect. For updates, retrieve the target
and compare the intended fields. If uncertain, report uncertainty and stop the write.
For comments, inspect current comments if accessible before repeating an append.

Authentication failures and unclassified HTTP errors are not fallback permission.
Use REST only for the operation-specific, previously tested replacement in the
compatibility record. Never print credentials or raw sensitive response details.

A record saved but not linked from the entry point is a partial operation. Report its
ID and the unfinished link. Retry only the missing step after inspecting current state.
Do not roll back by deleting a successfully created record without a separate request.
An unavailable source is not permission to create an authoritative local mirror.

## Check what the selected mapping needs

Requirements/tasks need search, retrieve, create, update, state/label resolution, and
read-back. Page-based glossary/ADRs also need Page list/retrieve/create/update and an
updatable entry record. Continuation needs full-body read/update on its owning record.
Textual dependencies need normal item read/update; native dependencies and attachments
are optional additional capabilities. Comment writes are optional and require both
capability and communication authority.

Safe read probes can check configuration, identity, pagination, and record retrieval.
Write probes require an explicitly authorized fixture area. A normal authorized record
update can provide evidence for that operation, but is not a pretext to perform unrelated
create/archive/delete tests. Record tested operation, environment/version when known,
observed result, and remaining limits. Do not rerun an old smoke script blindly: it may
create records, comments, change state, and archive data.

After a deployment change, recheck needed operations. Historical smoke-test results
are useful evidence, not a claim about today's server. Static skill validation checks
format only. Test new adapters against fresh-context discovery, existing-record update,
new-record discovery, conflict, unavailable access, and ambiguous write scenarios.
