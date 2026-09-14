---
name: ux-prototype
description: Explore UX uncertainty with flows, wireframes, mockups, or interactive prototypes before production implementation; offer useful design alternatives.
---

# UX and prototyping

Read the user's task, audience, product conventions, and relevant requirements.
Use [project-knowledge](../project-knowledge/SKILL.md) for durable sources or decisions.
Do not restart settled interviews; clarify only gaps that materially affect the design.

Choose the cheapest artifact that makes the current uncertainty inspectable:

| Question | Starting artifact |
| --- | --- |
| Can the user accomplish the task, including failure paths? | User flow |
| Is navigation and information hierarchy clear? | Rough wireframe |
| Does the interaction or state model work? | Clickable prototype with representative data |
| Does visual treatment work? | Polished mockup |

These are alternatives, not required stages. Start at low fidelity and add polish when
it helps the decision. Appearance does not imply settled behavior.

## Variants and artifacts

Offer multiple versions when materially different approaches are plausible. Generate
them when requested, comparing the same scenario and explaining tradeoffs. Recommend
without inventing agreement. Cosmetic variants suit visual questions. If an optional
offer goes unanswered, proceed with a stated approach within existing authority.

Use existing local tools and project conventions. A temporary app preview or
self-contained HTML may suffice; a flow needs no application. Keep prototypes
recognizable and separate from production behavior. External design services require
a request and available access.

Use realistic data density and fixtures. Make relevant state changes visible, include
the awkward case being investigated, and provide a reset or known starting scenario.
Real persistence or external mutations need an authorized purpose. Make requested
variants easy to compare without building unnecessary comparison infrastructure.
Keep implementation commentary outside the product experience.

## Check and learn

Check the artifact opens/runs and exercises the intended scenario. Cover relevant
interaction, keyboard, viewport, and simulated failures with existing tools. If rendering
or interaction cannot be exercised, say what was inspected and what remains untested.
A mockup proves neither backend correctness nor usability with actual users.

Provide the artifact/preview, any run instructions, scenario to try, and simulation gaps.
Invite focused feedback and iterate. When persisting, record the question, artifact
reference and version, actual decision/rationale, and open questions through the adapter.
Local prototype code is an artifact, not a second authoritative decision record.
Use [requirements](../requirements/SKILL.md) when findings change requirements in that mode.

Design preference adds no production authority. Reuse prototype code only as an explicit
decision with normal implementation and verification obligations; neither automatic
promotion nor mandatory rewriting is justified. Retain or remove alternatives as agreed.

Adapted from [Matt Pocock](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/prototype/SKILL.md). MIT, see LICENSE.
