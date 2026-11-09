# Roadmap

Authoritative long-term development roadmap and **sole source of truth for milestone definitions**.
AI-owned. See `AGENTS.md` → Ownership.

**This file owns:** milestone IDs, objectives, deliverables, completion criteria, dependencies, and lifecycle status.  
**This file does not own:** live session execution state (that is `20_PROGRESS.yaml` only).

Do not copy milestone criteria into Progress or Backlog. Progress stores only `current_milestone` (ID) plus execution RAM.

**Status values:** `planned` | `active` | `done` | `cancelled`

**ID conventions:**
- Program milestones: `M1`, `M2`, … (or named phases: `EVAL`, `RC`, etc.)
- Child milestones: `M1.1`, `M1.2`, … under a parent

---

## Index

| ID | Parent | Status | Title |
|----|--------|--------|-------|
| M1 | — | done | Core Kernel & Brain Architecture (v1 - v2) |
| M2 | — | active | genOS v3 Ergonomics, Superpowers Integration & Self-Hosting |
| M3 | — | planned | Package Distribution & CLI Bootstrapping |

---

## Suggested sequence

`M1` -> `M2` -> `M3`

---

## M1 — Core Kernel & Brain Architecture (v1 - v2)

- **Status:** done
- **Objective:** Establish the zero-context-loss Project Brain architecture, single source of truth ownership rules, YAML progress execution RAM, Obsidian wikilink compatibility, and basic Doctor audit.
- **Deliverables & Completion Criteria:**
  - Strict ownership rules defined in `AGENTS.md` eliminating duplicate state across brain files.
  - Project Brain partitioned into intent (`[[00_PROJECT.md]]`), execution RAM (`[[20_PROGRESS.yaml]]`), decisions (`[[30_DECISIONS.md]]`), ad-hoc backlog (`[[40_BACKLOG.md]]`), roadmap (`[[50_ROADMAP.md]]`), and workforce (`[[60_AGENTS.md]]`).
  - Obsidian wikilink compatibility (`[[wikilink]]`) standardized across internal references for Graph View visualization.
  - Automated diagnostic checklist and Doctor protocol validating YAML structure, milestone pointers, and index synchronization.
  - Single source of truth enforcement verified across multiple development sessions.
- **Done when:** Core kernel specification and brain architecture are fully verified, complete, and operating reliably across multiple sessions.

---

## M2 — genOS v3 Ergonomics, Superpowers Integration & Self-Hosting

- **Status:** active
- **Objective:** Overhaul genOS ergonomics with plain-text keyword commands, timeless model tiers, Hard Persona Gate + Ponytail restraint filter, 1-click framework updating with strict Brain shielding, copy-paste execution handoffs, and self-hosted dogfooding.
- **Deliverables:**
  - Plain-text keyword commands (`kickoff`, `shutdown`, `doctor`, `status`, `batch`, `update`) supported with optional user intent directives ([[DEC-001]]).
  - Pre-planning Hard Persona Gate requiring physical inspection of active agent definitions and Ponytail Ladder of Restraint evaluation ([[DEC-003]]).
  - Timeless 3-Tier Model Guidance (Flagship, Balanced, Fast) mapping platform models to cognitive complexity ([[DEC-002]]).
  - Dual-method framework auto-updater (`upstream` git tracking or GitHub release archive) with strict shielding of `brain/` and user files ([[DEC-004]]).
  - Copy-pasteable execution handoff blocks output at planning conclusion for frictionless fresh-session transitions ([[DEC-005]]).
  - Graphify Code Topology Hook ([[DEC-006]]) with dedicated skill and multi-IDE MCP profile presets.
  - Self-hosted Project Brain in `d:\GameOS` with clean starter templates preserved in `templates/brain/`.
  - Canonical system definitions for `Kernel`, `Updater`, `Skills`, and `Workforce` in `brain/systems/`.
- **Done when:** Self-hosting brain is fully initialized, all canonical systems defined, and passes Doctor with 100% clean check.

---

## M3 — Package Distribution & CLI Bootstrapping

- **Status:** planned
- **Objective:** Provide a lightweight CLI tool (`npx genos init` or `pip install genos-cli`) to scaffold or upgrade genOS in any project repository with a single command.
- **Deliverables:**
  - Lightweight CLI runner/tool (`genos init`, `genos update`, `genos doctor`).
  - Zero-dependency project initialization bootstrapping fresh projects from `templates/brain/`.
  - Automatic IDE environment detection and rule/config installation (.cursor, .gemini, etc.).
- **Done when:** A developer can execute a single CLI command in an arbitrary project root and immediately begin using genOS with full IDE integration.
