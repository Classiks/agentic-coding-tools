# Choose meaningful checks

Apply only relevant rows; this is not a mandatory checklist for every patch.

| Changed area | Questions the evidence should answer |
| --- | --- |
| UI and interaction | Is the relevant flow reachable and usable at affected viewport sizes, with focus, keyboard, accessibility, and motion behavior accounted for? |
| Async behavior | What happens on delay, cancellation, navigation, out-of-order completion, repetition, and recovery? |
| Persistent state | Do refresh, stale writes, concurrency, identity, atomicity, isolation, and recovery preserve required behavior? |
| External adapter | Which contract properties can doubles prove, and which need an authorized real-boundary check? Do failure and retry behaviors match? |
| State transitions | Are empty, invalid, skipped, repeated, and stale transitions handled according to the domain rules? |
| Migration | Are ownership, preserved data, repeatability, and recovery demonstrated with suitable fixtures? |
| Model-driven behavior | Is orchestration deterministic where possible, and which claims need selected live scenarios rather than mocked model output? |

Derive expected outcomes independently from requirements or established contracts.
Test policy at the lowest useful level. Use narrow fakes through normal injection,
not large mock graphs that reconstruct implementation internals. A test that copies
the production calculation for its expected value may reproduce the same defect.
For a regression, show that the test can detect the reported failure where practical,
without destructive rollback of the user's tree or a universal test-first sequence.

During development, use as many meaningful exploratory checks as needed; they may be
redundant or implementation-specific. Before handing over each review-ready slice,
curate new and changed tests: what requirement, regression, invariant, or boundary does
each protect, and is that protection worth its maintenance cost? No written essay per
test is needed. Keep readable scenarios with explicit expectations and small fixtures;
cheap execution alone does not justify a test with no useful failure signal.

Remove low-value exploratory clutter while preserving necessary coverage. Record useful
probe observations before removal as historical evidence. Do not remove a meaningful
failing test merely to produce a green suite or rewrite user-authored tests outside
scope. After cleanup, rerun applicable maintained checks against the delivered state.

Do not force a code test for a purely editorial change. Document and skill edits need
appropriate format, reference, and behavioral checks; distinguish static inspection
from an executed agent evaluation. No claim of runtime reliability follows from valid
Markdown. Where a behavior cannot be tested in the available environment, state the
specific missing evidence and its implication.
