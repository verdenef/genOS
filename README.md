# genOS

[![Framework Version](https://img.shields.io/badge/genOS-v3.2-2563eb?style=flat-square)](AGENTS.md)
[![Last Commit](https://img.shields.io/github/last-commit/verdenef/genOS/main?style=flat-square)](https://github.com/verdenef/genOS/commits/main)
[![Supported IDEs](https://img.shields.io/badge/Works%20with-Claude%20Code%20%7C%20Cursor%20%7C%20Antigravity%20%7C%20Codex-4f46e5?style=flat-square)](guides/guide.md#tool-setup-bootstrapping)
[![Stack Profiles](https://img.shields.io/badge/Stack%20Profiles-7-10b981?style=flat-square)](profiles/README.md)
[![Obsidian](https://img.shields.io/badge/Obsidian-Graph%20Ready-7c3aed?style=flat-square&logo=obsidian&logoColor=white)](guides/guide.md#obsidian-integration)
[![License: MIT](https://img.shields.io/badge/License-MIT-f59e0b?style=flat-square)](LICENSE)

**genOS** is a universal, stack-agnostic AI operating system for modern software development: a lightweight, deterministic **Project Brain** that maintains persistent memory across AI agents, chat sessions, and IDEs.

Humans provide intent and approvals. AI maintains the brain. Source code and live runtimes hold implementation truth. genOS stores the architectural and execution knowledge that cannot be inferred from code alone.

---

## The Unified AI Engineering Stack

genOS coordinates five complementary disciplines into one frictionless developer workflow:

| Layer | System | Responsibility |
|:---|:---|:---|
| **1. Memory & State** | **genOS** | Project Brain (`brain/`), zero-history recovery, milestone tracking, and mandatory Sanity Gates. |
| **2. Specialist Identity** | **Agency Agents** | Domain engineering rules (e.g. `unity-architect`, `backend-architect`) verified via the Hard Persona Gate before planning. Auto-installed via `guides/scripts/install_agent.py` upon human approval (no desktop app required). |
| **3. Code Topology *(Optional)*** | **Graphify** | Local, offline `--code-only` Tree-sitter AST call graphs (`graphifyy[mcp]`) for instant caller/callee queries and path analysis. |
| **4. Senior Restraint** | **Ponytail** | The Ladder of Restraint (YAGNI, reuse, stdlib, 1-liner) prunes over-engineering before writing code. |
| **5. Execution Rigor** | **Superpowers** | Test-driven development, subagent-driven task plans, copy-paste handoffs, and verification before completion. |

---

## Daily Commands

genOS eliminates prompt boilerplate. In any AI chat (Antigravity, Cursor, Claude Code, Claude Desktop, Codex), just type:

| Command | Action |
|:---|:---|
| `kickoff` | BOOTs from brain, verifies specialist rules, runs optional Graphify topology check, applies Ponytail filter, and proposes a plan + Model Tier recommendation + copy-pasteable execution handoff blocks. |
| `kickoff <intent>` | Scoped session — e.g. `kickoff fix the login flow` or `kickoff execute the approved plan: <path>`. |
| `shutdown` | Verifies milestone criteria, runs the mandatory Sanity Gate, and persists cold-start execution RAM. |
| `doctor` | Diagnoses and auto-repairs brain integrity issues. |
| `status` | Quick read-only summary of current milestone and execution RAM. |
| `batch` | Autonomous multi-task execution with dual-persona (Builder + QA Auditor) loops. |
| `update` | Verifies drift against GitHub `main` (stops if current), proposes an Upgrade & Migration Plan for approval, refreshes core framework files while strictly shielding `brain/`, `.obsidian/`, custom profiles, and project-installed agent skills/rules, then runs Doctor. |

### Timeless Model Tiers
genOS recommends models by capability tier rather than hardcoded version strings:
- **Flagship** (`kickoff` planning, `batch`, complex architecture) — start in a **new session**.
- **Balanced** (daily implementation, tweaks, debugging) — continue only if context is clean.
- **Fast** (`shutdown`, `doctor`, `status`) — minimal token overhead.

---

## Repository Structure

```
genOS/
├── AGENTS.md                        # Universal kernel — authoritative operational rules
├── CLAUDE.md                        # Claude Code entry point (points to AGENTS.md)
├── LICENSE                          # MIT License for genOS
├── README.md                        # Repository overview (this file)
├── THIRD_PARTY_NOTICES.md           # Upstream open-source attributions & licenses
├── .agents/skills/                  # On-demand skills (Superpowers, Ponytail, Graphify, genOS commands)
├── .cursor/rules/                   # Cursor IDE rules (genos, ponytail, graphify, Agency Agents)
├── brain/                           # Self-hosted Project Brain tracking genOS itself
│   ├── 00_PROJECT.md                # Intent, scope, architecture constraints
│   ├── 20_PROGRESS.yaml             # Cold-start execution RAM
│   ├── 30_DECISIONS.md              # Architectural Decision Records (ADRs)
│   ├── 40_BACKLOG.md                # Kanban queue for non-milestone work
│   ├── 50_ROADMAP.md                # Milestone definitions and criteria
│   ├── 60_AGENTS.md                 # Approved AI workforce roster
│   └── systems/                     # Modular system documents
├── templates/brain/                 # Pristine (_TBD_) starter Brain templates for new projects
├── profiles/                        # Stack profiles + profiles/templates/mcp-graphify.json
├── guides/                          # User guide (guide.md), workflow prompts, and plans
│   └── scripts/                     # Framework scripts (install_agent.py: Agency Agents auto-installer)
├── docs/superpowers/                # Design specifications and implementation plans
└── integrations/                    # Optional integrations (agency_agents.md)
```

---

## Quickstart

### Day 0: Install Into a New Project

#### Option A: 1-Prompt Auto-Install *(Recommended — Claude Code, Cursor, Antigravity, Codex)*
Open your project in an AI IDE/CLI with terminal access and paste:
```text
Install genOS into a `genOS/` subfolder in this repository from https://github.com/verdenef/genOS/archive/refs/heads/main.zip (using a temporary `_genOS_Temp/` folder, then deleting it after):
1. Copy `AGENTS.md`, `guides/`, `profiles/`, `integrations/`, `templates/`, and `README.md` into `genOS/`.
2. Initialize `genOS/brain/` from `templates/brain/` (do NOT copy the upstream repo's self-hosted `brain/`, `docs/superpowers/`, or `scratch/`).
3. Merge `.agents/` and `.cursor/` into the repository root, and create/append root `CLAUDE.md` so it points to `genOS/AGENTS.md` (preserving any existing files/rules in this repo).
4. Once installed, read `genOS/AGENTS.md` and begin Day 0 setup following `genOS/guides/prompts/setup-init.md`.
```

#### Option B: Manual Download *(for sandboxed or offline setups)*
1. Download or clone `verdenef/genOS` into your repository (either at root or inside a `genOS/` subfolder).
2. Because `brain/` in this upstream repo tracks **genOS itself**, initialize your project's `brain/` directory from [`templates/brain/`](templates/brain/) (or let `setup-init.md` reset it for you).
3. If installing inside a subfolder like `genOS/`: keep `.agents/`, `.cursor/`, and a root `CLAUDE.md` pointing to `genOS/AGENTS.md` at your repo root so Claude Code and Cursor auto-detect them.
4. Open your AI chat and paste [`guides/prompts/setup-init.md`](guides/prompts/setup-init.md).

### Day 1+: Daily Workflow
1. Open a fresh chat and type **`kickoff`**.
2. Review the plan, then copy-paste the generated execution command block into a new session.
3. When done, type **`shutdown`**.

### Upgrading an Existing Project (`v1`, `v2`, or `v3`)
Run **`update`** in chat (or paste [`guides/prompts/update.md`](guides/prompts/update.md) and point to an older `v1`/`v2` `genOS` folder). genOS fetches `main` read-only, verifies whether your files are outdated (stopping cleanly if already up to date), shows an Upgrade & Migration Plan for approval, refreshes core files while strictly shielding `brain/`, `.obsidian/`, custom profiles, project-installed Agency Agents, and source code, and runs `doctor`.

### Optional: Local Code Topology with Graphify
If you work on large codebases, install Graphify locally (powered by PyPI [`graphifyy`](https://pypi.org/project/graphifyy/)):
```bash
uv tool install "graphifyy[mcp]"
graphify extract . --code-only
```
Then ignore `graphify-out/` in `.gitignore`, scope code folders in `.graphifyignore`, and register `graphify-mcp --graph graphify-out/graph.json` from [`profiles/templates/mcp-graphify.json`](profiles/templates/mcp-graphify.json). When unconfigured, genOS agents silently fall back to standard text search.

For the full walkthrough, see the [genOS User Guide](guides/guide.md).  
**For AI agents:** Read and follow [`AGENTS.md`](AGENTS.md).

---

## Core Principles

1. **Zero-Chat-History Recovery:** Agents recover state from the Project Brain alone. No token degradation or context rot.
2. **Deterministic Ownership:** Every piece of project truth has exactly one authoritative file.
3. **Automated Sanity Gates:** Mandatory integrity audits guarantee the Brain is never corrupted.
4. **Local-Only Code Topology:** Graphify AST parsing uses `--code-only` offline without sending code to external LLMs, paired with Grep checks for runtime strings and scene/prefab refs.
5. **On-Disk Skills:** Skills in `.agents/skills/` are read dynamically from disk during `kickoff`—no manual UI settings uploads required.
6. **Zero-App Workforce Automation:** Specialist Agency Agents from `msitarzewski/agency-agents` install directly via `guides/scripts/install_agent.py` upon human approval—requiring only Python 3 stdlib, with zero external tools or desktop apps.

---

## Acknowledgments & Third-Party Licenses

genOS integrates and builds upon these open-source projects:

- **[Superpowers (`obra/superpowers`)](https://github.com/obra/superpowers)** by Jesse Vincent *(MIT License)* — Structured ideation, test-driven execution plans, subagent-driven workflows, and verification gates.
- **[Ponytail (`DietrichGebert/ponytail`)](https://github.com/DietrichGebert/ponytail)** by DietrichGebert *(MIT License)* — The Ladder of Restraint preventing over-engineering and unnecessary code bloat.
- **[Agency Agents (`msitarzewski/agency-agents`)](https://github.com/msitarzewski/agency-agents)** by AgentLand Contributors *(MIT License)* — Specialist domain agent personas fetched on demand via `guides/scripts/install_agent.py`.
- **[Graphify (`Graphify-Labs/graphify`)](https://github.com/Graphify-Labs/graphify)** *(Apache-2.0)* — Local, offline `--code-only` Tree-sitter AST knowledge graphs and MCP tooling (`graphifyy`).

Full license texts and copyright notices are preserved in [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).

---

## License

genOS is released under the [MIT License](LICENSE).
