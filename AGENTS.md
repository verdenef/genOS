# genOS Kernel

Every AI agent in this repository must follow this file. Read it before any other project file.

genOS stores **only** knowledge that cannot be reliably inferred from the runtime environment (e.g., containers, endpoints, schemas, assets), source code, or Runtime MCP.

Assume **no chat history**. Recover state from the Project Brain alone.

---

## Ownership (single source of truth)

| Domain | Authoritative file | Owner | Rule |
|--------|-------------------|-------|------|
| Project intent | `brain/00_PROJECT.md` | Human owns intent; AI may reorganize/summarize/clarify/maintain | Never change intent without explicit human approval |
| Session / current state | `brain/20_PROGRESS.yaml` | AI | Cold-start **execution RAM** only: `current_milestone` (ID), blockers, issues, scene, `session_summary` |
| Decisions | `brain/30_DECISIONS.md` | AI records; human approves intent-affecting decisions | Sole decision log |
| Durable ad-hoc queue | `brain/40_BACKLOG.md` | AI | Todo / Done / Icebox / Rejected for **non-milestone** work — **not** in-progress; **not** milestone definitions |
| Roadmap / milestones | `brain/50_ROADMAP.md` | AI maintains; human approves new program-level scope | **Sole** milestone authority: IDs, objectives, deliverables, completion criteria, dependencies, status |
| System knowledge + status | `brain/systems/**/<Name>.md` | AI | Each file owns its own Status and design knowledge (flat or categorized) |
| Systems navigation | `brain/systems/README.md` | AI | Index and links only — **no** status column |
| AI Workforce | `brain/60_AGENTS.md` | AI maintains; human approves/installs | Active roster of approved specialist AI agents |

**Do not mirror state across files.** If two places would disagree, the table above wins.

- In-progress work → only `PROGRESS.working_on` (never a Backlog "Doing" list)
- Milestone definitions / status → only `50_ROADMAP.md` (Progress stores **ID pointer** only)
- System status → only that system's `.md` file
- Decisions → only `30_DECISIONS.md`
- Vision/scope/constraints → only `00_PROJECT.md`
- Ad-hoc tasks → only `40_BACKLOG.md` (never restate milestone details here)

---

## Semantics: `_TBD_` and `null`

- `_TBD_` and `null` mean **unknown / unset**.
- Do **not** invent content to fill them.
- Do **not** treat them as an invitation to design domain architecture or rewrite intent.
- Ask the human, or leave unset, until real information exists.

---

## Empty Brain Protocol

The Project Brain is **uninitialized** when **any** of these is true:

- `00_PROJECT.md` Vision is `_TBD_` (or equivalent empty)
- `20_PROGRESS.yaml` → `session_summary` is `null` **and** `current_milestone` is `null`
- No accepted decisions exist **and** PROJECT intent is still unset

### When uninitialized, agents MUST

1. Run BOOT (read files) but **stop before inventing** vision, domain logic, systems design, roadmap fiction, or backlog fiction.
2. Tell the human the brain is empty and ask for intent (vision, scope, constraints, first goal).
3. Only perform structural maintenance: fix templates, clarify wording, sync format — without inventing project content.
4. On SHUTDOWN, write an honest `session_summary` (e.g. brain still uninitialized; waiting on human for Vision/first goal).

### When uninitialized, agents MUST NOT

- Invent Vision, Scope, Core User Flow, or Success Criteria
- Invent roadmap milestones or fill `50_ROADMAP.md` with guessed phases
- Fill system Purpose/Invariants/Responsibilities with guessed features
- Create fake `TASK` / `DEC` / milestone items to look productive
- Scaffold a full architecture or mock project “to get started”

Once the human provides intent (or accepts a proposed decision), update PROJECT / DECISIONS / ROADMAP / PROGRESS accordingly, then normal work may proceed.

---

## Missing context protocols

### Implementation project does not exist

- Do not invent folder layouts, scenes, or packages as if they were already chosen.
- Prefer brain + repo work (templates, decisions, backlog) until an implementation project exists.
- Ask the human before creating an engine/implementation project unless they already requested it.

### Runtime / Tooling MCP unavailable

- Use source code / configuration files on disk when present.
- Do not invent runtime hierarchy, database records, container state, or console output.
- Note MCP-unavailable in `session_summary` or `known_issues` if it blocked verification.
- Still run SHUTDOWN.

### Required information is missing

