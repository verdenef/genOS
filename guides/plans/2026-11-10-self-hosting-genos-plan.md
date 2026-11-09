# Self-Hosting genOS (genOS for genOS) Implementation Plan

> Saved as `guides/plans/2026-11-10-self-hosting-genos-plan.md`. Follows the `kickoff` protocol (`AGENTS.md`, `guides/prompts/workflow-kickoff.md`) and `writing-plans` format.

**Goal:** Transform `d:\GameOS` into a self-hosted, dogfooded genOS project that uses genOS to track its own architecture, decisions, and roadmap, while archiving clean starter templates for downstream projects.

**Architecture:** Separate genOS's living Project Brain (`brain/`) from the uninitialized starter template (`templates/brain/`). Populate genOS's Project Brain with its real intent, the canonical architectural decisions (`DEC-001` through `DEC-005`), the M1–M3 roadmap, and the four foundational system definitions.

**Tech Stack:** Markdown (`[[wikilink]]` Obsidian-compatible), YAML (`20_PROGRESS.yaml`), Git.

---

## Global Constraints

- **Single Source of Truth:** Follow `AGENTS.md` Ownership table strictly.
- **Zero Fiction / Grounded in Reality:** Document only decisions and architectural features that actually exist in genOS.
- **Downstream Safety:** Ensure `templates/brain/` preserves the pristine, uninitialized `_TBD_` templates so new downstream projects can be initialized with a clean slate.
- **Obsidian Compatibility:** All internal brain cross-references must use `[[wikilink]]` syntax.
- **Doctor Compliant:** After initialization, the Project Brain must pass the Doctor diagnostic check with all green checks.

---

## Persona Gate & Ponytail Restraint Filter

### Governing Agent Rules (Inspected: `.agents/skills/ponytail/SKILL.md`)
1. *"The best code is the code you never wrote." Climb the Ladder of Restraint (YAGNI -> Reuse -> Stdlib -> Minimal code).*
2. *"Be ruthless about cutting code volume."*
3. *"Never be lazy about security, input validation, trust boundaries, error handling, or test coverage."*

### Ladder of Restraint Evaluation (Pruned Complexity)
- **Rung 1 (YAGNI):** Do not invent an elaborate multi-directory system hierarchy for genOS. Four flat system documents (`Kernel.md`, `Updater.md`, `Skills.md`, `Workforce.md`) completely capture genOS's architectural surface.
- **Rung 2 (Reuse):** Reuse the existing genOS schema and files; do not create custom non-standard brain formats.
- **Rung 3 (Templates):** Store clean starter templates in `templates/brain/` by simply copying the existing blank state before writing genOS's self-hosting data.

---

## Tasks

### Task 1: Archive Clean Starter Templates into `templates/brain/`

**Files:**
- Create: `templates/brain/00_PROJECT.md`
- Create: `templates/brain/20_PROGRESS.yaml`
- Create: `templates/brain/30_DECISIONS.md`
- Create: `templates/brain/40_BACKLOG.md`
- Create: `templates/brain/50_ROADMAP.md`
- Create: `templates/brain/60_AGENTS.md`
- Create: `templates/brain/systems/README.md`
- Create: `templates/brain/systems/SYSTEM.md`

- [ ] **Step 1:** Create `templates/brain/` and `templates/brain/systems/` directories.
- [ ] **Step 2:** Copy current template files (`00_PROJECT.md`, `20_PROGRESS.yaml`, `30_DECISIONS.md`, `40_BACKLOG.md`, `50_ROADMAP.md`, `60_AGENTS.md`, `systems/README.md`, `systems/SYSTEM.md`) into `templates/brain/`.
- [ ] **Step 3:** Verify that all template files in `templates/brain/` contain clean `_TBD_` placeholders.

---

### Task 2: Initialize genOS Intent & Execution RAM

**Files:**
- Modify: `brain/00_PROJECT.md`
- Modify: `brain/20_PROGRESS.yaml`
- Modify: `brain/60_AGENTS.md`

- [ ] **Step 1: Write `brain/00_PROJECT.md`**
  - Define Vision: Zero-context-loss, location-agnostic operating kernel for AI-assisted software development across multiple IDEs and models.
  - Define Scope: Kernel protocols (`AGENTS.md`), memory surfaces (`brain/`), Superpowers & Agency skills, update pipeline.
  - Define Invariants: Single source of truth, filesystem-only persistence, zero-history recovery.
- [ ] **Step 2: Update `brain/60_AGENTS.md`**
  - Document the active workforce for developing genOS: `ponytail` (restraint), `writing-plans`, `writing-skills`, `systematic-debugging`, `test-driven-development`.
