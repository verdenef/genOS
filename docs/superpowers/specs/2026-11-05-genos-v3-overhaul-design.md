# genOS v3 Overhaul — Design Spec

**Date:** 2026-11-05
**Status:** Proposed
**Branch:** `genos-v3` (off `genosidian`)

---

## 1. Executive Summary

genOS v3 is a comprehensive quality-of-life and robustness overhaul addressing four areas:

1. **Command System:** Eliminate prompt copy-pasting with universal keyword triggers in `AGENTS.md` + IDE-native shortcuts.
2. **Kernel Hardening:** Bulletproof BOOT/SHUTDOWN with strict verification checklists against desync, YAML corruption, and state bleed.
3. **Streamlining & Cleanup:** Consolidate 10 prompt files → 5, remove repo bloat, eliminate documentation overlap.
4. **Model & Session Guidance:** Teach genOS to recommend the right model tier and session strategy per workflow.

**Core constraint:** genOS remains 100% pure text, zero scripts, zero runtime dependencies.

---

## 2. Command System

### 2.1 Universal Keyword Triggers (in `AGENTS.md`)

A new `## Commands` section in `AGENTS.md`. When the user's message is one of these keywords (case-insensitive, alone or with optional context), the agent executes the corresponding protocol inline:

| Keyword | Protocol | Description |
|---------|----------|-------------|
| `kickoff` | BOOT → state summary → load Agency Agents → propose plan → await approval | Start a development cycle |
| `shutdown` | Full SHUTDOWN sequence with Sanity Gate | End a development cycle |
| `doctor` | Diagnostic checklist → auto-repair → health table | Brain integrity check |
| `status` | Read-only PROGRESS + active milestone summary | Quick state check |
| `batch` | Autonomous batch workflow (pre-flight → dual-persona → atomic persistence) | Hands-free execution |

**Keyword detection rule (added to AGENTS.md):**

```markdown
## Commands

When the user's message matches a command keyword below (case-insensitive, optionally followed by context),
execute the corresponding protocol. The user does not need to paste a prompt file.

| Command | Protocol |
|---------|----------|
| `kickoff` | Run BOOT sequence → summarize project state → identify active milestone → **Hard Persona Gate:** read `60_AGENTS.md`, physically open and read each active agent's full definition file (`.cursor/rules/<agent>.mdc` or `.agents/skills/<agent>/SKILL.md`), cite 2-3 governing rules — do not guess agent rules from memory → propose implementation plan → wait for human approval |
| `shutdown` | Run SHUTDOWN sequence (see below) with mandatory Sanity Gate |
| `doctor` | Run Diagnostic Checklist (see below) → auto-repair → output Brain Health Report |
| `status` | Read `20_PROGRESS.yaml` + active milestone from `50_ROADMAP.md` → present concise summary. No code changes. |
| `batch` | Run Autonomous Batch protocol (see below) with TARGET_SCOPE: AUTO_RECOMMENDED unless user specifies scope |

If the message does not match a command, proceed with normal conversation while respecting AGENTS.md rules.

**Syntax:** `<command>` or `<command> <user intent>`

When user intent follows the command keyword, it takes priority over default behavior.
The agent still executes the full protocol (BOOT, validation, brain reads) but scopes
its plan to the user's stated goal. The agent must still validate that the intent
aligns with the active milestone and roadmap criteria.
```

### 2.2 IDE-Native Shortcuts

**Antigravity** (`.agents/skills/`):
- `genos-kickoff/SKILL.md` — thin wrapper: "Execute the `kickoff` command defined in `AGENTS.md`."
- `genos-shutdown/SKILL.md` — thin wrapper for `shutdown`
- `genos-doctor/SKILL.md` — thin wrapper for `doctor`

**Cursor** (`.cursor/rules/`):
- `genos-kickoff.mdc` — equivalent thin wrapper
- `genos-shutdown.mdc` — equivalent thin wrapper
- `genos-doctor.mdc` — equivalent thin wrapper

These are **convenience entry points only**. The canonical protocol definition lives in `AGENTS.md`. No logic duplication.

### 2.3 What Happens to `guides/prompts/`

Prompt files are **retained as human-readable reference documentation AND as an alternative trigger mechanism**. Users can still `@workflow-kickoff.md` to trigger a workflow — this gives explicit visual confirmation that the genOS protocol is loaded. Both paths (keyword and `@` mention) produce the same result.

The `guides/guide.md` user manual is updated to say: *"Type `kickoff` in any AI chat, or `@workflow-kickoff.md` for explicit confirmation. For protocol details, see `guides/prompts/`."*

