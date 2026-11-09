# Updater

## Purpose
Manages framework upgrade lifecycle while strictly preserving user project brain, custom configurations, and source code.

## Status
`active`

## Responsibilities
- Execute the Framework Update Protocol triggered by the `update` command or `@update.md`.
- Detect and implement dual-method upstream fetching (tracking git remote vs. GitHub archive zip).
- Enforce strict Brain shielding to protect all user memory, notes, profiles, and code.
- Apply framework refreshes to kernel files (`AGENTS.md`), guides, profiles, and packaged skills/rules.
- Trigger automatic post-update health audits via the Doctor Protocol.

## Dependencies
- [[Kernel]]: Integrated into kernel commands (`AGENTS.md`) and verified by the Doctor Protocol.
- [[30_DECISIONS.md]]: Governed by canonical architectural decision [[DEC-004]].

## Runtime References
- `AGENTS.md`: Section "Framework Update Protocol" defining the 4-step upgrade process and safety guarantees.
- `guides/prompts/update.md`: Interactive prompt guide for running framework updates.
- `.agents/skills/genos-update/SKILL.md`: Packaged skill enabling AI agents to execute the update procedure safely.
- `.cursor/rules/genos-update.mdc`: Cursor IDE rule trigger for updates.

## Invariants
- Strict Brain shielding: Never overwrite, modify, or delete any file in `brain/` (`00_PROJECT.md`, `20_PROGRESS.yaml`, `30_DECISIONS.md`, `40_BACKLOG.md`, `50_ROADMAP.md`, `60_AGENTS.md`, and all `brain/systems/*.md`).
- Environment protection: Never delete `.obsidian/`, never delete custom user profiles in `profiles/`, and never touch user source code.
- Dual-method fetching: Check if git remote `upstream` or `origin` tracks `verdenef/genOS`; fall back to fetching the latest release zip from `https://github.com/verdenef/genOS/archive/refs/heads/main.zip`.
- Staging cleanliness: Temporary update extraction directories (e.g., `_genOS_Update/`) must always be cleaned up and removed upon completion.
- Mandatory audit: Every update run must conclude with a full Doctor audit of the Project Brain.

## Notes
- Ensures downstream projects can continuously adopt genOS kernel enhancements and new skills with zero risk of data loss.
- Operates safely even in disconnected or non-git environments via the HTTP archive fallback method.

## Future Changes
- M3: Native CLI binary updater with automatic semantic release detection and selective patch application.
