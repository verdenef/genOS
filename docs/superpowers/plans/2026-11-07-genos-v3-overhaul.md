# genOS v3 Overhaul — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement the genOS v3 overhaul: command system, kernel hardening, prompt consolidation, documentation cleanup, model/session guidance, IDE shortcuts, bootstrapping guide, and repo hygiene.

**Architecture:** Pure-text, zero-dependency modifications to markdown files. No scripts, no binaries, no runtime changes. All work on a new `genos-v3` branch off `genosidian`.

**Tech Stack:** Markdown, YAML, git

## Global Constraints

- genOS remains 100% pure text, zero scripts, zero runtime dependencies
- No brain file schema changes — `brain/` structure is untouched
- Profiles and integrations are untouched
- All changes land on `genos-v3` branch
- No placeholders, TBD, or TODO in any deliverable
- Every file must be self-consistent — no broken cross-references
- Prompt files are retained as reference docs AND alternative triggers (not deleted from existence)

---

### Task 1: Branch Setup & Repo Hygiene

**Files:**
- Delete: `d:/GameOS/Agency_Agents_0.3.0_x64-setup.exe`
- Modify: `d:/GameOS/.gitignore`

**Interfaces:**
- Consumes: Current `genosidian` branch state
- Produces: Clean `genos-v3` branch with no binary bloat, ready for all subsequent tasks

- [ ] **Step 1: Create the `genos-v3` branch**

```bash
git checkout genosidian
git checkout -b genos-v3
```

- [ ] **Step 2: Delete the binary installer**

```bash
git rm "Agency_Agents_0.3.0_x64-setup.exe"
```

- [ ] **Step 3: Update `.gitignore`**

Add `*.exe` to the end of the file. Final contents:

```
.agents/
.cursor/
.obsidian/
*.exe
```

- [ ] **Step 4: Commit**

```bash
git add .gitignore
git commit -m "chore: remove binary installer, add *.exe to gitignore"
```

---

### Task 2: Kernel Overhaul — `AGENTS.md`

This is the largest and most critical task. It modifies the kernel with four new/rewritten sections.

**Files:**
- Modify: `d:/GameOS/AGENTS.md`

