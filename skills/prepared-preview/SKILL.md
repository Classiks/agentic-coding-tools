---
name: prepared-preview
description: Prepare a separate preview, isolated playtest, or exact replay when the user asks to try an implemented change.
---

# Prepared preview

- Open the intended build directly in the state the user needs to try. Give the exact URL or runnable command with the relevant route, seed, replay, or control settings.
- Use separate data directories, ports, and services where the preview could interfere with the main instance. Record the owning process, port, and temporary resources so the preview can be stopped without touching the main instance.
- Before handoff, run the exact URL or command in the user's environment or shell. Confirm it reaches the intended build and state. If access prevents that check, report which part is unverified.
- Give the user one concrete action to try and the result to look for. Record their response as preview acceptance only. Code inspection and merge decisions have their own authority.
