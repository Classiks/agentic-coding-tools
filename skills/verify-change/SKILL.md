---
name: verify-change
description: Check changes against intended behavior and repository gates, reporting evidence for the actual state rather than test volume or human acceptance.
---

# Verify a change

Read the request, established contracts, project checks, and complete intended change,
including staged, unstaged, new, removed, and configuration files. Use
[project-knowledge](../project-knowledge/SKILL.md) for durable sources. Expected behavior
comes from requirements, not whatever the implementation does.

Select checks that observe promised outcomes and changed integration boundaries.
Use [checks and test curation](references/checks.md) for relevant risks and retained tests.
Run the repository's applicable formatter, type checker, linter, tests, build, and
required integration/end-to-end checks with existing tools. Report unavailable required
checks; manual inspection cannot silently replace them.

Inspect actual outcomes and whether assertions would detect the failure. A green suite
or implementer's claim alone proves no criterion. Check during meaningful progress and
against the final state. Reuse still-valid evidence; rerun affected checks after fixes,
cleanup, or interacting changes. Broaden only when changed risk or failures warrant it.

Report each criterion as supported, failed, or not verified, with command/scenario,
observed result, checked content state, and limitations. A commit alone cannot identify
dirty work. Removed probes are historical evidence, not maintained reproducible tests.

Within an implementation mandate, fix in-scope failures and recheck. A standalone
read-only verification grants no edit authority. Use [diagnose-bug](../diagnose-bug/SKILL.md)
for unclear causes, then resume here. Distinguish baseline failures from regressions
using evidence; neither waive required failures nor repair unrelated code implicitly.
Persist findings/evidence through the configured contract when in scope.

Return results to the caller. Human review is a separate stage owned by
[guided-review](../guided-review/SKILL.md); do not restart an active review from here.
A failed or insufficiently verified change is not ready, though a requested informational
tour may proceed with gaps disclosed. Verification does not establish user acceptance.

Adapted from the user's Plane verification and implementation-slices guidance; no Plane runtime dependency.
