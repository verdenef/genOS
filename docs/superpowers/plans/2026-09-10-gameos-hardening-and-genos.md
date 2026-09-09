# GameOS Hardening & genOS Universal Framework Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement the Doctor self-check and unified Day 0 onboarding wizard in GameOS, then scaffold and publish the universal genOS framework repository to `https://github.com/verdenef/genOS.git`.

**Architecture:** 
Phase 1 hardens GameOS in-place by adding a pure-markdown Brain Doctor prompt, embedding an automated 5-point sanity gate into the SHUTDOWN protocol, and creating a unified `setup-init.md` wizard. Phase 2 extracts this hardened kernel into a domain-agnostic `genOS` repository featuring a plug-and-play Stack Profiles catalog (`profiles/`).

**Tech Stack:** Markdown, YAML, Git, GitHub (`verdenef/genOS`).

## Global Constraints

- **Single Source of Truth:** Never duplicate state across files. Respect ownership tables in `AGENTS.md`.
- **Zero-History Recovery:** All prompts and protocols must be fully self-contained and recoverable from file state alone.
- **Dependency-Free Doctor:** The integrity verification tool must be pure markdown and execute natively via LLM reasoning without external language runtimes.
- **Strict Separation:** GameOS remains specialized for game development; genOS is completely stack-agnostic with plug-and-play profiles.

---

### Task 1: Create GameOS Brain Doctor Prompt

**Files:**
- Create: `d:/GameOS/guides/prompts/workflow-doctor.md`

**Interfaces:**
- Consumes: `brain/` files (`00_PROJECT.md`, `20_PROGRESS.yaml`, `30_DECISIONS.md`, `40_BACKLOG.md`, `50_ROADMAP.md`, `60_AGENTS.md`, `brain/systems/*.md`).
- Produces: Structured health verification and automated repair report.

- [ ] **Step 1: Write `guides/prompts/workflow-doctor.md`**

Create `guides/prompts/workflow-doctor.md` with explicit diagnostic and auto-repair instructions covering YAML validity, pointer integrity, index synchronization, and system scopes.

- [ ] **Step 2: Verify prompt content against Brain invariants**

Inspect the prompt to verify it enforces all rules from `AGENTS.md`.

- [ ] **Step 3: Commit**

```bash
git add guides/prompts/workflow-doctor.md
git commit -m "feat(doctor): add standalone Brain doctor diagnostic prompt"
```

---

### Task 2: Integrate Mandatory SHUTDOWN Sanity Gate into GameOS

**Files:**
- Modify: `d:/GameOS/AGENTS.md:155-175`
- Modify: `d:/GameOS/guides/prompts/workflow-02-shutdown.md`

**Interfaces:**
- Consumes: Task 1 verification rules.
- Produces: Automated sanity check step before closing any session.

- [ ] **Step 1: Update SHUTDOWN sequence in `AGENTS.md`**

Add the 5-point Sanity Gate (YAML Validity, Milestone Pointer, Index Sync, No State Leakage, System Scopes) as Step 6 of the SHUTDOWN sequence.

- [ ] **Step 2: Update `guides/prompts/workflow-02-shutdown.md`**

Add the Sanity Gate verification step to the shutdown prompt instructions.

- [ ] **Step 3: Commit**

```bash
git add AGENTS.md guides/prompts/workflow-02-shutdown.md
git commit -m "feat(kernel): add mandatory SHUTDOWN sanity gate"
```

---

### Task 3: Create Unified Day 0 Onboarding Master Wizard for GameOS

**Files:**
- Create: `d:/GameOS/guides/prompts/setup-init.md`

**Interfaces:**
- Consumes: Blank repo detection, existing code scan, `setup-02-mcp`, `setup-03-workforce`.
- Produces: Single guided conversational onboarding flow.

- [ ] **Step 1: Write `guides/prompts/setup-init.md`**

Implement the 4-phase interactive wizard: Phase 1 (Project Detection & Brain Setup), Phase 2 (Automatic MCP Tooling Transition), Phase 3 (Optional AI Workforce Integration), Phase 4 (Doctor Check & Handoff).

- [ ] **Step 2: Verify wizard instructions**

Ensure the prompt explicitly prevents premature code execution and directs the user to `workflow-01-kickoff.md` only upon completion.

- [ ] **Step 3: Commit**

```bash
git add guides/prompts/setup-init.md
git commit -m "feat(setup): add unified Day 0 onboarding master wizard"
```

---

### Task 4: Update GameOS User Guide and Documentation

**Files:**
- Modify: `d:/GameOS/guides/guide.md`
- Modify: `d:/GameOS/README.md`

**Interfaces:**
- Consumes: Tasks 1-3.
- Produces: Clear, friction-free documentation for developers and their teams.

- [ ] **Step 1: Update `guides/guide.md`**

Replace multi-step onboarding instructions with the primary `setup-init.md` workflow, document `workflow-doctor.md`, and list individual setup prompts as advanced utilities.

- [ ] **Step 2: Update `README.md` Quickstart**

Update the repository README quickstart section to reflect `setup-init.md`.

- [ ] **Step 3: Commit**

