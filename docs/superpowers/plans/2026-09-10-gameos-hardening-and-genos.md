# genOS Universal Transformation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transform the repository into `genOS` (Universal AI Operating System) on branch `feat/genos`, integrating the Brain Doctor, SHUTDOWN sanity gate, plug-and-play Stack Profiles (`profiles/`), and the unified `setup-init.md` onboarding wizard.

**Architecture:**
Generalize the proven GameOS single-source-of-truth kernel into a universal, stack-agnostic software framework. Preserve game development as a first-class profile (`profiles/gamedev/`) alongside web, backend, mobile, AI/data, and CLI profiles. Add automated integrity checking and streamlined Day 0 onboarding.

**Tech Stack:** Markdown, YAML, Git branch `feat/genos`, GitHub (`verdenef/genOS`).

## Global Constraints

- **Single Source of Truth:** Never duplicate state across files. Respect ownership tables in `AGENTS.md`.
- **Zero-History Recovery:** All prompts and protocols must be fully self-contained and recoverable from file state alone.
- **Dependency-Free Doctor:** The integrity verification tool must be pure markdown and execute natively via LLM reasoning without external language runtimes.
- **Backward Compatibility:** Existing game projects can seamlessly use `profiles/gamedev/` without losing any functionality.
- **Git Branch:** All commits must be made to the `feat/genos` branch.

---

### Task 1: Create Pure-Markdown Brain Doctor (`workflow-doctor.md`)

**Files:**
- Create: `guides/prompts/workflow-doctor.md`

**Interfaces:**
- Consumes: Brain files (`00_PROJECT.md`, `20_PROGRESS.yaml`, `30_DECISIONS.md`, `40_BACKLOG.md`, `50_ROADMAP.md`, `60_AGENTS.md`, `brain/systems/*.md`).
- Produces: Diagnostic analysis, automated repair instructions, and formatted health report.

- [ ] **Step 1: Write `guides/prompts/workflow-doctor.md`**

Author the doctor prompt with explicit rules to diagnose and repair:
- YAML syntax and required keys in `20_PROGRESS.yaml`.
- Milestone pointer validity against `50_ROADMAP.md`.
- Index table synchronization in `50_ROADMAP.md` and `30_DECISIONS.md`.
- No state leakage or duplicate "Doing" items in `40_BACKLOG.md`.
- Systems listed in `systems_in_scope` matching files in `brain/systems/`.

- [ ] **Step 2: Verify prompt structure and formatting**

Check that the prompt contains clear diagnostic checklists and output templates.

- [ ] **Step 3: Commit to `feat/genos`**

```bash
git add guides/prompts/workflow-doctor.md
git commit -m "feat(doctor): add standalone Brain doctor diagnostic prompt"
```

---

### Task 2: Integrate Mandatory SHUTDOWN Sanity Gate into Kernel

**Files:**
- Modify: `AGENTS.md`
- Modify: `guides/prompts/workflow-02-shutdown.md`

**Interfaces:**
- Consumes: Task 1 verification rules.
- Produces: Enforced 5-point sanity audit before any session completion.

- [ ] **Step 1: Update SHUTDOWN sequence in `AGENTS.md`**

Add Step 6: Sanity Gate to the SHUTDOWN sequence in `AGENTS.md`.

- [ ] **Step 2: Update `guides/prompts/workflow-02-shutdown.md`**

Add the Sanity Gate verification checklist to the shutdown prompt.

- [ ] **Step 3: Commit to `feat/genos`**

```bash
git add AGENTS.md guides/prompts/workflow-02-shutdown.md
git commit -m "feat(kernel): add mandatory SHUTDOWN sanity gate"
```

---

### Task 3: Generalize Kernel to Universal `genOS` (`AGENTS.md`)

**Files:**
- Modify: `AGENTS.md`
- Modify: `brain/00_PROJECT.md`
- Modify: `brain/systems/SYSTEM.md`

**Interfaces:**
- Consumes: Design spec Section 3.1.
- Produces: Universal, domain-agnostic software development kernel.

- [ ] **Step 1: Generalize `AGENTS.md`**

Update title to "genOS Kernel". Replace game-specific terms ("Engine MCP", "scenes/prefabs/assets", "gameplay") with universal software engineering concepts ("Runtime Observers", "Source code / Endpoints / Components", "Domain logic").

- [ ] **Step 2: Generalize `brain/00_PROJECT.md` template**

Provide clean universal placeholders (Product Vision, Target Platforms/Environments, Core User Loop/Workflow, Architectural Constraints, Tech Stack).

