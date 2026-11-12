# Codebase-Aware Graphify Onboarding (Setup & Update) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make Day 0 setup (`guides/prompts/setup-init.md`), framework `update` (`AGENTS.md`, `guides/prompts/update.md`), and `kickoff tooling` actively detect existing/mature codebases and strongly recommend—and upon human approval install and build—local `--code-only` Graphify topology.

**Architecture:** Reuse the existing Phase 1/2 onboarding flow in `guides/prompts/setup-init.md`, the 5-phase verify-first updater (`AGENTS.md` + `guides/prompts/update.md`), `kickoff tooling` smart routing (`AGENTS.md`), and `profiles/templates/mcp-graphify.json` without introducing new commands or installer scripts. Key Graphify off **actual source code presence** (skip only for blank or pure prose/manuscript repos; in hybrid code + paper repos, recommend Graphify for the codebase and exclude `paper/`, `manuscript/`, `docs/`, `*.tex`, `*.bib`, `*.docx` in `.graphifyignore`), preserve `update`'s short-circuit when core files are current (emitting only a 1-line `kickoff tooling` tip if Graphify is missing), and preserve silent fallback during normal `kickoff`.

**Tech Stack:** Markdown (`[[wikilink]]`), YAML, Git.

---

## Global Constraints

- **Human Approval Gate Preserved:** Never auto-install `graphifyy[mcp]`, write `.gitignore`/`.mcp.json`, or run `graphify extract` without explicit human approval.
- **Local `--code-only` & Zero Brain Contamination (`[[DEC-006]]`):** Always build graphs offline with `--code-only`, keep `graphify-out/` gitignored, and never store graph artifacts in `brain/`.
- **Skip Blank & Pure-Prose Projects:** Do not push Graphify on blank greenfield repos (no source tree yet) or pure non-coding/prose repos; in hybrid code + manuscript repos, index only source code (excluding prose/manuscript paths in `.graphifyignore`); preserve silent fallback during normal `kickoff`.
- **Verify-First Short-Circuit Preserved (`[[DEC-008]]`):** If `update` finds all core files match upstream, short-circuit cleanly without mutating files (emit at most a 1-line `kickoff tooling` tip if an existing codebase lacks Graphify).
- **Ponytail Restraint & Doctor Compliance:** Minimal targeted edits with zero speculative scripts; maintain 100% clean Brain Health Report (`30_DECISIONS.md` Index sync, `50_ROADMAP.md` Index sync, valid YAML, `[[wikilink]]` syntax).

---

## Tasks

### Task 1: Codebase-Aware Graphify Onboarding in `setup-init.md` and `AGENTS.md` (`kickoff tooling`)

**Files:**
- Modify: `guides/prompts/setup-init.md` (lines 14–27, 37–41)
- Modify: `AGENTS.md` (line 182)

**Interfaces:**
- Consumes: `profiles/<profile>/profile.yaml` (`recommended_mcps`), `profiles/templates/mcp-graphify.json`, `.agents/skills/graphify/SKILL.md`.
- Produces: Active codebase-maturity detection (including hybrid code + paper repos) during Day 0 Phase 1/2 and `kickoff tooling` so existing codebases get approval-gated Graphify installation and initial graph generation.

- [ ] **Step 1: Update `guides/prompts/setup-init.md` Phase 1 Steps 2–4 (`Scan the workspace` & `Suggest a Stack Profile`, lines 14–27)**
  - Expand workspace scanning to note codebase maturity/size (existing source directories or ~20+ source files excluding `genOS/`, `node_modules/`, `vendor/`, `build/`, `.git/`), blank repos, pure prose manuscripts, and **hybrid code + research-paper repos**.
  - Note in Step 3–4 that hybrid code + paper repos stay in **one unified `brain/`** and may blend a coding profile + `academic-research` using 1-level `brain/systems/` category subfolders (e.g., `brain/systems/code/` and `brain/systems/research/` with globally unique filenames).

