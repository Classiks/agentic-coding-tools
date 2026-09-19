# Plane records

This skill stores project knowledge in Plane through existing configured access.
Select it as the knowledge adapter when requirements, decisions, or continuation records
belong there. Implementation and verification remain separate methods.

## Prerequisites

- An identified workspace, project, entry record, and content/state mapping.
- Existing authorized Plane MCP access or an explicitly configured, tested REST helper.
- A compatibility record describing which operations work through which transport.

Use [configuration](references/configuration.md) to supply project values and
[transport](references/transport.md) to check the required capabilities. The skill includes [a REST helper](scripts/plane_rest.py) using Python 3.10+ and its
standard library. It installs no server or packages. Configure `PLANE_BASE_URL`,
`PLANE_WORKSPACE_SLUG`, `PLANE_SERVICE_EMAIL`, and `PLANE_SERVICE_PASSWORD` in the
existing environment, or set `PLANE_SECRETS_FILE` to a private `KEY=value` file.
Existing environment values take precedence; the file is read literally, not executed.

Point the deployment's `rest_helper` or existing launcher at the installed script.
Keep credentials in deployment configuration, outside this skill. Use only operations
verified for that deployment; shipping the helper does not establish compatibility.


## Capabilities and limits

[Record recipes](references/records.md) cover requirements/tasks, glossary and ADRs,
findings, evidence, and continuation. [State mapping](references/states.md) translates
authorized semantic changes into project-specific states and labels.
[Failure handling](references/failures.md) addresses uncertain writes, conflicts, and
partial operations.

Support depends on the actual deployment. Signatures and historical successful reads
do not prove current write compatibility. Verify the operations needed by your mapping
in an authorized test area. Native relations and comments require their own capabilities;
comments also require communication authority. Multiple writes are not a transaction,
and read-before-write cannot guarantee concurrency safety without backend support.

This adapter replaces storage procedures, not all behavior of an older Plane workflow.
It does not impose local ADR storage, an implementation ban during outages, continuous
execution, or automatic acceptance based on tracker status. Choose those workflow
policies separately where appropriate.
