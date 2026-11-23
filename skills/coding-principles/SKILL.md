---
name: coding-principles
description: Apply engineering design and maintenance preferences when selected for design, implementation, or review.
---

# Coding principles

- Follow project rules. Default investment to project expectations. Favor stable boundaries, readability, and explicit failures in long-lived code. Keep PoC choices clear and reversible, and revisit shortcuts when maintaining them.
- Investment, cleanup authority, and review coverage are independent.

| Cleanup scope | Work authorized |
| --- | --- |
| Requirement-focused (default) | Make needed structural fixes and abstractions, including in untouched files. Skip incidental cleanup. |
| Related cleanup | Improve the additionally authorized area. |
| Broader refactoring | Address the selected findings or architectural concern. |

Report unresolved issues. When durable records are in scope, update the relevant record and capture distinct findings separately via [project-knowledge](../project-knowledge/SKILL.md). Discovery alone grants no fix authority.

## Make callers know less

- A deep module owns knowledge or a decision. Its contract covers behavior, effects, ordering, and failures. Keep that contract simpler than the work it provides. Even one method can expose too many modes.
- Ask what callers can stop knowing. Hide mechanics and centralize invariants. Keep consequential business decisions with their owners. Prefer domain operations over option bags, flags, and call-order protocols.
- Design for current needs beyond one caller's incidental workflow. Avoid speculative features, forwarding layers, and merging different concepts because syntax matches. Extract when it hides knowledge, even without reuse.
- In long-lived code, keep domain and application policy independent of infrastructure. Inject storage, clocks, IDs, randomness, and external clients through narrow collaborators at an explicit composition point. Keep pure computation in ordinary functions. Avoid hidden globals, service locators, and interfaces for every class. Simplify for scripts and PoCs when injection costs more than it adds and behavior stays testable.

## Keep code and tests readable

- Name domain responsibilities precisely. Reconsider vague boundaries. Extract coherent concepts, hidden complexity, or side effects. Skip arbitrary function-length limits.
- Prefer guard clauses and shallow nesting. Keep `else` when it clarifies exclusive branches. Infer obvious types and state types that clarify contracts or distinctions.
- Follow repository formatting and lint rules. Avoid unrelated formatting. Use judgment beyond tool rules.
- Skip busywork or coverage-padding tests. Retain only tests that verify meaningful behavior or boundaries. For each, ask what broken behavior it catches, what it misses, and whether it survives an internal refactor. Use explicit expectations, small fixtures, and clear setup, even with some repetition.
- Tests may follow implementation. Temporary, sloppy, or implementation-specific probe tests are fine during development, but remove them before human handoff and rerun affected checks.
- Document consequential contracts and constraints. A short introduction can orient readers in longer functions or important entry points. Use local comments for non-obvious reasons. Keep comments current and skip boilerplate.

Apply these agreed preferences. Abstraction guidance draws on Ousterhout's [modular-design notes](https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign) and [Chapter 6 extract](https://web.stanford.edu/~ouster/cgi-bin/aposd2ndEdExtract.pdf).