```bash
git add guides/guide.md README.md
git commit -m "docs: update guide and README for unified setup and doctor"
```

---

### Task 5: Scaffold the `genOS` Repository

**Files:**
- Target Directory: `d:/genOS`
- Remote: `https://github.com/verdenef/genOS.git`

**Interfaces:**
- Consumes: Hardened kernel from GameOS.
- Produces: Clean, initialized Git repository for genOS.

- [ ] **Step 1: Initialize local directory and Git repository for `genOS`**

Create directory structure for `genOS` (`brain/systems`, `profiles`, `guides/prompts`, `integrations`).

- [ ] **Step 2: Configure Git remote**

Set remote to `https://github.com/verdenef/genOS.git`.

- [ ] **Step 3: Commit initial scaffolding**

```bash
git commit -m "chore: initialize genOS repository structure"
```

---

### Task 6: Author Universal genOS Kernel & Brain Templates

**Files:**
- Create: `d:/genOS/AGENTS.md`
- Create: `d:/genOS/brain/00_PROJECT.md`
- Create: `d:/genOS/brain/20_PROGRESS.yaml`
- Create: `d:/genOS/brain/30_DECISIONS.md`
- Create: `d:/genOS/brain/40_BACKLOG.md`
- Create: `d:/genOS/brain/50_ROADMAP.md`
- Create: `d:/genOS/brain/60_AGENTS.md`
- Create: `d:/genOS/brain/systems/README.md`
- Create: `d:/genOS/brain/systems/SYSTEM.md`

**Interfaces:**
- Consumes: Design spec Section 3.1.
- Produces: Completely domain-agnostic software development kernel.

- [ ] **Step 1: Author universal `AGENTS.md`**

Generalize all game-engine terms to universal software engineering concepts (Runtime Observers, Domain Systems, Endpoints, Components).

- [ ] **Step 2: Author universal Brain templates**

Create standard clean templates for `00_PROJECT.md`, `20_PROGRESS.yaml`, `30_DECISIONS.md`, `40_BACKLOG.md`, `50_ROADMAP.md`, `60_AGENTS.md`, and `brain/systems/SYSTEM.md`.

- [ ] **Step 3: Commit**

```bash
git add AGENTS.md brain/
git commit -m "feat(kernel): add universal genOS kernel and brain templates"
```

---

### Task 7: Author genOS Stack Profiles

**Files:**
- Create: `d:/genOS/profiles/web-fullstack/`
- Create: `d:/genOS/profiles/backend-services/`
- Create: `d:/genOS/profiles/mobile/`
- Create: `d:/genOS/profiles/ai-data/`
- Create: `d:/genOS/profiles/cli-system/`
- Create: `d:/genOS/profiles/gamedev/`

**Interfaces:**
- Consumes: Stack profiles architecture from spec.
- Produces: Plug-and-play profile templates with recommended MCPs, agents, and systems.

- [ ] **Step 1: Create web-fullstack and backend-services profiles**

Define metadata, MCP recommendations, specialist agents, and starter systems.

- [ ] **Step 2: Create mobile, ai-data, cli-system, and gamedev profiles**

Define configurations for mobile apps, data/AI, CLI utilities, and game dev.

- [ ] **Step 3: Commit**

```bash
git add profiles/
git commit -m "feat(profiles): add stack profiles catalog"
```

---

### Task 8: Author genOS Guides & Workflows

**Files:**
- Create: `d:/genOS/guides/guide.md`
- Create: `d:/genOS/guides/prompts/setup-init.md`
- Create: `d:/genOS/guides/prompts/setup-tooling.md`
- Create: `d:/genOS/guides/prompts/setup-workforce.md`
- Create: `d:/genOS/guides/prompts/workflow-01-kickoff.md`
- Create: `d:/genOS/guides/prompts/workflow-02-shutdown.md`
- Create: `d:/genOS/guides/prompts/workflow-03-resume.md`
- Create: `d:/genOS/guides/prompts/workflow-doctor.md`
- Create: `d:/genOS/README.md`

**Interfaces:**
- Consumes: Universal kernel & profiles.
- Produces: Complete user-facing documentation and workflow prompts.

- [ ] **Step 1: Author `guides/prompts/setup-init.md` with Profile Selector**

Create interactive prompt with auto-detection of stack and profile selection.

- [ ] **Step 2: Author workflows and user guide**

Port kickoff, shutdown, resume, and doctor prompts.

- [ ] **Step 3: Author `README.md`**

Write comprehensive README introducing genOS.

- [ ] **Step 4: Commit**

```bash
git add guides/ README.md
git commit -m "docs: add genOS user guide, workflow prompts, and readme"
```

---

### Task 9: Push genOS to Remote Repository

**Files:**
- Remote: `https://github.com/verdenef/genOS.git`

**Interfaces:**
- Consumes: Complete `d:/genOS` repository.
- Produces: Published GitHub repository.

- [ ] **Step 1: Verify genOS Brain with Doctor prompt**

Run internal audit on the genOS repository.

- [ ] **Step 2: Push to GitHub**

```bash
git push -u origin main
```
