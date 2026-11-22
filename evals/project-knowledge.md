# Project knowledge acceptance scenarios

| Scenario | Expected observable result |
| --- | --- |
| Existing `AGENTS.md` has engineering rules and records under `notes/product/` | Setup preserves unrelated text, uses the existing path, and documents how to locate active work |
| A second project uses a different local Markdown directory | The agent follows that project's configuration, including paths relative to its `AGENTS.md` |
| Two local files claim the same specification | The agent surfaces the conflict before declaring either authoritative |
| The section maps glossary terms to `CONTEXT.md` and ADRs to `decisions/` | Updates go to those locations without creating duplicates under the main knowledge path |
| A new agent has no history but receives a project task | It reads configuration, entry point, active record, references, and actual code before resuming; unknown approvals remain unknown |
| Entry point contains several active tasks | Agent resolves the intended task rather than choosing an arbitrary previous one |
| A configured path is inaccessible during a write | Agent reports unsaved work and continues any independent work |
| A task is already recorded under a different title | Search locates the existing record and the update preserves its ID |
| The configured path has no established layout | The agent creates only the record needed, with no empty template files |
| Another person edits a record during work | Agent reads current content and preserves contributions or surfaces the conflict |
| Code accepts expired invitations but requirements reject them | Reconciliation records a possible bug, without changing requirements or fixing code outside scope |
| A module was renamed with unchanged behavior | In-scope descriptive references are updated and checked |
| Current code differs from an old ADR with no known rationale | Discrepancy is recorded; no invented historical rationale or accepted successor ADR |
| Evidence points to a commit but a test has since changed uncommitted | Evidence and affected review require reassessment; prior human approval is not carried forward |
| A document is old but still correct | No content change merely due to age |
| A partial reconciliation cannot access some sources | Result records inspected scope and limitations, not project-wide freshness |
| An interview ends without a request to save and no path is configured | The discussion stays in chat without triggering setup |
