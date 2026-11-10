# Systems Architecture

This directory defines the high-level components ("Systems") of the project. AI-maintained. See `AGENTS.md` → Ownership.

## What is a System?
In genOS, a "System" is a core architectural pillar of the project (e.g., `SaveSystem`, `Combat`, `Authentication`). It represents a discrete area of functionality with a specific purpose, defined boundaries, and clear responsibilities. 

## Single Source of Truth
**Status and system knowledge live only in each `brain/systems/<Name>.md`.**
- Do not put Status in this README file.
- The `Systems Index` table below is for navigation only.
- Store only design intent, invariants, dependencies, and notes that cannot be reliably inferred from the implementation source (code, assets, engine).
- **Do not duplicate implementation details** (like specific variable names, API endpoints, or exact code paths) unless strictly necessary for cross-system understanding.

## Relationship to Other Brain Files
- **PROJECT**: Defines the vision. Systems implement the vision.
- **ROADMAP**: Defines milestones. A milestone might require updating or creating a system.
- **DECISIONS**: Architectural choices that shape the system. If a system's core invariants change, a Decision should be recorded.
- **PROGRESS**: Tracks execution state. `systems_in_scope` tells the agent which systems to load into context for the current session.
- **Implementation**: The actual codebase. Systems documents are the semantic truth; the codebase is the implementation truth.

## Naming Conventions
- Use PascalCase for system names (e.g., `SaveSystem.md`, `PlayerMovement.md`).
- Keep names concise and descriptive.

## One Responsibility
- Every system must have exactly **one** primary responsibility.
- If a system becomes too large or handles multiple disparate domains, it must be split.

## Splitting and Merging
- **Split** a system when its responsibilities grow too broad, or when a distinct subsystem emerges that other systems need to depend on independently.
- **Merge** systems if their boundaries blur to the point where they are functionally a single component.
- Always update `DECISIONS.md` when splitting or merging systems, and update the `Systems Index` below.

## Directory Structure & Categorization
genOS supports two organizational layouts:
1. **Flat Layout (Default):** For small-to-medium projects, place system documents directly in `brain/systems/<Name>.md`.
2. **1-Level Category Subfolders (Recommended for 10+ Systems):** When systems scale, group them into single-level domain subfolders (e.g. `brain/systems/core/`, `brain/systems/gameplay/`, `brain/systems/ui/`, `brain/systems/network/`, `brain/systems/data/`).

**Critical Invariant — Globally Unique Names:** Every system filename must remain unique across all folders (e.g., only one `Combat.md`). This ensures Obsidian `[[Combat]]` wikilinks and `systems_in_scope: [Combat]` resolve cleanly and deterministically without path ambiguity.

## AI Maintenance
- Create new systems by duplicating `SYSTEM.md`.
- Keep the `Systems Index` table updated.
- Update a system document when its design intent, invariants, dependencies, or Status changes.
- **Do not** update system documents for pure code edits or minor bug fixes that don't alter the architecture.

---

## Systems Index

| System | Category | Description | File |
|--------|----------|-------------|------|
| [[Kernel]] | Core | Governs session lifecycle, state handoff, and execution protocols across AI agents. | `brain/systems/Kernel.md` |
| [[Updater]] | Maintenance | Manages framework upgrade lifecycle while strictly preserving user project brain, custom configurations, and source code. | `brain/systems/Updater.md` |
| [[Skills]] | Execution | Manages specialized agent capabilities, Superpowers execution patterns, and senior developer restraint protocols. | `brain/systems/Skills.md` |
| [[Workforce]] | Governance | Coordinates active, deferred, and milestone-specific AI agents, enforcing the Hard Persona Gate before planning. | `brain/systems/Workforce.md` |
