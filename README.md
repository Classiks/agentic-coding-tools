# AI workflow skills

Composable skills for planning, building, verifying, and understanding AI-assisted work.
Choose the methods you need and adapt their scope, autonomy, and review depth through
your prompt.

Prepare a selection from a local checkout:

```bash
./scripts/prepare-skills.sh --output ./prepared \
  --include implement-change verify-change guided-review coding-principles
```

The script copies complete skill folders and reports references to omitted skills.
Use the output with your agent's skill directory or an existing setup process.

Then ask your agent:

> Use implement-change and coding-principles for this change. Validate your work, then
> use guided-review to walk me through it in small portions. I need full code ownership.

- [Prepare and use skills](docs/preparing-skills.md)
- [Choose and compose workflows](docs/using-skills.md)
- [Write skills](docs/authoring-skills.md) and [knowledge adapters](docs/authoring-knowledge-adapters.md)
- [Evaluate behavior](evals/README.md)
- [Sources and adaptations](SOURCES.md)