- If a task needs unset PROJECT fields, unset decisions, unset roadmap criteria, or unset system invariants: **ask the human** or record `blocked` — do not guess.
- Prefer a `proposed` decision over silent invention when a choice is required.

---

## Knowledge boundaries

### Brain stores

- Design intent, research constraints, domain rules (as design)
- Cross-system invariants, architectural decisions
- Roadmap milestone definitions and status
- Current **execution** state (progress pointer, blockers, session handoff)
- Human decisions and approvals

### Brain must NOT store

Anything reliably inferable from the runtime environment (containers, endpoints, schemas, assets), source code, or Runtime MCP.

Never duplicate APIs, hierarchies, component values, or asset lists. Point to Runtime paths instead.

Never treat chat history as the source of milestone criteria — use `50_ROADMAP.md`.

---

## File Linking (Obsidian Compatibility)

genOS is natively compatible with **Obsidian**.
When an AI agent links to another markdown file within the `brain/` directory (e.g., cross-referencing a Decision from a System file, or linking to the Roadmap), you MUST use **Obsidian wikilinks** format: `[[filename.md]]` or `[[filename]]`.
- Do not use standard markdown links for internal brain files (e.g., `[Link](file.md)`).
- This ensures the human operator can utilize the Obsidian Graph View to visualize the project architecture.

---

## Zero-history recovery

After BOOT, recover from brain alone:

| Question | Source |
|----------|--------|
| What are we building? | `00_PROJECT.md` |
| Where are we executing now? | `20_PROGRESS.yaml` |
| What milestone / criteria? | `50_ROADMAP.md` (via `PROGRESS.current_milestone`) |
| What was decided? | `30_DECISIONS.md` |
| System intent/status? | `systems/<Name>.md` (scoped) |
| What's queued (ad-hoc)? | `40_BACKLOG.md` |
| What's in progress? | `PROGRESS.working_on` |
| Last session? | `session_summary`, `last_agent`, `last_ide` |

Never write “as discussed in chat.” Use `DEC-XXX`, `TASK-XXX`, roadmap IDs (`M1.2`, `M2`, …), or Runtime paths.

---

## Multi-agent protocol

1. `brain/` is the only shared handoff surface.
2. SHUTDOWN must set a self-contained `session_summary`.
3. Set `last_agent` and `last_ide` (use `cursor`, `antigravity`, or other host name as appropriate).
4. If `working_on` shows conflicting work, do not overlap without human confirmation.
5. Prefer short, atomic brain updates.

---

## Commands

When the user's message begins with a command keyword below (case-insensitive, optionally followed by context), execute the corresponding protocol. The user does not need to paste a prompt file. Users may also `@`-mention the corresponding prompt file in `guides/prompts/` as an alternative trigger — both paths produce the same result.

**Syntax:** `<command>` or `<command> <user intent>`

When user intent follows the command keyword, it takes priority over default behavior. The agent still executes the full protocol (BOOT, validation, brain reads) but scopes its plan to the user's stated goal. The agent must validate that the intent aligns with the active milestone and roadmap criteria.

| Command | Protocol |
|---------|----------|
| `kickoff` | Run BOOT sequence → summarize project state → identify active milestone → **Hard Persona Gate (Pre-Planning):** read `60_AGENTS.md`, physically open and read each active agent's full definition file (`.cursor/rules/<agent>.mdc` or `.agents/skills/<agent>/SKILL.md`) **before** thinking or formulating the plan, cite 2-3 governing rules — do not guess agent rules from memory → **Ponytail Restraint Filter:** evaluate the Ladder of Restraint (YAGNI, reuse, stdlib, 1-liner) to prune unnecessary code/features before proposing the plan → propose test-driven implementation plan → wait for human approval |
| `shutdown` | Run full SHUTDOWN sequence with mandatory Sanity Gate |
| `doctor` | Run Diagnostic Checklist → auto-repair all fixable issues → output Brain Health Report table |
| `status` | Read `20_PROGRESS.yaml` + active milestone from `50_ROADMAP.md` → present concise summary. No code changes. |
| `batch` | Run Autonomous Batch protocol with `TARGET_SCOPE: AUTO_RECOMMENDED` unless user specifies scope (e.g. `batch M1.2, M1.3`) |
| `update` | Run Framework Update protocol: smart fetch latest genOS release (git remote or GitHub archive), upgrade framework files while strictly shielding `brain/` and custom profiles, run Doctor |

