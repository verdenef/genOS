# genOS

**genOS** is a universal, stack-agnostic AI operating system for modern software development: a lightweight, deterministic **Project Brain** that maintains persistent memory across AI agents, chat sessions, and IDEs.

Humans provide intent and approvals. AI maintains the brain. Source code and live runtimes hold implementation truth. genOS stores the architectural and execution knowledge that cannot be inferred from code alone.

---

## Repository Structure

```
genOS/
├── AGENTS.md                 # Universal kernel — authoritative operational rules
├── README.md                 # Repository overview (this file)
├── brain/                    # The Project Brain (single source of truth)
│   ├── 00_PROJECT.md         # Intent, scope, architecture constraints
│   ├── 20_PROGRESS.yaml      # Cold-start execution RAM
│   ├── 30_DECISIONS.md       # Architectural Decision Records (ADRs)
│   ├── 40_BACKLOG.md         # Kanban queue for ad-hoc work
│   ├── 50_ROADMAP.md         # Milestone definitions and criteria
│   ├── 60_AGENTS.md          # Approved AI workforce roster
│   └── systems/              # Autonomous system documents
├── profiles/                 # Plug-and-play stack profiles
├── guides/                   # User guide and prompt references
│   ├── guide.md              # Official User Guide
│   └── prompts/              # Workflow reference files
└── integrations/             # Optional integrations (Agency Agents)
```

---

## Getting Started

See the [genOS User Guide](guides/guide.md) for setup, daily workflow, and commands.

**For AI agents:** Read and follow [`AGENTS.md`](AGENTS.md).

---

## Core Principles

1. **Zero-Chat-History Recovery:** Agents recover state from the Project Brain alone.
2. **Deterministic Ownership:** Every piece of project truth has exactly one authoritative file.
3. **Automated Sanity Gates:** Mandatory integrity audits guarantee the Brain is never corrupted.
4. **Stack Profiles:** One unified framework for web apps, microservices, mobile, data science, CLIs, and game development.