- [ ] **Step 2: Update `guides/prompts/setup-init.md` Phase 2 Step 3 (`Code Topology`, lines 37–41)**
  - Replace the passive optional bullet with explicit codebase-aware branching keyed off actual source code presence:
    - **Skip** only for pure non-coding/prose repos (no codebase) or blank greenfield repos with no source tree yet (note Graphify can be added later via `kickoff tooling`).
    - **Existing / mature codebase (including hybrid code + paper repos, or `graphify-mcp` in `recommended_mcps`):** Check whether `graphify` CLI and `graphify-out/graph.json` already exist. If missing, **strongly recommend** enabling local `--code-only` Graphify AST topology and ask human approval to run the full setup:
      1. Install once per machine: `uv tool install "graphifyy[mcp]"` (or `pipx install` / `pip install` fallback)
      2. Create repo-root `.graphifyignore` restricting scope to source code folders (and excluding prose/manuscript paths such as `paper/`, `manuscript/`, `docs/`, `*.tex`, `*.bib`, `*.docx` in hybrid repos)
      3. Add `graphify-out/` to `.gitignore` and build locally with `graphify extract . --code-only`
      4. Register the MCP server from `profiles/templates/mcp-graphify.json` in `.mcp.json` / `.cursor/mcp.json`

- [ ] **Step 3: Update `AGENTS.md` `### Kickoff Smart Routing` (`kickoff tooling` row, line 182)**
  - Update the `kickoff tooling` row so it reads:
    ``| `kickoff tooling` | Configure/refresh MCP servers from `profiles/<profile>/profile.yaml` (`recommended_mcps`) and offer approval-gated `--code-only` Graphify installation/graph build if an existing codebase lacks `graphify-out/graph.json` |``

- [ ] **Step 4: Verification**
  - Read modified lines in `guides/prompts/setup-init.md` and `AGENTS.md` to confirm formatting, table alignment, and human-approval gates.

---

### Task 2: Add Graphify Readiness Check to `update` & Align Documentation

**Files:**
- Modify: `AGENTS.md` (lines 330–341)
- Modify: `guides/prompts/update.md` (lines 23–65)
- Modify: `.agents/skills/genos-update/SKILL.md` (lines 8–10)
- Modify: `.cursor/rules/genos-update.mdc` (line 6)
- Modify: `guides/guide.md` (lines 86, 134–138)
- Modify: `README.md` (lines 191–199)

**Interfaces:**
- Consumes: `profiles/templates/mcp-graphify.json`, `.agents/skills/graphify/SKILL.md`, `AGENTS.md` Framework Update Protocol.
- Produces: Legacy/outdated `update` migration plans that detect existing codebases lacking Graphify and offer approval-gated setup, plus clean short-circuit behavior when already up to date.

- [ ] **Step 1: Update `AGENTS.md` `## Framework Update Protocol` (lines 330–341)**
  - **Phase 2 (`Verify Drift & Detect Generation`):** Alongside core file drift checks, inspect whether the host repository has an existing/mature coding codebase (skip only for blank or pure-prose repos; hybrid code + paper repos qualify) that lacks `graphify` CLI or `graphify-out/graph.json`.
    - In **Short-circuit if current**: preserve the no-mutation stop (`genOS is already up to date (v3.2). No changes made.`), appending a 1-line tip (`Tip: existing codebase detected without Graphify — run kickoff tooling to configure local --code-only code topology.`) only when an existing coding codebase lacks `graphify-out/graph.json`.
  - **Phase 3 (`Propose Upgrade Plan & Wait for Approval`):** When an upgrade is required and an existing coding codebase lacks Graphify, include a **Recommended Graphify Setup** section in the approval-gated Upgrade & Migration Plan (`uv tool install "graphifyy[mcp]"`, `.graphifyignore` excluding any manuscript/prose paths like `paper/`, `manuscript/`, `*.tex`, `*.bib`, `*.docx`, `.gitignore` `graphify-out/`, `graphify extract . --code-only`, and MCP registration via `profiles/templates/mcp-graphify.json`).
  - **Phase 4 & 5 (`Apply` & `Post-Upgrade Doctor`):** If approved by the human, run the Graphify setup alongside core updates (never touching `brain/` or user source code) and report Graphify status in the post-upgrade summary.

