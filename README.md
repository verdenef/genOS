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

### 2. Day 1: Daily Development
Whenever you are ready to build a milestone, open a fresh chat and paste:

**`guides/prompts/workflow-01-kickoff.md`**

When the milestone is verified and passing, save durable state to the Brain by pasting:

**`guides/prompts/workflow-02-shutdown.md`**

---

## Core Principles

1. **Zero-Chat-History Recovery:** Agents recover state from the Project Brain alone. No lost knowledge, no context window bloat, and no token degradation over long sessions.
2. **Deterministic Ownership:** Every piece of project truth has exactly one authoritative file. State is never mirrored or duplicated.
3. **Automated Sanity Gates:** The built-in Brain Doctor and mandatory SHUTDOWN audit guarantee that the Brain is never corrupted by hallucinating agents or syntax errors.
4. **Stack Profiles:** One unified framework for web apps, microservices, mobile, data science, CLIs, and game development.
