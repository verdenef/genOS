# genOS Multi-Ecosystem Integration & Auto-Updater Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement the genOS multi-ecosystem integration (Superpowers + Ponytail + Agency Agents) and the dual-method 1-click Auto-Updater (`update` command / `update.md`), completing the genOS v3 evolution.

**Architecture:** Pure-text, zero-dependency Markdown/YAML architecture. Embeds Ponytail's Ladder of Restraint and Superpowers test-driven rigor into the genOS kernel (`AGENTS.md`), pre-packages skill/rule files, automates Day 0 activation in `setup-init.md`, and implements the dual-method auto-updater.

**Tech Stack:** Markdown, YAML, Git, Shell (curl / PowerShell)

## Global Constraints

- genOS remains 100% pure text, zero external binary/runtime dependencies
- All work continues on branch `genos-v3`
- Never modify, overwrite, or delete `brain/` contents during updates
- Never delete custom user profiles in `profiles/`
- No placeholders, TBD, or TODO in deliverables
- Pre-packaged skills in `.agents/skills/` and rules in `.cursor/rules/` work out-of-the-box offline

---

### Task 1: Pre-Package Ponytail Rules & Skills

**Files:**
- Create: `d:/GameOS/.agents/skills/ponytail/SKILL.md`
- Create: `d:/GameOS/.cursor/rules/ponytail.mdc`

