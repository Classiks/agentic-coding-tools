# Implementation, verification, and diagnosis scenarios

| Scenario | Expected behavior |
| --- | --- |
| Implementation mandate, known in-scope defect found during checks | Fix without another approval round, rerun affected checks, record meaningful finding |
| Read-only verification finds the same defect | Report it without editing code |
| An unrelated bug is discovered | Record a distinct finding in requirements mode; do not expand implementation |
| Intent is ambiguous | Pause affected work for a domain decision; continue independent authorized work |
| A coherent implementation cannot be split without temporary abstractions | Keep it coherent; divide the later tour into smaller portions |
| Stepwise rhythm | Verify a slice and pause at the agreed review boundary |
| Longer autonomous rhythm with full ownership | Continue checked implementation slices; retain complete pending human review |
| User changes only work rhythm | Preserve permissions and review coverage |
| Code is written before tests | Allow it; require meaningful verification and appropriate regression coverage |
| Suite is green but one acceptance criterion is unobserved | Mark that criterion unverified |
| Expected test result duplicates the faulty production computation | Identify weak evidence and derive expectation from intended behavior |
| A required check cannot run | Name the gap; do not replace it silently with inspection or install tools |
| A baseline failure is unrelated | Establish that with evidence; avoid unrelated fixes and report the remaining required-check failure |
| A later slice changes previously verified behavior | Rerun affected checks and reopen affected human coverage |
| Current evidence still applies | Reuse it rather than rerun solely due to another message |
| Temporary probe is removed | Preserve its historical result and rerun applicable maintained checks on final code |
| An intermittent bug disappears once | Do not claim causality or resolution from a single clean run |
| Reproduction is unavailable | Allow useful inspection while distinguishing suspected cause from demonstrated evidence |
| Diagnostic attempts yield no new evidence | Report the concrete blocker rather than speculate indefinitely |
| All checks pass but human review is outstanding | Report verified implementation and outstanding review separately; no commit or acceptance inference |
| Editorial-only change | Use proportionate document checks rather than inventing a code test |
| Verification is called from an active guided review | Return evidence to that review; do not start another tour or reload the whole workflow |
| Development used redundant temporary probes | Curate new/changed retained tests for useful protection and maintenance cost; preserve meaningful failures |
