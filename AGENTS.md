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
| System knowledge + status | `brain/systems/<Name>.md` | AI | Each file owns its own Status and design knowledge |
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

## BOOT sequence

1. Read this file (`AGENTS.md`)
2. Read `brain/00_PROJECT.md`
3. Read `brain/20_PROGRESS.yaml`
4. Read `brain/30_DECISIONS.md` — while the log is small, read **all** non-rejected entries (use Index; skip only clearly irrelevant rejected/superseded noise)
5. Read `brain/50_ROADMAP.md` — Index always; then the section for `PROGRESS.current_milestone` (and its parent program milestone if needed for success criteria)
6. Read `brain/60_AGENTS.md` if it exists, to understand the current approved AI workforce.
7. Read `brain/systems/README.md` (navigation only)
8. Read only `brain/systems/<Name>.md` listed in `systems_in_scope` (plus any system the task directly touches)
9. Read `brain/40_BACKLOG.md` if ad-hoc queue context is needed
10. **System Initialization Protocol:** Detect whether `brain/systems/` contains only `README.md` and `SYSTEM.md`. If so, recognize that the project has not yet initialized its systems architecture. Read `00_PROJECT.md`, `50_ROADMAP.md`, and `30_DECISIONS.md`. Propose the initial set of project systems and wait for human approval. Upon approval, generate one system document per approved system using `SYSTEM.md`.
11. **Optional Integrations:** If the human requests an integration (e.g., AI workforce evaluation), read the relevant protocol in `integrations/` and execute it only *after* the roadmap is defined.
12. **If Empty Brain Protocol applies → stop inventing; ask human**
13. Plan against **ROADMAP completion criteria** for `current_milestone` (not chat)
14. Implement (only when intent and required facts exist)

---

## SHUTDOWN sequence

Mandatory. Incomplete SHUTDOWN breaks the next agent.

1. Update relevant `brain/systems/<Name>.md` if design intent, invariants, dependencies, or **Status** changed (not for pure code edits)
2. Update `brain/20_PROGRESS.yaml` (execution fields only, including honest `session_summary` and `current_milestone` ID)
3. Record decisions in `brain/30_DECISIONS.md` when applicable; keep Index in sync with entries
4. Update `brain/50_ROADMAP.md` when a milestone is started, completed, cancelled, or its definition changes (status + Index row)
5. Update `brain/40_BACKLOG.md` for ad-hoc queue columns only — never milestone status
6. **Sanity Gate (Mandatory Integrity Audit):**
   - Confirm `20_PROGRESS.yaml` is valid, parseable YAML with all required keys.
   - Verify `current_milestone` in `PROGRESS.yaml` matches an existing, active ID in `50_ROADMAP.md`.
   - Ensure all index tables in `50_ROADMAP.md` and `30_DECISIONS.md` match their section headers.
   - Ensure no milestone tasks or "Doing" states leaked into `40_BACKLOG.md`.
   - Ensure all `systems_in_scope` exist in `brain/systems/`.
   - Auto-repair any syntax or index desyncs before reporting completion.
7. Brief human summary in chat; durable record is ROADMAP + PROGRESS + Backlog + Decisions

Clear or rewrite stale `systems_in_scope` / `working_on` so the next agent is not misled.

When advancing milestones: set the finished milestone to `done` in ROADMAP, set the next to `active`, and point `PROGRESS.current_milestone` at the new ID.

If PROJECT intent must change, ask the human first. If a new **program-level** roadmap phase needs invented scope, ask the human first (do not fill `_TBD_` stubs).

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
