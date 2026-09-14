# Choose and compose workflows

Select skills by the decisions you want help with. Installing a skill makes it available;
it does not require using it on every task. A name in a prompt or AGENTS.md must resolve
to an available file. Referenced instructions load when needed, not automatically.

| Need | Skills |
| --- | --- |
| Apply the writing style throughout work | unslop, retaining its "Must always apply" instruction |
| Stress-test an idea | grilling |
| Interview with terminology and documentation | grill-with-docs, combining grilling and domain-modeling |
| Refine terms and design decisions | domain-modeling |
| Describe desired behavior | requirements and to-spec |
| Divide substantial work into verifiable tasks | to-tickets |
| Explore a user experience | ux-prototype |
| Implement and validate | implement-change and verify-change |
| Investigate an unclear failure | diagnose-bug |
| Apply engineering preferences | coding-principles |
| Understand a change | guided-review |
| Configure knowledge and resume work | setup-project and project-knowledge, with a selected adapter |
| Reconcile documentation with code | reconcile-knowledge |

## Set independent expectations

| Choice | Meaning |
| --- | --- |
| Investment | Long-lived code earns maintenance effort; a PoC favors clear, reversible shortcuts |
| Cleanup scope | Requirement-focused by default; related cleanup or broader refactoring needs corresponding authority |
| Work rhythm | Pause after coherent slices or work longer autonomously |
| Review coverage | Full ownership, focused human review, or delegated verification |
| Portion size | How much the user sees at once, independent of implementation slice size |

> Use implement-change and coding-principles. This is long-lived code. Implement the
> agreed scope autonomously and validate it, then give me a guided-review in small
> portions. Keep full ownership; don't commit.

AI validation precedes handoff in every mode. Tests may follow implementation.
Disposable probes can help development; retained tests must justify maintenance cost.
Full ownership includes tests and deletions, with confirmations tied to inspected
content. A tour explains the changes using file references and optional questions.
It records inspection but cannot prove comprehension or enforce it technically.

> Use ux-prototype to explore navigation. Start with a wireframe and offer alternatives
> if they expose a real choice. Record decisions through our configured knowledge adapter.

## Configure knowledge only when needed

Use setup-project to configure the `Project knowledge` section in AGENTS.md. Select a
primary store and explicit exceptions, with an adapter that supplies concrete access
procedures. See [the adapter contract](authoring-knowledge-adapters.md). A local glossary
exception need not move design decisions out of the primary store.

Methods own content; adapters own storage mechanics. New sessions retrieve originals
and inspect the working tree. Routine handoffs reconcile affected documentation;
reconcile-knowledge handles requested catch-up. No skill can guarantee zero drift or
atomic external writes. Pure discussion and ephemeral review need no storage setup.

Interaction preferences use defaults and an optional separate `Agent interaction`
section in AGENTS.md. Prompt overrides apply to the session. Declining comprehension
questions must not disrupt the tour; it does not waive review confirmation.

## Learn through actual work

Grilling leads one interview; domain modeling joins its rounds. To-spec synthesizes
settled decisions without repeating the interview, and to-tickets divides work only
when helpful. Implementation coordinates checks and review without moving those
responsibilities into an adapter.

Read a skill, identify a decision it should improve, and observe it on a real task.
Use [the evaluation cases](../evals/README.md) to investigate failures and wasted steps.
Change instructions based on those observations rather than adding more rules by default.
