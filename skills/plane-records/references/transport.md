# Plane operation routing

## Existing access, not installation

Use the supplied Plane MCP tools by their current signatures. Names below are tool
resource names; a host may prefix them. Read the exact compatibility record configured
by the project or its deployment. Do not discover credentials or guess helper paths.

The existing record format contains `plane_ce`, `plane_mcp`, `tested_at`, `workspace`,
`rest_helper`, and `operations`. Each operation records `mcp` as `passed`, `missing`,
or `broken`; tested fallbacks also name `rest` and `rest_status="passed"`.

Check workspace and known deployment versions against the intended connection. A
version mismatch invalidates the old capability assumption. Unknown current versions
must be reported as unverified; do not silently label the old record current. A
successful operation verifies that operation only, not the entire deployment.

- `mcp="passed"`: use its matching supplied tool/action.
- `mcp="missing"` or `"broken"` plus `rest_status="passed"`: use the explicitly named
  existing `rest_helper` and subcommand, after checking its help matches this recipe.
- No classified result: treat as unverified. Safe read probes can establish current
  read capability. Do not test writes implicitly on live project data.
- A failed passed operation is a new failure, not permission to invent a REST fallback.

Do not change the compatibility file silently to claim success. Report newly observed
results and update deployment records only when maintaining them is in scope.

## MCP operations and compatibility keys

| Compatibility key | Tool/action and required values |
| --- | --- |
| project.list | `project(action="list")` |
| state.list | `state(action="list", project_id=P)` |
| label.list | `label(action="list", project_id=P)` |
| workitem.search | `workitem(action="search", query=Q)` |
| workitem.retrieve | `workitem(action="retrieve", project_id=P, workitem_id=I)` |
| workitem.create | `workitem(action="create", project_id=P, name=T, state=S, description_html=H)` |
| workitem.update | `workitem(action="update", project_id=P, workitem_id=I, <only changed fields>)` |
| workitem.manage_label | `workitem(action="manage_label", project_id=P, workitem_id=I, add_label_id=L or remove_label_id=L)` |
| workitem.comment.create | `workitem_comment(action="create", project_id=P, workitem_id=I, comment_html=H)` |
| page.list | `page(action="list", project_id=P)` |
| page.retrieve | `page(action="retrieve", project_id=P, page_id=D)` |
| page.create | `page(action="create", project_id=P, name=T, description_html=H, access=A)` |
| page.update | `page(action="update", project_id=P, page_id=D, <name and/or description_html>)` |
| page.archive / page.unarchive | `page(action="archive", project_id=P, page_id=D, archive=true/false)` |
| workitem.archive / workitem.unarchive | `workitem(action="archive", project_id=P, workitem_id=I, archive=true/false)` |

Additional read capabilities include `workitem_comment` list/retrieve and
`workitem_relation` list/list_definitions. Supplied signatures alone do not establish
compatibility. Probe safe reads when needed. Native relationship creation and Page
attachments need their own tested capability; text references are the supported
alternative described in records.md.

## Existing REST helper recipe

Use exactly the configured executable path, quoted safely, followed by the registered
subcommand. `P`, `D`, and `I` below are resolved UUIDs, not names. Check
`<helper> <subcommand> --help` without authentication or writes first. If the help or
implementation no longer matches, stop instead of guessing changed arguments.

| Operation | Arguments after the helper path |
| --- | --- |
| List project Pages | `page-list P` |
| Retrieve a Page | `page-get P D` |
| Create a Page | `page-create P TITLE --access A --description-stdin` |
| Update body | `page-update P D --description-stdin` |
| Update title, optionally body | `page-update P D --name TITLE [--description-stdin]` |
| Archive / restore Page | `page-archive P D` / `page-unarchive P D` |
| Archive / restore work item | `workitem-archive P I` / `workitem-unarchive P I` |

For body writes, put the exact HTML in a temporary file and supply it on stdin using
safe shell quoting. Do not interpolate prose or secrets into executable shell text.
Retrieve with `page-get` after Page writes; use tested workitem.retrieve after work-item
archive operations. If archived records cannot be retrieved, use a verified archived
listing; otherwise report the verification limitation rather than infer success.

The existing helper reads its credentials from the established environment or a
configured secrets file and performs session authentication itself. Never read or
print those credentials to construct a call. It offers no generic work-item CRUD,
relation, or comment fallback. The bundled `scripts/plane_rest.py` implements these
recipes using Python 3.10+ and the standard library. Select it through deployment
configuration; never switch transport merely because the file is present.

When replacing an old plane-work installation, point its launcher at the installed
plane-records helper and explicitly configure PLANE_SECRETS_FILE or the required
environment variables. The helper has no machine-specific secrets-file default.
