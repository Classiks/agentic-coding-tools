# Map semantic changes to Plane

The method supplies the requested change and its authority. The adapter resolves
Plane representations and checks the saved result. Do not implement an independent
approval workflow in this adapter.

List states with `state(action="list", project_id=P)` and labels with
`label(action="list", project_id=P)`. Resolve configured names to UUIDs and check
uniqueness within the project. Preserve mappings already chosen by the project.
If a required state or label is missing, report it; do not create workflow vocabulary
or substitute a vaguely similar state without a setup decision.

The user's existing Plane workflow uses the following mapping. Adopt it only where
configured, rather than requiring all projects to use these names:

| Supplied semantic state | Existing Plane state |
| --- | --- |
| Captured, not yet clarified | Inbox |
| Clarification or unresolved product intent | Exploring |
| Approved for implementation | Ready |
| Implementation active | In progress |
| Evidence ready for review | Verification |
| Accepted | Done |
| Rejected | Rejected |

For this mapping, `blocked` is an independent label, not a state. Kind is one of
`idea`, `requirement`, `decision`, `bug`, `technical-debt`. Use exactly one kind label
where that convention is selected, preserving other labels. When changing kind, remove
only the prior kind and add the new one using manage_label; read back and report partial
updates. Other projects may provide different explicit mappings.

Update a supplied state with workitem.update(state=resolved UUID), then retrieve and
verify. Resolve only the active items identified by the method, not an entire future
batch. Missing evidence or disagreement with code is a finding; it does not authorize
reversing an accepted state. Preserve explicit user transitions and request a decision
on ambiguous conflicting changes. Ready/Done names alone do not establish who approved
what; the method and recorded project authority determine that.

If acceptance authorizes updating descriptive Pages, the method supplies which claims
are now established. The adapter updates and verifies those Pages through normal
record operations. It does not wait for acceptance to save a desired-outcome proposal,
nor present a proposal as already implemented behavior.

Archive/restore only on an in-scope request, through the classified transport route.
Check current state and tool restrictions first; never mark an item completed merely
to satisfy archive preconditions. Preserve IDs and references. Deletion of Pages or
work items has no verified recipe in the inspected deployment and is outside ordinary
maintenance. Do not use an available delete command as proof it is supported or allowed.