- [ ] **Step 3: Generalize `brain/systems/SYSTEM.md` template**

Update system template to fit any software domain (Web, Backend, API, UI, Service, Game).

- [ ] **Step 4: Commit to `feat/genos`**

```bash
git add AGENTS.md brain/00_PROJECT.md brain/systems/SYSTEM.md
git commit -m "feat(kernel): generalize kernel and templates to genOS universal framework"
```

---

### Task 4: Author Stack Profiles Catalog (`profiles/`)

**Files:**
- Create: `profiles/README.md`
- Create: `profiles/web-fullstack/profile.yaml`
- Create: `profiles/backend-services/profile.yaml`
- Create: `profiles/mobile/profile.yaml`
- Create: `profiles/ai-data/profile.yaml`
- Create: `profiles/cli-system/profile.yaml`
- Create: `profiles/gamedev/profile.yaml`

**Interfaces:**
- Consumes: Spec Section 3.2.
- Produces: Modular presets with recommended MCP tools, starter systems, and specialist AI roles.

- [ ] **Step 1: Create `profiles/README.md` catalog guide**

Document how profiles work, how to create custom profiles, and how `setup-init.md` consumes them.

- [ ] **Step 2: Create Web & Backend profiles (`web-fullstack`, `backend-services`)**

Define configurations for modern web (React/Next.js/Vue, Node, PostgreSQL, Playwright) and backend services (Go, Rust, FastAPI, Docker, Redis).

- [ ] **Step 3: Create Mobile, AI/Data, CLI, and GameDev profiles**

Define configurations for Mobile (Flutter/React Native), AI/Data (Python, PyTorch, Vector DBs), CLI (Rust/Go), and GameDev (Unity/Godot/Unreal).

- [ ] **Step 4: Commit to `feat/genos`**

```bash
git add profiles/
git commit -m "feat(profiles): add stack profiles catalog for web, backend, mobile, ai, cli, and gamedev"
```

---

### Task 5: Author Unified Day 0 Onboarding Master Wizard (`setup-init.md`)

**Files:**
- Create: `guides/prompts/setup-init.md`

**Interfaces:**
- Consumes: Stack profiles catalog, blank vs existing repo detection, MCP tooling, and workforce setup.
- Produces: Single interactive onboarding prompt with profile selection.

- [ ] **Step 1: Author `guides/prompts/setup-init.md`**

Implement 4-phase wizard:
- Phase 1: Repo Inspection & Profile Selection (auto-detects stack and asks to confirm profile).
- Phase 2: Project Brain Population (`00_PROJECT.md`, `50_ROADMAP.md`, starter systems).
- Phase 3: Runtime Tooling / MCP Setup (profile-based MCP configuration).
- Phase 4: AI Workforce Selection (profile-based specialist roles in `60_AGENTS.md`) & Handoff to `workflow-01-kickoff.md`.

- [ ] **Step 2: Verify wizard instructions**

Ensure strict halt preventing premature code execution.

- [ ] **Step 3: Commit to `feat/genos`**

```bash
git add guides/prompts/setup-init.md
git commit -m "feat(setup): add unified Day 0 onboarding master wizard with profile selection"
```

---

### Task 6: Update Guides, Workflows & Documentation

**Files:**
- Modify: `guides/guide.md`
- Modify: `guides/prompts/workflow-01-kickoff.md`
- Modify: `guides/prompts/workflow-03-resume-session.md`
- Modify: `README.md`

**Interfaces:**
- Consumes: Tasks 1-5.
- Produces: Cohesive genOS documentation and generalized workflows.

- [ ] **Step 1: Update `guides/guide.md`**

Document genOS Day 0 wizard, profiles catalog, doctor diagnostics, and daily workflows.

- [ ] **Step 2: Generalize `workflow-01-kickoff.md` and `workflow-03-resume-session.md`**

Update references from GameOS to genOS.

- [ ] **Step 3: Overhaul `README.md`**

Rewrite README to introduce genOS as the universal agentic operating system for all software development.

- [ ] **Step 4: Commit to `feat/genos`**

```bash
git add guides/ README.md
git commit -m "docs: overhaul guides and README for genOS universal framework"
```

---

### Task 7: Verification & Brain Doctor Run

**Files:**
- Test all Brain files against `workflow-doctor.md`

- [ ] **Step 1: Run Doctor validation on repository**

Audit `brain/` files, verify YAML syntax, check roadmap pointers, and confirm clean state.

- [ ] **Step 2: Review git status on `feat/genos`**

Ensure all changes are cleanly committed to branch `feat/genos`.
