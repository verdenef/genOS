# Workforce Gap Check & Lifecycle Routing Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Surface `kickoff workforce` and `kickoff tooling` natively inside `AGENTS.md`, expand workforce audits to read `20_PROGRESS.yaml` and `brain/systems/*.md`, and add an automatic **Workforce Gap Check** during normal `kickoff` so newly needed specialist personas (such as Security or Accessibility) are caught and proposed for approval before planning.

**Architecture:** Reuse the existing `kickoff workforce` variant (`guides/prompts/workflow-kickoff.md`) and zero-dependency installer (`guides/scripts/install_agent.py`) rather than inventing a new top-level command. Update `AGENTS.md`, `guides/prompts/workflow-kickoff.md`, `integrations/agency_agents.md`, `brain/systems/Workforce.md`, and record `DEC-009` in `brain/`.

**Tech Stack:** Markdown (`[[wikilink]]`), YAML, Git.

---

## Global Constraints

- **No New Top-Level Command:** Keep the 6 top-level commands unchanged (`kickoff`, `shutdown`, `doctor`, `status`, `batch`, `update`). Use `kickoff workforce` for explicit re-audits and `kickoff`'s Hard Persona Gate for automatic gap detection.
- **Human Approval Gate Preserved:** Never auto-install newly discovered agents without explicit human approval.
- **Ponytail Restraint:** Minimal, targeted edits with zero speculative scripts or duplicate docs.
- **Doctor Compliance:** Maintain 100% clean Brain Health Report (`30_DECISIONS.md` Index sync, `50_ROADMAP.md` Index sync, valid YAML, `[[wikilink]]` syntax).

---

## Tasks

### Task 1: Wire `kickoff workforce` / `kickoff tooling` & Workforce Gap Check Into Kernel & Kickoff Prompt

**Files:**
- Modify: `AGENTS.md` (lines 163, 176–184)
- Modify: `guides/prompts/workflow-kickoff.md` (lines 24–28)

**Interfaces:**
- Consumes: `brain/60_AGENTS.md`, `brain/20_PROGRESS.yaml`, `guides/scripts/install_agent.py --list <keyword>`.
- Produces: Native kernel routing for `kickoff workforce` / `kickoff tooling` and pre-planning gap prompts before planning uncovered domains.

- [ ] **Step 1: Update `AGENTS.md` `## Commands` (`kickoff` row) and `### Kickoff Smart Routing`**
  - In `kickoff` row (`AGENTS.md:163`), add inside the Hard Persona Gate step:
    `check for domain gaps against active milestone, systems_in_scope, or user intent (if uncovered—e.g. security, stats, accessibility—query install_agent.py --list and ask approval before planning)`
  - In `### Kickoff Smart Routing` (`AGENTS.md:176-182`), add two rows:
    - ``| `kickoff tooling` | Configure/refresh MCP servers from `profiles/<profile>/profile.yaml` (`recommended_mcps`) |``
    - ``| `kickoff workforce` | Re-audit `00_PROJECT.md`, `20_PROGRESS.yaml`, `50_ROADMAP.md`, `30_DECISIONS.md`, and `brain/systems/*.md` (`integrations/agency_agents.md`) to add needed specialists or retire completed Milestone Agents |``

- [ ] **Step 2: Update `guides/prompts/workflow-kickoff.md` Step 4 (`Hard Persona Gate`)**
  - Add sub-bullet under Step 4:
    `- **Workforce Gap Check:** Compare active milestone, systems_in_scope, and user intent against brain/60_AGENTS.md (including Deferred Agents). If an uncovered discipline emerges (e.g., security, accessibility, payments, stats), run python <genos>/guides/scripts/install_agent.py --list <keyword> and ask human approval to install and add it before formulating the plan.`

- [ ] **Step 3: Verification**
  - Read modified lines in `AGENTS.md` and `guides/prompts/workflow-kickoff.md` to confirm formatting and zero contradictions.

---

### Task 2: Expand `integrations/agency_agents.md` Audit Scope & Update `brain/systems/Workforce.md`

**Files:**
- Modify: `integrations/agency_agents.md` (lines 12, 43–44)
- Modify: `brain/systems/Workforce.md`

**Interfaces:**
- Consumes: `brain/00_PROJECT.md`, `brain/20_PROGRESS.yaml`, `brain/50_ROADMAP.md`, `brain/30_DECISIONS.md`, `brain/systems/*.md`.
- Produces: Complete project-progress workforce evaluation rules for both automatic `kickoff` checks and manual `kickoff workforce` runs.

- [ ] **Step 1: Update `integrations/agency_agents.md`**
  - Step 1 (`Audit the Project`): expand from `00_PROJECT.md, 50_ROADMAP.md, and 30_DECISIONS.md` to include `20_PROGRESS.yaml` (`working_on`, `systems_in_scope`) and active `brain/systems/*.md` documents.
  - `## Lifecycle Maintenance`: document both automatic `kickoff` Workforce Gap Checks and explicit `kickoff workforce` re-audits (including promoting `Deferred Agents` when their milestone becomes active and retiring completed Milestone Agents).

- [ ] **Step 2: Update `brain/systems/Workforce.md`**
  - Add Workforce Gap Check and `kickoff workforce` progress-based re-evaluation to `Responsibilities` and `Invariants`, referencing `[[DEC-009]]` alongside `[[DEC-003]]` and `[[DEC-007]]`.

- [ ] **Step 3: Verification**
  - Confirm `[[wikilink]]` syntax and clean formatting in both files.

---

### Task 3: Record `DEC-009`, Update Roadmap/Progress, Verify & Push

**Files:**
- Modify: `brain/30_DECISIONS.md`
- Modify: `brain/50_ROADMAP.md`
- Modify: `brain/20_PROGRESS.yaml`

**Interfaces:**
- Consumes: Tasks 1–2 edits.
- Produces: Synchronized Project Brain (`DEC-009`, `M2` deliverable, `session_summary`) passing all Doctor and test checks.

- [ ] **Step 1: Record `DEC-009: Automatic Workforce Gap Check & Kernel Subcommand Routing` in `brain/30_DECISIONS.md`** (Index row + detailed decision entry).
- [ ] **Step 2: Add `[[DEC-009]]` deliverable under `M2` in `brain/50_ROADMAP.md`**.
- [ ] **Step 3: Update `brain/20_PROGRESS.yaml` `session_summary`**.
- [ ] **Step 4: Run full verification**
  - Doctor audit (`run_doctor_audit.py`: expect `9` decisions matching Index, `8/8` checks PASS).
  - Unit tests (`python -m unittest discover -s guides/scripts -p "test_*.py" -v`: expect `13/13` OK).
  - Wikilink check (`0` non-wikilink internal refs in `brain/`).
- [ ] **Step 5: Commit & push to `main` and sync `genos-v3`**.

---

## Execution Handoff

After saving this plan, start execution using one of the following commands:

**Option 1: Subagent-Driven Execution (Recommended):**
```
kickoff execute the approved plan: docs/superpowers/plans/2026-11-12-workforce-gap-and-lifecycle-routing.md using subagent-driven-development
```

**Option 2: Single-Agent Sequential Execution:**
```
kickoff execute the approved plan: docs/superpowers/plans/2026-11-12-workforce-gap-and-lifecycle-routing.md
```
