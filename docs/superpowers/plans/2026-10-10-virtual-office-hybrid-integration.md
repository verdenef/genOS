# genOS Virtual Office (Hybrid Integration) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement the genOS Virtual Office Hybrid Integration, enabling projects to deploy a persistent, semi-autonomous development team powered by Grok Bot cloud workers synchronized with the genOS Project Brain via git branches and PR reviews.

**Architecture:** A lightweight integration layer consisting of:
1. Architecture documentation in `integrations/virtual-office/README.md`.
2. An interactive setup wizard prompt in `integrations/virtual-office/setup-virtual-office.md` that reads `brain/60_AGENTS.md` and generates copy-paste ready Grok Bot system prompts with BOOT/SHUTDOWN protocols and git branch workflows.
3. A daily coordination prompt in `guides/prompts/workflow-virtual-office.md` used by the Lead Bot to read the roadmap, propose daily work assignments for human approval, and dispatch tasks to Builder/QA bots.
4. Framework documentation updates across `README.md` and `guides/guide.md`.
5. Automated validation via Python verification scripts.

**Tech Stack:** Markdown prompt engineering, genOS Kernel v2 (`AGENTS.md`), GitHub Branch/PR workflows, Python 3 verification scripts.

## Global Constraints

- genOS `brain/` remains the single source of truth; bots must never store durable project memory solely in Grok cloud state.
- Strictly adhere to genOS BOOT and SHUTDOWN lifecycle protocols.
- Git branch isolation: Builder and QA bots must work on dedicated branches (`bot/<agent-name>`), never committing directly to `main`.
- Human approval gate: All work requires human review and merge via GitHub PRs.
- 2-retry self-healing budget for inter-bot reviews before escalating to human operator.
- No placeholders, `TODO`, or `TBD` anywhere in deliverables.

---

### Task 1: Create Integration Overview (`integrations/virtual-office/README.md`)

**Files:**
- Create: `d:/GameOS/integrations/virtual-office/README.md`
- Test: `scratch/verify_task1_virtual_office_readme.py`

