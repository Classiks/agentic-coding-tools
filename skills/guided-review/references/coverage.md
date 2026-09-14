# Coverage and resumption

## Inventory the actual change

Determine the intended baseline and task boundaries; do not assume HEAD~1 or that
all dirty files belong to the task. Preserve overlapping user work and clarify it
when ownership affects scope.

With Git, inspect status, the relevant committed comparison, staged and unstaged diffs,
and baseline-to-working-tree changes. Ordinary diffs omit new files; list them with
`git ls-files --others --exclude-standard` and inspect separately. Include mode/type
changes and both sides of renames/deletions. Do not stage or commit for convenience.

Full ownership includes tests, config, docs, generated text, and any ignored artifacts
that are actual deliverables. Inspect binary changes through suitable previews or tools;
uninspectable artifacts remain coverage gaps. No mechanical-change exemption applies.

## Track confirmed content

Use a compact session record. For durable resumption, apply
[project-knowledge](../../project-knowledge/SKILL.md) and store it with the work item.
Ordinary review can proceed without configuring storage.

Record the baseline, complete inventory, mode, and for each portion:

- ID, exact file ranges/artifacts, and old/new side.
- Checkable content identity, not line numbers or timestamps alone.
- Pending, presented, confirmed, or needs renewed review.
- Explicit user confirmation and the content state it covered.
- Verification evidence and gaps, separate from confirmation.

Use existing versions, content digests, or snapshots for dirty states. A commit alone
is insufficient. File digests are conservative; if one changes and the affected portion
cannot be identified reliably, reopen that file's portions. No new service is needed.

## Reassess changes and resume

Before accepting confirmation, check for intervening edits. Refresh the inventory
before later portions and final handoff. Add new changes; reopen modified portions and
unchanged callers whose meaning changed through dependencies. Refresh affected checks.
Preserve old confirmations as history. Pure line shifts only update navigation when
content and meaning are demonstrably unchanged.

On resumption, retrieve the record and compare actual files and requirements. Missing
content identity or confirmation provenance means pending coverage, not reconstructed
approval. Disclose concurrent edits that prevent a stable comparison.

Full ownership finishes only when every current change is accounted for and confirmed.
Renames need acknowledgment and removals baseline-side inspection. Disclose review
bookkeeping without recursively reviewing its own confirmations; other docs remain
in scope. Focused mode names omissions. Changing mode never relabels pending work as
confirmed, and completed review grants no additional commit or acceptance authority.
