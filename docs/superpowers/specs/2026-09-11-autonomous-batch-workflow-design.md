# Autonomous Batch Workflow Design

**Date:** 2026-09-11  
**Status:** Approved by User  
**Target Delivery:** `guides/prompts/workflow-autonomous-batch.md` in genOS  

---

## 1. Problem Statement & Motivation

Developers utilizing advanced AI models (such as Fable 5 or Claude 3.5 Sonnet) in agent-driven IDEs (like Cursor Composer or Antigravity) frequently want to execute multiple roadmap milestones or backlog tasks autonomously in a single session without constant human interruption.

However, standard AI workflows have two major vulnerabilities when automated:
1. **The Politeness Trap:** The AI stops and asks for human permission after every minor file change or task, breaking hands-free automation.
2. **The Hallucination & Code Drift Trap:** Unattended agents generate code without verification, introduce subtle syntax errors, violate system invariants, or fail to persist memory into the Project Brain, resulting in corrupted project state.

---

## 2. Design Goals

- **Zero-Interruption Execution:** The agent moves continuously from task to task across a batch without asking "Should I proceed?".
- **Dual-Persona Quality Gate (Builder + QA Auditor):** Every code change is verified by an adversarial QA persona before state is persisted.
- **Workforce Pre-flight Safety Gate:** Automation strictly requires a designated QA/Auditor agent in `brain/60_AGENTS.md`. If missing, the runner halts and directs the user to install the appropriate specialist from Agency Agents.
- **Atomic Brain Persistence:** State is persisted to `brain/systems/`, `50_ROADMAP.md`, and `20_PROGRESS.yaml` after *every* single completed task, ensuring zero data loss if an IDE context window terminates.
- **Automated Sanity Gate:** Mandatory validation of YAML syntax, index tables, and backlog isolation after each cycle.
- **Self-Healing Budget:** A 2-retry error correction loop for compilation/build errors before escalating to human help.

---

## 3. Architecture & Operational Protocol

### Phase 0: Pre-flight Workforce Gate
1. Scan `brain/60_AGENTS.md`:
   - Verify that an active **Builder** role (e.g., `unity-architect`, `frontend-developer`, `backend-architect`) is registered.
   - Verify that an active **QA/Auditor** role (e.g., `game-tester`, `code-reviewer`, `test-automator`, `qa-engineer`) is registered.
2. **Hard Halt if QA is Missing:**
   - If no QA/Auditor role is found, halt immediately.
   - Inspect the active profile in `profiles/` (e.g., `profiles/gamedev/` or `profiles/web-fullstack/`).
   - Provide the user with the exact recommended agent from `msitarzewski/agency-agents` and installation instructions.
   - Resume only when the user confirms the QA agent is recorded in `brain/60_AGENTS.md`.

### Phase 1: Target Scope & Batch Selection
The user sets their batch preference at the top of the prompt:
- **Explicit Batch:** `TARGET: [TASK_ID_1, TASK_ID_2, ...]` (e.g., `[M2.2, M2.3]` or `[BACKLOG-002, BACKLOG-014]`).
- **Active Milestone:** `TARGET: ACTIVE_MILESTONE` (resolves active milestone from `50_ROADMAP.md`).
- **Smart Backlog Recommendation (`TARGET: AUTO_RECOMMENDED`):**
  - Scans `40_BACKLOG.md` and `50_ROADMAP.md`.
  - Analyzes current project phase, dependencies, and active systems.
  - Automatically selects a cohesive, safe batch of 2–4 related tasks.
  - Locks in the batch order.

### Phase 2: Dual-Persona Execution Loop (Per Task)
For each item in the batch, the agent executes:

```
[Task Triage]
      │
      ▼
[Builder Persona] ──► Reads system invariants ──► Implements code & assets ──► Local build check
      │
      ▼
[QA Auditor Persona] ──► Edge-case & null audit ──► Automated tests ──► System invariants check
      │
      ├── (Passes) ──► [Atomic Brain Persistence]
      │
      └── (Fails)  ──► Self-healing retry (Max 2 attempts)
                         ├── (Fixed) ──► [Atomic Brain Persistence]
                         └── (Unresolved) ──► Log to PROGRESS.blocked & HALT for human
```

### Phase 3: Atomic Brain Persistence & Sanity Gate
Upon QA sign-off for an item:
1. Update affected `brain/systems/<System>.md` documents with new invariants or component paths.
2. Mark item as `done` in `50_ROADMAP.md` (for milestones) or move from `Todo` to `Done` in `40_BACKLOG.md` (for backlog tasks).
3. Update `brain/20_PROGRESS.yaml`:
   - Record completed work in `session_summary`.
   - Update `current_milestone` pointer if milestone advanced.
   - Clear completed item from `working_on`.
4. Run Sanity Gate:
   - Validate YAML syntax.
   - Validate index tables in `50_ROADMAP.md` and `30_DECISIONS.md`.
   - Verify no state leakage into `40_BACKLOG.md`.

### Phase 4: Auto-Looping & Halting Valves
- **Check Remaining Items:**
  - If tasks remain in the active batch: **Do NOT pause for chat input.** Immediately advance to the next item, select the required Agency Agent, and begin Phase 2.
  - If all tasks in the batch are finished: Perform final SHUTDOWN, run the Brain Doctor check, output the Batch Completion Summary, and conclude.
- **Halting Valves (Pause for Human):**
  1. Build or test failure persists after the 2-retry self-healing budget.
  2. Implementation requires a permanent architectural shift altering intent (requires a new `DEC-XXX`).

---

## 4. Deliverables & Affected Files

1. **New Prompt Template:** `guides/prompts/workflow-autonomous-batch.md`
   - Complete autonomous batch runner prompt with pre-flight gates, dual-persona loop, auto-advancing logic, and self-healing budget.
2. **User Guide Update:** `guides/guide.md`
   - Documenting the autonomous batch workflow and when to use it.
3. **README Update:** `README.md`
   - Adding `workflow-autonomous-batch.md` to the Prompt Reference table.
