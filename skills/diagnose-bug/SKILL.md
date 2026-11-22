---
name: diagnose-bug
description: Investigate an unclear bug or regression with evidence and discriminating experiments; obvious fixes need no separate diagnostic workflow.
---

# Diagnose a bug

Establish expected versus observed behavior and seek a repeatable signal. Tests,
captured inputs, a debugger, or measurements may suffice. For intermittent failures,
record conditions and frequency; one clean run does not prove a fix.

State plausible causes and predictions that distinguish them. Run the most useful
experiment, update the explanation, and avoid accumulating speculative patches.
Compare performance under comparable conditions. Inspect code even without reproduction,
but label suspected causes honestly. If attempts stop producing evidence, report what
is known and what observation or access is missing.

Use [project-knowledge](../project-knowledge/SKILL.md) when reading expected behavior
or recording substantive findings. Record expected and observed behavior, reproduction
details, the supported cause, and any evidence of a fix.
Diagnosis alone does not authorize fixes. Within an existing mandate, fix the supported
in-scope cause and add useful regression coverage; test-first is optional.

Remove only your disposable diagnostic changes and preserve useful tests and others'
work. For an authorized fix, check the reported failure and run the applicable
repository checks against the final state. Report cause, evidence, changes, and
uncertainty. Unrelated bugs remain findings.

Adapted from [Matt Pocock](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/diagnosing-bugs/SKILL.md). MIT, see LICENSE.
