# Decisions

Authoritative decision log. AI records entries; humans approve intent-affecting decisions.
See `AGENTS.md` → Ownership.

Record a decision when intent, architecture, or constraints change in a way future agents cannot infer from runtime environment or source code.

**ID format:** `DEC-001`, `DEC-002`, …  
**Status:** `proposed` | `accepted` | `superseded` | `rejected`

Do not duplicate implementation details. Link to systems or runtime paths when useful.
Keep the Index in sync with entries below. Do not leave blank placeholder rows.

---

## Index

| ID | Status | Date | Title |
|----|--------|------|-------|
| DEC-001 | accepted | 2026-11-09 | Plain-Text Keyword Command Architecture |
| DEC-002 | accepted | 2026-11-10 | Timeless 3-Tier Model Guidance |
| DEC-003 | accepted | 2026-11-09 | Hard Persona Gate and Ponytail Restraint Filter |
| DEC-004 | accepted | 2026-11-09 | Dual-Method Framework Auto-Updater with Strict Brain Shielding |
| DEC-005 | accepted | 2026-11-10 | Copy-Pasteable Execution Handoff Blocks |
| DEC-006 | accepted | 2026-11-10 | Graphify Code Topology Integration |

---

## Template

```markdown
### DEC-XXX: Title
- **Status:** proposed
- **Date:** YYYY-MM-DD
- **Reason:**
- **Impact:**
- **Supersedes:** none
```

---

## Decisions

<!-- Entries go below. Newest first preferred. -->

### DEC-006: Graphify Code Topology Integration
- **Status:** accepted
- **Date:** 2026-11-10
- **Reason:** In large or sprawling codebases, navigating call chains and calculating blast radius with standard text search (`grep`, file globs) requires multiple tool turns and high token usage. Pre-mapped local AST call graphs accelerate pre-planning exploration without context rot.
- **Impact:** Integrated Graphify (PyPI `graphifyy[mcp]`, CLI `graphify extract . --code-only` / `graphify update .`, MCP `graphify-mcp --graph graphify-out/graph.json`) as an optional Pre-Planning Code Topology Hook during `kickoff`. Added `.agents/skills/graphify/SKILL.md`, `.cursor/rules/graphify.mdc`, and `profiles/templates/mcp-graphify.json` plus `recommended_mcps` across stack profiles. Enforced zero Brain contamination (graph artifacts stay in `graphify-out/`, gitignored, never in `brain/`), explicit `--code-only` offline privacy, mandatory Grep confirmation for string/asset references and `INFERRED` edges, and silent fallback to native text tools when Graphify is unconfigured.
- **Supersedes:** none

### DEC-005: Copy-Pasteable Execution Handoff Blocks
- **Status:** accepted
- **Date:** 2026-11-10
- **Reason:**
  In multi-session AI software development, context window degradation is the leading driver of instruction drift, forgotten invariants, and subtle hallucination. While genOS mandates cold-start session resets after planning via [[20_PROGRESS.yaml]], human operators frequently experienced friction transitioning between the planning session and the fresh execution session. Manually formulating the execution command often resulted in omitted execution flags (e.g., omitting subagent workflows or failing to pass the exact plan path).
- **Impact:**
  - Planners must conclude every `kickoff` plan with copy-pasteable execution command blocks.
  - Two standard copy-pasteable command formats are supported:
    1. Standard sequential execution: `kickoff execute the approved plan: <path-to-plan>`
    2. Subagent-driven execution: `kickoff execute the approved plan: <path-to-plan> using subagent-driven-development`
  - Eliminates human friction when transitioning between a Flagship model session (planning) and a fresh execution session.
  - Formalized in `AGENTS.md` under Model & Session Guidance; integrated into [[Kernel]] and [[Workforce]].
- **Supersedes:** none

### DEC-002: Timeless 3-Tier Model Guidance
- **Status:** accepted
- **Date:** 2026-11-10
- **Reason:**
  Hardcoding specific model release identifiers (such as `claude-3-5-sonnet-20241022` or `gpt-4o-2024-08-06`) directly into framework rules leads to rapid obsolescence as model vendors release updates every few months. Additionally, different phases of development exhibit drastically different reasoning requirements: planning and kickoff require deep reasoning; implementation requires fast, standard code generation; and shutdown, doctor, or status audits only need lightweight verification.
