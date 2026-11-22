# Choose and compose workflows

Select skills by the decisions you want help with. Installing a skill makes it available;
it does not require using it on every task. A name in a prompt or AGENTS.md must resolve
to an available file. Referenced instructions load when needed, not automatically.

| Need | Skills |
| --- | --- |
| Apply the writing style throughout work | unslop, retaining its "Must always apply" instruction |
| Check shared meaning and intended actions before proceeding | align |
| Stress-test an idea | grilling |
| Interview, refine terms, and write a spec when asked | grill-with-docs |
| Refine terms and design decisions | domain-modeling |
| Investigate an unclear failure | diagnose-bug |
| Apply engineering preferences | coding-principles |
| Understand a change | guided-review |
| Configure local Markdown records and resume work | project-knowledge |
| Reconcile documentation with code | reconcile-knowledge |

## Set independent expectations

| Choice | Meaning |
| --- | --- |
| Investment | Long-lived code earns maintenance effort; a PoC favors clear, reversible shortcuts |
| Cleanup scope | Requirement-focused by default; related cleanup or broader refactoring needs corresponding authority |
| Work rhythm | Pause after coherent slices or work longer autonomously |
| Review coverage | Full ownership, focused human review, or delegated verification |
| Portion size | How much the user sees at once, independent of implementation slice size |

> Use coding-principles. This is long-lived code. Implement the
> agreed scope autonomously and validate it, then give me a guided-review in small
> portions. Keep full ownership; don't commit.

AI validation precedes handoff in every mode. Tests may follow implementation.
Disposable probes can help development; retained tests must justify maintenance cost.
Full ownership includes tests and deletions, with confirmations tied to inspected
content. Each portion gives a rough effort-based progress estimate alongside the portion
count. A tour explains the changes using file references and optional questions.
It records inspection but cannot prove comprehension or enforce it technically.

## Configure knowledge only when needed

Use the `Project knowledge` section in `AGENTS.md` to set the local Markdown path and
explain how to find active work. Keep existing conventions and map glossary or ADR
locations explicitly when useful. See [project knowledge](../skills/project-knowledge/SKILL.md).

When resuming work, read the current records and inspect the working tree. Check
affected documentation at handoff. Use [reconcile-knowledge](../skills/reconcile-knowledge/SKILL.md)
for a requested catch-up. Pure discussion and one-off reviews can proceed without setup.

Interaction preferences use defaults and an optional separate `Agent interaction`
section in AGENTS.md. Prompt overrides apply to the session. Declining comprehension
questions must not disrupt the tour; it does not waive review confirmation.

## Learn through actual work

Read a skill, identify a decision it should improve, and observe it on a real task.
Use [the evaluation cases](../evals/README.md) to investigate failures and wasted steps.
Change instructions based on those observations rather than adding more rules by default.
