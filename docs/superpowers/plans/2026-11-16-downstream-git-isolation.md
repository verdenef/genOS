# Downstream genOS Sidecar Git Isolation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ensure downstream projects using genOS as a sidecar (`genOS/`) only track and push `genOS/brain/` (and `.gitignore`) to GitHub, completely ignoring all framework scaffolding (`guides/`, `profiles/`, `templates/`, `integrations/`, `AGENTS.md`, etc.).

**Architecture:** Create a native nested `.gitignore` template (`templates/sidecar.gitignore`) using Git's allowlist pattern (`/*`, `!/brain/`, `!/.gitignore`). Update Day 0 setup (`guides/prompts/setup-init.md`) to automatically deploy this `.gitignore` whenever genOS is placed in a subfolder, update 1-prompt auto-install scripts and guides (`guides/guide.md`, `README.md`), record `DEC-011`, and update roadmap and system docs with 100% Doctor integrity verification.

**Tech Stack:** Git, Markdown (`[[wikilink]]`), YAML, Python.

---

## Global Constraints

- **Single Source of Truth (`AGENTS.md`):** Do not duplicate milestone or system state across brain files.
- **Obsidian Wikilink Compatibility:** All internal brain cross-references MUST use `[[wikilink]]` syntax.
- **Strict Brain Shielding (`[[DEC-004]]`):** Do not touch or overwrite existing brain files outside of standard decision and roadmap updates.
- **Ponytail Restraint Filter:** Minimal, targeted changes without creating unnecessary scripts or abstractions.
- **Doctor Compliance:** 100% PASS on YAML integrity, index synchronization in `30_DECISIONS.md` and `50_ROADMAP.md`, and system scopes.

---

## Tasks

### Task 1: Create `templates/sidecar.gitignore` & Test Git Ignore Behavior

**Files:**
- Create: `templates/sidecar.gitignore`
- Test: Local simulated git repo verification script

**Interfaces:**
- Consumes: Git directory-level ignore specifications.
- Produces: Reusable `.gitignore` template for downstream sidecars.

- [ ] **Step 1: Create `templates/sidecar.gitignore`**
  ```gitignore
  # Ignore all genOS framework scaffolding in downstream projects
  /*

  # Allowlist project-specific memory and this ignore file
  !/brain/
  !/.gitignore
  ```

- [ ] **Step 2: Verify git behavior using a temporary simulation in scratch/**
  - Create a scratch directory with a simulated parent repo and a `genOS/` subfolder containing `brain/00_PROJECT.md`, `AGENTS.md`, `guides/guide.md`, and `.gitignore`.
  - Run `git status` in the scratch repo to confirm Git only tracks `genOS/brain/00_PROJECT.md` and `genOS/.gitignore`, completely ignoring `genOS/AGENTS.md` and `genOS/guides/`.
  - Clean up scratch artifacts.

- [ ] **Step 3: Commit `templates/sidecar.gitignore`**
  ```bash
  git add templates/sidecar.gitignore
  git commit -m "feat(templates): add sidecar gitignore template for downstream projects"
  ```

---

### Task 2: Automate Sidecar Git Isolation in `setup-init.md`, `guide.md`, and `README.md`

**Files:**
- Modify: `guides/prompts/setup-init.md` (Phase 1, Step 1)
- Modify: `guides/guide.md` (lines 48–53, 56–58)
- Modify: `README.md` (Option A Auto-Install & sidecar instructions)

**Interfaces:**
- Consumes: `templates/sidecar.gitignore`.
- Produces: Automated deployment during Phase 1 onboarding and updated installation documentation.

- [ ] **Step 1: Update `guides/prompts/setup-init.md`**
  - In Phase 1 Step 1 (`Clean Slate & Layout Check`), add an explicit step:
    - If genOS is inside a subfolder (e.g. `genOS/`), verify whether `genOS/.gitignore` exists. If missing, copy `templates/sidecar.gitignore` to `genOS/.gitignore` (or create it with `/*`, `!/brain/`, `!/.gitignore`) so downstream git commits never track framework scaffolding.

- [ ] **Step 2: Update `guides/guide.md` & `README.md`**
  - Update Option A 1-Prompt Auto-Install command block to copy `templates/sidecar.gitignore` into `genOS/.gitignore`.
  - Add guidance on cleaning up existing projects that already pushed scaffolding (`git rm -r --cached genOS/guides genOS/profiles ...`).

- [ ] **Step 3: Verification**
  - Verify formatting and table alignment in `setup-init.md`, `guide.md`, and `README.md`.
  - Run unit test suite: `python -m unittest discover -s guides/scripts -p "test_*.py" -v` (13/13 OK).

- [ ] **Step 4: Commit changes**
  ```bash
  git add guides/prompts/setup-init.md guides/guide.md README.md
  git commit -m "feat(setup): automate sidecar gitignore isolation and update setup docs"
  ```

---

### Task 3: Record `DEC-011`, Update Systems, Roadmap, Progress, and Verify

**Files:**
- Modify: `brain/30_DECISIONS.md`
- Modify: `brain/50_ROADMAP.md`
- Modify: `brain/systems/Kernel.md`
- Modify: `brain/systems/Updater.md`
- Modify: `brain/20_PROGRESS.yaml`

**Interfaces:**
- Consumes: Tasks 1–2 completion.
- Produces: Fully synchronized Project Brain with `DEC-011`, `M2` deliverable, and passing Doctor audit.

- [ ] **Step 1: Record `DEC-011: Downstream genOS Sidecar Git Isolation` in `brain/30_DECISIONS.md`**
  - Add row to `## Index` table: `| DEC-011 | accepted | 2026-11-16 | Downstream genOS Sidecar Git Isolation |`
  - Add entry under `## Decisions` detailing the nested `.gitignore` architecture, reason, and impact using `[[wikilink]]` syntax.

- [ ] **Step 2: Update `brain/50_ROADMAP.md`**
  - Add `[[DEC-011]]` deliverable under `## M2`.

- [ ] **Step 3: Update `brain/systems/Kernel.md` and `brain/systems/Updater.md`**
  - Add `[[DEC-011]]` to Dependencies and update Responsibilities/Invariants regarding sidecar git isolation.

- [ ] **Step 4: Update `brain/20_PROGRESS.yaml`**
  - `last_updated: "2026-11-16"`
  - `session_summary`: self-contained summary of the sidecar Git isolation implementation.

- [ ] **Step 5: Run full Doctor and unit test verification**
  - Python check: valid YAML, 11 decisions matching Index, 3 milestones matching Index, 0 non-wikilinks.
  - Unit tests: 13/13 passing.

- [ ] **Step 6: Commit and push**
  - Commit to `main`: `git commit -am "feat(brain): record DEC-011 and update roadmap, systems, and progress"`
  - Push to `main` and sync `genos-v3`.

---

## Execution Handoff

After reviewing and approving this plan, start execution in a fresh session using one of the following commands:

**Option 1: Subagent-Driven Execution (Recommended):**
```
kickoff execute the approved plan: docs/superpowers/plans/2026-11-16-downstream-git-isolation.md using subagent-driven-development
```

**Option 2: Single-Agent Sequential Execution:**
```
kickoff execute the approved plan: docs/superpowers/plans/2026-11-16-downstream-git-isolation.md
```
