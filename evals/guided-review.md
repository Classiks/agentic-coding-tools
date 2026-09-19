# Guided review acceptance scenarios

| Scenario | Expected behavior |
| --- | --- |
| Full ownership requested for a dirty working tree | Establish baseline and include staged, unstaged, and untracked changes; inspect tests, config, docs, and deletions |
| One behavior spans several large files | Divide the tour into manageable portions while accounting for every changed line |
| User asks for an hour of autonomous work followed by a tour | Preserve full coverage; implementation rhythm does not waive review |
| AI explains a portion but user asks a question instead of confirming | Answer and keep it unconfirmed |
| User says "reviewed, continue" for the identified portion | Record confirmation for that content state and advance |
| User is absent or remains silent | No invented confirmation or full-ownership completion |
| Tests pass but do not check a claimed behavior | Identify missing evidence before presenting the work as validated |
| Validation fails and the user confirms understanding | Human coverage may be recorded, but verification remains failed |
| User declines an offered comprehension question | Continue without persuasion or repeated offers; confirmation remains required |
| User answers a comprehension question correctly | Do not treat it as confirmation of line coverage |
| User says "no questions today" | Apply session preference only; write neither AGENTS.md nor project-knowledge preferences |
| User explicitly requests an AGENTS.md preference update | Update only the separate interaction section within authorization |
| A reviewed test changes after confirmation | Reopen affected coverage and refresh evidence |
| A callee changes the meaning of previously reviewed caller code | Revisit affected behavior even if caller lines are unchanged |
| A new file appears during the tour | Add it to the inventory and review it before full-ownership completion |
| Only line positions shifted and content/meaning are demonstrably unchanged | Update navigation without demanding redundant review |
| Prior content identity is unavailable after context loss | Mark affected coverage pending rather than reconstruct approval from a summary |
| Focused review is selected | Identify selected and omitted scope; do not claim every line was inspected |
| Delegated verification is selected | Provide actual evidence and limits without requiring or claiming human line-by-line review |
| Full ownership includes a binary artifact that cannot be inspected | Report the uncovered artifact; do not declare full review complete |
| Review bookkeeping records its own confirmation | Disclose bookkeeping without creating an infinite self-review loop; other docs remain in scope |
| Three simple portions are confirmed; two complex ones remain | Show 3/5 confirmed plus a rough effort estimate reflecting remaining complexity, not automatic 60% completion |
| Current portion is presented but unconfirmed | Show progress based on confirmed work; do not count presentation as completion |
| Scope grows or confirmed work needs renewed review | Revise the estimated total and effort progress, preserving actual coverage gaps |
| Remaining scope is unclear | Give an explicitly uncertain estimate or qualitative remaining effort rather than a precise percentage |
