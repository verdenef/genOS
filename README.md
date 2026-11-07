# genOS

**genOS** is a universal, stack-agnostic AI operating system for modern software development: a lightweight, deterministic **Project Brain** that maintains persistent memory across AI agents, chat sessions, and IDEs.

Humans provide intent and approvals. AI maintains the brain. Source code and live runtimes hold implementation truth. genOS stores the architectural and execution knowledge that cannot be inferred from code alone.

---

## The Unified AI Engineering Stack

genOS natively coordinates four disciplines into one frictionless developer workflow:

| Layer | System | Responsibility |
|:---|:---|:---|
| **1. Memory & State** | **genOS** | Project Brain, zero-history recovery, milestone tracking, and mandatory Sanity Gates. |
| **2. Specialist Identity** | **Agency Agents** | Domain engineering rules (e.g. `unity-architect`, `backend-architect`) loaded before planning. |
| **3. Senior Restraint** | **Ponytail** | The Ladder of Restraint (YAGNI, reuse, stdlib, 1-liner) cuts over-engineering before writing code. |
| **4. Execution Rigor** | **Superpowers** | Test-driven development, bite-sized plan breakdown, and verification before completion. |

---

## Daily Commands

genOS eliminates prompt copy-pasting. In any AI chat (Antigravity, Cursor, Claude Desktop, Claude Code), just type:

| Command | Action |
|:---|:---|
| `kickoff` | BOOTs from brain, adopts specialist persona, applies Ponytail filter, and proposes plan |
| `kickoff <intent>` | Scoped session — e.g. `kickoff let's fix the UI bugs today` |
| `shutdown` | Verifies milestone criteria, runs the 18-point Sanity Gate, and persists state |
| `doctor` | Diagnoses and auto-repairs brain integrity issues |
| `status` | Quick read-only summary of current milestone and execution RAM |
| `batch` | Autonomous multi-task execution with dual-persona (Builder + QA Auditor) loops |
| `update` | 1-Click framework updater from GitHub with zero data loss in `brain/` |

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

## Quickstart

1. **Day 0 Setup:** Copy `genOS` into your repository, open your AI chat, and paste [`guides/prompts/setup-init.md`](guides/prompts/setup-init.md).
2. **Day 1+ Development:** In a fresh session, simply type **`kickoff`**.
3. **Finish Milestone:** When verified, type **`shutdown`**.

For the complete guide, see the [genOS User Guide](guides/guide.md).

**For AI agents:** Read and follow [`AGENTS.md`](AGENTS.md).

---

## Core Principles

1. **Zero-Chat-History Recovery:** Agents recover state from the Project Brain alone. No token degradation or context rot.
2. **Deterministic Ownership:** Every piece of project truth has exactly one authoritative file.
3. **Automated Sanity Gates:** Mandatory integrity audits guarantee the Brain is never corrupted.
4. **Unified Engineering Stack:** Eliminates bloat and ensures test-driven rigor out-of-the-box.
5. **Stack Profiles:** One unified framework for web apps, microservices, mobile, data science, CLIs, and game development.
