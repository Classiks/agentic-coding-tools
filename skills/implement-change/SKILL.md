---
name: implement-change
description: Implement an authorized change in coherent slices, self-verify, and hand off at the requested rhythm and human-review coverage.
---

# Implement a change

## Establish the agreement

Read the task, project instructions, relevant code/tests, and actual working tree.
Identify scope and baseline, preserving pre-existing work. Resolve only missing
consequential decisions; existing authorization persists.

Keep scope, action permissions, quality investment, work rhythm, and review coverage
independent. State the effective agreement briefly. Without a specified rhythm,
implement the authorized coherent change and hand it off. Do not infer a waiver of
full ownership or claim human review when coverage is unknown.

Load [requirements](../requirements/SKILL.md) when requirements-driven work is selected
and [project-knowledge](../project-knowledge/SKILL.md) for durable sources or records.
Load optional methods only when relevant. Reuse instructions already in context.

## Implement and validate

For substantial work, outline coherent slices with outcomes and checks. A small change
needs no planning artifact. A slice may span several review portions; do not manufacture
small diffs through disposable adapters, duplicated logic, or worse architecture.

Implement within scope and project rules. Include meaningful regression coverage for
behavior changes; tests may follow code but should accompany useful progress.
Use [verify-change](../verify-change/SKILL.md) at checkpoints and before handoff.
Fix in-scope self-check defects without another approval round, then recheck. Investigate
unclear causes with [diagnose-bug](../diagnose-bug/SKILL.md), returning to this workflow.
Record substantive findings under the selected requirements/knowledge rules.

Pause only affected work for missing decisions, authority, or blocking dependencies.
Continue independent authorized work. If attempts produce no new evidence, report the
concrete blocker. Do not hide failures by weakening tests or shrinking promised behavior.
Out-of-scope bugs remain findings unless additional work is authorized.

## Respect rhythm and hand off

For stepwise work, validate the slice and use [guided-review](../guided-review/SKILL.md)
at the agreed boundary. For autonomous work, continue ready slices after checks and
provide the tour at handoff. Longer autonomy changes timing, not review coverage.

Verify the final state, including interactions between slices and documentation effects.
Report behavior, evidence, open findings, and pending human review separately. Later
edits require reassessing affected evidence and confirmations. Follow guided-review
for human coverage; delegated verification makes no claim of human inspection.
Implementation alone grants no authority to commit, install tools, or send messages.

Adapted from the user's Plane implementation guidance and [Matt Pocock](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/implement/SKILL.md). MIT notice for the latter in LICENSE.
