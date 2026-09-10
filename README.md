# genOS

**genOS** is a universal, stack-agnostic AI operating system for modern software development: a lightweight, deterministic **Project Brain** that maintains persistent memory across AI agents, chat sessions, and IDEs.

Humans provide intent and approvals. AI maintains the brain. Source code and live runtimes hold implementation truth. genOS stores the architectural and execution knowledge that cannot be inferred from code alone.

---

## Repository Structure

```
genOS/
├── AGENTS.md                 # Universal kernel — authoritative operational rules
├── README.md                 # Repository overview
├── profiles/                 # Plug-and-play stack profiles
│   ├── web-fullstack/        # React / Next.js / Vue / Node / PostgreSQL
│   ├── backend-services/     # Go / Rust / FastAPI / Docker / Redis
│   ├── mobile/               # Flutter / React Native / Swift / Kotlin
│   ├── ai-data/              # Python / PyTorch / LangChain / Vector DBs
│   ├── cli-system/           # Rust / Go / C CLI & systems tools
│   └── gamedev/              # Unity / Godot / Unreal (GameOS profile)
├── guides/                   # Complete user guide and prompt templates
│   ├── guide.md              # Official User Guide
│   └── prompts/
│       ├── setup-init.md     # All-in-one Day 0 onboarding wizard
│       ├── workflow-01-kickoff.md
│       ├── workflow-02-shutdown.md
│       ├── workflow-03-resume-session.md
│       ├── workflow-autonomous-batch.md # Hands-free multi-task autonomous runner
│       └── workflow-doctor.md
├── integrations/             # AI workforce integrations (Agency Agents)
└── brain/                    # The Project Brain (single source of truth)
    ├── 00_PROJECT.md         # Intent, scope, architecture constraints
    ├── 20_PROGRESS.yaml      # Cold-start execution RAM
    ├── 30_DECISIONS.md       # Architectural Decision Records (ADRs)
    ├── 40_BACKLOG.md         # Kanban queue for ad-hoc work
    ├── 50_ROADMAP.md         # Milestone definitions and criteria
    ├── 60_AGENTS.md          # Approved AI workforce roster
    └── systems/              # Autonomous system documents
        ├── README.md
        └── SYSTEM.md         # Canonical system template
```

---

## Quickstart

### 1. Day 0: Setup & Profile Selection
Copy the `genOS/` folder into your project repository. Open a chat in your IDE (Cursor, Antigravity, Claude Code) and paste:

**`guides/prompts/setup-init.md`**

The wizard will:
1. Detect your stack and recommend a profile from `profiles/`.
2. Ask for your vision and initialize `brain/00_PROJECT.md` & `brain/50_ROADMAP.md`.
3. Configure your recommended runtime MCP tools.
4. Optionally install tailored AI specialist roles into `brain/60_AGENTS.md`.
5. Prune unused profiles to keep your repository clean.

### 2. Day 1: Daily Development
Whenever you are ready to build a milestone, open a fresh chat and paste:

**`guides/prompts/workflow-01-kickoff.md`**

When the milestone is verified and passing, save durable state to the Brain by pasting:

**`guides/prompts/workflow-02-shutdown.md`**

---

## The Workflow in Action

Here is what using genOS looks like in practice:

### 1. Day 0 — Setup & Initialization
Paste `guides/prompts/setup-init.md` into your IDE chat:

> **Agent:** Detected stack: React / Node.js / PostgreSQL. Suggested profile: `profiles/web-fullstack`. What is your project vision and constraints?  
> **Human:** "Building TaskPulse, a real-time collaborative task manager."  
> **Agent:** Initialized `brain/00_PROJECT.md`, starter systems, and proposed M1.0 in `brain/50_ROADMAP.md`. Recommended MCPs: Playwright & PostgreSQL. Recommended workforce: Frontend Developer & Backend Architect. Pruned unused profiles.  
> **Agent:** 🎉 Day 0 Complete! Close this chat session.

---

