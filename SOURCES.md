# Sources and adaptations

## Reused skills

Matt Pocock sources are pinned to revision `3cca18b368ae95cdbdebbff572ccafa662551015`
of [mattpocock/skills](https://github.com/mattpocock/skills/tree/3cca18b368ae95cdbdebbff572ccafa662551015).
Each derived skill has a direct source link and the original MIT notice in its directory.

| Skill | Upstream path below skills/ | Retained method and material departures |
| --- | --- | --- |
| grilling | productivity/grilling/SKILL.md | Decision dependencies and fact investigation; no mandatory subagents or exhaustive interview |
| grill-with-docs | engineering/grill-with-docs/SKILL.md | One interview with domain modeling; portable references and optional synthesis |
| domain-modeling | engineering/domain-modeling/SKILL.md and CONTEXT-FORMAT.md / ADR-FORMAT.md | Precise terminology and decision rationale; inline short formats, configured storage, historical status preserved |
| to-spec | engineering/to-spec/SKILL.md | Synthesis; no tracker mandate, story quota, test-seam approval, or automatic Ready transition |
| to-tickets | engineering/to-tickets/SKILL.md | Behavioral slices and wide-refactor sequencing; configured layout, no extra publication or readiness gate |
| implement-change | engineering/implement/SKILL.md | Implement/check/review sequence, also informed by user-local Plane guidance; no mandatory TDD, continuous execution, or commit |
| diagnose-bug | engineering/diagnosing-bugs/SKILL.md | Discriminating experiments; no fixed hypothesis count, test-first phase gate, or helper dependency |
| ux-prototype | engineering/prototype/SKILL.md and UI.md / LOGIC.md | Question-led artifacts and comparisons; optional variants, no fixed switcher, no-test rule, automatic promotion, or archival branch |

The explanation method in guided-review adapts
[pstack teach](https://github.com/backnotprop/pstack/blob/18e0e908a13553b0e58d065ab26dbc9a972ec8ba/skills/teach/SKILL.md),
revision `18e0e908a13553b0e58d065ab26dbc9a972ec8ba`. Lauren Tan's MIT notice is included.
Paced explanations and honest rationale remain; mandatory delegation, host/model choices,
visuals, and blanket quiz prohibition do not. Coverage, confirmation, invalidation, and
interaction settings are this project's design.

## Project-authored methods

Requirements, project-knowledge, setup-project, local-records, reconcile-knowledge, and
coding-principles implement the user's agreed requirements. Implementation and verification
also draw on the user's installed plane-implement, plane-verify, and implementation-slices
instructions. No external upstream provenance is claimed for those user-local instructions.

Plane-records supplies concrete configuration, MCP/REST routing, records, and state mapping.
It uses existing access rather than bundling or installing a helper. The old local-ADR
mandate and universal outage implementation ban conflict with this package and are omitted.
See [setup and transport limitations](skills/plane-records/README.md).

Coding-principles draws on Ousterhout's [modular-design notes](https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign),
[Chapter 6 extract](https://web.stanford.edu/~ouster/cgi-bin/aposd2ndEdExtract.pdf), and
[editor discussion](https://web.stanford.edu/~ouster/cgi-bin/cs190-spring16/lecture.php?topic=editorReview).
It reflects personal choices, not wholesale adoption of either design book. No book text
is bundled. All upstream skills are adaptation sources, not runtime dependencies.

Unslop and skill-creator inform editing and authoring; they are not runtime requirements.
Current authoring guidance is linked from [writing skills](docs/authoring-skills.md).
