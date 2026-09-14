---
name: coding-principles
description: >-
  Apply this engineering style when selected for design, implementation, or review, scaling maintainability investment and cleanup scope to the task.
---

# Coding principles

Follow binding project rules and the selected investment level, defaulting to project
expectations. Quality ambition does not determine cleanup scope or review coverage.

## Design investment and scope

For long-lived code, invest in readability, stable boundaries, and explicit failures.
For a PoC, keep code clear and favor inexpensive, reversible decisions. Useful generality
can simplify either; speculative features cannot. Reassess shortcuts when maintaining a PoC.

Cleanup scope defaults to **requirement-focused**: change what the requirement needs,
including sensible abstractions and structural fixes that avoid degrading the design.
Relevance is not limited to already touched files. Do not add incidental cleanup.
With **related cleanup**, improve the additionally authorized area. With **broader
refactoring**, address the explicitly selected findings or architectural concern.
A quality preference alone does not expand scope.

Surface substantive unresolved issues in the handoff. Persist them through
[project-knowledge](../project-knowledge/SKILL.md) when durable project records are in
scope; use [requirements](../requirements/SKILL.md) in requirements-driven work.
Do not create an independent backlog or treat discovery as permission to fix.

## Abstractions that remove knowledge

Design a deep module around knowledge or a decision it owns. Its interface includes
everything callers must understand: behavior, side effects, ordering, and failures,
not just signatures. Keep that interface substantially simpler than what it provides.
A single method with many modes can still be a complicated interface.

Keep functionality grounded in current needs, but avoid an interface shaped around one
caller's incidental workflow. For example, a text model can delete a range while the UI
interprets Backspace and selections. Do not add hypothetical features to appear general.

Before extracting or introducing a module, ask what callers can stop knowing. Hide
implementation mechanics and centralize invariants; preserve consequential business
choices at the level that owns them. Prefer clear domain operations over option bags,
mode flags, or leaked call-order protocols. Reuse is not a prerequisite. Conversely,
similar syntax is not enough reason to merge different concepts. Avoid forwarding
layers that add navigation without hiding knowledge.

## Structure and readability

- Name operations and state by domain meaning and responsibility. Make intended use
  understandable without opening the implementation; vague names can signal a muddled
  boundary, not merely a naming problem.
- Keep functions coherent, without arbitrary line limits. Extract to name a concept,
  hide complexity, or separate policy and side effects, not to fragment a readable flow.
- Prefer guard clauses for invalid inputs and early exits. Reduce deep nesting, but
  retain `else` when it makes mutually exclusive branches easier to understand.
- Prefer inferred types when the type is clear from the code. Use explicit types when
  needed for a contract, meaningful distinction, or clarity; for example, Java `var`
  is welcome when the initializer makes the type apparent.
- Follow the repository formatter and linter. Do not introduce a competing style or
  reformat unrelated files. Human judgment handles what formatting tools cannot.

For long-lived code, keep domain/application policy independent of infrastructure.
Inject meaningful side effects through narrow collaborators at an explicit composition
point: storage, clocks, IDs, randomness, and external clients. Keep pure computation as
ordinary functions; avoid hidden globals, service locators, and interfaces for every
class. Small scripts and PoCs may use simpler arrangements when injection adds more
complexity than value and important behavior remains straightforward to test.

## Tests and explanations

Treat maintained tests as readable accounts of behavior: explicit expectations, small
fixtures, and simple setup. Prefer a little repetition over clever test infrastructure
that obscures the scenario. Development probes may be disposable or implementation-
specific. Before each review-ready slice, every retained new or changed test must earn
its maintenance cost through meaningful protection; curate them using
[the verification guidance](../verify-change/references/checks.md). No mandatory TDD.

For longer functions and important entry points, a one-to-three-sentence introduction
may frame purpose and flow even when the code is self-explanatory. Document consequential
contracts and constraints. Local comments explain non-obvious reasoning, not the next
line's mechanics. Keep explanations current; neither function length nor public visibility
alone requires boilerplate documentation.

Abstraction guidance draws on Ousterhout's [modular-design notes](https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign)
and [Chapter 6 extract](https://web.stanford.edu/~ouster/cgi-bin/aposd2ndEdExtract.pdf).
These are agreed preferences, not wholesale adoption of a design book.
