---
name: domain-modeling
description: Refine domain terminology, relationships, and consequential design decisions; use for model or ADR changes, not merely reading a glossary.
---

# Domain modeling

For durable sources or results, use [project-knowledge](../project-knowledge/SKILL.md).
Compare relevant terms, decisions, and code. Challenge overloaded names with concrete
scenarios, suggest precise alternatives, and expose contradictions. Code does not
establish desired behavior. Join an active interview rather than duplicate it.

Define project-specific terms in one or two sentences. Identify confusing alternatives
where useful, for example an invitation grants a time-limited opportunity to join;
membership exists after acceptance. Preserve established domain-context ownership and
link related glossaries. General programming terms need no glossary entry.

Offer an ADR for a consequential tradeoff that is costly to reverse or surprising
without context, or write one on request. Include context, actual decision, rationale,
and useful alternatives or consequences. Mark proposals explicitly. Never infer
historical reasons from code; link superseding decisions without erasing predecessors.

The glossary owns language, the specification desired behavior, and ADRs rationale.
Link instead of copying. Configuration selects each location; a local CONTEXT.md does
not imply local ADRs.

Adapted from [Matt Pocock](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/domain-modeling/SKILL.md). MIT, see LICENSE.
