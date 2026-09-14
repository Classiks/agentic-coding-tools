# Evaluate the suite

The tables specify expected behavior. They are not executed tests or proof of reliability.
Run static checks and host discovery separately from these behavioral evaluations.

| Area | Cases |
| --- | --- |
| Requirements and authority | [requirements](requirements.md) |
| Source selection, resumption, drift | [project knowledge](project-knowledge.md) |
| Coverage and conversation | [guided review](guided-review.md) |
| Implementation, evidence, diagnosis | [implementation and verification](implementation-verification.md) |
| Artifact choice and variants | [UX/prototyping](ux-prototype.md) |

## Run on actual hosts

Use a disposable local project or an explicitly authorized fixture area. Give the agent
the task and project inputs, not the expected-results table. Record host/model, installed
skill revision, prompt, fixture state, trace, resulting artifacts, and observed failures.
Compare with the previous revision or without the skill under equivalent conditions.
Repeat important cases before drawing conclusions about consistency.

Start with these three exercises, separately in private Codex and work OpenCode:

1. Full ownership over a dirty diff containing a new test, a deletion, and a config change.
   Let the agent validate and begin the tour. Ask a question without confirming, then
   explicitly confirm one portion. Change that portion before resumption. Check that
   coverage remains pending where appropriate and renewed review reflects the change.
2. A confirmed requirement rejects expired invitations while code accepts them. Configure
   local records and ask for read-only reconciliation. Check that the agent records a
   discrepancy without fixing code or changing desired behavior. Then authorize the fix
   and inspect its actual regression evidence and retained tests.
3. A navigation question with two plausible approaches and no app/tool installation.
   Ask for an initial wireframe and an offer of alternatives. Check artifact choice,
   comparisons when requested, and honest limits on usability claims.

For Plane, use its configured test area to exercise update, creation/discovery, conflict,
and uncertain-write cases only when authorized. Local tests cannot establish Plane
transport compatibility. See [adapter prerequisites](../skills/plane-records/README.md).

## Check activation separately

| Request | Expected routing |
| --- | --- |
| "Stress-test this decision with me; don't save anything" | Grilling; no mandatory storage setup |
| "Summarize this existing glossary" | No domain-redesign interview |
| "Turn our settled discussion into a spec" | to-spec; no repeated grilling |
| "Find why this intermittent failure occurs; don't edit" | diagnose-bug; no repair or commit |
| "Explain the changed lines in small portions" | guided-review |
| "Make this spelling correction" | No whole requirements or diagnosis workflow |
| "Use local records in this sandbox" | local-records; no Plane dependency |

Judge observable choices rather than exact phrasing. A passing format check, a promising
single run, and a consistently useful workflow are different levels of evidence.
