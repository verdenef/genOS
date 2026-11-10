# Kernel

## Purpose
Governs session lifecycle, state handoff, and execution protocols across AI agents and development environments.

## Status
`active`

## Responsibilities
- Define and enforce the core genOS protocol in `AGENTS.md`.
- Manage session initialization through the BOOT sequence and zero-history recovery.
- Govern session termination through the SHUTDOWN sequence and mandatory Sanity Gate verification.
- Provide Smart Kickoff routing (Resume, Fresh Start, Advance, Scoped Intent) for automated context switching.
- Enforce timeless 3-tier Model & Session guidance (Flagship, Balanced, Fast) and generate copy-pasteable execution handoff blocks.
- Guarantee single source of truth ownership across all Project Brain files.

## Dependencies
- [[Updater]]: Invoked for framework maintenance and upgrades via the `update` command.
- [[Skills]]: Leverages operational skills for plan authoring, execution, and verification.
- [[Workforce]]: Reads and verifies active agent personas during BOOT and pre-planning gates.
- [[30_DECISIONS.md]]: Governed by canonical architectural decisions ([[DEC-001]], [[DEC-002]], [[DEC-005]]).

## Runtime References
- `AGENTS.md`: Canonical genOS operating kernel specification, ownership table, lifecycle protocols, and commands.
- `CLAUDE.md`: Anthropic Claude Code bootstrap pointer directing agents to `AGENTS.md`.
- `guides/prompts/workflow-kickoff.md`: Session kickoff protocol and prompt specification.
- `guides/prompts/workflow-shutdown.md`: Session shutdown protocol and Sanity Gate checklist.
- `guides/prompts/workflow-batch.md`: Autonomous batch loop runner specification.

## Invariants
- Zero-history recovery: Every agent recovers state completely from the Project Brain alone without relying on chat history.
- Single source of truth: Domain ownership strictly follows the `AGENTS.md` Ownership table; no state mirroring across files.
- Location-agnostic pathing: All relative paths are evaluated relative to the directory containing `AGENTS.md`.
- Obsidian compatibility: All internal brain cross-references must use `[[wikilink]]` syntax.
- Mandatory Sanity Gate: SHUTDOWN must execute all Sanity Gate checks with zero tolerance for errors or desynchronization.

## Notes
- Serves as the central operating system for all AI agents working in the repository.
- Decouples project architectural memory from specific IDEs, proprietary platform databases, or context compaction mechanisms.
- Supports both Tier 1 auto-load IDEs (Antigravity, Cursor, Claude Code, Codex) and Tier 2/3 environments through plain-text commands.

## Future Changes
- M3: CLI distribution package (`npx genos` / pip installer) for automated bootstrapping.
