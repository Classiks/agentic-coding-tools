# Prepare and use skills

Run `scripts/prepare-skills.sh` from a checkout to assemble complete skill folders into
a directory of your choice. It requires Bash 3.2 or later and standard Unix utilities
available on Linux/macOS. It downloads nothing and changes no agent configuration.

```bash
./scripts/prepare-skills.sh --output ./prepared --all

./scripts/prepare-skills.sh --output ./work-skills --all \
  --exclude plane-records ux-prototype

./scripts/prepare-skills.sh --output ./review-skills \
  --include guided-review verify-change project-knowledge local-records
```

Both `--include` and `--exclude` accept multiple space-separated names and repeated
occurrences. Choose `--all` or `--include`; exclusions win regardless of argument order.
Duplicate names are copied once. Unknown names, missing arguments, and empty selections
fail before copying.

The output directory must not exist, and must be outside the source `skills` directory.
Its parent directories are created if needed. A copy failure can leave incomplete output;
the script reports this and does not silently remove files. Use a fresh directory for
another attempt after inspecting the failure.

## Selection and references

The output contains `<name>/SKILL.md` alongside each skill's references, license, and
optional README. The script copies exactly the selected skills. It reports relative
Markdown links to omitted skills, including links in supporting files, without adding
them automatically. Read the referring instruction to decide whether that route applies.
The report covers file links, not arbitrary prose references or host configuration.

For example, guided-review uses verify-change for validation, but a configured knowledge
adapter is needed only for durable sources or progress. A link alone cannot distinguish
an unconditional prerequisite from an optional handoff. Include skills needed by the
workflow you intend to use.

## Connect to an agent host

Copy the prepared folders as siblings into the host's supported skill directory. Preserve
complete folders rather than copying SKILL.md alone. Read a skill's README, when present,
for additional prerequisites. Preparing files does not provide external service access.

Project-local `.agents/skills` is documented by both
[Codex](https://learn.chatgpt.com/docs/build-skills) and
[OpenCode](https://opencode.ai/docs/skills). A setup script can place the prepared folders
in the project before cloning it into a sandbox, or in the clone before the agent starts.
They then follow the project's normal clone/pull workflow.

Inspect existing skill locations before combining installations. Same-name copies may
be ambiguous; choose the intended version rather than assuming project scope replaces
a global copy. Test in a fresh session by asking the agent to load a selected skill,
report its actual path, and resolve one of its references. Discovery alone does not
establish correct workflow execution. If a shortcut loses arguments or reference context,
use the skill name and file path in ordinary language.

These checks address reported duplicate-root and invocation failures; they are not a claim
that every host version has those bugs. Consult the documentation for the installed host
version. [Duplicate-root report](https://github.com/anomalyco/opencode/issues/32202),
[invocation-context report](https://github.com/anomalyco/opencode/issues/41245).

## Update a prepared bundle

Prepare the new selection into a fresh directory and compare it with the previous bundle.
Record the source revision in your existing setup process. When deploying an update,
preserve local adaptations and remove obsolete files deliberately; preparation does not
synchronize an existing installation. Update project references before removing a selected
adapter or method.

Run the script's regression tests with `python3 -m unittest discover -s scripts/tests -v`.
Python is used for these development tests only, not bundle preparation.