- **Impact:**
  - Replaced hardcoded model strings with a timeless 3-tier capability model:
    1. **Flagship / Deep Reasoning Tier:** High reasoning effort / thinking mode for `kickoff`, architectural planning, and autonomous `batch`. Always requires a new session.
    2. **Balanced / Standard Tier:** Standard reasoning for daily feature implementation, iterative coding, and debugging. Continued session allowed if context remains clean.
    3. **Fast / Lightweight Tier:** Minimal overhead for `shutdown`, `doctor`, and `status`.
  - Added explicit cross-platform mapping across Claude Desktop/Code, Antigravity/Gemini, and Cursor/OpenAI in `AGENTS.md`.
  - Enforced the rule that fresh sessions are always preferred over context compaction.
  - Managed by [[Kernel]] and referenced by [[Workforce]].
- **Supersedes:** none

### DEC-004: Dual-Method Framework Auto-Updater with Strict Brain Shielding
- **Status:** accepted
- **Date:** 2026-11-09
- **Reason:**
  Downstream projects adopting genOS require a seamless, automated method to receive framework enhancements (`AGENTS.md`, `guides/`, official `profiles/`, `.agents/skills/`, `.cursor/rules/`) as genOS evolves. However, downstream projects are cloned or installed in varying environments: some track upstream git remotes (`origin` or `upstream`), while others are standalone repos or extracted archives without git remote tracking. Most critically, any framework updater must guarantee zero data loss or overwrite of the project's living brain files or custom code.
- **Impact:**
  - Implemented the `update` command protocol with dual-method framework fetching:
    1. Git remote fetch if tracking `verdenef/genOS`.
    2. GitHub main release zip archive download and unpack (`_genOS_Update/`) for non-tracking projects.
  - Enforced strict brain shielding: the updater MUST NEVER touch or overwrite `brain/` (`[[00_PROJECT.md]]`, `[[20_PROGRESS.yaml]]`, `[[30_DECISIONS.md]]`, `[[40_BACKLOG.md]]`, `[[50_ROADMAP.md]]`, `[[60_AGENTS.md]]`, and `brain/systems/*.md`), `.obsidian/`, custom `profiles/`, or user source code.
  - Automatically runs the Doctor Diagnostic Checklist immediately post-update to verify brain integrity.
  - Governed by [[Updater]] and [[Kernel]].
- **Supersedes:** none

### DEC-003: Hard Persona Gate and Ponytail Restraint Filter
- **Status:** accepted
- **Date:** 2026-11-09
- **Reason:**
  Autonomous AI agents frequently hallucinate compliance with specialized roles or skip restraint principles during planning, causing bloated architectures, unnecessary dependencies, and premature abstractions. Agents often rely on generic training data rather than adhering to repo-specific skills and constraints.
- **Impact:**
  - Enforced the **Hard Persona Gate (Pre-Planning)** in the `kickoff` protocol: agents MUST read `[[60_AGENTS.md]]`, physically open and read active agent rule definition files (`.cursor/rules/<agent>.mdc` or `.agents/skills/<agent>/SKILL.md`) before formulating a plan, and cite 2-3 governing rules.
  - Integrated the **Ponytail Restraint Filter**: agents must explicitly evaluate the Ladder of Restraint (Rung 1: YAGNI -> Rung 2: Reuse existing code -> Rung 3: Stdlib/primitives -> Rung 4: Minimal one-liner) to prune unnecessary complexity before proposing implementation plans.
  - Prevents over-engineering, enforces codebase minimalism, and aligns multi-agent operations with project standards.
  - Enforced across [[Kernel]], [[Workforce]], and [[Skills]].
- **Supersedes:** none

### DEC-001: Plain-Text Keyword Command Architecture
- **Status:** accepted
- **Date:** 2026-11-09
- **Reason:**
  Prior workflows relied on users typing slash-commands (e.g. `/kickoff`), pasting verbose workflow prompt files from `guides/prompts/`, or using IDE-specific `@`-mentions. This created user friction, required memorizing complex paths, and caused compatibility issues across diverse IDEs (Antigravity, Cursor, Claude Code, Codex) that support different command syntaxes.
- **Impact:**
  - Replaced prompt-pasting with 6 first-class plain-text keyword commands: `kickoff`, `shutdown`, `doctor`, `status`, `batch`, and `update`.
  - Commands are detected case-insensitively at the beginning of user messages (`<command>` or `<command> <user intent>`).
  - Optional user intent following a command (e.g., `kickoff add login flow`) automatically scopes session execution while preserving full BOOT sequence and roadmap validation.
  - Preserved backward compatibility with `@`-mentions for prompt files in `guides/prompts/`.
  - Documented as core command loop in `AGENTS.md` and managed by [[Kernel]].
- **Supersedes:** none