**Interfaces:**
- Consumes: [Spec sections 2, 3, 6, 10](file:///d:/GameOS/docs/superpowers/specs/2026-11-05-genos-v3-overhaul-design.md)
- Produces: The authoritative v3 kernel with Commands, hardened BOOT/SHUTDOWN, Model & Session Guidance, and Bootstrapping

- [ ] **Step 1: Add `## Commands` section**

Insert after the `## Multi-agent protocol` section and before `## BOOT sequence`. Full content:

```markdown
## Commands

When the user's message begins with a command keyword below (case-insensitive, optionally followed by context), execute the corresponding protocol. The user does not need to paste a prompt file. Users may also `@`-mention the corresponding prompt file in `guides/prompts/` as an alternative trigger — both paths produce the same result.

**Syntax:** `<command>` or `<command> <user intent>`

When user intent follows the command keyword, it takes priority over default behavior. The agent still executes the full protocol (BOOT, validation, brain reads) but scopes its plan to the user's stated goal. The agent must validate that the intent aligns with the active milestone and roadmap criteria.

| Command | Protocol |
|---------|----------|
| `kickoff` | Run BOOT sequence → summarize project state → identify active milestone → **Hard Persona Gate:** read `60_AGENTS.md`, physically open and read each active agent's full definition file (`.cursor/rules/<agent>.mdc` or `.agents/skills/<agent>/SKILL.md`), cite 2-3 governing rules — do not guess agent rules from memory → propose implementation plan → wait for human approval |
| `shutdown` | Run full SHUTDOWN sequence with mandatory Sanity Gate |
| `doctor` | Run Diagnostic Checklist → auto-repair all fixable issues → output Brain Health Report table |
| `status` | Read `20_PROGRESS.yaml` + active milestone from `50_ROADMAP.md` → present concise summary. No code changes. |
| `batch` | Run Autonomous Batch protocol with `TARGET_SCOPE: AUTO_RECOMMENDED` unless user specifies scope (e.g. `batch M1.2, M1.3`) |

If the message does not match a command, proceed with normal conversation while respecting AGENTS.md rules.

### Kickoff Smart Routing

The `kickoff` command automatically determines session type from brain state:

| Brain state | Agent behavior |
|-------------|---------------|
| `session_summary` exists + `working_on` has items | Resume: "You were mid-work on X. Here's where you left off." |
| `working_on` is empty + `current_milestone` is active | Fresh start: "Active milestone is Mx.y. Here's a plan." |
| Milestone just completed, next milestone exists | Advance: "Mx.y is done. Next up is Mx.z. Here's the plan." |
| User provided intent after `kickoff` | Scoped: Use user's directive as session goal, still validate against roadmap |
```

- [ ] **Step 2: Rewrite `## BOOT sequence`**

Replace the existing BOOT sequence section with the hardened version that includes inline VALIDATE steps. Full replacement content:

```markdown
## BOOT sequence

1. Read this file (`AGENTS.md`)
2. Read `brain/00_PROJECT.md`
   - VALIDATE: If Vision is `_TBD_`, activate Empty Brain Protocol and stop.
3. Read `brain/20_PROGRESS.yaml`
   - VALIDATE: File is parseable YAML. All required keys exist:
     `current_milestone`, `working_on`, `systems_in_scope`, `blocked`,
     `session_summary`, `last_agent`, `last_ide`, `known_issues`
   - VALIDATE: If any key is missing, add it with `null` and log a warning.
4. Read `brain/30_DECISIONS.md` — while the log is small, read **all** non-rejected entries (use Index; skip only clearly irrelevant rejected/superseded noise)
   - VALIDATE: Index table row count matches decision section count.
     If mismatched, log warning but continue (Doctor will repair).
5. Read `brain/50_ROADMAP.md` — Index always; then the section for `PROGRESS.current_milestone` (and its parent program milestone if needed for success criteria)
   - VALIDATE: `current_milestone` from PROGRESS points to a valid milestone ID.
   - VALIDATE: That milestone's status is `active` (not `done`/`cancelled`).
   - If pointer is invalid, log error and ask human which milestone is active.
6. Read `brain/60_AGENTS.md` if it exists, to understand the current approved AI workforce.
7. Read `brain/systems/README.md` (navigation only)
8. Read only `brain/systems/<Name>.md` listed in `systems_in_scope` (plus any system the task directly touches)
   - VALIDATE: Every entry in `systems_in_scope` has a corresponding file.
   - If a file is missing, remove the entry and log a warning.
9. Read `brain/40_BACKLOG.md` if ad-hoc queue context is needed
10. **System Initialization Protocol:** Detect whether `brain/systems/` contains only `README.md` and `SYSTEM.md`. If so, recognize that the project has not yet initialized its systems architecture. Read `00_PROJECT.md`, `50_ROADMAP.md`, and `30_DECISIONS.md`. Propose the initial set of project systems and wait for human approval. Upon approval, generate one system document per approved system using `SYSTEM.md`.
11. **Optional Integrations:** If the human requests an integration (e.g., AI workforce evaluation), read the relevant protocol in `integrations/` and execute it only *after* the roadmap is defined.
12. **If Empty Brain Protocol applies → stop inventing; ask human**
13. Plan against **ROADMAP completion criteria** for `current_milestone` (not chat)
14. Implement (only when intent and required facts exist)
```

- [ ] **Step 3: Rewrite `## SHUTDOWN sequence`**

Replace the existing SHUTDOWN sequence section with the hardened version containing the explicit Sanity Gate checklist. Full replacement content:

```markdown
## SHUTDOWN sequence

Mandatory. Incomplete SHUTDOWN breaks the next agent.

### State Updates
1. Update relevant `brain/systems/<Name>.md` if design intent, invariants, dependencies, or **Status** changed (not for pure code edits)
2. Update `brain/20_PROGRESS.yaml` (execution fields only, including honest `session_summary` and `current_milestone` ID)
3. Record decisions in `brain/30_DECISIONS.md` when applicable; keep Index in sync with entries
4. Update `brain/50_ROADMAP.md` when a milestone is started, completed, cancelled, or its definition changes (status + Index row)
5. Update `brain/40_BACKLOG.md` for ad-hoc queue columns only — never milestone status

### Sanity Gate (Mandatory — Zero Tolerance)

Run every check. If ANY check fails, repair it before completing SHUTDOWN.

**YAML Integrity:**
- [ ] `20_PROGRESS.yaml` parses as valid YAML
- [ ] All required keys present: `current_milestone`, `working_on`, `systems_in_scope`, `blocked`, `session_summary`, `last_agent`, `last_ide`, `known_issues`
- [ ] No unquoted special characters (colons in values, brackets, etc.)
- [ ] `working_on` and `systems_in_scope` are arrays (not strings)

**Milestone Pointer Integrity:**
- [ ] `current_milestone` points to a valid ID in `50_ROADMAP.md`
- [ ] That milestone's status is `active` (not `done`, `planned`, or `cancelled`)
- [ ] If milestone was just completed: old milestone set to `done`, next milestone set to `active`, pointer updated

**Index Synchronization:**
- [ ] Every milestone section header in `50_ROADMAP.md` has a matching Index row
- [ ] Every Index row has a matching section header
- [ ] All statuses in Index match the status in the section body
- [ ] Every decision header in `30_DECISIONS.md` has a matching Index row
- [ ] All decision statuses in Index match their section body

**State Isolation (No Bleed):**
- [ ] `40_BACKLOG.md` has NO "Doing" column or in-progress markers
- [ ] `40_BACKLOG.md` has NO milestone deliverable duplicates
- [ ] `working_on` in PROGRESS contains ONLY items actively being worked on (cleared on SHUTDOWN)
- [ ] No system outside `systems_in_scope` was modified

**System Scopes:**
- [ ] Every entry in `systems_in_scope` has a file in `brain/systems/`
- [ ] `brain/systems/README.md` has NO status column

**Cross-References:**
- [ ] All internal brain file links use `[[wikilink]]` syntax (not `[text](file)`)

### Post-Gate
6. Clear stale `working_on` / `systems_in_scope` for the next agent.
7. Set `last_agent` and `last_ide` (use `cursor`, `antigravity`, or other host name as appropriate).
8. Write self-contained `session_summary`.
9. Brief human summary in chat; durable record is ROADMAP + PROGRESS + Backlog + Decisions.

When advancing milestones: set the finished milestone to `done` in ROADMAP, set the next to `active`, and point `PROGRESS.current_milestone` at the new ID.

If PROJECT intent must change, ask the human first. If a new **program-level** roadmap phase needs invented scope, ask the human first (do not fill `_TBD_` stubs).
```

- [ ] **Step 4: Add `## Doctor Protocol` section**

Insert after the SHUTDOWN sequence section. This absorbs the doctor logic from the prompt file into the kernel:

```markdown
## Doctor Protocol

Run when the user issues the `doctor` command. Perform a comprehensive inspection of all Project Brain files.

### Diagnostic Checklist

1. **YAML Validity (`brain/20_PROGRESS.yaml`):** Verify valid YAML. Confirm all required keys exist. Confirm `working_on` is either `null` or an array. Confirm `systems_in_scope` is an array.
2. **Milestone Pointer Integrity:** Check `current_milestone` points to an actual milestone ID in `50_ROADMAP.md`. Confirm that milestone's status is `active`.
3. **Index Synchronization:** Verify every milestone in `50_ROADMAP.md` has an Index row with matching status. Verify every decision in `30_DECISIONS.md` has an Index row with matching status.
4. **State Isolation:** Confirm `40_BACKLOG.md` has no "Doing" column, no in-progress markers, and no milestone deliverable duplicates. Confirm `00_PROJECT.md` is not empty (unless uninitialized).
5. **System Scopes:** Confirm every entry in `systems_in_scope` has a matching file in `brain/systems/`. Confirm `brain/systems/README.md` has no status column.
6. **Obsidian Compatibility:** Verify all internal brain file cross-references use `[[wikilink]]` syntax.

### Auto-Repair Actions

| Check failure | Repair |
|---------------|--------|
| Missing YAML keys | Add key with `null` default |
| Invalid milestone pointer | Ask human (cannot guess) |
| Index/section desync | Rebuild Index from section headers |
| State bleed (Doing in Backlog) | Remove the invalid column/markers |
| Missing system file for scope entry | Remove from `systems_in_scope` |
| Standard markdown links in brain | Convert to `[[wikilink]]` |
| Stale `working_on` from prior session | Clear to `[]` |

### Output

After diagnostics and repairs, output the Brain Health Report:

| Component | Status | Details |
|:---|:---:|:---|
| `00_PROJECT.md` | [✅ / ⚠️ / ❌] | [Status description] |
| `20_PROGRESS.yaml` | [✅ / ⚠️ / ❌] | [YAML validity & current milestone ID] |
| `30_DECISIONS.md` | [✅ / ⚠️ / ❌] | [Decisions count & index sync status] |
| `40_BACKLOG.md` | [✅ / ⚠️ / ❌] | [Queue health & leakage check] |
| `50_ROADMAP.md` | [✅ / ⚠️ / ❌] | [Milestones count & active milestone status] |
| `brain/systems/` | [✅ / ⚠️ / ❌] | [Systems count & scope verification] |
| Obsidian Links | [✅ / ⚠️ / ❌] | [Standard links found & auto-healed count] |
```

- [ ] **Step 5: Add `## Model & Session Guidance` section**

Insert after the Doctor Protocol section:

```markdown
## Model & Session Guidance

genOS recovers from the Project Brain alone. New sessions are always preferred over compacting — a fresh BOOT with a clean context window produces better results than a compacted history.

### Per-Command Recommendations

| Command | Recommended Model Tier | Session Strategy |
|---------|----------------------|------------------|
| `kickoff` | Mid-tier (e.g. Flash High, Sonnet) | **New session** always |
| `shutdown` | Low-tier (e.g. Flash Low, Haiku) | Continue current session |
| `doctor` | Low-tier (e.g. Flash Low, Haiku) | **New session** if prior session was long |
| `status` | Lowest available | Either — minimal token use |
| `batch` | High-tier (e.g. Opus, Pro) | **New session** always |
| Complex implementation | High-tier (e.g. Opus, Pro) | **New session** after every ~50 exchanges |
| Simple fixes / tweaks | Mid-tier | Continue if context is clean |

### Rules
- After SHUTDOWN, always start a **new session** for the next milestone.
- If context feels degraded (repetition, forgetting instructions), start a new session.
- Never compact as a substitute for SHUTDOWN → new session.
- When presenting recommendations, agents should state: "💡 Recommended: [Model tier] in a [new/continued] session."
```

- [ ] **Step 6: Add `## Bootstrapping` section**

Insert after the Model & Session Guidance section:

```markdown
## Bootstrapping

genOS commands require the agent to know this kernel exists. How this happens depends on the tool.

### Tier 1: Auto-Load (Zero Setup)

IDEs that automatically inject repo-root rules into every session.

| Tool | Mechanism | User action per session |
|------|-----------|----------------------|
| Antigravity | `AGENTS.md` auto-loaded as `<RULE>` | Type `kickoff` |
| Cursor | `.cursor/rules/genos.mdc` with `alwaysApply: true` | Type `kickoff` |
| Claude Code | `CLAUDE.md` references `AGENTS.md` | Type `kickoff` |
| Codex | `AGENTS.md` auto-detected at repo root | Type `kickoff` |

### Tier 2: File Access, No Auto-Load

Tools that can read files but don't auto-inject rules.

| Tool | One-time setup | User action per session |
|------|---------------|----------------------|
| Claude Desktop (with filesystem MCP) | Add `AGENTS.md` as Project Knowledge | Type `kickoff` |
| Grok Bot (with file tools) | Pin `AGENTS.md` path in system prompt | Type `kickoff` |

If no Project/pin support: type `Read AGENTS.md and kickoff`.

### Tier 3: No File Access

Plain web chats without filesystem access cannot read or write brain files. genOS requires filesystem access.
```

- [ ] **Step 7: Verify the full AGENTS.md is internally consistent**

Read the complete file. Verify:
- No duplicate section headers
- Commands table references match section names (BOOT, SHUTDOWN, Doctor Protocol)
- No broken cross-references
- Ownership table is unchanged
- Prohibitions section is unchanged
- All existing sections not mentioned above are preserved exactly

- [ ] **Step 8: Commit**

```bash
git add AGENTS.md
git commit -m "feat(kernel): add command system, hardened BOOT/SHUTDOWN, model guidance, bootstrapping"
```

---

### Task 3: Prompt Consolidation

**Files:**
- Rename: `d:/GameOS/guides/prompts/workflow-01-kickoff.md` → `d:/GameOS/guides/prompts/workflow-kickoff.md`
- Rename: `d:/GameOS/guides/prompts/workflow-02-shutdown.md` → `d:/GameOS/guides/prompts/workflow-shutdown.md`
- Rename: `d:/GameOS/guides/prompts/workflow-autonomous-batch.md` → `d:/GameOS/guides/prompts/workflow-batch.md`
- Rename: `d:/GameOS/guides/prompts/setup-04-framework-upgrade.md` → `d:/GameOS/guides/prompts/setup-upgrade.md`
- Delete: `d:/GameOS/guides/prompts/setup-tooling.md`
- Delete: `d:/GameOS/guides/prompts/setup-workforce.md`
- Delete: `d:/GameOS/guides/prompts/workflow-03-resume-session.md`
- Delete: `d:/GameOS/guides/prompts/setup-obsidian-migration.md`
- Delete: `d:/GameOS/guides/prompts/workflow-doctor.md`

**Interfaces:**
- Consumes: [Spec sections 4.2, 4.3](file:///d:/GameOS/docs/superpowers/specs/2026-11-05-genos-v3-overhaul-design.md)
- Produces: 5 prompt files (down from 10), each marked as reference doc + alternative trigger

- [ ] **Step 1: Rename the 4 prompt files**

```bash
cd guides/prompts
git mv workflow-01-kickoff.md workflow-kickoff.md
git mv workflow-02-shutdown.md workflow-shutdown.md
git mv workflow-autonomous-batch.md workflow-batch.md
git mv setup-04-framework-upgrade.md setup-upgrade.md
```

- [ ] **Step 2: Delete the 5 absorbed prompt files**

```bash
git rm setup-tooling.md
git rm setup-workforce.md
git rm workflow-03-resume-session.md
git rm setup-obsidian-migration.md
git rm workflow-doctor.md
```

- [ ] **Step 3: Update `workflow-kickoff.md`**

Rewrite to serve as both reference documentation and alternative trigger. Absorb resume-session, tooling, workforce, and obsidian-migration functionality. Add a header noting command system:

```markdown
# Kickoff — Reference & Alternative Trigger

> **Primary trigger:** Type `kickoff` in any AI chat where genOS is loaded.
> **Alternative trigger:** `@workflow-kickoff.md` for explicit confirmation.
> **Full protocol definition:** `AGENTS.md` → Commands → `kickoff`

This file provides detailed reference for the kickoff workflow and serves as an alternative trigger mechanism.

---

Begin the next development cycle using genOS.

Follow AGENTS.md exactly.

BOOT the project from the Project Brain.

Determine the active milestone from the Project Brain.

Before writing any code:

1. Summarize your understanding of the current project state.
2. Identify the active milestone.
3. Explain why it is the next milestone.
4. **Hard Persona Gate (Mandatory Tool Call):**
   - Check `brain/60_AGENTS.md` for designated specialist roles.
   - Use your file viewing tool to read the agent's full definition file (e.g., `.agents/skills/<agent>/SKILL.md` or `.cursor/rules/<agent>.mdc`).
   - In your response, explicitly cite the file path you inspected and list 2–3 governing rules or anti-patterns from that skill that will dictate how you implement this milestone.
5. Present a concise implementation plan that strictly adheres to those cited agent rules.
6. Identify any architectural risks or dependencies.
7. Wait for my approval before modifying the implementation.

## Variants

- `kickoff` — standard milestone kickoff (or resume if mid-work)
- `kickoff <intent>` — scoped session with user-directed goal
- `kickoff tooling` — reconfigure MCP servers (reads profile's `recommended_mcps`)
- `kickoff workforce` — reconfigure AI workforce (follows `integrations/agency_agents.md`)

Rules:
- Do not skip BOOT.
- Do not use chat history as project memory.
- Treat the Project Brain as authoritative.
- Do not begin future milestones.
- Only implement the current milestone after approval.
```

- [ ] **Step 4: Update `workflow-shutdown.md`**

Add the reference/trigger header:

```markdown
# Shutdown — Reference & Alternative Trigger

> **Primary trigger:** Type `shutdown` in any AI chat where genOS is loaded.
> **Alternative trigger:** `@workflow-shutdown.md` for explicit confirmation.
> **Full protocol definition:** `AGENTS.md` → SHUTDOWN sequence

This file provides detailed reference for the shutdown workflow and serves as an alternative trigger mechanism.

---
```

Keep the rest of the existing shutdown instructions below the header unchanged.

- [ ] **Step 5: Update `workflow-batch.md`**

Add the reference/trigger header:

```markdown
# Autonomous Batch — Reference & Alternative Trigger

> **Primary trigger:** Type `batch` in any AI chat where genOS is loaded.
> **Alternative trigger:** `@workflow-batch.md` for explicit confirmation.
> **Full protocol definition:** `AGENTS.md` → Commands → `batch`

This file provides detailed reference for the autonomous batch workflow and serves as an alternative trigger mechanism.

---
```

Keep the rest of the existing batch instructions (TARGET_SCOPE config, phases 0-5) below the header unchanged.

- [ ] **Step 6: Update `setup-upgrade.md`**

Add a note that it was renamed:

```markdown
# Framework Upgrade

> Previously `setup-04-framework-upgrade.md`. Renamed for clarity in genOS v3.

---
```

Keep existing content below.

- [ ] **Step 7: Verify all 5 remaining files exist and no deleted files remain**

```bash
ls guides/prompts/
```

Expected: `setup-init.md`, `setup-upgrade.md`, `workflow-kickoff.md`, `workflow-shutdown.md`, `workflow-batch.md`

- [ ] **Step 8: Commit**

```bash
cd ../..
git add guides/prompts/
git commit -m "refactor(prompts): consolidate 10 prompt files to 5, add command system headers"
```

---

### Task 4: Documentation Cleanup — `README.md`

**Files:**
- Modify: `d:/GameOS/README.md`

**Interfaces:**
- Consumes: [Spec section 5.2](file:///d:/GameOS/docs/superpowers/specs/2026-11-05-genos-v3-overhaul-design.md)
- Produces: Trimmed landing page with zero overlap with `guide.md` or `AGENTS.md`

- [ ] **Step 1: Rewrite `README.md`**

Replace entire contents with:

```markdown
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
```

- [ ] **Step 2: Commit**

```bash
git add README.md
git commit -m "docs(readme): trim to landing page, eliminate overlap with guide and kernel"
```

---

### Task 5: Documentation Cleanup — `guides/guide.md`

**Files:**
- Modify: `d:/GameOS/guides/guide.md`

**Interfaces:**
- Consumes: [Spec section 5.3](file:///d:/GameOS/docs/superpowers/specs/2026-11-05-genos-v3-overhaul-design.md)
- Produces: Updated user guide leading with command system, matching 5-file prompt structure

- [ ] **Step 1: Rewrite `guides/guide.md`**

Replace entire contents with:

```markdown
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
```

- [ ] **Step 2: Commit**

```bash
git add guides/guide.md
git commit -m "docs(guide): rewrite with command system, bootstrapping table, consolidated prompt reference"
```

---

### Task 6: IDE Shortcuts — Antigravity & Cursor

**Files:**
- Create: `d:/GameOS/.agents/skills/genos-kickoff/SKILL.md`
- Create: `d:/GameOS/.agents/skills/genos-shutdown/SKILL.md`
- Create: `d:/GameOS/.agents/skills/genos-doctor/SKILL.md`
- Create: `d:/GameOS/.cursor/rules/genos-kickoff.mdc`
- Create: `d:/GameOS/.cursor/rules/genos-shutdown.mdc`
- Create: `d:/GameOS/.cursor/rules/genos-doctor.mdc`
- Create: `d:/GameOS/.cursor/rules/genos.mdc`

**Interfaces:**
- Consumes: [Spec section 2.2, 10](file:///d:/GameOS/docs/superpowers/specs/2026-11-05-genos-v3-overhaul-design.md)
- Produces: IDE-native shortcuts that delegate to the kernel

- [ ] **Step 1: Create Antigravity skills**

`d:/GameOS/.agents/skills/genos-kickoff/SKILL.md`:
```markdown
---
name: genos-kickoff
description: "Start or resume a genOS development session. Execute the kickoff command from AGENTS.md."
---

# genOS Kickoff

Execute the `kickoff` command as defined in `AGENTS.md` → Commands.

Read `AGENTS.md` and follow the `kickoff` protocol exactly.
```

`d:/GameOS/.agents/skills/genos-shutdown/SKILL.md`:
```markdown
---
name: genos-shutdown
description: "End a genOS development session. Execute the shutdown command from AGENTS.md."
---

# genOS Shutdown

Execute the `shutdown` command as defined in `AGENTS.md` → SHUTDOWN sequence.

Read `AGENTS.md` and follow the SHUTDOWN protocol exactly, including the mandatory Sanity Gate.
```

`d:/GameOS/.agents/skills/genos-doctor/SKILL.md`:
```markdown
---
name: genos-doctor
description: "Diagnose and repair genOS Project Brain integrity issues."
---

# genOS Doctor

Execute the `doctor` command as defined in `AGENTS.md` → Doctor Protocol.

Read `AGENTS.md` and follow the Doctor Protocol exactly, including auto-repair actions and the Brain Health Report output.
```

- [ ] **Step 2: Create Cursor rules**

`d:/GameOS/.cursor/rules/genos.mdc`:
```markdown
---
description: "genOS kernel loader — ensures AGENTS.md is read on every session."
alwaysApply: true
---

Read and follow `AGENTS.md` in the project root. It defines the genOS operating system, including commands (`kickoff`, `shutdown`, `doctor`, `status`, `batch`), BOOT/SHUTDOWN protocols, and all project memory rules.
```

`d:/GameOS/.cursor/rules/genos-kickoff.mdc`:
```markdown
---
description: "genOS kickoff — start or resume a development session."
alwaysApply: false
---

Execute the `kickoff` command as defined in `AGENTS.md` → Commands. Follow the full BOOT and kickoff protocol.
```

`d:/GameOS/.cursor/rules/genos-shutdown.mdc`:
```markdown
---
description: "genOS shutdown — end a development session and persist state."
alwaysApply: false
---

Execute the `shutdown` command as defined in `AGENTS.md` → SHUTDOWN sequence. Include the mandatory Sanity Gate.
```

`d:/GameOS/.cursor/rules/genos-doctor.mdc`:
```markdown
---
description: "genOS doctor — diagnose and repair brain integrity."
alwaysApply: false
---

Execute the `doctor` command as defined in `AGENTS.md` → Doctor Protocol. Include auto-repair and Brain Health Report.
```

- [ ] **Step 3: Commit**

Note: These files are in `.gitignore`'d directories (`.agents/`, `.cursor/`). They will be committed via force-add or by temporarily adjusting gitignore, OR they are kept as local-only IDE configuration. Decide based on project convention.

If the project wants these tracked (for team sharing):
```bash
git add -f .agents/skills/genos-kickoff/SKILL.md
git add -f .agents/skills/genos-shutdown/SKILL.md
git add -f .agents/skills/genos-doctor/SKILL.md
git add -f .cursor/rules/genos.mdc
git add -f .cursor/rules/genos-kickoff.mdc
git add -f .cursor/rules/genos-shutdown.mdc
git add -f .cursor/rules/genos-doctor.mdc
git commit -m "feat(ide): add Antigravity skills and Cursor rules for genOS commands"
```

If the project wants these as user-local only, skip the commit — they live outside git.

---

### Task 7: Final Verification & Cross-Reference Audit

**Files:**
- All files modified in Tasks 1-6

**Interfaces:**
- Consumes: All prior task outputs
- Produces: Verified, consistent `genos-v3` branch ready for PR

- [ ] **Step 1: Verify file structure**

```bash
# Prompts should be exactly 5 files
ls guides/prompts/
# Expected: setup-init.md  setup-upgrade.md  workflow-batch.md  workflow-kickoff.md  workflow-shutdown.md

# Binary should be gone
ls *.exe
# Expected: no results

# .gitignore should have *.exe
cat .gitignore
```

- [ ] **Step 2: Verify AGENTS.md sections**

Read the full `AGENTS.md` and confirm these sections exist in order:
1. Ownership table
2. Semantics
3. Empty Brain Protocol
4. Missing context protocols
5. Knowledge boundaries
6. File Linking
7. Zero-history recovery
8. Multi-agent protocol
9. **Commands** ← NEW
10. BOOT sequence ← HARDENED
11. SHUTDOWN sequence ← HARDENED
12. **Doctor Protocol** ← NEW
13. **Model & Session Guidance** ← NEW
14. **Bootstrapping** ← NEW
15. Location-Agnostic Pathing
16. Optional Integrations
17. Runtime / Tooling MCP
18. Systems template
19. Decision template
20. Roadmap milestone template
21. Prohibitions

- [ ] **Step 3: Cross-reference check**

Verify:
- `README.md` links to `guides/guide.md` (not to deleted prompt files)
- `guide.md` references correct prompt file names (no old numbered names)
- `guide.md` command table matches `AGENTS.md` Commands table
- `AGENTS.md` Ownership table is unchanged
- No reference to `workflow-01-kickoff.md`, `workflow-02-shutdown.md`, `workflow-03-resume-session.md`, `setup-02-mcp.md`, `setup-03-workforce.md`, `setup-04-framework-upgrade.md`, `workflow-autonomous-batch.md`, or `workflow-doctor.md` exists anywhere in tracked files (only new names used)

```bash
git grep -l "workflow-01-kickoff\|workflow-02-shutdown\|workflow-03-resume\|setup-04-framework\|workflow-autonomous-batch\|workflow-doctor\|setup-tooling\|setup-workforce\|setup-obsidian-migration" -- ":(exclude).git"
```

Expected: no results (or only the spec file which is historical documentation)

- [ ] **Step 4: Final commit (if any fixes needed)**

```bash
git add -A
git commit -m "fix: resolve cross-reference issues from v3 overhaul"
```

- [ ] **Step 5: Push branch for review**

```bash
git push -u origin genos-v3
```