---

## 3. Kernel & Brain Hardening

### 3.1 Hardened BOOT Sequence

Replace the current BOOT steps with a strict numbered checklist that includes validation at each step:

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
4. Read `brain/30_DECISIONS.md`
   - VALIDATE: Index table row count matches decision section count.
     If mismatched, log warning but continue (Doctor will repair).
5. Read `brain/50_ROADMAP.md` — Index always; then the section for
   `PROGRESS.current_milestone` (and its parent if needed)
   - VALIDATE: `current_milestone` from PROGRESS points to a valid milestone ID.
   - VALIDATE: That milestone's status is `active` (not `done`/`cancelled`).
   - If pointer is invalid, log error and ask human which milestone is active.
6. Read `brain/60_AGENTS.md` if it exists.
7. Read `brain/systems/README.md` (navigation only)
8. Read only `brain/systems/<Name>.md` listed in `systems_in_scope`
   - VALIDATE: Every entry in `systems_in_scope` has a corresponding file.
   - If a file is missing, remove the entry and log a warning.
9. Read `brain/40_BACKLOG.md` if ad-hoc queue context is needed
10. System Initialization Protocol (if `brain/systems/` has only README.md + SYSTEM.md)
11. If Empty Brain Protocol applies → stop inventing; ask human
12. Plan against ROADMAP completion criteria for `current_milestone`
13. Implement (only when intent and required facts exist)
```

### 3.2 Hardened SHUTDOWN Sequence

Rewrite SHUTDOWN with explicit verification steps:

```markdown
## SHUTDOWN sequence

Mandatory. Incomplete SHUTDOWN breaks the next agent.

### State Updates
1. Update relevant `brain/systems/<Name>.md` if design intent, invariants,
   dependencies, or Status changed.
2. Update `brain/20_PROGRESS.yaml` — execution fields only.
3. Record decisions in `brain/30_DECISIONS.md` when applicable.
4. Update `brain/50_ROADMAP.md` when a milestone is started, completed,
   cancelled, or its definition changes.
5. Update `brain/40_BACKLOG.md` for ad-hoc queue items only.

### Sanity Gate (Mandatory — Zero Tolerance)

Run every check. If ANY check fails, repair it before completing SHUTDOWN.

**YAML Integrity:**
- [ ] `20_PROGRESS.yaml` parses as valid YAML
- [ ] All required keys present: `current_milestone`, `working_on`,
      `systems_in_scope`, `blocked`, `session_summary`, `last_agent`,
      `last_ide`, `known_issues`
- [ ] No unquoted special characters (colons in values, brackets, etc.)
- [ ] `working_on` and `systems_in_scope` are arrays (not strings)

**Milestone Pointer Integrity:**
- [ ] `current_milestone` points to a valid ID in `50_ROADMAP.md`
- [ ] That milestone's status is `active` (not `done`, `planned`, or `cancelled`)
- [ ] If milestone was just completed: old milestone set to `done`,
      next milestone set to `active`, pointer updated

**Index Synchronization:**
- [ ] Every milestone section header in `50_ROADMAP.md` has a matching Index row
- [ ] Every Index row has a matching section header
- [ ] All statuses in Index match the status in the section body
- [ ] Every decision header in `30_DECISIONS.md` has a matching Index row
- [ ] All decision statuses in Index match their section body

**State Isolation (No Bleed):**
- [ ] `40_BACKLOG.md` has NO "Doing" column or in-progress markers
- [ ] `40_BACKLOG.md` has NO milestone deliverable duplicates
- [ ] `working_on` in PROGRESS contains ONLY items actively being worked on
      (cleared on SHUTDOWN)
- [ ] No system outside `systems_in_scope` was modified

**System Scopes:**
- [ ] Every entry in `systems_in_scope` has a file in `brain/systems/`
- [ ] `brain/systems/README.md` has NO status column

**Cross-References:**
- [ ] All internal brain file links use `[[wikilink]]` syntax (not `[text](file)`)

