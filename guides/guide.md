# genOS User Guide

Welcome to genOS! This guide explains how to use the framework day-to-day. genOS is a universal, stack-agnostic AI operating system: it relies on you (the human) to provide intent, while the AI agents handle implementation, state tracking, and memory management.

---

## Commands

genOS uses simple keyword commands. Type them in any AI chat where genOS is loaded:

| Command | What it does |
|---------|-------------|
| `kickoff` | Start or resume a development session — BOOTs from brain, proposes plan |
| `kickoff <intent>` | Scoped session — e.g., `kickoff let's build the save system today` |
| `shutdown` | End a session — persists state, runs integrity checks |
| `status` | Quick read-only summary of current project state |
| `doctor` | Diagnose and auto-repair brain integrity issues |
| `batch` | Hands-free autonomous execution with QA verification |

You can also `@`-mention the corresponding prompt file (e.g., `@workflow-kickoff.md`) for explicit confirmation that the workflow is loaded.

---

## Day 0: Setup & Initialization

Before you can use genOS for daily development, it needs to be initialized for your specific project.

### The All-in-One Setup Wizard

Once you have placed the `genOS` folder inside your project repository, open a chat with your AI agent and paste:

**`guides/prompts/setup-init.md`**

This interactive wizard guides you through:
1. **Stack Profile Selection:** Detects your stack and suggests a profile from `profiles/`.
2. **Project Brain Setup:** Asks for your vision, initializes `brain/00_PROJECT.md`, proposes milestones.
3. **Runtime Tooling / MCP:** Configures live runtime MCP servers for your stack.
4. **AI Workforce (Optional):** Recommends specialist AI agent roles.
5. **Doctor Check & Handoff:** Runs integrity check and directs you to start coding.

---

## The Daily Workflow

AI agents have no chat history. Every time you start a new conversation, the agent recovers state exclusively from the Project Brain.

### 1. Starting Work

Open a new session and type `kickoff`. The agent will:
- BOOT from the brain and recover full project context
- Summarize where you left off (if mid-milestone) or propose a new plan
- Load specialist agent personas and cite their rules
- Wait for your approval before writing code

### 2. Implementation

Once you approve the plan, the agent writes code and modifies project files. Chat normally during this phase.

### 3. Ending Work

Type `shutdown`. The agent will:
- Update the roadmap, progress, and system documents
- Run the mandatory Sanity Gate (18-point integrity audit)
- Instruct you to close the chat

### 4. Next Session

Open a new session. Type `kickoff`. The agent picks up exactly where you left off.

> **Always prefer a new session over compacting.** genOS is designed for zero-history recovery — a fresh BOOT with a clean context window produces better results than a compacted history.

### 5. Autonomous Batch Development

Type `batch` for hands-free execution. The agent alternates between a Builder persona and an adversarial QA Auditor with a 2-retry self-healing budget. Requires a QA agent in `brain/60_AGENTS.md`.

### 6. Diagnostics

Type `doctor` to scan all brain files, auto-repair issues, and output a health report.

---

## Tool Setup (Bootstrapping)

genOS commands work when the agent knows the kernel (`AGENTS.md`) exists.

| Your tool | One-time setup | Then just type... |
|-----------|---------------|-------------------|
| **Antigravity** | Nothing — already auto-loads `AGENTS.md` | `kickoff` |
| **Cursor** | Add `.cursor/rules/genos.mdc` with `alwaysApply: true` | `kickoff` |
| **Claude Code** | Add `Read and follow AGENTS.md.` to `CLAUDE.md` | `kickoff` |
| **Claude Desktop** | Add `AGENTS.md` as Project Knowledge | `kickoff` |
| **Other** (with file access) | Type `Read AGENTS.md and kickoff` | 6 words, not 30 lines |

---

## Prompt Reference

Prompt files are retained as detailed protocol references and alternative triggers:

| File | Command Equivalent | Purpose |
|:---|:---|:---|
| `setup-init.md` | *(Day 0 only — paste)* | One-time interactive setup wizard |
| `setup-upgrade.md` | *(paste)* | Safely update genOS framework |
| `workflow-kickoff.md` | `kickoff` | Start/resume development session |
| `workflow-shutdown.md` | `shutdown` | End session, persist state |
| `workflow-batch.md` | `batch` | Autonomous multi-task execution |

---

## Obsidian Integration

genOS is natively compatible with **Obsidian**. Open the `genOS/brain/` folder as an Obsidian Vault for:
- **Visual Graph Mapping:** See how systems, milestones, and decisions connect via `[[wikilinks]]`.
- **Properties UI:** Edit YAML frontmatter and status fields via a clean UI.
- **Human-AI Separation:** Plan and direct in Obsidian; let AI execute in your IDE.

---

## Maintenance & Upgrades

### Upgrading genOS

When a new version of genOS is released, paste `guides/prompts/setup-upgrade.md` to safely update the framework while preserving your project's Brain.

### Standalone Reconfiguration

- **Tooling / MCP:** `kickoff tooling`
- **Workforce:** `kickoff workforce`
