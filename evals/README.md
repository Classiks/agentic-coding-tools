# Evaluate the suite

The tables specify expected behavior. They are not executed tests or proof of reliability.
Run static checks and host discovery separately from these behavioral evaluations.

| Area | Cases |
| --- | --- |
| Local Markdown setup, resumption, and drift | [project knowledge](project-knowledge.md) |
| Coverage and conversation | [guided review](guided-review.md) |

## Run on actual hosts

Use a disposable local project. Give the agent the task and project inputs, not the
expected-results table. Record host/model, installed
skill revision, prompt, fixture state, trace, resulting artifacts, and observed failures.
Compare with the previous revision or without the skill under equivalent conditions.
Repeat important cases before drawing conclusions about consistency.

Start with these three exercises, separately in private Codex and work OpenCode:

1. Full ownership over a dirty diff containing a new test, a deletion, and a config change.
   Let the agent validate and begin the tour. Ask a question without confirming, then
   explicitly confirm one portion. Change that portion before resumption. Check that
   coverage remains pending where appropriate and renewed review reflects the change.
2. A confirmed requirement rejects expired invitations while code accepts them. Set
   the project Markdown path in `AGENTS.md` and ask for read-only reconciliation.
   Check that the agent reports the discrepancy and leaves code and records intact.
3. Ask for one interview about invitations and memberships in a project with an
   existing glossary. Request a spec after settling the decisions. Check that the
   agent links existing terms and decisions, includes acceptance examples, and
   carries forward open choices without restarting the interview.

## Check activation separately

| Request | Expected routing |
| --- | --- |
| "Before doing anything, tell me what you understood and would do" | align; restate intent and bounded actions, then wait |
| "Stress-test this decision with me. Keep it in chat." | grilling; continue without setting up storage |
| "Refine the glossary terms for invitations and memberships" | domain-modeling; resolve terminology against concrete scenarios |
| "Summarize this existing glossary" | Read the glossary without opening a domain-design interview |
| "Turn our settled discussion into a spec" | grill-with-docs synthesizes it without repeating the interview |
| "Find why this intermittent failure occurs. Keep the investigation read-only." | diagnose-bug; collect evidence and report likely causes |
| "Explain the changed lines in small portions" | guided-review |
| "Build this in a separate worktree and hand it to Morgan to integrate" | isolated-parallel-work checks the checkout and hands off the commit and evidence |
| "Let me try the fix in a separate preview at the failing step" | prepared-preview verifies the exact build and entry point |
| "Have another agent independently confirm this disputed result" | independent-review gives the reviewer the reproduction context and omits prior verdicts |
| "Review these module boundaries for long-term maintenance" | coding-principles; assess which decisions each module owns |
| "Cut the stock phrasing in this handoff" | unslop; rewrite while preserving meaning |
| "Configure our records under `notes/product/`" | project-knowledge; set the path and active-work directions in `AGENTS.md` |
| "Catch the docs up after the refactor" | reconcile-knowledge; compare the relevant local records with current code |

Judge observable choices rather than exact phrasing. A passing format check, a promising
single run, and a consistently useful workflow are different levels of evidence.

## Alignment cases

- "Align: simplify this paragraph." Expect a brief interpretation and intended edit,
  then a pause. No file edits, broad rewrite, or unsolicited audit.
- "Align: I want fewer interruptions, not less review." Expect the distinction in new
  words without inventing implementation work or waiving coverage.
- Correct "remove the feature" to "hide the entry point." Expect revised scope and a
  fresh confirmation check before action.
- Confirm an aligned instruction to edit one paragraph. Expect that edit within existing
  permissions, without expanding to related documents or adding another approval gate.
