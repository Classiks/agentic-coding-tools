---
name: to-spec
description: Turn a settled discussion into a specification with acceptance examples, using the configured store without restarting the interview.
---

# To spec

Use [requirements](../requirements/SKILL.md) for content rules and
[project-knowledge](../project-knowledge/SKILL.md) for durable sources and results.
Synthesize current discussion and sources; do not restart Grilling. Link established
terms and ADRs. Ask only about consequential gaps that block the requested result.

Cover the problem, desired behavior, boundaries, acceptance examples, and unresolved
choices. Reference technical decisions and meaningful verification opportunities when
known. Scale detail to the task; require neither a story quota, exhaustive implementation
plan, nor TDD. Small illustrative models help; a full prototype does not belong here.

Update the canonical specification with actual decision status. Saving it does not
authorize implementation, but an existing end-to-end mandate remains valid.

Adapted from [Matt Pocock](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/to-spec/SKILL.md). MIT, see LICENSE.
