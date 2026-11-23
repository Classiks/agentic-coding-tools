---
name: isolated-parallel-work
description: Handle explicitly requested work in a separate writing thread or worktree for later handoff to a named integrator.
---

# Isolated parallel work

- Record the task, exact base ref and resolved commit, absolute checkout path, branch, write ownership, dependencies, named integrator, and runtime resources such as ports, services, and data directories.
- Follow `AGENTS.md` for checkout and build setup. Use the assigned checkout or have the receiving thread create one as instructed. Verify the thread's actual checkout, branch, and starting commit before writing. Resolve mismatches before proceeding. Preserve existing uncommitted work.
- Use separate writable runtime directories. Coordinate access to shared ports and services.
- Keep preparation read-only. The implementer writes within the assigned checkout and scope. The named integrator handles integration under separate authority. Cleanup needs its own authorization.
- At handoff, give the integrator the checkout, branch, base and final commit SHAs, any changes outside the final commit, observed verification and its limits, required assets or artifacts and their paths, and any resources or processes still in use.
- Use [project-knowledge](../project-knowledge/SKILL.md) when durable handoff records are configured.
- Before authorized cleanup, confirm the integrator has received the result and nothing still uses the checkout or its processes.
