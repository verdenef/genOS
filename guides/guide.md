# genOS User Guide

Welcome to genOS! This guide explains how to use the framework day-to-day. genOS is a universal, stack-agnostic AI operating system: it relies on you (the human) to provide intent, while the AI agents handle implementation, state tracking, and memory management.

---

## Day 0: Setup & Initialization

Before you can use genOS for daily development, it needs to be initialized for your specific project.

### 1. The All-in-One Setup Wizard (Recommended)

Once you have placed the `genOS` folder inside your project repository, open a chat with your AI agent in your IDE (e.g. Cursor, Antigravity, Claude Code) and paste:

**`guides/prompts/setup-init.md`**

This interactive wizard guides you through 4 seamless phases:
1. **Stack Profile Selection:** Inspects your repo, detects whether you're building a blank or existing project, and suggests a curated profile from `profiles/` (e.g., `web-fullstack`, `backend-services`, `mobile`, `ai-data`, `cli-system`, or `gamedev`).
2. **Project Brain Setup:** Asks for your high-level vision, initializes `brain/00_PROJECT.md`, proposes milestones for `brain/50_ROADMAP.md`, and (for existing projects) reverse-engineers code into starter `brain/systems/*.md`.
3. **Runtime Tooling / MCP:** Proposes and configures the live runtime MCP servers (e.g., Playwright, Database, Docker, Engine) recommended for your stack.
4. **AI Workforce (Optional):** Recommends tailored specialist AI agent roles from Agency Agents to populate `brain/60_AGENTS.md`.
5. **Doctor Check & Handoff:** Runs the automated integrity check and instructs you to start coding.

---

### Standalone Configuration Utilities

If you ever need to reconfigure tooling or workforce independently later:
* **Tooling / MCP Reconfiguration:** `guides/prompts/setup-tooling.md`
* **Workforce Reconfiguration:** `guides/prompts/setup-workforce.md`
* **Framework Upgrades:** `guides/prompts/setup-04-framework-upgrade.md`

---

## The Daily Workflow

AI agents have no chat history. Every time you start a new conversation or switch IDEs, the agent recovers state exclusively from the Project Brain (`brain/`).

To maintain flawless synchronization, genOS uses a strict **BOOT** and **SHUTDOWN** cycle.

### 1. Starting Work (Milestone Kickoff)
When you are ready to begin working on a milestone, open a fresh chat with your AI agent and paste:

**`guides/prompts/workflow-01-kickoff.md`**

The AI will BOOT from the Brain, summarize the active milestone from `50_ROADMAP.md`, and propose an implementation plan for your approval before modifying any code.

### 2. Implementation
Once you approve the plan, the agent writes code and modifies project files. You can chat back and forth normally during this phase.

### 3. Context Switching (Changing IDEs mid-session)
If you switch IDEs (e.g., from Cursor to Antigravity) in the middle of a task, open a chat in the new IDE and paste:

**`guides/prompts/workflow-03-resume-session.md`**

The AI will read execution RAM (`20_PROGRESS.yaml`) and summarize exactly where you left off, allowing you to resume immediately.

### 4. Ending Work (Milestone Shutdown)
When a milestone is complete and tests pass, you must save state back to the Brain before closing the chat:

**`guides/prompts/workflow-02-shutdown.md`**

The AI updates `50_ROADMAP.md`, logs execution state to `20_PROGRESS.yaml`, updates affected `brain/systems/` documents, and runs the mandatory **Sanity Gate** to guarantee zero corruption.

### 5. Autonomous Batch Development (Hands-Free Execution)
If you want an advanced AI model (e.g. Fable 5, Claude 3.5 Sonnet in Cursor Composer or Agent mode) to execute multiple tasks or milestones in an uninterrupted loop without pausing to ask for permission:

**`guides/prompts/workflow-autonomous-batch.md`**

- **Pre-flight Safety Gate:** Strictly requires a designated QA/Auditor agent in `brain/60_AGENTS.md` before code generation begins.
- **Dual-Persona Cycle:** Alternates between a Specialist Builder and an adversarial QA Auditor with a 2-retry self-healing budget.
- **Atomic Brain Persistence:** Saves state to `brain/systems/`, updates the roadmap/backlog, and passes the Sanity Gate after every completed item.
- **Smart Backlog Clustering:** In `TARGET_SCOPE: AUTO_RECOMMENDED` mode, automatically selects 2–4 cohesive backlog tasks matching the active project phase.

### 6. Diagnostics & Brain Doctor (On-Demand)
If your Brain ever feels desynced, you had an unexpected IDE crash, or an agent made an invalid edit, paste:

**`guides/prompts/workflow-doctor.md`**

The Brain Doctor inspects all 6 brain files, repairs syntax and index mismatches, and outputs a complete health table.

---

## 7. Obsidian UI Integration

genOS is designed to be fully compatible with **Obsidian**. By opening the `genOS/brain/` folder (or your repository root) as an Obsidian Vault, you can:
- **Visualize the Project Graph:** Every `[[wikilink]]` between systems, milestones, and decisions is mapped visually.
- **Edit Properties Easily:** Use Obsidian's properties interface to change metadata.
- **Separate Human and AI Workspaces:** Use Obsidian to plan, organize, and direct the project as the Human Director, while your AI agent executes the actual code in Cursor/Antigravity.

**Upgrading Legacy Projects to Obsidian:**
If you upgraded an older genOS project that didn't use `[[wikilinks]]` originally, your Graph View might look empty because your systems use plain-text references. To fix this, open a chat in your project and run this one-time migration prompt:
> *"Please review `50_ROADMAP.md`, `30_DECISIONS.md`, and all `brain/systems/*.md`. Find any plain-text mentions of systems, milestones, or decisions, and intelligently convert them into Obsidian `[[wikilinks]]` so my Graph View connects properly."*

---

## Maintenance & Upgrades

### Upgrading genOS
1. Download the latest genOS release.
2. Extract it into your repository as `_genOS_Update/`.
3. Paste: **`guides/prompts/setup-04-framework-upgrade.md`**
4. The AI will selectively upgrade your kernel (`AGENTS.md`) and tools while preserving your project's `brain/` data.
