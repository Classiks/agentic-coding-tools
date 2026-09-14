# Plane configuration

Keep these values in the adapter-owned subsection of the project's knowledge section,
or in an explicitly referenced non-secret configuration file. These are Plane-specific
fields; they do not belong in the generic AGENTS.md template.

| Field | Meaning and resolution |
| --- | --- |
| Workspace slug | Must match the existing authenticated connection and compatibility record |
| Project UUID | Target of every project-scoped operation |
| Project identifier and name | Human-readable cross-checks; resolve a missing UUID using `project(action="list")`, matching identifier and name, then retain the actual UUID |
| Entry record | Object kind `page` or `workitem`, UUID, and expected title; include project UUID for project Pages |
| Compatibility record | Explicit path to the deployment's operation results and version information; see transport reference |
| Object mapping | Existing locations for requirements/tasks, glossary, ADRs, findings, and continuation records; use defaults below only if no established convention conflicts |
| State and kind mapping | Semantic state names and kind labels mapped to existing project names or IDs; resolve names with state/label list |
| Creation state | Explicit existing state for proposed new work; never rely silently on a server default |
| Page access | Existing project's intended visibility value for newly created Pages; preserve existing visibility on updates |

Existing declarations such as `Plane workspace slug`, `Plane project`, `Plane identifier`,
`Plane documentation index`, and `Plane documentation index ID` can supply these values.
Read and resolve them rather than creating a conflicting second declaration. A title
checks the retrieved identity; it does not replace a UUID. A missing or renamed title
requires inspection, not automatic recreation. Project creation and access changes
are outside ordinary knowledge setup.

## Default content mapping

When the project has no conflicting convention, propose this mapping during setup:
- Requirements, tasks, and bug findings are work items.
- Glossary and ADRs are project Pages, linked from the entry record.
- Evidence and current continuation state live in sections of the corresponding item.
- The entry record links the glossary, decision index or individual ADRs, and active
  work. Do not maintain a second copy of those records in the index.

Explicit project exceptions override these defaults. ADRs may instead use work items
with a decision kind if that is the project's existing choice. Do not silently choose
work items because Page transport is unavailable. Confirm the required access before
claiming the mapping is usable.

## Fresh-context resolution

Read configuration, resolve project identity, retrieve the entry record by kind and ID,
then follow the active-work reference and only relevant glossary/ADR/spec links. If the
entry or active task is missing, locate candidates through the search recipes and
resolve ambiguity before selecting an authoritative replacement. A new record is not
fully discoverable until its entry or parent reference is saved and verified.

Credentials and connection launch commands remain in existing host/deployment setup.
No passwords, tokens, private environment files, or service identities belong in the
project declaration. A portable package contains no fixed personal-machine paths.
