# Autonomous Batch Workflow Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create the `workflow-autonomous-batch.md` prompt in genOS for uninterrupted, multi-task batch execution in AI agents (Cursor Composer/Agent, Fable 5, Antigravity) with dual-persona QA validation, workforce pre-flight gates, and atomic brain persistence.

**Architecture:** A deterministic prompt engine that functions as an uninterrupted state machine: Pre-flight Workforce Audit Gate -> Target Scope Resolution (Explicit / Active Milestone / Auto-Recommended clustering) -> Dual-Persona Loop (Specialist Builder + QA Auditor with 2-retry self-healing) -> Atomic Brain Persistence & Sanity Gate -> Auto-Advance Loop -> Final Batch Completion Summary.

**Tech Stack:** Markdown prompt engineering, genOS Kernel v2 (`AGENTS.md`), Python verification scripting.

## Global Constraints

- Never alter or bypass the core ownership rules in `AGENTS.md`.
- `brain/` files must remain strictly protected; updates during the batch loop must be atomic per completed task.
- Workforce Gate is a hard gate: if no QA/Auditor agent is recorded in `brain/60_AGENTS.md`, the runner must halt and provide installation instructions from `msitarzewski/agency-agents`.
- In `AUTO_RECOMMENDED` mode, batch clustering must be capped between 2 to 4 cohesive tasks to protect the AI context window.
- Error self-healing budget is strictly capped at 2 retries before escalating to human help.

---

### Task 1: Create `guides/prompts/workflow-autonomous-batch.md`

**Files:**
- Create: `d:/GameOS/guides/prompts/workflow-autonomous-batch.md`
- Test: `scratch/verify_autonomous_batch_prompt.py`

**Interfaces:**
- Consumes: `brain/60_AGENTS.md`, `brain/50_ROADMAP.md`, `brain/40_BACKLOG.md`, `brain/20_PROGRESS.yaml`, `brain/systems/*.md`, `profiles/<profile>/profile.yaml`.
- Produces: The executable prompt template for hands-free autonomous development.

- [ ] **Step 1: Write test script to verify prompt structure and required sections**

```python
# scratch/verify_autonomous_batch_prompt.py
import os
import re

prompt_path = "guides/prompts/workflow-autonomous-batch.md"
assert os.path.exists(prompt_path), f"Missing {prompt_path}"

with open(prompt_path, "r", encoding="utf-8") as f:
    content = f.read()

required_sections = [
    "Pre-flight Workforce Gate",
    "TARGET_SCOPE",
    "Builder Persona",
    "QA Auditor Persona",
    "Self-Healing Budget",
    "Atomic Brain Persistence",
    "Sanity Gate",
    "Auto-Advance",
    "Halting Valves",
]

for section in required_sections:
    assert section in content, f"Missing required section: {section}"

print("Prompt verification PASSED.")
```

- [ ] **Step 2: Run test to verify it fails before file creation**

Run: `python scratch/verify_autonomous_batch_prompt.py`  
Expected: FAIL with `Missing guides/prompts/workflow-autonomous-batch.md`

- [ ] **Step 3: Implement `guides/prompts/workflow-autonomous-batch.md`**

Author the complete autonomous batch runner prompt with:
- Configuration header (`TARGET_SCOPE: AUTO_RECOMMENDED | ACTIVE_MILESTONE | [IDs]`).
- Pre-flight Workforce Gate (scans `brain/60_AGENTS.md` for Builder and QA/Auditor, halts and gives install instructions if missing).
- Triage & Auto-cluster logic for large backlogs.
- Dual-persona loop (Builder executes, QA audits code quality, null-safety, and tests).
- 2-retry self-healing budget.
- Atomic persistence to `brain/systems/`, `50_ROADMAP.md` / `40_BACKLOG.md`, and `20_PROGRESS.yaml`.
- Sanity Gate verification after each task.
- Non-stop loop condition (proceed immediately without asking "Should I continue?").
- Halting valves for persistent errors or intent-altering architectural choices.

- [ ] **Step 4: Run test to verify prompt passes verification**

Run: `python scratch/verify_autonomous_batch_prompt.py`  
Expected: `Prompt verification PASSED.`

- [ ] **Step 5: Commit prompt to Git**

Run:
```powershell
git add guides/prompts/workflow-autonomous-batch.md
git commit -m "feat(prompts): add autonomous batch workflow runner with dual-persona QA gates"
```

---

### Task 2: Update Documentation (`guides/guide.md` and `README.md`)

**Files:**
- Modify: `d:/GameOS/guides/guide.md`
- Modify: `d:/GameOS/README.md`

**Interfaces:**
- Consumes: `workflow-autonomous-batch.md`
- Produces: Updated user guide and reference tables.

- [ ] **Step 1: Update `guides/guide.md`**

Add a dedicated section under "## The Daily Workflow" explaining the Autonomous Batch Workflow, when to use it, the Pre-flight QA Gate, and how to trigger it with Fable 5 / Cursor Agent.

- [ ] **Step 2: Update `README.md`**

Add `workflow-autonomous-batch.md` to the **Daily Prompt Reference** table with direct file links and descriptions.

- [ ] **Step 3: Verify markdown formatting and table rendering**

Verify that both files render cleanly with zero broken table syntax.

- [ ] **Step 4: Commit documentation updates**

Run:
```powershell
git add guides/guide.md README.md
git commit -m "docs: document autonomous batch workflow in guide and README"
```

---

### Task 3: Mirror and Verify with `D:\Baybayin-Capstone\genOS`

**Files:**
- Copy: `guides/prompts/workflow-autonomous-batch.md` -> `D:/Baybayin-Capstone/genOS/guides/prompts/`
- Copy: `guides/guide.md` -> `D:/Baybayin-Capstone/genOS/guides/`
- Copy: `README.md` -> `D:/Baybayin-Capstone/genOS/`

**Interfaces:**
- Consumes: Updated genOS framework files
- Produces: Synchronized test project ready for autonomous Fable 5 execution.

- [ ] **Step 1: Copy updated files to `D:\Baybayin-Capstone\genOS`**
- [ ] **Step 2: Run verification audit on Baybayin project to ensure 100% integrity**
- [ ] **Step 3: Push changes to `feat/genos` on remote repository**
