# Authoring a knowledge adapter skill

A knowledge adapter supplies access to a project's authoritative information. It can
be referenced in the `Project knowledge` section of AGENTS.md. The shared template
and domain methods do not enumerate storage implementations. Add a new adapter
without changing those methods or introducing a new common configuration field for
each backend.

Read the [shared contract](../skills/project-knowledge/SKILL.md). The adapter implements
its storage responsibilities; it does not redefine requirements, interviewing,
decision authority, implementation permissions, or review policy.

## What the skill must specify

| Responsibility | Instructions the adapter must supply |
| --- | --- |
| Selection | A precise description explaining when the adapter applies; being installed does not make it the project's default |
| Configuration | Required source identities, scope, entry reference, and access prerequisites; distinguish reusable instructions from project-specific values |
| Discovery | How to locate existing records and active work without chat history, including any pagination or incomplete-search limitations |
| Reading | How to retrieve current authoritative content, relevant relationships, and decision context |
| Identity and references | Stable record identities, references between records, and how new records become discoverable from the entry point |
| Writing | How to update a matching record, create a genuinely new one, preserve unrelated contributions, and maintain relationships |
| Verification | How to read back changes and distinguish successful, partial, failed, and uncertain operations |
| Conflicts and retries | Available revision checks or other conflict handling; detect uncertain earlier success before retrying creation; disclose lack of atomicity |
| Limits | Unsupported information types or operations, unavailable access, and actual storage limitations |

Support the information types selected for the project: requirements, tasks, domain
terms, decisions, findings, and continuation records. If an adapter cannot handle a
required type, report the gap so the project can choose an explicit exception. Never
silently create another authoritative store.

Keep required backend details in the adapter, using references for substantial
conditional instructions. Do not include credentials in skill files or AGENTS.md;
describe how existing authorized access is located. The current package requires no
new installations. An adapter that needs missing tools is unavailable until those
prerequisites are deliberately provided.

## Referencing an adapter from AGENTS.md

Use the [generic section template](../skills/setup-project/references/agents-section.md).
Fill the template with the adapter's source identities, entry reference, and project
configuration. For example, `Adapter: team-knowledge at .agents/skills/team-knowledge/SKILL.md`
resolves an installed method without copying it into AGENTS.md. A name alone is insufficient
if the host cannot locate it. Do not assume automatic loading.

An inline adapter can describe the same responsibilities directly in AGENTS.md.
No skill wrapper is required merely to satisfy the contract. Conversely, when a skill
provides the method, AGENTS.md should supply project values and reference it rather
than duplicate the method text.

## Review before use

Check a fresh-context lookup, update of an existing record, creation and subsequent
discovery, a conflicting edit, unavailable access, and an ambiguous write result.
Use fixtures or an explicitly authorized test area. Do not test writes against a
live project implicitly. Report which behaviors were actually exercised and which
remain instructions only; valid Markdown does not prove a reliable adapter.

Keep provenance and license notices for reused instructions. Package required files
with the skill and preserve relative references. The existing adapters can illustrate
implementations, but their storage choices are not part of the common contract.