- [ ] **Step 2: Mirror the Graphify readiness check in `guides/prompts/update.md` (lines 23–65)**
  - Update Sections 2 (`Verify Drift & Detect Installation Generation`), 3 (`Propose Upgrade & Migration Plan`), 4 (`Apply Approved Upgrade`), and 5 (`Post-Upgrade Doctor & Proof`), adding a `Code Topology (Graphify)` row to the Upgrade Health Report table (`✅ Configured / ⏭️ Skipped / ℹ️ Tip`).

- [ ] **Step 3: Concisely align `.agents/skills/genos-update/SKILL.md`, `.cursor/rules/genos-update.mdc`, `guides/guide.md`, and `README.md`**
  - Note in `genos-update/SKILL.md` and `genos-update.mdc` that outdated repos with an existing codebase also get an approval-gated Graphify setup recommendation in the Upgrade & Migration Plan.
  - Update `guides/guide.md` (Day 0 Setup Wizard bullet 3 and `Code Topology with Graphify` section) and `README.md` (`Upgrading an Existing Project` / `Local Code Topology with Graphify` sections) to reflect codebase-aware recommendation during both Day 0 setup and `update`.

- [ ] **Step 4: Verification**
  - Read all modified sections across the 6 files and run `python -m unittest discover -s guides/scripts -p "test_*.py" -v` (expect `13/13` OK).

---

### Task 3: Record `DEC-010`, Update System Docs / Roadmap / Progress, Verify & Push

**Files:**
- Modify: `brain/30_DECISIONS.md`
- Modify: `brain/50_ROADMAP.md`
- Modify: `brain/systems/Updater.md`
- Modify: `brain/systems/Skills.md`
- Modify: `brain/systems/Kernel.md`
- Modify: `brain/20_PROGRESS.yaml`

**Interfaces:**
- Consumes: Tasks 1–2 edits.
- Produces: Synchronized Project Brain (`DEC-010`, `M2` deliverable, updated system docs, `session_summary`) passing all Doctor, test, and wikilink checks.

- [ ] **Step 1: Record `DEC-010: Codebase-Aware Graphify Recommendation in Setup & Update` in `brain/30_DECISIONS.md`** (Index row + detailed decision entry using `[[wikilink]]` syntax).
- [ ] **Step 2: Add `[[DEC-010]]` deliverable under `M2` in `brain/50_ROADMAP.md`**.
- [ ] **Step 3: Update `brain/systems/Updater.md` (`Responsibilities`, `Dependencies`), `brain/systems/Skills.md` (`Responsibilities`, `Dependencies`), and `brain/systems/Kernel.md` (`Dependencies` adding `[[DEC-009]]` and `[[DEC-010]]`)**.
- [ ] **Step 4: Update `brain/20_PROGRESS.yaml` `last_updated` (`2026-11-12`) and `session_summary`**.
- [ ] **Step 5: Run full verification**
  - Doctor audit (`run_doctor_audit.py`: expect `10` decisions matching Index, `8/8` checks PASS).
  - Unit tests (`python -m unittest discover -s guides/scripts -p "test_*.py" -v`: expect `13/13` OK).
  - Wikilink check (`0` non-wikilink internal refs in `brain/`).
- [ ] **Step 6: Commit & push to `main` and sync `genos-v3`**.

---

## Execution Handoff

After reviewing and approving this plan, start execution in a fresh session using one of the following commands:

**Option 1: Subagent-Driven Execution (Recommended):**
```
kickoff execute the approved plan: docs/superpowers/plans/2026-11-12-graphify-codebase-onboarding.md using subagent-driven-development
```

**Option 2: Single-Agent Sequential Execution:**
```
kickoff execute the approved plan: docs/superpowers/plans/2026-11-12-graphify-codebase-onboarding.md
```