### Post-Gate
6. Clear stale `working_on` / `systems_in_scope` for the next agent.
7. Set `last_agent` and `last_ide`.
8. Write self-contained `session_summary`.
9. Brief human summary in chat.
```

### 3.3 Hardened Doctor

The Doctor checklist in the `doctor` command protocol mirrors the Sanity Gate but adds **auto-repair actions**:

| Check | Auto-Repair |
|-------|-------------|
| Missing YAML keys | Add key with `null` default |
| Invalid milestone pointer | Ask human (cannot guess) |
| Index/section desync | Rebuild Index from section headers |
| State bleed (Doing in Backlog) | Move items to PROGRESS.working_on or remove |
| Missing system file for scope entry | Remove from `systems_in_scope` |
| Standard markdown links in brain | Convert to `[[wikilink]]` |
| Stale `working_on` from prior session | Clear to `[]` |

---

## 4. Prompt Consolidation

### 4.1 Current State (10 files)

```
guides/prompts/
├── setup-init.md
├── setup-04-framework-upgrade.md
├── setup-obsidian-migration.md     ← rarely used, one-time
├── setup-tooling.md                ← subset of setup-init
├── setup-workforce.md              ← subset of setup-init
├── workflow-01-kickoff.md
├── workflow-02-shutdown.md
├── workflow-03-resume-session.md   ← thin, rarely used
├── workflow-autonomous-batch.md
└── workflow-doctor.md
```

### 4.2 Proposed State (5 files)

```
guides/prompts/
├── setup-init.md                   ← KEEP (Day 0 wizard)
├── setup-upgrade.md                ← RENAME from setup-04-framework-upgrade.md
├── workflow-kickoff.md             ← RENAME from workflow-01-kickoff.md
│                                      ABSORB: resume-session (add "resume" variant)
│                                      ABSORB: setup-tooling (add tooling reconfigure section)
│                                      ABSORB: setup-workforce (add workforce reconfigure section)
├── workflow-shutdown.md            ← RENAME from workflow-02-shutdown.md
└── workflow-batch.md               ← RENAME from workflow-autonomous-batch.md
│                                      (doctor is now a command, no standalone file needed)
```

### 4.3 Absorbed Files

| Removed File | Absorbed Into | How |
|-------------|---------------|-----|
| `setup-tooling.md` | `workflow-kickoff.md` | "If the user says `kickoff tooling`, run MCP reconfiguration" |
| `setup-workforce.md` | `workflow-kickoff.md` | "If the user says `kickoff workforce`, run workforce reconfiguration" |
| `workflow-03-resume-session.md` | `workflow-kickoff.md` | Kickoff already reads PROGRESS; resume is just a lighter BOOT |
| `setup-obsidian-migration.md` | `workflow-kickoff.md` | One-time migration absorbed as a BOOT-time auto-detection step |
| `workflow-doctor.md` | `AGENTS.md` (command) | Doctor is now a kernel command; prompt file deleted |

---

## 5. Documentation Cleanup

### 5.1 Scope Delineation (Zero Overlap)

| File | Audience | Scope | Must NOT contain |
|------|----------|-------|------------------|
| `README.md` | Humans (GitHub visitors, new users) | What genOS is, repo structure, quickstart (link to guide), core principles | Workflow details, agent rules, kernel internals |
| `guides/guide.md` | Humans (daily users) | How to use genOS day-to-day: setup, commands, Obsidian, maintenance | Agent behavioral rules, BOOT/SHUTDOWN internals |
| `AGENTS.md` | AI agents | Operational kernel: ownership, BOOT, SHUTDOWN, commands, protocols, prohibitions | User-facing tutorials, marketing copy |

### 5.2 README.md Changes

Trim to:
1. One-paragraph description
2. Repository structure tree
3. "Getting Started" → link to `guides/guide.md`
4. Core principles (4 bullets)
5. Link to `AGENTS.md` for contributors/AI agents

Remove: The entire "Workflow in Action" example section (duplicates guide.md), the Daily Prompt Reference table (belongs in guide.md).

### 5.3 guide.md Changes

Update to:
1. Lead with the **command system**: "Type `kickoff` to start, `shutdown` to finish, `doctor` to diagnose."
2. Reference prompt files as "detailed protocol references" rather than "paste this into chat."
3. Consolidate the prompt reference table to match the new 5-file structure.

---

## 6. Model & Session Guidance

### 6.1 New Section in `AGENTS.md`

```markdown
## Model & Session Guidance

genOS recovers from the Project Brain alone. New sessions are always preferred
over compacting — a fresh BOOT with a clean context window produces better results
than a compacted history.

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
- When presenting recommendations, agents should state:
  "💡 Recommended: [Model tier] in a [new/continued] session."