- [ ] **Step 3: Update `brain/20_PROGRESS.yaml`**
  - Set `current_milestone: M2`
  - Set `systems_in_scope: [Kernel, Updater, Skills, Workforce]`
  - Set `last_agent: antigravity`
  - Set `last_ide: antigravity`
  - Set `working_on: []`
  - Set `session_summary` documenting transition to self-hosting.

---

### Task 3: Record Canonical Decisions (`DEC-001` through `DEC-005`)

**Files:**
- Modify: `brain/30_DECISIONS.md`

- [ ] **Step 1:** Update Decisions Index table with `DEC-001` through `DEC-005`.
- [ ] **Step 2:** Write detailed decision entries:
  - `DEC-001`: Plain-Text Keyword Command Architecture (`kickoff`, `shutdown`, `doctor`, `status`, `batch`, `update`).
  - `DEC-002`: Timeless 3-Tier Model Guidance (Flagship, Balanced, Fast).
  - `DEC-003`: Hard Persona Gate and Ponytail Restraint Filter (Pre-planning mandatory file read & Ladder of Restraint).
  - `DEC-004`: Dual-Method Framework Auto-Updater with Strict Brain Shielding.
  - `DEC-005`: Copy-Pasteable Execution Handoff Blocks.

---

### Task 4: Define genOS Roadmap (M1, M2, M3)

**Files:**
- Modify: `brain/50_ROADMAP.md`

- [ ] **Step 1:** Update Roadmap Index:
  - `M1` | `done` | Core Kernel & Brain Architecture (v1/v2)
  - `M2` | `active` | genOS v3 Ergonomics, Superpowers Integration & Self-Hosting
  - `M3` | `planned` | Package Distribution & CLI Bootstrapping
- [ ] **Step 2:** Write M1 section (completed criteria for kernel, progress RAM, Obsidian compatibility).
- [ ] **Step 3:** Write M2 section (active criteria for keyword commands, auto-updater, ponytail gate, copy-paste handoff, self-hosting brain).
- [ ] **Step 4:** Write M3 stub (planned criteria for `npx genos` or Python installer).

---

### Task 5: Define Core Systems & Navigation Index

**Files:**
- Create: `brain/systems/Kernel.md`
- Create: `brain/systems/Updater.md`
- Create: `brain/systems/Skills.md`
- Create: `brain/systems/Workforce.md`
- Modify: `brain/systems/README.md`

- [ ] **Step 1:** Create `Kernel.md` (Purpose: execution protocol, BOOT/SHUTDOWN sequences, Sanity Gate, Location-Agnostic pathing).
- [ ] **Step 2:** Create `Updater.md` (Purpose: upstream release fetching, strict brain & user code protection).
- [ ] **Step 3:** Create `Skills.md` (Purpose: Superpowers skill integration, `.agents/skills/` lifecycle).
- [ ] **Step 4:** Create `Workforce.md` (Purpose: `60_AGENTS.md`, persona management, pre-planning Hard Persona Gate).
- [ ] **Step 5:** Update `brain/systems/README.md` systems index table with links to the four systems.

---

### Task 6: Audit & Verification (Doctor Protocol)

- [ ] **Step 1:** Run `doctor` diagnostic audit on `d:\GameOS\brain/`.
- [ ] **Step 2:** Verify all checks pass:
  - Valid YAML in `20_PROGRESS.yaml`
  - Milestone pointer `M2` matches `50_ROADMAP.md` and is `active`
  - Decisions index in `30_DECISIONS.md` has 5 entries matching sections
  - Systems in scope exist in `brain/systems/`
  - All internal links use `[[wikilink]]` format
- [ ] **Step 3:** Commit all changes to `genos-v3` branch.

---

## Risks & Dependencies

- **Downstream Contamination Risk:** Downstream projects must not inadvertently receive genOS's own brain.
  - *Mitigation:* The `Framework Update Protocol` already explicitly shields `brain/` from overwrites. For fresh projects, the new `templates/brain/` directory will serve as the source of truth for blank initialization.
- **Obsidian Compatibility:** Cross-references between systems, decisions, and roadmap must strictly adhere to `[[wikilink]]` syntax.

---

## Model & Session Recommendation

💡 Recommended: **Claude Opus / Sonnet (Thinking: High)** or **Gemini Pro (Thinking: High)** in a **new session**.

### Copy-Pasteable Execution Command

**Option 1: Subagent-Driven Execution (Recommended):**
```
kickoff execute the approved plan: guides/plans/2026-11-10-self-hosting-genos-plan.md using subagent-driven-development
```

**Option 2: Single-Agent Sequential Execution:**
```
kickoff execute the approved plan: guides/plans/2026-11-10-self-hosting-genos-plan.md
```
