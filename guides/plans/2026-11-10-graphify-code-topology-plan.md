# Graphify Code Topology Integration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Integrate Graphify as an optional, high-leverage code topology sensor and skill in genOS to provide agents with instant call-hierarchy navigation and blast-radius calculation during pre-planning.

**Architecture:** Create `.agents/skills/graphify/SKILL.md` and `.cursor/rules/graphify.mdc` to guide agent interaction with Graphify. Add standard MCP server templates to `profiles/` and update `AGENTS.md` to introduce an optional Pre-Planning Code Topology Hook during `kickoff` that degrades silently if Graphify is absent. Document the decision as `DEC-006` in `brain/30_DECISIONS.md`.

**Tech Stack:** Tree-sitter AST, Model Context Protocol (MCP), Markdown (`[[wikilink]]`), YAML.

---

## Global Constraints

- **Zero Brain Contamination:** No Graphify caches or AST data in `brain/`. The Project Brain holds only semantic truth.
- **Graceful Fallback:** If Graphify is not installed on a user's machine, the agent must fall back silently to native search tools (`grep`, `find_files`) with zero errors.
- **Git Hygiene:** Add `.graphify/` and `*.graphify` to `.gitignore`.
- **Doctor Compliance:** Maintain 100% clean check in `brain/` with matching Indexes, active milestone pointers, and Obsidian `[[wikilink]]` syntax.

---

## Tasks

### Task 1: Create Graphify Agent Skill and Cursor Rule

**Files:**
- Create: `.agents/skills/graphify/SKILL.md`
- Create: `.cursor/rules/graphify.mdc`

**Interfaces:**
- Consumes: Graphify CLI or MCP tools (`get_callers`, `get_dependencies`, `get_blast_radius`).
- Produces: Verified symbol call chains and impacted files for implementation plan interfaces.

- [x] **Step 1: Write `.agents/skills/graphify/SKILL.md`**
  - Define frontmatter: `name: graphify`, `description: "Query codebase AST call graphs, caller hierarchies, and calculate blast radius for implementation planning."`
  - Define Invariants: Local AST parsing, never guess call hierarchies, silent fallback if unconfigured.
  - Define Workflow: Check graph freshness -> Query callers/callees -> Compute blast radius -> Enrich plan `Interfaces:` block.

- [x] **Step 2: Write `.cursor/rules/graphify.mdc`**
  - Add Cursor IDE matching rule with `globs: *` and `alwaysApply: false`.
  - Provide instructions for Cursor agent on using Graphify MCP tools.

- [x] **Step 3: Verification**
  - Confirm `.agents/skills/graphify/SKILL.md` and `.cursor/rules/graphify.mdc` exist and contain no syntax errors.

---

### Task 2: Configure MCP Presets and Git Hygiene

**Files:**
- Modify: `.gitignore`
- Modify: `profiles/gamedev/profile.yaml`
- Modify: `profiles/web-fullstack/profile.yaml`
- Modify: `profiles/backend-services/profile.yaml`
- Create: `profiles/templates/mcp-graphify.json`

**Interfaces:**
- Consumes: Standard MCP JSON schema.
- Produces: Reusable MCP server configuration snippets for Cursor, Claude Code, and Antigravity.

- [x] **Step 1: Update `.gitignore`**
  - Append `.graphify/` and `*.graphify` to prevent caching artifacts from entering version control.

- [x] **Step 2: Add `graphify-mcp` to profile presets**
  - In `profiles/gamedev/profile.yaml`, `profiles/web-fullstack/profile.yaml`, and `profiles/backend-services/profile.yaml`, add `graphify-mcp` to `recommended_mcps`.

- [x] **Step 3: Create `profiles/templates/mcp-graphify.json`**
  - Provide ready-to-copy MCP configuration block for `@graphify/mcp-server`.

- [x] **Step 4: Verification**
  - Verify `.gitignore` contains `.graphify/`.
  - Validate profile YAML files with `python -c "import yaml; yaml.safe_load(...)"`.

---

### Task 3: Integrate Code Topology Hook into Kickoff and Systems

**Files:**
- Modify: `AGENTS.md`
- Modify: `guides/prompts/workflow-kickoff.md`
- Modify: `brain/systems/Skills.md`

**Interfaces:**
- Consumes: Kickoff protocol and system skills registry.
- Produces: Explicit step in `kickoff` for optional code topology verification before planning.

- [x] **Step 1: Update `AGENTS.md` Commands table and Kickoff protocol**
  - In the `kickoff` command row, add:
    `... → **Code Topology Hook (Optional):** if Graphify is available, verify graph freshness and query blast radius/callers → **Ponytail Restraint Filter:** ...`
  - In `Kickoff Smart Routing` / Kickoff rules, document the silent fallback behavior.

- [x] **Step 2: Update `guides/prompts/workflow-kickoff.md`**
  - Add Step 4b (Code Topology & Blast Radius):
    `4b. **Code Topology Check (Optional):** If Graphify is available, inspect call chains and blast radius for in-scope components before proposing task breakdowns.`

- [x] **Step 3: Update `brain/systems/Skills.md`**
  - Add `graphify` to the active skills catalog and runtime references.

- [x] **Step 4: Verification**
  - Read modified sections and verify exact line formatting and Obsidian `[[wikilink]]` syntax.

---

### Task 4: Log Architectural Decision (`DEC-006`) and Doctor Audit

**Files:**
- Modify: `brain/30_DECISIONS.md`
- Modify: `brain/50_ROADMAP.md`

**Interfaces:**
- Consumes: Validated design specification (`2026-11-10-graphify-code-topology-integration-design.md`).
- Produces: Canonical decision record and roadmap deliverable update.

- [x] **Step 1: Record `DEC-006` in `brain/30_DECISIONS.md`**
  - Add Index row: `DEC-006` | `accepted` | 2026-11-10 | Graphify Code Topology Integration
  - Write detailed decision section under `## Decisions` documenting Reason, Impact, Invariants, and Fallbacks.

- [x] **Step 2: Update `brain/50_ROADMAP.md`**
  - In `## M2 — genOS v3 Ergonomics, Superpowers Integration & Self-Hosting`, add `DEC-006` Graphify integration to the Deliverables list.

- [x] **Step 3: Run Doctor Audit**
  - Execute Doctor audit script to ensure all checks pass (YAML valid, Index sync, Systems scope, Milestone pointer).

- [x] **Step 4: Git Commit**
  - Commit all implementation changes to branch `genos-v3`.

---

## Execution Handoff

After saving this plan, start execution using one of the following commands:

**Option 1: Subagent-Driven (Recommended):**
```
kickoff execute the approved plan: docs/superpowers/plans/2026-11-10-graphify-code-topology.md using subagent-driven-development
```

**Option 2: Inline Execution:**
```
kickoff execute the approved plan: docs/superpowers/plans/2026-11-10-graphify-code-topology.md
```