### 2. Day 1 — Milestone Kickoff
Open a fresh chat (clean context window) and paste `guides/prompts/workflow-01-kickoff.md`:

> **Agent:** BOOT sequence complete from Project Brain.  
> - Active Milestone: **M1.0 — Database Schema & Workspace Seeding**  
> - Deliverables & Criteria loaded from `50_ROADMAP.md`.  
> - Proposed Plan: 1) Create Prisma schema, 2) Run migration, 3) Seed sample workspace.  
> - *Awaiting your approval before modifying code.*  
> **Human:** "Plan approved. Proceed."  
> *(Agent implements code, runs tests, inspects runtime)*

---

### 3. Day 1 — Milestone Shutdown
When work is complete and tested, paste `guides/prompts/workflow-02-shutdown.md`:

> **Agent:** Executing SHUTDOWN:  
> - Verified M1.0 completion criteria in `50_ROADMAP.md` [done].  
> - Activated M1.1 (Authentication) in roadmap [active].  
> - Updated `20_PROGRESS.yaml` with session summary and new milestone pointer.  
> - Automated Sanity Gate: YAML validity ✓, Index sync ✓, Scope checks ✓.  
> 🎉 Memory persisted. Close chat or commit to Git!

---

### 4. Diagnostics & Self-Healing (Anytime)
If an agent crash occurs or files feel out of sync, paste `guides/prompts/workflow-doctor.md`:

> **Agent:** Inspecting all Brain files... Fixed 1 index table desync. Verified all milestone pointers and system scopes. Project Brain is 100% healthy.

---

## Daily Prompt Reference

| Stage | Prompt File | Purpose |
| :--- | :--- | :--- |
| **Day 0** | [`setup-init.md`](file:///d:/GameOS/guides/prompts/setup-init.md) | One-time interactive setup wizard (stack, brain, tools, workforce) |
| **Start Coding** | [`workflow-01-kickoff.md`](file:///d:/GameOS/guides/prompts/workflow-01-kickoff.md) | Zero-history BOOT, review criteria, propose plan for human approval |
| **Mid-Session** | [`workflow-03-resume-session.md`](file:///d:/GameOS/guides/prompts/workflow-03-resume-session.md) | Hot-reload in-flight execution RAM when switching IDEs or after crashes |
| **Autonomous** | [`workflow-autonomous-batch.md`](file:///d:/GameOS/guides/prompts/workflow-autonomous-batch.md) | Uninterrupted multi-task batch execution with dual-persona QA gates |
| **Finish Work** | [`workflow-02-shutdown.md`](file:///d:/GameOS/guides/prompts/workflow-02-shutdown.md) | Advance roadmap, update RAM, run mandatory Sanity Gate |
| **Diagnostics** | [`workflow-doctor.md`](file:///d:/GameOS/guides/prompts/workflow-doctor.md) | Scan and self-repair syntax, index tables, and memory integrity |
| **Tooling** | [`setup-tooling.md`](file:///d:/GameOS/guides/prompts/setup-tooling.md) | Reconfigure runtime tooling and MCP servers independently |
| **Workforce** | [`setup-workforce.md`](file:///d:/GameOS/guides/prompts/setup-workforce.md) | Reconfigure specialist Agency Agents independently |
| **Upgrades** | [`setup-04-framework-upgrade.md`](file:///d:/GameOS/guides/prompts/setup-04-framework-upgrade.md) | Safely update genOS framework while strictly preserving the Brain |

---

## Core Principles

1. **Zero-Chat-History Recovery:** Agents recover state from the Project Brain alone. No lost knowledge, no context window bloat, and no token degradation over long sessions.
2. **Deterministic Ownership:** Every piece of project truth has exactly one authoritative file. State is never mirrored or duplicated.
3. **Automated Sanity Gates:** The built-in Brain Doctor and mandatory SHUTDOWN audit guarantee that the Brain is never corrupted by hallucinating agents or syntax errors.
4. **Stack Profiles:** One unified framework for web apps, microservices, mobile, data science, CLIs, and game development.
