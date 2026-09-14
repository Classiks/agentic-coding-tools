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

Use [project-knowledge](../project-knowledge/SKILL.md) for durable requirements and
[requirements](../requirements/SKILL.md) for findings when that mode is selected.
Diagnosis alone does not authorize fixes. Within an existing mandate, fix the supported
in-scope cause and add useful regression coverage; test-first is optional.

Remove only your disposable diagnostic changes, preserve useful tests and others' work,
and recheck after cleanup. Return findings to an active implementation/verification
workflow. If working independently on an authorized fix, use
[verify-change](../verify-change/SKILL.md) for final checks. Report cause, evidence,
changes, and uncertainty. Unrelated bugs remain findings.

Adapted from [Matt Pocock](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/diagnosing-bugs/SKILL.md). MIT, see LICENSE.
