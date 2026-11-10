# Verify-First & Plan-Gated Framework Updater Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Upgrade the genOS `update` command and `guides/prompts/update.md` so any `v1`, `v2`, or outdated `v3` project verifies drift against upstream first, short-circuits if current, presents an Upgrade & Migration Plan for approval, and runs post-update Doctor using the newly installed `AGENTS.md`.

**Architecture:** Add a lightweight `> **Framework Version:** 3.2` header to `AGENTS.md`, rewrite `guides/prompts/update.md` as a self-contained 5-phase workflow (`Fetch Read-Only` -> `Verify Drift` -> `Plan & Wait for Approval` -> `Apply` -> `Doctor`), update `AGENTS.md`, `.agents/skills/genos-update/SKILL.md`, `.cursor/rules/genos-update.mdc`, `README.md`, `guides/guide.md`, and record `DEC-008` in `brain/`.

**Tech Stack:** Markdown (`[[wikilink]]`), YAML, Git.

---

## Global Constraints

- **Self-Contained `update.md`:** Must work when pasted directly into a legacy v1 repo whose local `AGENTS.md` lacks Doctor/Update sections.
- **No Unapproved Writes:** Phase 1 & 2 never alter repository files; Phase 3 waits for explicit human approval before Phase 4 writes.
- **Strict Brain & Agent Shielding:** Never overwrite `brain/`, `.obsidian/`, custom profiles, source code, or project-installed Agency Agents during file synchronization.
- **Zero Drift Across Docs:** All `update` summaries (`AGENTS.md`, `SKILL.md`, `.mdc`, `README.md`, `guides/guide.md`, `brain/systems/Updater.md`) must agree cleanly.

---

## Tasks

### Task 1: Add Version Header & Upgrade `Framework Update Protocol` in `AGENTS.md`

**Files:**
- Modify: `AGENTS.md`

- [x] **Step 1:** Add `> **Framework Version:** 3.2` right below `# genOS Kernel` in `AGENTS.md`.
- [x] **Step 2:** Update the `update` row in `AGENTS.md` `## Commands` table to reflect `Verify drift -> propose Upgrade Plan -> wait for approval -> apply core refresh -> run Doctor`.
- [x] **Step 3:** Replace `## Framework Update Protocol` (`AGENTS.md`) with the 5-phase flow (Smart Fetch Read-Only, Drift & Version Verification with short-circuit if current, Propose Upgrade Plan & Wait for Approval, Apply Approved Upgrade + Root Discovery & Obsolete Prompt Cleanup + Strict Shields, Post-Upgrade Doctor using newly installed `AGENTS.md`).

### Task 2: Rewrite `guides/prompts/update.md` & Align Skill/Rule/Guides

**Files:**
- Modify: `guides/prompts/update.md`
- Modify: `.agents/skills/genos-update/SKILL.md`
- Modify: `.cursor/rules/genos-update.mdc`
- Modify: `README.md`
- Modify: `guides/guide.md`

- [x] **Step 1:** Rewrite `guides/prompts/update.md` as a self-contained 5-phase prompt explicitly listing canonical files vs obsolete v1/v2 prompts to prune (`setup-04-framework-upgrade.md`, `setup-tooling.md`, `setup-workforce.md`, `setup-obsidian-migration.md`, `workflow-01-kickoff.md`, `workflow-02-shutdown.md`, `workflow-03-resume-session.md`, `workflow-doctor.md`, `workflow-autonomous-batch.md`), repo-root `CLAUDE.md`/`.agents/`/`.cursor/` verification, strict shielding, and reading the newly fetched `AGENTS.md` before Doctor.
- [x] **Step 2:** Update `.agents/skills/genos-update/SKILL.md` and `.cursor/rules/genos-update.mdc`.
- [x] **Step 3:** Update `update` summary lines in `README.md` and `guides/guide.md`.

### Task 3: Update Brain (`DEC-008`, `Updater.md`, `50_ROADMAP.md`, `20_PROGRESS.yaml`) & Verify

**Files:**
- Modify: `brain/30_DECISIONS.md`
- Modify: `brain/50_ROADMAP.md`
- Modify: `brain/systems/Updater.md`
- Modify: `brain/20_PROGRESS.yaml`

- [x] **Step 1:** Record `DEC-008: Verify-First & Plan-Gated Framework Updater` in `brain/30_DECISIONS.md` (Index + entry).
- [x] **Step 2:** Update `brain/50_ROADMAP.md` (`M2` deliverables) and `brain/systems/Updater.md` (`[[DEC-008]]`, 5-phase invariants).
- [x] **Step 3:** Update `brain/20_PROGRESS.yaml` `session_summary`.
- [x] **Step 4:** Verify with `verify_configs.py`, `run_doctor_audit.py` (`8/8` pass), and `python -m unittest discover -s guides/scripts -p "test_*.py" -v`.
- [x] **Step 5:** Commit to `main`, push `origin main`, and fast-forward sync `genos-v3`.

---

## Execution Handoff

**Option 1: Subagent-Driven (Recommended):**
```
kickoff execute the approved plan: docs/superpowers/plans/2026-11-10-verify-plan-update.md using subagent-driven-development
```

**Option 2: Inline Execution:**
```
kickoff execute the approved plan: docs/superpowers/plans/2026-11-10-verify-plan-update.md
```
