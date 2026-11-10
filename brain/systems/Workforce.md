# Workforce

## Purpose
Coordinates active, deferred, and milestone-specific AI agents, enforcing the Hard Persona Gate before planning.

## Status
`active`

## Responsibilities
- Serve as the authoritative catalog and coordination layer for project AI agents.
- Enforce the Hard Persona Gate during the Kickoff protocol, requiring physical inspection of active persona files prior to plan formulation.
- Require plans to explicitly cite 2-3 governing rules from active agent definitions.
- Coordinate domain specialist selection from external agency catalogs (e.g. Agency Agents integration).
- Maintain clear separation between Core Agents, Milestone Agents, Optional Specialists, and Deferred Agents.

## Dependencies
- [[Kernel]]: Integrated into BOOT Sequence step 6 and Kickoff protocol pre-planning validation.
- [[Skills]]: Leverages skill definitions to supply behavioral rules and capabilities for workforce personas.
- [[30_DECISIONS.md]]: Governed by canonical architectural decision [[DEC-003]].

## Runtime References
- `brain/60_AGENTS.md`: Authoritative roster of active, deferred, and removed agents for the project.
- `integrations/agency_agents.md`: Workforce selection protocol mapping domain needs to Agency Agents definitions.
- `.agents/skills/`: Directory housing behavioral instructions for active agents.
- `.cursor/rules/`: Directory housing IDE persona rules for Cursor agents.

## Invariants
- Single source of truth: The active workforce roster lives exclusively in `[[60_AGENTS.md]]`.
- Hard Persona Gate: Agents must physically read the active persona rule files from disk before formulating an implementation plan—guessing agent rules from memory is strictly forbidden.
- Explicit citation: Kickoff implementation plans must explicitly cite 2-3 governing rules from the active workforce definitions.
- Separation of concerns: Workforce roles define domain authority and perspectives; core kernel rules remain authoritative for state management and protocol enforcement.

## Notes
- Enables flexible, specialized team configurations tailored to specific technical domains without bloating the kernel.
- Works synergistically with the Ponytail restraint filter to ensure specialized agents remain lean and disciplined.

## Future Changes
- M3: Automatic workforce profile recommendations during project initialization based on detected languages and frameworks.
