# Updater

## Purpose
Manages framework upgrade verification, migration planning, and execution while strictly shielding user project brains, custom configurations, project-installed Agency Agents, and source code.

## Status
`active`

## Responsibilities
- Execute the 5-phase Framework Update Protocol triggered by `update`, `@update.md`, or pasting `guides/prompts/update.md` onto legacy `v1`/`v2` installations.
- Perform read-only upstream fetching (`verdenef/genOS` git remote, GitHub `main.zip`, or local copy) and verify whether core files have drifted before proposing changes (short-circuiting cleanly if already current).
- Propose an explicit Upgrade & Migration Plan (core files, repo-root `CLAUDE.md`/`.agents/`/`.cursor/`, obsolete `v1`/`v2` prompt pruning, shield list, post-sync Doctor repairs) and wait for human approval before modifying files.
- Enforce strict shielding for `brain/`, `.obsidian/`, custom profiles, user code, and project-installed Agency Agents.
- Trigger post-upgrade Doctor audits using the **newly installed `AGENTS.md`** so legacy `v1`/`v2` brain schema gaps are migrated safely without losing history.

## Dependencies
- [[Kernel]]: Integrated into kernel commands and version header (`> **Framework Version:**`) in `AGENTS.md`, and verified by the Doctor Protocol.
- [[30_DECISIONS.md]]: Governed by [[DEC-004]], [[DEC-007]], and [[DEC-008]].

## Runtime References
- `AGENTS.md`: Version header and "Framework Update Protocol" defining the 5-phase Verify → Plan → Approve → Apply → Doctor lifecycle.
- `guides/prompts/update.md`: Self-contained interactive prompt guide supporting both current `v3` and legacy `v1`/`v2` upgrades.
- `.agents/skills/genos-update/SKILL.md`: Packaged skill enabling AI agents to run drift checks and plan-gated updates safely.
- `.cursor/rules/genos-update.mdc`: Cursor IDE rule trigger for updates.

## Invariants
- Verify before modifying: Read-only upstream comparison runs first; zero target files change until drift is confirmed and the human approves the Upgrade Plan.
- Self-contained legacy support: `guides/prompts/update.md` never depends on the target repo's outdated `AGENTS.md` having Doctor or update instructions; Doctor always runs against the newly updated `AGENTS.md`.
- Strict shielding: Never overwrite, modify, or delete `brain/` during file sync (`00_PROJECT.md`, `20_PROGRESS.yaml`, `30_DECISIONS.md`, `40_BACKLOG.md`, `50_ROADMAP.md`, `60_AGENTS.md`, `brain/systems/*.md`). Never delete `.obsidian/`, custom profiles in `profiles/`, project-installed Agency Agents in `.agents/skills/` or `.cursor/rules/`, or user source code.
- Staging cleanliness: Temporary update extraction directories (`_genOS_Update/`) must always be deleted before finishing (both when short-circuiting and after upgrading).

## Notes
- Ensures legacy `v1`/`v2` projects can be upgraded safely simply by pasting `guides/prompts/update.md` and pointing to the old `genOS` directory.

## Future Changes
- M3: Native CLI binary updater with automatic semantic release detection and selective patch application.
