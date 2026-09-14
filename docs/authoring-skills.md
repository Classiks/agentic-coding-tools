# Write skills that earn their context

Start from an actual task and a correction the agent needed. Write the smallest procedure
that would change that decision next time. Generic advice such as "write clean code"
rarely justifies a skill. This follows the [Agent Skills authoring guidance](https://agentskills.io/skill-creation/best-practices).

1. Give the skill one recognizable job. Put its trigger in the description and distinguish
   likely neighboring tasks. "Read a glossary" should not activate domain redesign.
2. Keep task-specific decisions in the prompt, stable project rules in AGENTS.md, and
   reusable methods in skills. Adapters own backend mechanics.
3. Put common instructions in SKILL.md. Add references only for substantial conditional
   detail and state when to read each. Tiny formats can stay inline.
4. Use existing judgment for ordinary steps. Be precise about fragile behavior, such as
   uncertain writes or invalidated review confirmations. Add no approval gate the task
   did not need.
5. Link required methods explicitly, preserve sibling paths, and avoid recursive handoffs.
   A link is an instruction to read when needed, not a dependency loader. Reuse loaded
   instructions while they remain current.
6. Retain upstream links, revisions, and license notices when adapting work. Describe
   material departures in SOURCES.md instead of repeating an adaptation essay per skill.

The [format specification](https://agentskills.io/specification) requires YAML frontmatter
with a nonempty description of at most 1,024 characters and a matching lowercase directory
name of at most 64 characters. This package uses only name and description. Host-specific
metadata is unnecessary until a concrete integration needs it.

## Keep documentation useful

The root README explains the project and its first use. Shared usage and authoring
procedures belong in docs. Put human setup instructions in a skill-specific README
only when needed; agent instructions remain in SKILL.md and conditional references.
Keep reports in the conversation. Extract lasting lessons into the relevant maintained
guide instead of accumulating progress reports or histories of superseded proposals.

Preserve existing task authority across method handoffs. Pure discussion needs no storage
setup, and a helper should return to its caller rather than restart the active workflow.
Shorter text is useful only if it preserves these decisions and fragile operational rules.

## Evaluate the decision, not the wording

Before changing a skill, choose a realistic success case and a near miss where it should
stay inactive. Also test the costly failure it is meant to prevent. Examine the trace
for wrong files, repeated loading, needless questions, and unsupported completion claims.
Compare with the previous skill or no skill using equivalent fixtures and host/model
settings. Keep outputs and checked repository states; a single good run is preliminary
feedback, not reliability evidence. See [Agent Skills evaluation guidance](https://agentskills.io/skill-creation/evaluating-skills).

Validate frontmatter, local references, and the copied installation separately from
behavior. Existing skill-creator validation can check metadata; it does not execute the
workflow. Use [our cases](../evals/README.md) for manual runs without installing an evaluator.
A new knowledge adapter must also satisfy [the adapter authoring contract](authoring-knowledge-adapters.md).