If the message does not match a command, proceed with normal conversation while respecting AGENTS.md rules.

### Kickoff Smart Routing

The `kickoff` command automatically determines session type from brain state:

| Brain state | Agent behavior |
|-------------|---------------|
| `session_summary` exists + `working_on` has items | Resume: "You were mid-work on X. Here's where you left off." |
| `working_on` is empty + `current_milestone` is active | Fresh start: "Active milestone is Mx.y. Here's a plan." |
| Milestone just completed, next milestone exists | Advance: "Mx.y is done. Next up is Mx.z. Here's the plan." |
| User provided intent after `kickoff` | Scoped: Use user's directive as session goal, still validate against roadmap |

---

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
8. Read only `brain/systems/<Name>.md` (or within 1-level category subdirectories `brain/systems/**/<Name>.md`) listed in `systems_in_scope` (plus any system the task directly touches)
   - VALIDATE: Every entry in `systems_in_scope` has a corresponding file (searched recursively).
   - If a file is missing, remove the entry and log a warning.
9. Read `brain/40_BACKLOG.md` if ad-hoc queue context is needed
10. **System Initialization Protocol:** Detect whether `brain/systems/` contains only `README.md` and `SYSTEM.md`. If so, recognize that the project has not yet initialized its systems architecture. Read `00_PROJECT.md`, `50_ROADMAP.md`, and `30_DECISIONS.md`. Propose the initial set of project systems and wait for human approval. Upon approval, generate one system document per approved system using `SYSTEM.md`.
11. **Optional Integrations:** If the human requests an integration (e.g., AI workforce evaluation), read the relevant protocol in `integrations/` and execute it only *after* the roadmap is defined.
12. **If Empty Brain Protocol applies → stop inventing; ask human**
13. Plan against **ROADMAP completion criteria** for `current_milestone` (not chat)
14. Implement (only when intent and required facts exist)

---

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
- [ ] Every entry in `systems_in_scope` has a file in `brain/systems/` (flat or in a 1-level category subfolder)
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

---

## Doctor Protocol

Run when the user issues the `doctor` command. Perform a comprehensive inspection of all Project Brain files.

### Diagnostic Checklist

1. **YAML Validity (`brain/20_PROGRESS.yaml`):** Verify valid YAML. Confirm all required keys exist. Confirm `working_on` is either `null` or an array. Confirm `systems_in_scope` is an array.
2. **Milestone Pointer Integrity:** Check `current_milestone` points to an actual milestone ID in `50_ROADMAP.md`. Confirm that milestone's status is `active`.
3. **Index Synchronization:** Verify every milestone in `50_ROADMAP.md` has an Index row with matching status. Verify every decision in `30_DECISIONS.md` has an Index row with matching status.
4. **State Isolation:** Confirm `40_BACKLOG.md` has no "Doing" column, no in-progress markers, and no milestone deliverable duplicates. Confirm `00_PROJECT.md` is not empty (unless uninitialized).
5. **System Scopes:** Confirm every entry in `systems_in_scope` has a matching file in `brain/systems/` (flat or in a 1-level category subfolder). Confirm `brain/systems/README.md` has no status column.
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

---

## Framework Update Protocol

Run when the user issues the `update` command or `@update.md`. Safely upgrades the genOS framework while guaranteeing zero data loss in the Project Brain.

### Upgrade Steps
1. **Fetch Latest Framework (Dual-Method):**
   - Check if git remote `upstream` or `origin` tracks `verdenef/genOS`. If yes, fetch the latest commit.
   - If not a tracking clone, download the latest release archive from `https://github.com/verdenef/genOS/archive/refs/heads/main.zip` via curl or PowerShell `Invoke-WebRequest` into a temporary `_genOS_Update/` directory and unpack it.
2. **Strict Brain & User Protection:**
   - **NEVER** overwrite, modify, or delete any file in `brain/` (`00_PROJECT.md`, `20_PROGRESS.yaml`, `30_DECISIONS.md`, `40_BACKLOG.md`, `50_ROADMAP.md`, `60_AGENTS.md`, and all `brain/systems/*.md`).
   - **NEVER** delete the `.obsidian/` directory if present.
   - **NEVER** delete custom user profiles in `profiles/`.
   - **NEVER** touch user source code.
3. **Apply Framework Refresh:**
   - Update `AGENTS.md` kernel.
   - Update `guides/` (user guide and workflow prompt references).
   - Update official `profiles/` presets.
   - Update pre-packaged `.agents/skills/` and `.cursor/rules/`.