```

---

## 7. Repo Hygiene

### 7.1 Delete

| File | Reason |
|------|--------|
| `Agency_Agents_0.3.0_x64-setup.exe` | 6.7 MB binary in repo root. Not referenced. Users install Agency Agents via GitHub, not a Windows installer. |

### 7.2 Rename/Move

| From | To | Reason |
|------|-----|--------|
| `setup-04-framework-upgrade.md` | `setup-upgrade.md` | Remove arbitrary numbering |
| `workflow-01-kickoff.md` | `workflow-kickoff.md` | Remove arbitrary numbering |
| `workflow-02-shutdown.md` | `workflow-shutdown.md` | Remove arbitrary numbering |
| `workflow-autonomous-batch.md` | `workflow-batch.md` | Shorter, cleaner |

### 7.3 .gitignore Additions

```
*.exe
```

---

## 8. File Change Summary

### AGENTS.md (MODIFY — Major)
- Add `## Commands` section with keyword trigger table and protocol definitions
- Add `## Model & Session Guidance` section
- Rewrite BOOT sequence with inline VALIDATE steps
- Rewrite SHUTDOWN sequence with explicit Sanity Gate checklist
- Absorb Doctor protocol from `workflow-doctor.md`
- Absorb Autonomous Batch protocol from `workflow-batch.md` (or reference it)

### guides/guide.md (MODIFY)
- Lead with command system
- Update prompt reference table to 5 files
- Remove overlap with README.md

### README.md (MODIFY)
- Trim to landing page: description, structure, quickstart link, principles
- Remove workflow examples and prompt table

### guides/prompts/ (MODIFY + DELETE)
- Rename 4 files (drop numbering)
- Delete 5 absorbed files
- Update remaining files to note they are reference docs, not primary triggers

### .agents/skills/ (NEW — 3 files)
- `genos-kickoff/SKILL.md`
- `genos-shutdown/SKILL.md`
- `genos-doctor/SKILL.md`

### .cursor/rules/ (NEW — 3 files)
- `genos-kickoff.mdc`
- `genos-shutdown.mdc`
- `genos-doctor.mdc`

### Root (DELETE)
- `Agency_Agents_0.3.0_x64-setup.exe`

### .gitignore (MODIFY)
- Add `*.exe`

---

## 9. Branch Strategy

1. Create `genos-v3` branch off `genosidian`
2. All changes land on `genos-v3`
3. Human reviews and merges to `genosidian` (or `main`) via PR

---

## 10. Bootstrapping Guide (Per-Tool Setup)

genOS commands require the agent to know the kernel exists. How this happens depends on your tool.

### Tier 1: Auto-Load (Zero Setup)

These IDEs automatically inject repo-root rules into every session.

| Tool | How it works | User action per session |
|------|-------------|----------------------|
| **Antigravity** | `AGENTS.md` auto-loaded as `<RULE>` | Just type `kickoff` |
| **Cursor** | `.cursor/rules/genos.mdc` with `alwaysApply: true` | Just type `kickoff` |
| **Claude Code** | `CLAUDE.md` references `AGENTS.md` | Just type `kickoff` |
| **Codex** | `AGENTS.md` auto-detected at repo root | Just type `kickoff` |

**Setup (one-time):**
- Antigravity: Nothing — already works.
- Cursor: Create `.cursor/rules/genos.mdc` with `alwaysApply: true` containing: `Read and follow AGENTS.md in the project root.`
- Claude Code: Add to `CLAUDE.md`: `Read and follow AGENTS.md.`

### Tier 2: File Access, No Auto-Load (Minimal Setup)

These tools can read your files but don't auto-inject rules.

| Tool | One-time setup | User action per session |
|------|---------------|----------------------|
| **Claude Desktop** (with filesystem MCP) | Add `AGENTS.md` as Project Knowledge | Just type `kickoff` |
| **Grok Bot** (with file tools) | Pin `AGENTS.md` path in system prompt | Just type `kickoff` |

**If no Project/pin support:** Type `Read AGENTS.md and kickoff` (6 words instead of pasting 30 lines).

### Tier 3: No File Access (Not Supported)

Plain web chats (ChatGPT free tier, browser-only Grok, etc.) cannot read or write brain files. genOS requires filesystem access — these tools are not compatible.

---

## 11. Workflow Showcase

### Day 0 — First-Time Setup (one-time, any tool)

> **Human:** *[pastes setup-init.md]*
>
> **Agent:** Detected stack: Unity 6 / C#. Suggested profile: `gamedev`. What's your project vision?
>
> **Human:** Building a survival crafting game with base building and co-op.
>
> **Agent:** ✅ Brain initialized. Roadmap proposed: M1.0 — Core Movement & World.
> MCP configured: Unity MCP. Workforce: Game Designer, Unity Architect, QA Tester.
> 🎉 Day 0 Complete! Close this chat. Type `kickoff` in a new session to begin.

---

### Day 1 — First Milestone (new session)

