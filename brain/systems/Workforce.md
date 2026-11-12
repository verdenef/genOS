# Workforce

## Purpose
Coordinates active, deferred, and milestone-specific AI agents, enforcing the Hard Persona Gate before planning.

## Status
`active`

## Responsibilities
- Serve as the authoritative catalog and coordination layer for project AI agents.
- Enforce the Hard Persona Gate during the Kickoff protocol, requiring physical inspection of active persona files prior to plan formulation ([[DEC-003]]).
- Require plans to explicitly cite 2-3 governing rules from active agent definitions.
- Coordinate domain specialist selection and automated zero-dependency installation from external agency catalogs (e.g. Agency Agents integration via `guides/scripts/install_agent.py`) after human approval ([[DEC-007]]).
- Maintain clear separation between Core Agents, Milestone Agents, Optional Specialists, and Deferred Agents.
- Enforce the pre-planning Workforce Gap Check during `kickoff` and progress-based re-audits via `kickoff workforce` ([[DEC-009]]), detecting uncovered disciplines against active milestones, `systems_in_scope`, and user intent, promoting Deferred Agents, and retiring completed Milestone Agents under mandatory human approval.

## Dependencies
- [[Kernel]]: Integrated into BOOT Sequence step 6 and Kickoff protocol pre-planning validation.
- [[Skills]]: Leverages skill definitions to supply behavioral rules and capabilities for workforce personas.
- [[Updater]]: Coordinates with the framework updater to ensure project-installed Agency Agents are shielded from overwrites during framework upgrades.
- [[30_DECISIONS.md]]: Governed by canonical architectural decisions [[DEC-003]], [[DEC-007]], and [[DEC-009]].

## Runtime References
- `brain/60_AGENTS.md`: Authoritative roster of active, deferred, and removed agents for the project.
- `integrations/agency_agents.md`: Workforce selection protocol mapping domain needs to Agency Agents definitions.
- `guides/scripts/install_agent.py`: Zero-dependency stdlib auto-installer for fetching upstream Agency Agents into dual `.agents/skills/` and `.cursor/rules/` targets.
- `.agents/skills/`: Directory housing behavioral instructions for active agents.
- `.cursor/rules/`: Directory housing IDE persona rules for Cursor agents.

## Invariants
- Single source of truth: The active workforce roster lives exclusively in [[60_AGENTS.md]].
- Hard Persona Gate: Agents must physically read the active persona rule files from disk before formulating an implementation plan—guessing agent rules from memory is strictly forbidden ([[DEC-003]]).
- Explicit citation: Kickoff implementation plans must explicitly cite 2-3 governing rules from the active workforce definitions.
- Approval before installation: AI agents recommend specialist agents from catalog/profiles but must obtain explicit human approval before invoking `install_agent.py`.
- Clean core & update shielding: Core genOS repository ships only core framework rules/skills; project-installed Agency Agents in `.agents/skills/` and `.cursor/rules/` are owned by the project repo and strictly preserved during framework `update` ([[DEC-007]]).
- Verbatim persona integrity: Upstream persona markdown bodies are preserved verbatim with safely quoted YAML frontmatter, never summarized or modified.
- Separation of concerns: Workforce roles define domain authority and perspectives; core kernel rules remain authoritative for state management and protocol enforcement.
- Workforce Gap Check & lifecycle routing: Pre-planning must check active milestones, `systems_in_scope`, and user intent for uncovered domain gaps; `kickoff workforce` audits live progress ([[20_PROGRESS.yaml]]) and active system documents, promoting Deferred Agents and retiring completed Milestone Agents under mandatory human approval ([[DEC-009]]).

## Notes
- Enables flexible, specialized team configurations tailored to specific technical domains without bloating the kernel.
- Works synergistically with the Ponytail restraint filter to ensure specialized agents remain lean and disciplined.

## Future Changes
- M3: Automatic workforce profile recommendations during project initialization based on detected languages and frameworks.