4. **Cleanup & Verification:**
   - Remove temporary `_genOS_Update/` folder if created.
   - Run the Doctor Protocol to audit the Project Brain.
   - Output the Upgrade Summary table.

---

## Model & Session Guidance

genOS recovers from the Project Brain alone. New sessions are always preferred over compacting — a fresh BOOT with a clean context window produces better results than a compacted history.

### Host Platform Detection

Check `20_PROGRESS.yaml: last_ide` and the active environment to identify the host platform (Claude Desktop / Claude Code, Antigravity, Cursor, etc.). When stating model recommendations, always output the **exact model name AND thinking / reasoning effort level** tailored to that platform.

### Per-Command Recommendations

| Command | Claude Desktop / Code | Antigravity / Gemini | Cursor | Session Strategy |
|---------|-----------------------|----------------------|--------|------------------|
| `kickoff` (planning) | `Claude 3.7 Sonnet` (Thinking: High) or `Opus` | `Gemini Pro` (Thinking: High) | `Claude 3.7 Sonnet` (Reasoning: High) | **New session** always |
| `batch` / Complex build | `Claude Opus` (Thinking: High) | `Gemini Pro` (Thinking: High) | `Claude 3.7 Sonnet` (High) / `o3-mini` (High) | **New session** always |
| Simple fixes / tweaks | `Claude 3.5 Sonnet` or `3.7` (Thinking: Low) | `Gemini Flash` (Thinking: Low) | `Claude 3.5 Sonnet` | Continue if context is clean |
| `shutdown` | `Claude 3.5 Haiku` (Thinking: Off/Low) | `Gemini Flash` (Thinking: Low) | `Claude 3.5 Haiku` / `GPT-4o-mini` | Continue current session |
| `doctor` | `Claude 3.5 Haiku` (Thinking: Low) | `Gemini Flash` (Thinking: Low) | `Claude 3.5 Haiku` | **New session** if prior was long |
| `status` | Lowest available model | Lowest available model | Lowest available model | Either — minimal token use |

### Rules
- Detect host platform on BOOT.
- Format recommendation as: "💡 Recommended: [Platform Model] (Thinking/Effort: [Level]) in a [new/continued] session."
- After SHUTDOWN, always start a **new session** for the next milestone.
- If context feels degraded (repetition, forgetting instructions), start a new session.
- Never compact as a substitute for SHUTDOWN → new session.

---

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

---

## Location-Agnostic Pathing

- genOS may be installed at the repository root or inside a subdirectory (e.g., `genOS/`).
- **CRITICAL:** All file paths mentioned in this kernel (e.g., `brain/00_PROJECT.md`) are relative to the directory containing this `AGENTS.md` file, *not* the repository root.
- Do not store project truth in IDE-local memory or chat.

---

## Optional Integrations

genOS supports optional integrations (such as AI workforce management) stored in the `integrations/` directory.
- The genOS kernel remains fully independent of these integrations.
- Do not auto-install or assume any specific integration is active unless requested or defined in the Brain.

---

## Runtime / Tooling MCP

- MCP + source = implementation truth.
- Brain = semantic truth.
- Update brain only when non-inferable knowledge changed.
- Do not dump MCP output into the brain.

---

## Systems template

Do not use an inline template. When creating a new system, duplicate `brain/systems/SYSTEM.md` and fill in its sections.

---

## Decision template

```markdown
### DEC-XXX: Title
- **Status:** proposed
- **Date:** YYYY-MM-DD
- **Reason:**
- **Impact:**
- **Supersedes:** none
```

Statuses: `proposed` | `accepted` | `superseded` | `rejected`

---

## Roadmap milestone template

```markdown
## Mx.y — Title

- **Status:** planned
- **Objective:**
- **Deliverables:**
- **Completion criteria:**
- **Dependencies:**
- **Systems:**
```

Statuses: `planned` | `active` | `done` | `cancelled` — keep the Index in sync.

---

## Prohibitions

- Do not invent PROJECT intent or domain logic under Empty Brain Protocol
- Do not invent roadmap program milestones without human approval
- Do not duplicate state across brain files
- Do not store milestone criteria or milestone status in PROGRESS or BACKLOG
- Do not skip SHUTDOWN
- Do not load all system files by default
- Do not create extra documentation files unless the human requests them
- Do not treat chat history as durable memory
- Do not fill `_TBD_` / `null` with guesses