> **Human:** kickoff
>
> **Agent:** 🔄 BOOT complete.
> 📍 Active Milestone: **M1.0 — Core Movement & World**
> 📋 Last session: Day 0 setup completed. Brain initialized, roadmap active.
> 🎯 Plan:
> 1. Create player controller with WASD movement
> 2. Set up terrain generation
> 3. Add basic camera follow
>
> 💡 Recommended: High-tier model (Opus/Pro) in this new session.
> Awaiting your approval.
>
> **Human:** approved
>
> *[Agent implements, tests, iterates...]*

---

### End of Session (same session)

> **Human:** shutdown
>
> **Agent:** Running SHUTDOWN...
> ✅ M1.0 completion criteria verified — all 3 deliverables passing.
> ✅ M1.0 → `done`. M1.1 (Crafting System) → `active`.
> ✅ PROGRESS updated: `current_milestone: M1.1`
> ✅ Sanity Gate: 18/18 checks passed.
> 🎉 Memory persisted. Close this chat and start a new session for M1.1.

---

### Day 2 — Continue Development (new session)

> **Human:** kickoff
>
> **Agent:** 🔄 BOOT complete.
> 📍 Active Milestone: **M1.1 — Crafting System**
> 📋 Last session: M1.0 completed — movement, terrain, camera all passing. Milestone advanced to M1.1.
> 🎯 Plan:
> 1. Create resource gathering interaction
> 2. Build crafting recipe data model
> 3. Implement crafting UI
>
> 💡 Recommended: High-tier model in this new session.
> Awaiting your approval.

---

### Mid-Session Resume (new session, mid-milestone)

> **Human:** kickoff let's focus on the crafting UI today
>
> **Agent:** 🔄 BOOT complete.
> 📍 Active Milestone: **M1.1 — Crafting System**
> 📋 Last session: Resource gathering and recipe data model implemented. Crafting UI remaining.
> 🎯 Scoped to your request — Crafting UI plan:
> 1. Grid-based inventory layout
> 2. Drag-and-drop recipe slots
> 3. Crafting progress bar animation
>
> 💡 Recommended: Mid-tier model (Flash High / Sonnet) for UI work.
> Awaiting your approval.

---

### Quick Check (any session)

> **Human:** status
>
> **Agent:** 📍 M1.1 — Crafting System (`active`)
> 📋 Last: Resource gathering + recipe model done. Crafting UI in progress.
> ⚠️ 0 blockers, 0 known issues.

---

### Something Feels Wrong (any session)

> **Human:** doctor
>
> **Agent:** Running diagnostics...
>
> | Component | Status | Details |
> |:---|:---:|:---|
> | `00_PROJECT.md` | ✅ | Vision set, scope defined |
> | `20_PROGRESS.yaml` | ⚠️ | Missing `known_issues` key — auto-added as `[]` |
> | `30_DECISIONS.md` | ✅ | 2 decisions, index synced |
> | `40_BACKLOG.md` | ✅ | No state bleed |
> | `50_ROADMAP.md` | ✅ | 4 milestones, M1.1 active |
> | `brain/systems/` | ✅ | 3 systems, all scopes valid |
> | Obsidian Links | ⚠️ | 1 standard link healed → `[[wikilink]]` |
>
> 🩺 2 issues auto-repaired. Brain is healthy.

---

### Hands-Free Batch (new session)

> **Human:** batch M1.2, M1.3
>
> **Agent:** 🔄 BOOT complete. Pre-flight workforce gate: ✅ Builder + QA registered.
> 📦 Batch: M1.2 (Base Building), M1.3 (Co-op Multiplayer)
> Executing autonomously...
>
> *[Builder implements M1.2 → QA audits → Sanity Gate → advances → Builder implements M1.3 → QA audits → Sanity Gate]*
>
> 🎉 Batch complete! 2/2 milestones done. 36/36 sanity checks passed.

---

### Claude Desktop / Tier 2 Tool (new session, no auto-load)

> **Human:** Read AGENTS.md and kickoff
>
> **Agent:** 🔄 BOOT complete.
> 📍 Active Milestone: **M1.1 — Crafting System**
> ...
>
> *(Same flow as above — the 6-word bootstrap replaces pasting a 30-line file)*

---

## 12. Migration Notes

- Existing users who memorized "paste `workflow-01-kickoff.md`" still find their files — they just have cleaner names and the command system as the primary path.
- No brain file schema changes — `brain/` structure is untouched.
- Profiles are untouched — no structural changes to `profiles/`.
- The `integrations/` directory is untouched.
- Day 0 setup (`setup-init.md`) is the only workflow that still requires pasting — by design, since the kernel isn't loaded yet.
