# AGENTS.md section template

This is a template, not active project configuration. Replace placeholders during
setup and remove unused exceptions. Resolve project paths relative to AGENTS.md.
Use the identities and configuration fields required by the selected adapter.
The template does not enumerate or select storage implementations.

```markdown
## Project knowledge

Contract version: 1
Shared rules: Read the supplied `project-knowledge` skill.
Primary store: <authoritative knowledge source as identified by its adapter>
Entry point: <resolvable starting reference in the selected source>
Adapter: <available skill name and location, or inline instructions below>
Exceptions: <none, or information type → location and adapter>
Resume: <where to find active items and each item's continuation record>
Access checked: <actual successful reads; mark remaining access unverified>

For an inline adapter:
- Find and read: <search, identities, and retrieval of current complete records>
- Write: <updates, creation, and relationships>
- Verify and resolve conflicts: <read-back, concurrent changes, and failures>
```

The adapter defines backend-specific configuration and access details. Keep them in
an adapter configuration subsection when needed; do not expand this template with
backend-specific choices. Existing project conventions determine actual values.
An exception is explicit and refers to its own source and adapter.
