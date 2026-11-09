# Skills

## Purpose
Manages specialized agent capabilities, Superpowers execution patterns, and senior developer restraint protocols.

## Status
`active`

## Responsibilities
- Provide structured operational skills that guide agents through complex development phases.
- Enforce the Ponytail Ladder of Restraint (YAGNI -> Reuse -> Stdlib -> Minimal code) to prune unnecessary complexity before implementation.
- Support plan formulation and execution workflows (`writing-plans`, `executing-plans`, `subagent-driven-development`).
- Guide rigorous testing and verification cycles (`test-driven-development`, `verification-before-completion`, `systematic-debugging`).
- Provide IDE-agnostic capability discovery and tool reference mappings.

## Dependencies
- [[Kernel]]: Integrated into Kickoff Pre-Planning gates and verification checkpoints.
- [[Workforce]]: Powers the active capabilities assigned to declared agent personas in `[[60_AGENTS.md]]`.
- [[30_DECISIONS.md]]: Governed by canonical architectural decision [[DEC-003]].

## Runtime References
- `.agents/skills/ponytail/SKILL.md`: Senior developer restraint and Ladder of Restraint evaluation.
- `.agents/skills/writing-plans/SKILL.md`: Structured implementation planning protocol.
- `.agents/skills/executing-plans/SKILL.md`: Checkpoint-driven implementation plan execution.
- `.agents/skills/subagent-driven-development/SKILL.md`: Parallel/hierarchical subagent task distribution.
- `.agents/skills/test-driven-development/SKILL.md`: Test-first red-green-refactor implementation discipline.
- `.agents/skills/verification-before-completion/SKILL.md`: Evidence-based verification before claiming completion.
- `.agents/skills/systematic-debugging/SKILL.md`: Multi-phase root-cause diagnosis protocol.
- `.agents/skills/using-superpowers/SKILL.md`: Skill discovery, loading, and execution rules.
- `.cursor/rules/`: IDE-specific mirror of skills for Cursor environments.

## Invariants
- Canonical location: All skills live in `.agents/skills/<name>/SKILL.md` or `.cursor/rules/`.
- Version controlled: All skills are tracked in Git as first-class repository assets.
- Dynamic file access: Skills are read dynamically using native file reading tools on demand, never requiring manual UI uploads or external host settings.
- Restraint first: The Ponytail Ladder of Restraint must be evaluated before proposing or implementing new architecture or code.

## Notes
- Bridges the gap between generic model outputs and disciplined engineering practices.
- Decouples skill logic from IDE implementations, allowing Antigravity, Cursor, and Claude Code to share the identical skill definitions.

## Future Changes
- M3: Dynamic skill installation and capability dependency resolution via CLI tooling.