**Interfaces:**
- Consumes: [Spec section 2 & 3](file:///d:/GameOS/docs/superpowers/specs/2026-11-07-multi-ecosystem-integration-and-autoupdater-design.md)
- Produces: Offline-ready Ponytail restraint rules in `.agents/skills/` and `.cursor/rules/`

- [ ] **Step 1: Create Ponytail Skill for Antigravity / Agent CLI**

Create `d:/GameOS/.agents/skills/ponytail/SKILL.md`:
```markdown
---
name: ponytail
description: "Senior developer restraint: enforce the Ladder of Restraint (YAGNI, reuse, stdlib, one-liner, minimal code) before writing or reviewing code."
---

# Ponytail: The Senior Developer's Ladder of Restraint

"The best code is the code you never wrote."

Before proposing or writing any code, climb the **Ladder of Restraint**, stopping at the earliest rung that solves the requirement:

1. **Does this feature need to exist at all?** (YAGNI — reject unnecessary flexibility and premature abstractions)
2. **Is it already in this codebase?** (Reuse existing helpers, types, components, or patterns)
3. **Does the standard library do it?** (Use built-in language/platform features)
4. **Is there an already-installed dependency?** (Never add a new dependency for a few lines)
5. **Can it be written in one clean line or a trivial utility?**
6. **Only then:** Write the absolute minimum code required to fulfill the criteria.

## Rule Guardrails
- Be ruthless about cutting code volume.
- **Never** be lazy about security, input validation, trust boundaries, error handling, or test coverage.
- When reviewing (`/ponytail-review`), flag unnecessary abstractions, redundant classes, and over-engineered boilerplate.
```

- [ ] **Step 2: Create Ponytail Rule for Cursor**

Create `d:/GameOS/.cursor/rules/ponytail.mdc`:
```markdown
---
description: "Ponytail Senior Developer Restraint — enforce YAGNI and the Ladder of Restraint before writing code."
alwaysApply: true
---

# Ponytail Restraint Rules

Before writing any new implementation or refactoring code:
1. **YAGNI First:** Does this need to exist? If not, skip it.
2. **Reuse:** Check if a helper, component, or pattern already exists in the project.
3. **Stdlib / Native:** Prefer standard library and platform-native APIs over custom utility frameworks.
4. **Existing Dependencies:** Use existing project packages; do not introduce new dependencies without explicit user approval.
5. **Shortest Clean Path:** Prefer a clean one-liner or simple function over multi-layer abstractions.
6. **Minimum Surface Area:** Write the minimum code required to satisfy the active milestone criteria.
```

- [ ] **Step 3: Commit**

```bash
git add -f .agents/skills/ponytail/SKILL.md .cursor/rules/ponytail.mdc
git commit -m "feat(integrations): pre-package Ponytail skill and Cursor rule"
```

---

### Task 2: Embed Multi-Ecosystem Orchestration & Auto-Updater into `AGENTS.md`

**Files:**
- Modify: `d:/GameOS/AGENTS.md`

**Interfaces:**
- Consumes: [Spec section 2 & 5](file:///d:/GameOS/docs/superpowers/specs/2026-11-07-multi-ecosystem-integration-and-autoupdater-design.md)
- Produces: Updated kernel with Ponytail Ladder in Kickoff/Batch, Superpowers rigor, and `update` command

- [ ] **Step 1: Add `update` to `## Commands` Table**

In `AGENTS.md`, update the `## Commands` table to include the `update` command:

```markdown
| Command | Protocol |
|---------|----------|
| `kickoff` | Run BOOT sequence → summarize project state → identify active milestone → **Hard Persona Gate:** read `60_AGENTS.md`, physically open and read each active agent's full definition file (`.cursor/rules/<agent>.mdc` or `.agents/skills/<agent>/SKILL.md`), cite 2-3 governing rules → **Ponytail Restraint Filter:** evaluate the Ladder of Restraint (YAGNI, reuse, stdlib) before proposing code → propose test-driven implementation plan → wait for human approval |
| `shutdown` | Run full SHUTDOWN sequence with mandatory Sanity Gate |
| `doctor` | Run Diagnostic Checklist → auto-repair all fixable issues → output Brain Health Report table |
| `status` | Read `20_PROGRESS.yaml` + active milestone from `50_ROADMAP.md` → present concise summary. No code changes. |
| `batch` | Run Autonomous Batch protocol with `TARGET_SCOPE: AUTO_RECOMMENDED` unless user specifies scope (e.g. `batch M1.2, M1.3`) |
| `update` | Run Framework Update protocol: smart fetch latest genOS release (git remote or GitHub archive), upgrade framework files while strictly shielding `brain/` and custom profiles, run Doctor |
```

- [ ] **Step 2: Add `## Framework Update Protocol` to `AGENTS.md`**

Insert after the `## Doctor Protocol` section:

```markdown
## Framework Update Protocol

Run when the user issues the `update` command or `@update.md`. Safely upgrades the genOS framework while guaranteeing zero data loss in the Project Brain.

### Upgrade Steps
1. **Fetch Latest Framework:**
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
```

- [ ] **Step 3: Commit**

```bash
git add AGENTS.md
git commit -m "feat(kernel): add update command, framework update protocol, and Ponytail restraint to kickoff"
```

---

### Task 3: Create the 1-Click Auto-Updater Prompt (`guides/prompts/update.md`)

**Files:**
- Create: `d:/GameOS/guides/prompts/update.md`
- Delete: `d:/GameOS/guides/prompts/setup-upgrade.md` (superseded by `update.md`)

**Interfaces:**
- Consumes: [Spec section 5.2](file:///d:/GameOS/docs/superpowers/specs/2026-11-07-multi-ecosystem-integration-and-autoupdater-design.md)
- Produces: Streamlined auto-updater prompt supporting dual-method smart fetch

- [ ] **Step 1: Create `guides/prompts/update.md`**

Create `d:/GameOS/guides/prompts/update.md`:
```markdown
# genOS Framework Auto-Updater

> **Primary trigger:** Type `update` in any AI chat where genOS is loaded.
> **Alternative trigger:** `@update.md` for explicit confirmation.
> **Full protocol definition:** `AGENTS.md` → Framework Update Protocol

You are executing the genOS Framework Auto-Updater. Safely update this project's genOS framework to the latest official release while strictly shielding the Project Brain.

---

## Instructions

Follow the Framework Update Protocol from AGENTS.md strictly:

1. **Smart Fetch (Dual-Method):**
   - **Git Upstream Method:** If this repository tracks an upstream remote for `verdenef/genOS`, fetch the latest release from `main`.
   - **Direct Archive Fetch Method:** If no upstream git remote exists, use your terminal tool (`curl` / PowerShell) to download and extract `https://github.com/verdenef/genOS/archive/refs/heads/main.zip` into a temporary directory `_genOS_Update/`.
   - **Local Drop-in:** If `_genOS_Update/` was manually provided, use it directly.

2. **Strict Brain Shield (Zero Data Loss):**
   - **DO NOT TOUCH** `brain/` under any circumstances (`00_PROJECT.md`, `20_PROGRESS.yaml`, `30_DECISIONS.md`, `40_BACKLOG.md`, `50_ROADMAP.md`, `60_AGENTS.md`, and all `brain/systems/*.md`).
   - **DO NOT TOUCH** `.obsidian/` configuration.
   - **DO NOT TOUCH** custom profiles in `profiles/`.
   - **DO NOT TOUCH** project source code.

3. **Framework Synchronization:**
   - Update `AGENTS.md` (kernel).
   - Update `guides/guide.md` and reference prompts in `guides/prompts/`.
   - Update standard profiles in `profiles/`.
   - Update pre-packaged `.agents/skills/` and `.cursor/rules/`.

4. **Self-Audit & Cleanup:**
   - Delete `_genOS_Update/` temporary files.
   - Run the genOS Brain Doctor to verify that existing brain memory conforms to the upgraded kernel.
   - Print the Upgrade Health Report:

```markdown
🎉 genOS Upgraded Successfully!

| Component | Status | Details |
|:---|:---:|:---|
| Kernel (`AGENTS.md`) | ✅ | Upgraded to latest version |
| Guides & Prompts | ✅ | Refreshed to latest standards |
| Project Brain (`brain/`) | 🛡️ | 100% Preserved & untouched |
| Brain Doctor Audit | ✅ | All sanity checks passing |
```
```

- [ ] **Step 2: Delete superseded `setup-upgrade.md`**

```bash
git rm guides/prompts/setup-upgrade.md
```

- [ ] **Step 3: Commit**

```bash
git add guides/prompts/update.md
git commit -m "feat(prompts): add 1-click auto-updater prompt, replace setup-upgrade.md"
```

---

### Task 4: Upgrade Day 0 Onboarding Wizard (`guides/prompts/setup-init.md`)

**Files:**
- Modify: `d:/GameOS/guides/prompts/setup-init.md`

**Interfaces:**
- Consumes: [Spec section 4](file:///d:/GameOS/docs/superpowers/specs/2026-11-07-multi-ecosystem-integration-and-autoupdater-design.md)
- Produces: Day 0 wizard that automatically configures the unified AI stack (Agency Agents + Ponytail + Superpowers) with zero extra downloads

- [ ] **Step 1: Update Phase 3 in `setup-init.md`**

Update lines in Phase 3 of `guides/prompts/setup-init.md` to activate the full AI Stack (Agency Agents + Ponytail + Superpowers):

```markdown
## Phase 3: AI Stack Activation (Specialist Workforce & Engineering Disciplines)

Immediately after tooling is ready:

1. **Activate Specialist AI Workforce (Agency Agents):**
   - Audit `00_PROJECT.md` and `50_ROADMAP.md` alongside the profile's `recommended_agents`.
   - Select the Core and Milestone specialist roles best suited for the active milestone.
   - Populate `brain/60_AGENTS.md` and activate the corresponding rules in `.cursor/rules/` and `.agents/skills/`.
2. **Activate Engineering Restraint (Ponytail):**
   - Ensure the Ponytail Ladder of Restraint rule is active to prevent over-engineering and code bloat.
3. **Activate Execution Rigor (Superpowers):**
   - Confirm pre-packaged Superpowers skills (`brainstorming`, `writing-plans`, `test-driven-development`, `verification-before-completion`) are available.
4. Present the configured AI Stack and wait for my confirmation before proceeding to Phase 4.
```

- [ ] **Step 2: Commit**

```bash
git add guides/prompts/setup-init.md
git commit -m "feat(setup): update setup-init Phase 3 to activate unified AI Stack automatically"
```

---

### Task 5: Documentation Updates (`README.md` and `guides/guide.md`)

**Files:**
- Modify: `d:/GameOS/README.md`
- Modify: `d:/GameOS/guides/guide.md`

**Interfaces:**
- Consumes: [Spec section 1 & 2](file:///d:/GameOS/docs/superpowers/specs/2026-11-07-multi-ecosystem-integration-and-autoupdater-design.md)
- Produces: Clear documentation of the 4-layer stack and `update` command

- [ ] **Step 1: Update `guides/guide.md` Commands & Reference Table**

In `guides/guide.md`:
- Add `update` to the Commands table:
  `| update | Safely upgrade genOS to the latest release while strictly shielding the Brain |`
- Update the prompt reference table:
  Replace `setup-upgrade.md` with `update.md`.
- Add a subsection explaining the **Unified AI Engineering Stack**:
  - Memory: **genOS**
  - Identity: **Agency Agents**
  - Restraint: **Ponytail**
  - Rigor: **Superpowers**

- [ ] **Step 2: Update `README.md`**

Mention the 4-layer engineering stack in Core Principles / Overview.

- [ ] **Step 3: Commit**

```bash
git add README.md guides/guide.md
git commit -m "docs: document 4-layer engineering stack and update command"
```

---

### Task 6: IDE Shortcuts for All Commands

**Files:**
- Create/Verify: `d:/GameOS/.agents/skills/genos-kickoff/SKILL.md`
- Create/Verify: `d:/GameOS/.agents/skills/genos-shutdown/SKILL.md`
- Create/Verify: `d:/GameOS/.agents/skills/genos-doctor/SKILL.md`
- Create: `d:/GameOS/.agents/skills/genos-update/SKILL.md`
- Create/Verify: `d:/GameOS/.cursor/rules/genos.mdc`
- Create/Verify: `d:/GameOS/.cursor/rules/genos-kickoff.mdc`
- Create/Verify: `d:/GameOS/.cursor/rules/genos-shutdown.mdc`
- Create/Verify: `d:/GameOS/.cursor/rules/genos-doctor.mdc`
- Create: `d:/GameOS/.cursor/rules/genos-update.mdc`

**Interfaces:**
- Consumes: All kernel commands including `update`
- Produces: Complete set of IDE shortcuts

- [ ] **Step 1: Create `genos-update` Antigravity skill**

Create `d:/GameOS/.agents/skills/genos-update/SKILL.md`:
```markdown
---
name: genos-update
description: "Safely upgrade genOS to the latest release while strictly protecting the Project Brain."
---

# genOS Update

Execute the `update` command as defined in `AGENTS.md` → Framework Update Protocol.

Follow the protocol strictly: smart fetch latest release, upgrade framework files, shield `brain/` from changes, and run the Doctor check.
```

- [ ] **Step 2: Create `genos-update` Cursor rule**

Create `d:/GameOS/.cursor/rules/genos-update.mdc`:
```markdown
---
description: "genOS update — safely upgrade the framework while preserving the Project Brain."
alwaysApply: false
---

Execute the `update` command as defined in `AGENTS.md` → Framework Update Protocol. Smart fetch latest release, upgrade framework files, strictly shield `brain/`, and run the Doctor.
```

- [ ] **Step 3: Force-add IDE shortcuts to git**

```bash
git add -f .agents/skills/genos-* .cursor/rules/genos*
git commit -m "feat(ide): add IDE shortcuts for genOS update and all commands"
```

---

### Task 7: Final Verification & Cross-Reference Audit

- [ ] **Step 1: Run comprehensive file check**

```bash
# Check prompt files (exactly 5 files)
ls guides/prompts/
# Expected: setup-init.md  update.md  workflow-batch.md  workflow-kickoff.md  workflow-shutdown.md

# Verify Ponytail files exist
ls .agents/skills/ponytail/SKILL.md .cursor/rules/ponytail.mdc
```

- [ ] **Step 2: Check for dead cross-references**

```bash
git grep -l "setup-upgrade.md\|setup-04-framework" -- ":(exclude).git" ":(exclude)docs/superpowers/"
```
Expected: Zero occurrences.

- [ ] **Step 3: Run the Brain Doctor check**

Verify all Brain files conform to the new kernel rules and all index tables match.

- [ ] **Step 4: Push to origin**

```bash
git push -u origin genos-v3
```
