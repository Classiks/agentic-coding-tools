---
name: diagnose-bug
description: Investigate unclear bugs and regressions. Obvious fixes need no diagnostic workflow.
---

# Diagnose a bug

- Establish expected and observed behavior. Seek a repeatable signal. For intermittent failures, record conditions and frequency. One clean run is insufficient.
- Predict outcomes that distinguish plausible causes. Run the best experiment and update the explanation. Avoid speculative patches. Compare performance under comparable conditions.
- Inspect code even without reproduction. Label suspicions. When experiments stop yielding evidence, report what you know and what observation or access is missing.
- For any induced failure, diff the tested code or fixture against its original. Verify the mutation landed and the failure has the expected cause.
- Read expectations and record substantive findings through [project-knowledge](../project-knowledge/SKILL.md). Include expected and observed behavior, reproduction, supported cause, and fix evidence.
- Fix only the supported, authorized cause and add useful regression coverage. Test-first is optional. Diagnosis alone grants no fix authority. Record unrelated bugs.
- Remove your disposable changes. Preserve useful tests and others' work. For authorized fixes, rerun the original reproduction and applicable repository checks against the final state. Report cause, evidence, changes, and uncertainty.

Adapted from [Matt Pocock](https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/skills/engineering/diagnosing-bugs/SKILL.md). MIT, see LICENSE.
