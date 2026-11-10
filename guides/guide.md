# genOS User Guide

Welcome to genOS! This guide explains how to use the framework day-to-day. genOS is a universal, stack-agnostic AI operating system: it relies on you (the human) to provide intent, while AI agents handle implementation, state tracking, and memory management.

---

## Commands

genOS uses simple keyword commands. Type them in any AI chat where genOS is loaded:

| Command | What it does |
|---------|-------------|
| `kickoff` | Start or resume a session — BOOTs from brain, checks specialist rules, runs optional Graphify topology check, applies Ponytail restraint, and proposes a plan |
| `kickoff <intent>` | Scoped session — e.g., `kickoff let's build the save system today` or `kickoff execute the approved plan: <path>` |
| `shutdown` | End a session — persists state, verifies Sanity Gate checks, records `session_summary` |
| `status` | Quick read-only summary of current project state |
| `doctor` | Diagnose and auto-repair brain integrity issues |
| `batch` | Hands-free autonomous execution with QA verification |
| `update` | Verify if local genOS is outdated, propose an Upgrade & Migration Plan for approval, then refresh core files while strictly shielding the Brain |

You can also `@`-mention the corresponding prompt file (e.g., `@workflow-kickoff.md`) for explicit confirmation that the workflow is loaded.

---

## The Unified AI Engineering Stack

genOS coordinates five complementary disciplines into one frictionless workflow:

| Layer | System | Responsibility |
|:---|:---|:---|
| **1. Memory & State** | **genOS** | Project Brain, zero-history recovery, milestone criteria, and atomic SHUTDOWN gates. |
| **2. Specialist Identity** | **Agency Agents** | Domain-specific engineering rules (e.g. `unity-architect`, `backend-architect`) verified before planning. Auto-installed via `guides/scripts/install_agent.py` upon human approval (zero-app Python stdlib installer). |
| **3. Code Topology *(Optional)*** | **Graphify** | Local `--code-only` Tree-sitter AST call graphs (`graphifyy[mcp]`) for instant caller/callee queries. |
| **4. Senior Restraint** | **Ponytail** | The Ladder of Restraint (YAGNI, reuse, stdlib, 1-liner) cuts over-engineering before writing code. |
| **5. Execution Rigor** | **Superpowers** | Test-driven development, subagent-driven task plans, copy-paste handoffs, and verification before completion. |

You do not need to invoke five separate tools. Typing `kickoff` automatically engages the entire stack (and skips Graphify silently if unconfigured).

---

## Day 0: Setup & Initialization

Before you can use genOS for daily development, initialize it for your specific project:

1. **Clean Starter Brain:** Because `brain/` inside the upstream genOS repo tracks genOS itself, copy the clean `_TBD_` files from `templates/brain/` into your project's `brain/` directory (the setup wizard also verifies this).
2. **Root Discovery (if placed in a subfolder like `genOS/`):** Keep `.agents/`, `.cursor/`, and a root `CLAUDE.md` pointing to `genOS/AGENTS.md` at the repository root.

### Repository Structure

```
genOS/
├── AGENTS.md                        # Universal kernel — authoritative operational rules
├── CLAUDE.md                        # Claude Code entry point (points to AGENTS.md)
├── README.md                        # Repository overview
├── .agents/skills/                  # On-demand skills (Superpowers, Ponytail, Graphify, genOS commands)
├── .cursor/rules/                   # Cursor IDE rules (genos, ponytail, graphify, Agency Agents)
├── brain/                           # Self-hosted Project Brain tracking genOS itself
├── templates/brain/                 # Pristine (_TBD_) starter Brain templates for new projects
├── profiles/                        # Stack profiles + profiles/templates/mcp-graphify.json
├── guides/                          # User guide (guide.md), workflow prompts, and plans
│   └── scripts/                     # Framework scripts (install_agent.py: Agency Agents auto-installer)
├── docs/superpowers/                # Design specifications and implementation plans
└── integrations/                    # Optional integrations (agency_agents.md)
```

### The All-in-One Setup Wizard

Once genOS is inside your project repository, open a chat with your AI agent and paste:

**`guides/prompts/setup-init.md`**

This interactive wizard guides you through:
1. **Stack Profile Selection:** Detects your stack and suggests a profile from `profiles/`.
2. **Project Brain Setup:** Asks for your vision, initializes `brain/00_PROJECT.md`, proposes milestones.
3. **Runtime Tooling / MCP:** Configures live runtime MCP servers for your stack (including optional `graphify-mcp`).
4. **AI Workforce & Skills:** Recommends specialist AI agent roles from `msitarzewski/agency-agents`. Upon human approval, automatically installs them via `guides/scripts/install_agent.py` into `.agents/skills/` and `.cursor/rules/` without any external desktop app, then confirms Ponytail, Graphify, and Superpowers skills.
5. **Doctor Check & Handoff:** Runs integrity check and directs you to start coding in a fresh session.

---

## The Daily Workflow

AI agents have no chat history. Every time you start a new conversation, the agent recovers state exclusively from the Project Brain.

### 1. Starting Work (`kickoff`)

