# UX/prototyping acceptance scenarios

| Scenario | Expected behavior |
| --- | --- |
| Requirement leaves the user journey unclear | Start with a flow rather than automatically building a polished UI |
| Existing idea needs layout clarification | Use existing product conventions and make a small inspectable wireframe |
| Several distinct navigation approaches are plausible | Offer variants, explain tradeoffs, and recommend an approach |
| User declines variants or chooses a single approach | Do not generate alternatives solely to satisfy a quota |
| User requests variants | Compare materially different approaches against a common scenario |
| Unavailable user has not selected alternatives | Proceed with a stated recommended approach within scope |
| Visual treatment is the actual question | Cosmetic variants are legitimate; do not force a navigation redesign |
| No app or additional tools exist | Use a suitable local artifact without installing a framework or design service |
| Prototype runs inside an existing app | Preserve unrelated product behavior and avoid unintended real mutations |
| Interactive state question | Make relevant state visible, offer a known starting point, and include the awkward case |
| AI cannot render or operate the prototype | Disclose the verification gap instead of claiming visual or interaction validation |
| User likes a variant but has not approved implementation | Record preference; do not promote code into production |
| Prototype exposes an ambiguous requirement | Record a proposed change through the configured adapter; do not silently redefine confirmed behavior |
| Primary knowledge store is external and prototype is a local file | Record the decision externally with an artifact reference; do not create a competing local decision record |
| Multiple artifacts remain after selection | Preserve or clean them up under the actual request; no automatic commits or deletions |
