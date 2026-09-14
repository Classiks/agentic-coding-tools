# Project knowledge acceptance scenarios

| Scenario | Expected observable result |
| --- | --- |
| Existing AGENTS.md has engineering rules and an established docs directory | Setup preserves unrelated text and offers the existing convention; no migration or tool installation |
| Both Plane and local files claim the same specification | Setup surfaces the conflict before declaring either authoritative |
| Plane is primary, CONTEXT.md is a local exception | Domain terms update locally; ADRs use Plane; no duplicated local ADR |
| Inline storage instructions replace an adapter skill | Methods use them if finding, reading, writing, and verification are sufficiently specified |
| A new agent has no history but receives a project task | It reads configuration, entry point, active record, references, and actual code before resuming; unknown approvals remain unknown |
| Entry point contains several active tasks | Agent resolves the intended task rather than choosing an arbitrary previous one |
| Plane is unavailable | No silent authoritative local fallback and no invented successful update |
| Plane write times out after creating a record | Agent checks whether the record exists before attempting creation again |
| Another person edits a record during work | Agent reads current content and preserves contributions or surfaces the conflict |
| Code accepts expired invitations but requirements reject them | Reconciliation records a possible bug, without changing requirements or fixing code outside scope |
| A module was renamed with unchanged behavior | In-scope descriptive references are updated and checked |
| Current code differs from an old ADR with no known rationale | Discrepancy is recorded; no invented historical rationale or accepted successor ADR |
| Evidence points to a commit but a test has since changed uncommitted | Evidence and affected review require reassessment; prior human approval is not carried forward |
| A document is old but still correct | No content change merely due to age |
| A partial reconciliation cannot access some sources | Result records inspected scope and limitations, not project-wide freshness |
| to-spec receives a settled discussion | It synthesizes without repeating Grilling or automatically marking implementation ready |
| to-tickets receives a small change or cyclic proposed dependencies | It avoids needless decomposition or resolves the cycle before presenting usable tasks |
| A pure interview saves nothing and no knowledge store exists | Continue discussion without mandatory storage setup |
| A one-line inline adapter says only "save it there" | Ask for missing access/identity/conflict procedures before claiming an operational adapter |
