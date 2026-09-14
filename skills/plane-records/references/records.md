# Plane record recipes

Use configuration.md for identities and transport.md for operation routing. `P` is
the project UUID, `I` a work-item UUID, `D` a Page UUID, and `H` the exact HTML body.

## Find and read

For a known work-item UUID, retrieve it with project_id=P and workitem_id=I. For a
human identifier such as ABC-12, use a compatible retrieve_by_identifier operation
if verified; otherwise search the identifier, validate project and sequence, and
retrieve the matching UUID. Search also by meaningful title terms before creation.
Search results may span the workspace: verify returned project identity. Follow
pagination when the response says more results exist, using supplied cursors. A
nonempty next_cursor alone need not mean another page exists. If an operation cannot
page through a truncated result, do not claim exhaustive absence.

Retrieve full content, avoiding sparse field sets that omit description_html or
relationships. Read relevant comments using `workitem_comment(action="list",
project_id=P, workitem_id=I)` with cursor/per_page where supported; retrieve a specific
comment with action="retrieve" and comment_id. Comment reads are separate capabilities
and may need a safe probe. If important comments cannot be read, qualify the context.

For Pages, list within project scope or retrieve the known ID through the selected
route. The inspected REST page-list helper exposes no cursor argument: inspect result
completeness and use known IDs or a compatible paginated route if needed; do not alter
the helper or guess URL parameters. Match title as a cross-check, not durable identity.

## Work-item creation and updates

1. Search for an existing matching problem, resolve the configured creation state and
   kind label, and prepare content supplied by the method.
2. Use workitem.create with project_id, name, state UUID, and description_html; include
   resolved label UUIDs or parent UUID only when applicable. Preserve selected visibility
   and unrelated metadata. Do not use a default state as an implicit user decision.
3. Retrieve the returned UUID, verify title, body, state, labels, and parent as relevant.
4. Update the entry or parent record with the new reference and read it back. If linking
   fails after creation, report the created ID and unfinished discoverability operation.

For updates, retrieve the latest record and merge only intended content. Pass only
changed fields to workitem.update. A description_html write replaces the body, not a
section. Preserve unrelated sections, links, decisions, and formatting. Render supplied
Markdown as appropriate HTML; escape literal code/text, retain meaningful structure,
and compare semantic content after reading back, allowing harmless server normalization.
Use description_stripped only for deliberately plain text; do not send competing bodies.

Use manage_label to add or remove a specific label instead of replacing all labels.
Use update(parent=UUID) for a chosen parent only if that field is supported and the
relationship is in scope. Neither parenting nor a no-blockers condition grants approval.

## Pages, decisions, and glossary

Create/update through the page recipes in transport.md. Preserve existing content and
visibility, resolve access before creation, and respect locked or archived records.
Do not unlock, unarchive, or widen access to force a write. Save the returned UUID and
link new Pages from the configured entry or decision index. Retrieve after both writes.

An ADR Page holds the decision content supplied by Domain Modeling. A glossary Page
holds terminology. On a confirmed superseding decision, create/link its successor and
mark the predecessor as superseded without erasing the old rationale. Report partial
cross-record updates; multiple writes are not a transaction. Source and code-state
references identify the relevant version, including uncommitted evidence where needed.

## Content sections and continuation

Preserve an existing work-item format. Otherwise add only needed sections: Problem,
Desired outcome, Decisions, Open questions, Acceptance criteria, Non-goals, Dependencies,
Implementation summary, Evidence, Review, and Continuation. Do not create empty sections
or invent method decisions to fill them. The adapter determines HTML representation,
not the requirements or acceptance policy.

Keep current evidence and continuation with the item. Include source references,
current decisions, unresolved questions, actual next step, and outstanding review as
supplied by the caller. Do not bury the only current continuation in an append-only
comment stream. Comments are optional contextual history; creating them requires the
applicable communication authorization. Retrieve a created comment by returned ID to
verify it. Without comment-write authority, update the authorized canonical record.

## Relations and links

Store identity as kind + project UUID + object UUID, with human identifier/title and
verified URL when available. Preserve server/user-provided canonical URLs. If a URL
must be constructed, use the deployment's verified UI URL convention, not a guessed
route. UUID references remain usable through adapter retrieval without a browser URL.

For native dependencies, first use workitem_relation list_definitions and list.
With verified write support, create with project_id, workitem_id, workitem_ids, and
relation_type from the returned built-in dependency definitions. For example, a
blocked_by relation points from the dependent item to its blocker; verify direction
by rereading. Custom relations require definition ID and matching directional label.
Do not create new relation definitions as part of routine linking.

If native relations are unverified or unavailable, record explicit `Blocked by`
references in the dependent item's body and the task list in the parent/spec entry.
Label them as textual references, not native edges. Use the same approach for Page
references; attach_to_workitem is optional and requires verified support. Link new
records into the established entry structure rather than creating a second index.