Open a new session and type `kickoff`. The agent will:
- BOOT from the brain and recover full project context
- Read active specialist agent files (`Hard Persona Gate`) and cite 2–3 governing rules
- Optionally verify Graphify code graph freshness and inspect callers/dependencies
- Prune unnecessary complexity via Ponytail's Ladder of Restraint
- Propose a test-driven plan, recommend a **Model Tier** (**Flagship** / **Balanced** / **Fast**), and print **copy-pasteable execution command blocks**
- Wait for your approval before writing code

### 2. Execution

Once you approve the plan, start a fresh execution session and paste one of the handoff command blocks (standard sequential or `subagent-driven-development`).

### 3. Ending Work (`shutdown`)

Type `shutdown`. The agent will:
- Update the roadmap, progress, and system documents
- Run the mandatory Sanity Gate
- Persist a self-contained `session_summary` and clear or retain `working_on` appropriately
- Instruct you to close the chat

### 4. Next Session

Open a new session. Type `kickoff`. The agent picks up exactly where you left off.

> **Always prefer a new session over compacting.** genOS is designed for zero-history recovery — a fresh BOOT with a clean context window produces better results than a compacted history.

### 5. Autonomous Batch Development

Type `batch` for hands-free execution. The agent alternates between a Builder persona and an adversarial QA Auditor with a 2-retry self-healing budget. Requires a QA agent in `brain/60_AGENTS.md`.

### 6. Diagnostics

Type `doctor` to scan all brain files, auto-repair issues, and output a health report.

---

## Optional: Code Topology with Graphify

For medium-to-large codebases, Graphify (PyPI `graphifyy`) maps classes, methods, and call edges locally so agents don't waste tokens hunting across files:

1. **Install once per machine:**
   ```bash
   uv tool install "graphifyy[mcp]"
   ```
2. **Scope & build locally (offline, no API key):**
   - Create a `.graphifyignore` at repo root to restrict parsing to your source folders (excluding third-party packs, docs, and builds).
   - Add `graphify-out/` to `.gitignore`.
   - Build the initial graph: `graphify extract . --code-only`
   - Refresh incrementally after code edits: `graphify update .`
3. **Wire MCP (optional alongside CLI `graphify explain`):**
   - Use [`profiles/templates/mcp-graphify.json`](profiles/templates/mcp-graphify.json) in `.mcp.json` / `.cursor/mcp.json` (for Claude Code / Cursor).
   - For standalone desktop apps launched outside a project folder (like Claude Desktop's Chat tab), point `command` and `--graph` to their absolute paths.
4. **Important Limit:** Code graphs are syntactic—agents still run `grep` for string-based lookups (`GameObject.Find`, `FindProperty`, menu paths, scene/prefab files) and Grep-confirm `INFERRED` edges.

---

## Tool Setup (Bootstrapping)

genOS commands work when the agent knows the kernel (`AGENTS.md`) exists. Skills in `.agents/skills/` are read directly off disk during `kickoff`—you do **not** need to upload them manually into Claude settings.

| Your tool | One-time setup | Then just type... |
|-----------|---------------|-------------------|
| **Antigravity** | Nothing — auto-loads `AGENTS.md` | `kickoff` |
| **Cursor** | Keep `.cursor/rules/genos.mdc` (`alwaysApply: true`) at repo root | `kickoff` |
| **Claude Code** | Keep `CLAUDE.md` pointing to `AGENTS.md` at repo root | `kickoff` |
| **Claude Desktop** | Use `.mcp.json` in the Code tab, or add `AGENTS.md` + absolute MCP paths for Chat tab | `kickoff` |
| **Other** (with file access) | Type `Read AGENTS.md and kickoff` | Plain text |

---

## Prompt Reference

Prompt files are retained as detailed protocol references and alternative triggers:

| File | Command Equivalent | Purpose |
|:---|:---|:---|
| `setup-init.md` | *(Day 0 only — paste)* | One-time interactive setup wizard |
| `update.md` | `update` | Safely update genOS framework |
| `workflow-kickoff.md` | `kickoff` | Start/resume development session |
| `workflow-shutdown.md` | `shutdown` | End session, persist state |
| `workflow-batch.md` | `batch` | Autonomous multi-task execution |

---

## Obsidian Integration

genOS is natively compatible with **Obsidian**. Open your `brain/` folder as an Obsidian Vault for:
- **Visual Graph Mapping:** See how systems, milestones, and decisions connect via `[[wikilinks]]` (`brain/systems/` supports flat files or 1-level category subfolders).
- **Properties UI:** Edit YAML frontmatter and status fields cleanly.
- **Human-AI Separation:** Plan and direct in Obsidian; let AI execute in your IDE.

---

## Maintenance & Upgrades

### Upgrading genOS

When a new version of genOS is released, type `update` (or `@update.md`)—or paste [`guides/prompts/update.md`](prompts/update.md) and point to a legacy `v1`/`v2` `genOS` folder. genOS fetches `main` read-only, checks whether your installation is outdated (stopping cleanly if already current), shows an Upgrade & Migration Plan for approval, refreshes core files (`AGENTS.md`, `guides/`, `profiles/`, root `CLAUDE.md`, core skills/rules), strictly shields your Project Brain and project-installed Agency Agents, and runs Doctor using the updated `AGENTS.md`.

### Standalone Reconfiguration

- **Tooling / MCP:** `kickoff tooling`
- **Workforce:** `kickoff workforce` (or query and install agents directly with `python guides/scripts/install_agent.py --list [keyword]` and `python guides/scripts/install_agent.py <category>/<agent>`)
