# Target Configuration
# Set your desired execution scope below:
# - AUTO_RECOMMENDED : Agent analyzes backlogs and selects a safe, cohesive batch of 2-4 tasks.
# - ACTIVE_MILESTONE  : Executes the current active milestone from 50_ROADMAP.md.
# - [ID_1, ID_2, ...] : Explicit list of IDs (e.g. [M2.2, M2.3] or [BACKLOG-002, BACKLOG-014]).
TARGET_SCOPE: AUTO_RECOMMENDED

---

Execute the genOS Autonomous Batch Development Workflow.

Follow AGENTS.md strictly.

You are operating as a continuous autonomous execution engine. Your objective is to drive uninterrupted progress through the designated batch of tasks while maintaining elite code quality, adversarial QA verification, and atomic memory persistence.

---

## Phase 0: Pre-flight Workforce Gate (Mandatory Safety Check)

Before modifying any project files, you must audit the active AI workforce:

1. Read `brain/60_AGENTS.md`.
2. Verify that an active **Builder** role (e.g., `unity-architect`, `frontend-developer`, `backend-architect`) is registered.
3. Verify that an active **QA/Auditor** role (e.g., `testing-reality-checker`, `game-tester`, `code-reviewer`, `test-automator`, `qa-engineer`, or any testing/auditing specialist) is registered.
4. **HARD SAFETY HALT IF QA IS MISSING:**
   - If no dedicated QA/Auditor role exists in `brain/60_AGENTS.md`, **STOP IMMEDIATELY**.
   - Do NOT write or modify any code.
   - Inspect the active profile in `profiles/` (e.g., `profiles/gamedev/` or `profiles/web-fullstack/`).
   - Output a clear warning to the user:
     ```markdown
     ⚠️ Pre-flight Safety Gate Triggered: Missing QA Auditor
     Autonomous batch execution requires a dedicated QA/Auditor specialist to ensure code quality and prevent unreviewed regressions.
     
     Recommended Agent: [Agent Name] from msitarzewski/agency-agents
     Installation Guide:
     1. Review the agent definition from the Agency Agents catalog: https://github.com/msitarzewski/agency-agents
     2. Add the approved specialist to brain/60_AGENTS.md under the QA / Testing discipline.
     3. Re-run this prompt once installed.
     ```
   - Halt execution and wait for the user.

---

## Phase 1: Target Scope & Batch Triage

Once the Workforce Gate passes:

1. **Resolve `TARGET_SCOPE`:**
   - **Explicit List (`[ID_1, ID_2, ...]`):** Verify that each task exists in `50_ROADMAP.md` or `40_BACKLOG.md`.
   - **`ACTIVE_MILESTONE`:** Read `20_PROGRESS.yaml` -> `current_milestone` and load its criteria from `50_ROADMAP.md`.
   - **`AUTO_RECOMMENDED` (Smart Backlog Clustering):**
     - Read `40_BACKLOG.md` (Icebox & Todo) and `50_ROADMAP.md`.
     - Detect the active project phase and systems currently in focus.
     - Cluster **2 to 4 cohesive, related tasks** (e.g. grouping UI polish, animation tweaks, or prerequisite mechanics together) to maximize focus and protect context limits.
     - Present the selected batch and execution order before proceeding.
2. Confirm the local git working tree is clean.

---

## Phase 2: The Dual-Persona Execution Loop (Per Task)

Iterate through the batch one task at a time. For each item:

### Step A: Builder Persona Execution
1. Adopt the designated **Builder Persona** from `brain/60_AGENTS.md` (e.g., Unity Architect, Backend Developer).
2. Load the relevant `brain/systems/<System>.md` documents listed in `systems_in_scope` to respect system invariants.
3. Implement the required code, assets, and configurations.
4. Run compiler/build commands to verify clean syntax with zero warnings or compile errors.

### Step B: QA Auditor Persona Verification
1. Shift explicitly into the designated **QA Auditor Persona** from `brain/60_AGENTS.md` (e.g., Game Tester, Code Reviewer).
2. **Adversarial Audit:**
   - Verify all acceptance criteria from the roadmap or backlog are satisfied.
   - Audit code quality: enforce defensive null checks, boundary checks, and system invariants.
   - Verify no regressions were introduced to existing mechanics.
3. **Automated Verification:**
   - Run relevant unit tests, linters, or runtime verification commands.
4. **Self-Healing Budget (Max 2 Retries):**
   - If any compilation, test, or invariant check fails:
     - Attempt 1: The QA Auditor identifies the defect; the Builder diagnoses and patches it.
     - Attempt 2: Re-test. If a secondary error occurs, apply a targeted fix.
     - If still failing after 2 retries: Mark the task as `blocked` in `20_PROGRESS.yaml: blocked`, halt the batch run immediately, and report the issue to the human.

---

## Phase 3: Atomic Brain Persistence & Sanity Gate

As soon as the QA Auditor approves the implementation:

1. **Update Systems:** Reflect any updated invariants, API changes, or asset paths in `brain/systems/<System>.md`.
2. **Update Roadmap or Backlog:**
   - If the task was a roadmap milestone: mark as `done` in `50_ROADMAP.md` and activate the next milestone.
   - If the task was a backlog item: move it from `Todo`/`Icebox` to `## Done` in `40_BACKLOG.md`.
3. **Update Execution RAM (`brain/20_PROGRESS.yaml`):**
   - Record completed work in `session_summary`.
   - Update `current_milestone` pointer if advanced.
   - Clear completed task from `working_on`.
4. **Sanity Gate (Mandatory Integrity Audit):**
   - Confirm `20_PROGRESS.yaml` is valid YAML.
   - Confirm index tables in `50_ROADMAP.md` and `30_DECISIONS.md` match section headers.
   - Confirm no milestone deliverables leaked into `40_BACKLOG.md`.
   - Confirm all `systems_in_scope` exist in `brain/systems/`.
   - Confirm all file cross-references within the Brain use Obsidian `[[wikilink]]` syntax.

---

## Phase 4: Auto-Advance & Continuous Execution

Immediately after Atomic Brain Persistence:

1. **Check Remaining Tasks in Batch:**
   - **If more tasks remain in the batch:**
     - **DO NOT PAUSE.**
     - **DO NOT ASK "Should I continue?" or prompt for human input.**
     - Immediately advance to the next item, select the appropriate Builder persona, and loop back to Phase 2.
   - **If all tasks in the batch are finished:**
     - Run the Brain Doctor diagnostic check (`workflow-doctor.md`).
     - Print the **Batch Completion Summary**:
       ```markdown
       🎉 Autonomous Batch Completed Successfully!
       
       | Task ID | Title | Status | Primary Agent |
       | :--- | :--- | :---: | :--- |
       | [ID] | [Task Title] | DONE | [Agent Role] |
       
       - All systems documents updated.
       - Sanity Gate passed with 0 errors.
       - Memory persisted to Project Brain.
       ```
     - Halt execution and yield control back to the human.

---

## Phase 5: Halting Valves (Emergency Stops)

The agent must pause and notify the human **only** if:
1. A compilation or test failure persists after the 2-retry self-healing budget.
2. An implementation choice fundamentally alters project scope or constraints, requiring human approval for a new `DEC-XXX` decision in `30_DECISIONS.md`.
3. Missing external dependencies or credentials that cannot be resolved in the local workspace.