**Interfaces:**
- Consumes: [`2026-10-10-virtual-office-hybrid-design.md`](file:///d:/GameOS/docs/superpowers/specs/2026-10-10-virtual-office-hybrid-design.md)
- Produces: Definitive user and agent guide for the Virtual Office integration.

- [ ] **Step 1: Write test script to verify README structure and required sections**

Create `scratch/verify_task1_virtual_office_readme.py`:
```python
import os
from pathlib import Path

target_file = Path("d:/GameOS/integrations/virtual-office/README.md")
assert target_file.exists(), f"File {target_file} does not exist"

content = target_file.read_text(encoding="utf-8")
required_sections = [
    "# genOS Virtual Office Integration",
    "## 1. Overview",
    "## 2. Prerequisites",
    "## 3. Architecture & Data Flow",
    "## 4. Bot Roles & Responsibilities",
    "## 5. Branch & PR Conventions",
    "## 6. Daily Operational Cycle",
    "## 7. Troubleshooting & Escalation"
]

for section in required_sections:
    assert section in content, f"Missing section: {section}"

assert "[[60_AGENTS.md]]" in content or "60_AGENTS.md" in content
assert "bot/<agent-name>" in content
assert len(content.splitlines()) >= 80

print("Task 1 verification PASSED!")
```

- [ ] **Step 2: Run test to verify it fails before creation**

Run: `python scratch/verify_task1_virtual_office_readme.py`
Expected: FAIL with "File d:/GameOS/integrations/virtual-office/README.md does not exist"

- [ ] **Step 3: Write `integrations/virtual-office/README.md`**

Create `d:/GameOS/integrations/virtual-office/README.md`:
```markdown
# genOS Virtual Office Integration

The genOS Virtual Office turns Grok Bot's cloud agent platform into a persistent, semi-autonomous development team for any genOS project. Each Agency Agent defined in `brain/60_AGENTS.md` maps to a dedicated Grok Bot, coordinated by a designated **Lead Bot**.

All durable project state flows strictly through the genOS Project Brain (`brain/`) via git branches and PR reviews, preserving the single-source-of-truth guarantee with zero memory drift.

---

## 1. Overview

- **genOS is the Brain:** Grok Bots are compute workers, not memory holders. Durable decisions, system invariants, and progress pointers live only in your repository's `brain/` directory.
- **Semi-Autonomous Execution:** The Lead Bot proposes daily work assignments based on `50_ROADMAP.md`. You approve the plan in the Grok app, and the bots execute autonomously.
- **Git Branch Isolation:** Every bot works in its own branch (`bot/<agent-name>`), pushes commits to GitHub, and submits pull requests for your review.
- **Obsidian Graph Sync:** When PRs are merged to `main`, pulling locally automatically updates your Obsidian Graph View.

---

## 2. Prerequisites

1. **Grok Bot App:** Installed on your phone, tablet, or desktop with an active subscription.
2. **GitHub Repository:** Your genOS project repository pushed to GitHub.
3. **Active Workforce:** Specialist agents defined in `brain/60_AGENTS.md` (or configured via `setup-workforce.md`).
4. **GitHub Access for Grok Bots:** Grant Grok Bot repository access (read/write) so bots can clone, create branches, and push commits.

---

## 3. Architecture & Data Flow

```
┌────────────────────────────────────────┐
│        Grok Bot Remote App             │
│  (Human reviews & approves proposals)  │
│                                        │
│   ┌────────┐                           │
│   │  Lead  │ ← Coordinator Bot         │
│   │  Bot   │                           │
│   └───┬────┘                           │
│       │ dispatches tasks via chat      │
│   ┌───┴────┐       ┌───────┐           │
│   │Builder │       │  QA   │           │
│   │  Bot   │       │  Bot  │           │
│   └───┬────┘       └───┬───┘           │
└───────┼────────────────┼───────────────┘
        │ git push       │ git review
        ▼────────────────▼
┌────────────────────────────────────────┐
│           GitHub Repository            │
│  - main branch: genOS brain/ & code    │
│  - bot/builder branch (PR open)        │
│  - bot/qa branch (PR comments / fixes) │
└────────────────────────────────────────┘
        ▲
        │ git pull
        ▼
┌────────────────────────────────────────┐
│          Your Local Machine            │
│  - Cursor / Antigravity / Obsidian     │
└────────────────────────────────────────┘
```

---

## 4. Bot Roles & Responsibilities

### Lead Bot (Coordinator)
- **Authority:** Reads `brain/50_ROADMAP.md` and `brain/40_BACKLOG.md` on `main`.
- **Responsibilities:** Formulates daily task assignments, presents proposals to human, dispatches tasks to Builder/QA bots, monitors progress, and prepares daily handoff summaries.
- **Restrictions:** Never writes application code, modifies system files, or changes architectural decisions.

### Builder Bots (Mapped from `60_AGENTS.md`)
- **Authority:** Full read/write access to source code and relevant `brain/systems/*.md` files on their branch.
- **Branch:** `bot/<agent-name>` (e.g. `bot/unity-architect`, `bot/backend-engineer`).
- **Protocol:** Must execute the genOS BOOT sequence, implement assigned deliverables, run local tests, perform SHUTDOWN with Sanity Gate checks, and open a PR.

### QA Bot (Mapped from `60_AGENTS.md`)
- **Authority:** Read-only access to main, checkout access to Builder branches.
- **Branch:** `bot/<qa-agent-name>`.
- **Protocol:** Performs adversarial verification per `workflow-autonomous-batch.md` standards. Runs tests, inspects code quality, posts reviews on GitHub PRs, and tags Builder bots if fixes are needed (2-retry budget).

---

## 5. Branch & PR Conventions

- **Branch Naming:** `bot/<agent-name>` (e.g., `bot/lead`, `bot/frontend-dev`, `bot/qa-tester`).
- **Commit Messages:** Follow conventional commits (e.g., `feat(combat): implement hitbox collision handling`, `docs(brain): update combat system status`).
- **Pull Requests:** Titled `[Bot Work] <Task Description>`. Must include a summary of code changes, test results, and brain updates.
- **Merges:** Always squash or merge via GitHub web/mobile UI after reviewing changes.

---

## 6. Daily Operational Cycle

1. **Morning Briefing:** You prompt the Lead Bot in the project thread (`guides/prompts/workflow-virtual-office.md`). The Lead Bot inspects the roadmap and posts proposed assignments.
2. **Approval:** You reply "Approved" (or tweak the tasks).
3. **Execution:** Lead Bot tags Builder bots with clear deliverables. Builders execute in parallel on separate branches.
4. **Peer Review:** QA Bot tests each builder branch and posts approval or feedback (2-retry limit).
5. **Human Review & Merge:** You review the PRs on GitHub, merge approved branches into `main`, and your local Obsidian Graph reflects all progress.

---

## 7. Troubleshooting & Escalation

- **Merge Conflicts:** If two bots touch the same `brain/` file, the human resolves conflicts during PR merge.
- **Blocked Bots:** If a bot hits an error after 2 retries, the Lead Bot escalates to the human in the Grok thread with full error output and options.
- **Brain Integrity:** If brain files desync, paste `guides/prompts/workflow-doctor.md` into your IDE to auto-heal.
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python scratch/verify_task1_virtual_office_readme.py`
Expected: PASS with "Task 1 verification PASSED!"

- [ ] **Step 5: Commit**

```bash
git add integrations/virtual-office/README.md scratch/verify_task1_virtual_office_readme.py
git commit -m "docs(virtual-office): add overview and architecture README"
```

---

### Task 2: Create Setup Prompt Generator (`integrations/virtual-office/setup-virtual-office.md`)

**Files:**
- Create: `d:/GameOS/integrations/virtual-office/setup-virtual-office.md`
- Test: `scratch/verify_task2_setup_virtual_office.py`

**Interfaces:**
- Consumes: `brain/60_AGENTS.md`, `AGENTS.md`, `brain/00_PROJECT.md`
- Produces: An interactive IDE setup prompt that generates tailor-made Grok Bot system prompts for each agent in the workforce.

- [ ] **Step 1: Write test script to verify setup prompt structure**

Create `scratch/verify_task2_setup_virtual_office.py`:
```python
import os
from pathlib import Path

target_file = Path("d:/GameOS/integrations/virtual-office/setup-virtual-office.md")
assert target_file.exists(), f"File {target_file} does not exist"

content = target_file.read_text(encoding="utf-8")
required_elements = [
    "Virtual Office Setup Wizard",
    "brain/60_AGENTS.md",
    "Lead Bot",
    "Builder Bots",
    "QA Bot",
    "System Prompt Template",
    "BOOT sequence",
    "SHUTDOWN sequence",
    "Sanity Gate",
    "bot/<agent-name>"
]

for el in required_elements:
    assert el in content, f"Missing required element: {el}"

assert len(content.splitlines()) >= 90
print("Task 2 verification PASSED!")
```

- [ ] **Step 2: Run test to verify it fails before creation**

Run: `python scratch/verify_task2_setup_virtual_office.py`
Expected: FAIL with "File d:/GameOS/integrations/virtual-office/setup-virtual-office.md does not exist"

- [ ] **Step 3: Write `integrations/virtual-office/setup-virtual-office.md`**

Create `d:/GameOS/integrations/virtual-office/setup-virtual-office.md`:
```markdown
I want to set up a Grok Bot Virtual Office for this genOS project.

Follow AGENTS.md strictly.

You are the Virtual Office Setup Wizard. Your job is to audit our project's approved AI workforce in `brain/60_AGENTS.md`, extract all specialist personas, and generate ready-to-paste system prompts and setup instructions for our Grok Bots.

---

## Step 1: Audit Project Workforce & Constraints

1. Read `brain/00_PROJECT.md` to extract the project name, vision, and core stack.
2. Read `brain/60_AGENTS.md` to identify:
   - The active specialist agents (Builder personas).
   - The designated QA/Auditor agent.
3. If `brain/60_AGENTS.md` is empty or unset, stop and advise running `guides/prompts/setup-workforce.md` first.

---

## Step 2: Generate Grok Bot System Prompts

For each bot, generate a concise, production-ready system prompt tailored for Grok Bot's cloud computing environment. Format each prompt in a clean code block so it can be copied directly into the Grok app.

### A. Lead Bot System Prompt (`[Project] Lead Bot`)
Generate a prompt containing:
- **Role:** Project Coordinator & Lead Architect.
- **Authority:** Reads `main` branch: `brain/50_ROADMAP.md` and `brain/40_BACKLOG.md`.
- **Responsibilities:**
  - Propose daily work assignments based on the active milestone.
  - Await explicit human approval before dispatching tasks.
  - Tag Builder and QA bots in the shared thread with specific task criteria.
  - Track branch and PR statuses; escalate unresolvable blockers after 2 retries.
  - Never write production code or commit directly to git.

### B. Builder Bot System Prompts (One per agent in `60_AGENTS.md`)
For each builder agent, generate a prompt containing:
- **Persona & Discipline:** Extracted verbatim from `60_AGENTS.md`.
- **Branch Rule:** Always create and work in `bot/<agent-name>`.
- **genOS Lifecycle:**
  1. **BOOT:** Pull latest `main`. Read `AGENTS.md`, `00_PROJECT.md`, `20_PROGRESS.yaml`, and the assigned task criteria from `50_ROADMAP.md`.
  2. **WORK:** Implement deliverables, write unit/integration tests, run verification commands.
  3. **SHUTDOWN:** Update relevant `brain/systems/*.md` status/design notes, update `20_PROGRESS.yaml` session summary, run the Sanity Gate check, commit, and push.
  4. **HANDOFF:** Post completion note in the thread and tag QA Bot.

### C. QA Bot System Prompt (`[Project] QA Auditor`)
Generate a prompt containing:
- **Persona:** Adversarial Auditor extracted from `60_AGENTS.md`.
- **Workflow:** Checkout builder branches, run test suites, inspect code against acceptance criteria, and post review verdicts.
- **Budget Rule:** Provide concrete fix feedback. If a builder cannot resolve issues within 2 retries, tag Lead Bot for human escalation.

---

## Step 3: Output Setup Checklist for the Human

Provide step-by-step instructions for completing setup in the Grok app:
1. Creating each bot with the recommended naming format (`[Project] <Role>`).
2. Pasting the generated system prompt into each bot.
3. Creating a single shared Grok thread (e.g. `[Project] Virtual Office`) and inviting all bots.
4. Authorizing GitHub repository access for each bot.
5. Providing the daily kick-off command: "Paste `guides/prompts/workflow-virtual-office.md` to begin daily operations."
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python scratch/verify_task2_setup_virtual_office.py`
Expected: PASS with "Task 2 verification PASSED!"

- [ ] **Step 5: Commit**

```bash
git add integrations/virtual-office/setup-virtual-office.md scratch/verify_task2_setup_virtual_office.py
git commit -m "feat(virtual-office): add setup prompt generator"
```

---

### Task 3: Create Daily Lead Bot Prompt (`guides/prompts/workflow-virtual-office.md`)

**Files:**
- Create: `d:/GameOS/guides/prompts/workflow-virtual-office.md`
- Test: `scratch/verify_task3_workflow_virtual_office.py`

**Interfaces:**
- Consumes: `brain/50_ROADMAP.md`, `brain/40_BACKLOG.md`, `brain/20_PROGRESS.yaml`
- Produces: The daily command prompt executed inside the Grok Bot Virtual Office thread.

- [ ] **Step 1: Write test script to verify daily workflow prompt structure**

Create `scratch/verify_task3_workflow_virtual_office.py`:
```python
import os
from pathlib import Path

target_file = Path("d:/GameOS/guides/prompts/workflow-virtual-office.md")
assert target_file.exists(), f"File {target_file} does not exist"

content = target_file.read_text(encoding="utf-8")
required_sections = [
    "Phase 1: Morning Briefing & Roadmap Audit",
    "Phase 2: Task Dispatch & Branch Isolation",
    "Phase 3: QA Verification & Peer Review Loop",
    "Phase 4: Pull Request Preparation & Daily Summary",
    "Escalation Valve",
    "Sanity Gate"
]

for section in required_sections:
    assert section in content, f"Missing section: {section}"

assert "50_ROADMAP.md" in content
assert "bot/<agent-name>" in content
assert "2-retry" in content or "two retries" in content.lower()
print("Task 3 verification PASSED!")
```

- [ ] **Step 2: Run test to verify it fails before creation**

Run: `python scratch/verify_task3_workflow_virtual_office.py`
Expected: FAIL with "File d:/GameOS/guides/prompts/workflow-virtual-office.md does not exist"

- [ ] **Step 3: Write `guides/prompts/workflow-virtual-office.md`**

Create `d:/GameOS/guides/prompts/workflow-virtual-office.md`:
```markdown
Good morning Lead Bot. We are initiating the daily Virtual Office cycle.

Follow AGENTS.md strictly.

Operate as the Virtual Office Coordinator across the following 4 phases:

---

## Phase 1: Morning Briefing & Roadmap Audit

1. **Pull Latest Main:** Ensure your repository view on `main` is up to date.
2. **Inspect the Brain:**
   - Read `brain/20_PROGRESS.yaml` to identify the `current_milestone` pointer and any active blockers.
   - Read `brain/50_ROADMAP.md` to load the active milestone's objectives, deliverables, and completion criteria.
   - Read `brain/40_BACKLOG.md` for prioritized non-milestone items.
3. **Formulate the Daily Agenda:**
   - Select 1 to 3 deliverable tasks appropriate for today's work.
   - Map each task to the specific specialist Builder Bot from `brain/60_AGENTS.md`.
4. **Present the Plan to the Human:**
   Post your proposal in this thread using this exact format:
   ```markdown
   📋 Daily Agenda — [Project Name]
   Active Milestone: [Milestone ID] — [Milestone Title]

   Proposed Task Assignments:
   • @[Builder-Bot-1] → [Specific Deliverable / Feature]
   • @[Builder-Bot-2] → [Specific Deliverable / Feature]
   • @[QA-Bot] → Verification & regression suite for assigned tasks

   Awaiting human approval to dispatch. Reply "Approved" or adjust tasks.
   ```
5. **HALT:** Do not instruct bots to begin work until the human responds with approval.

---

## Phase 2: Task Dispatch & Branch Isolation

Once approved:
1. Dispatch each task to the assigned Builder Bot by tagging them in the thread.
2. Instruct each Builder Bot to:
   - Create a clean git branch: `bot/<agent-name>`.
   - Run the genOS BOOT sequence.
   - Implement the feature and accompanying tests.
   - Run local validation.
   - Run SHUTDOWN sequence with the Sanity Gate checks.
   - Push branch to GitHub and notify this thread with "Ready for QA".

---

## Phase 3: QA Verification & Peer Review Loop

1. When a Builder Bot posts "Ready for QA", tag the QA Bot to review the branch.
2. The QA Bot must:
   - Check out `bot/<agent-name>`.
   - Run test commands and verify deliverables against roadmap completion criteria.
   - If issues found: Tag the Builder Bot with exact failure logs.
   - **Self-Healing Budget:** Builder bots have a strict 2-retry limit to fix issues.
3. **Escalation Valve:** If tests fail after 2 retries, tag the human with an Escalation Summary detailing the issue, logs, and proposed resolution.

---

## Phase 4: Pull Request Preparation & Daily Summary

1. Once QA approves the branch:
   - Builder Bot opens a GitHub Pull Request against `main`.
2. Lead Bot posts the End-of-Day Summary in this thread:
   ```markdown
   🎉 Daily Work Complete!

   Ready Pull Requests:
   • PR #[Number]: [Task Title] by @[Builder-Bot] (QA: Approved ✓)

   To finalize:
   1. Review and merge the PR(s) on GitHub.
   2. Pull main in your local IDE to sync your Obsidian Graph View.
   ```
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python scratch/verify_task3_workflow_virtual_office.py`
Expected: PASS with "Task 3 verification PASSED!"

- [ ] **Step 5: Commit**

```bash
git add guides/prompts/workflow-virtual-office.md scratch/verify_task3_workflow_virtual_office.py
git commit -m "feat(virtual-office): add daily workflow lead bot prompt"
```

---

### Task 4: Update Framework Documentation (`README.md` and `guides/guide.md`)

**Files:**
- Modify: `d:/GameOS/README.md`
- Modify: `d:/GameOS/guides/guide.md`
- Test: `scratch/verify_task4_docs_tables.py`

**Interfaces:**
- Consumes: Tasks 1-3 deliverables.
- Produces: Integrated references in the main project documentation.

- [ ] **Step 1: Write test script to verify docs updates**

Create `scratch/verify_task4_docs_tables.py`:
```python
import os
from pathlib import Path

readme_path = Path("d:/GameOS/README.md")
guide_path = Path("d:/GameOS/guides/guide.md")

readme = readme_path.read_text(encoding="utf-8")
guide = guide_path.read_text(encoding="utf-8")

# Check README
assert "workflow-virtual-office.md" in readme, "README missing workflow-virtual-office.md link"
assert "setup-virtual-office.md" in readme or "integrations/virtual-office" in readme, "README missing virtual office integration"

# Check guide.md
assert "workflow-virtual-office.md" in guide, "guide.md missing workflow-virtual-office.md link"
assert "Virtual Office" in guide, "guide.md missing Virtual Office section"

print("Task 4 verification PASSED!")
```

- [ ] **Step 2: Run test to verify it fails before modification**

Run: `python scratch/verify_task4_docs_tables.py`
Expected: FAIL

- [ ] **Step 3: Modify `README.md` and `guides/guide.md`**

In `README.md`:
1. In the Repository Structure diagram, update `integrations/`:
   ```markdown
   ├── integrations/             # AI workforce integrations (Agency Agents & Virtual Office)
   │   ├── agency_agents.md      # Workforce selection protocol
   │   └── virtual-office/       # Grok Bot Virtual Office team integration
   ```
2. In the Daily Prompt Reference table, add:
   ```markdown
   | **Virtual Office** | [`workflow-virtual-office.md`](file:///d:/GameOS/guides/prompts/workflow-virtual-office.md) | Daily multi-bot dispatch and coordinator workflow in Grok Bot |
   ```

In `guides/guide.md`:
Add a section for **Virtual Office Integration (Grok Bot & Cloud Agents)** explaining setup and the daily workflow, and add `workflow-virtual-office.md` to the Prompt Reference table.

- [ ] **Step 4: Run test to verify it passes**

Run: `python scratch/verify_task4_docs_tables.py`
Expected: PASS with "Task 4 verification PASSED!"

- [ ] **Step 5: Commit**

```bash
git add README.md guides/guide.md scratch/verify_task4_docs_tables.py
git commit -m "docs: document virtual office integration in README and user guide"
```

---

### Task 5: End-to-End Verification & Synchronize to Capstone

**Files:**
- Modify: `scratch/verify_genos.py`
- Test: Full framework regression verification
- Sync: Copy updated framework files to `D:/Baybayin-Capstone/genOS/`

**Interfaces:**
- Consumes: All deliverables from Tasks 1-4.
- Produces: 100% verified framework with zero regression and Capstone synchronized.

- [ ] **Step 1: Update `verify_genos.py` to include new prompts and integration files**

Add `guides/prompts/workflow-virtual-office.md` and `integrations/virtual-office/README.md` to `expected_prompts` / verification paths in `verify_genos.py`.

- [ ] **Step 2: Run `verify_genos.py`**

Run: `python C:/Users/Red/.gemini/antigravity-ide/brain/afafabfc-153d-4309-a190-2de3c8992cf7/scratch/verify_genos.py`
Expected: Output `PASSED: 0 errors found.`

- [ ] **Step 3: Copy integration and prompt files to Capstone**

Execute:
```powershell
Copy-Item "d:/GameOS/integrations/virtual-office" "D:/Baybayin-Capstone/genOS/integrations/virtual-office" -Recurse -Force
Copy-Item "d:/GameOS/guides/prompts/workflow-virtual-office.md" "D:/Baybayin-Capstone/genOS/guides/prompts/workflow-virtual-office.md" -Force
Copy-Item "d:/GameOS/README.md" "D:/Baybayin-Capstone/genOS/README.md" -Force
Copy-Item "d:/GameOS/guides/guide.md" "D:/Baybayin-Capstone/genOS/guides/guide.md" -Force
```

- [ ] **Step 4: Final Git Commit and Push**

```bash
git add .
git commit -m "feat(virtual-office): complete hybrid integration and sync with capstone"
git push
```
