# genOS Framework Auto-Updater

> **Primary trigger:** Type `update` in any AI chat where genOS is loaded (or paste this file into an existing/legacy `v1`–`v3` repo and point to its `genOS` directory).  
> **Alternative trigger:** `@update.md`  
> **Authoritative kernel spec:** `AGENTS.md` → Framework Update Protocol

You are executing the genOS Framework Auto-Updater. First verify whether the existing genOS installation is outdated, propose an explicit Upgrade & Migration Plan, wait for human approval, and only then upgrade framework files while strictly shielding the Project Brain and project-installed agents.

*(Self-contained for legacy `v1`/`v2` upgrades: do NOT rely on an outdated local `AGENTS.md` for Doctor or update rules—always read the newly fetched `AGENTS.md` inside `_genOS_Update/` or the upstream source before migrating.)*

---

## Instructions

### 1. Fetch Upstream Source (Read-Only)
Do **not** modify any project files yet. Locate the latest official genOS source (`main`):
- **Git Upstream Method:** If this repository tracks an upstream remote for `verdenef/genOS`, fetch `main`.
- **Direct Archive Fetch Method:** Otherwise, download and extract `https://github.com/verdenef/genOS/archive/refs/heads/main.zip` into a temporary `_genOS_Update/` folder via `curl` or PowerShell `Invoke-WebRequest`.
- **Local Drop-In / Path Method:** If `_genOS_Update/` or a local `genOS` source path was provided by the human, inspect it directly.

### 2. Verify Drift & Detect Installation Generation
Determine whether the genOS installation lives at repository root or inside a subdirectory (e.g. `genOS/`), then audit it against upstream:
- **Version Check:** Check `AGENTS.md` for `> **Framework Version:**` and compare all core framework files (`AGENTS.md`, `CLAUDE.md` at repo root, `guides/guide.md`, `guides/scripts/install_agent.py`, canonical prompts in `guides/prompts/`, standard `profiles/`, core `.agents/skills/` and `.cursor/rules/`), **excluding** `brain/`.
- **Legacy (`v1`/`v2`) Signals:** Note if `AGENTS.md` lacks `## Commands` / `## Framework Update Protocol`, if obsolete replaced prompts exist (`setup-04-framework-upgrade.md`, `setup-tooling.md`, `setup-workforce.md`, `setup-obsidian-migration.md`, `workflow-01-kickoff.md`, `workflow-02-shutdown.md`, `workflow-03-resume-session.md`, `workflow-doctor.md`, `workflow-autonomous-batch.md`), if `CLAUDE.md`/`.agents/`/`.cursor/` are missing from repo root, or if `brain/` has legacy schema issues (`Status` column in `brain/systems/README.md`, missing keys in `20_PROGRESS.yaml`).
- **Short-Circuit if Up to Date:** If all core framework files and repo-root discovery entries match upstream cleanly and no obsolete prompts remain, delete `_genOS_Update/`, output:
  `✅ genOS is already up to date. No changes made.`
  and **STOP**.

### 3. Propose Upgrade & Migration Plan (Wait for Approval)
If outdated, present a clear plan before modifying any files:
1. **Detected State → Target:** e.g., `Legacy v1 → v3.2` or `v3 outdated → v3.2`.
2. **Core Files to Add/Update:** `AGENTS.md`, `guides/guide.md`, `guides/scripts/`, canonical `guides/prompts/` (`setup-init.md`, `update.md`, `workflow-kickoff.md`, `workflow-shutdown.md`, `workflow-batch.md`), standard `profiles/`, repo-root `CLAUDE.md`, and core `.agents/skills/` + `.cursor/rules/`.
3. **Obsolete v1/v2 Files to Remove (if any):** List exact legacy prompts to prune.
4. **Strict Shield List (Untouched During File Sync):**
   - `brain/` (`00_PROJECT.md`, `20_PROGRESS.yaml`, `30_DECISIONS.md`, `40_BACKLOG.md`, `50_ROADMAP.md`, `60_AGENTS.md`, `brain/systems/*.md`, plus any project-specific subfolders in `brain/`)
   - `.obsidian/` configuration
   - Custom profiles in `profiles/`
   - Project source code
   - Project-installed Agency Agents in `.agents/skills/` or `.cursor/rules/`
5. **Post-Sync Doctor Check:** Note any non-destructive `v1`/`v2` schema repairs Doctor will run after syncing.

**STOP and wait for human approval before applying changes.**

### 4. Apply Approved Upgrade
Once approved:
1. Record before-hashes (or line counts/paths) of `brain/` and any project-installed Agency Agents.
2. Apply approved updates to `AGENTS.md`, `guides/`, standard `profiles/`, repo-root `CLAUDE.md`, and ONLY core skills/rules (`genos*`, `ponytail`, `graphify`, Superpowers in `.agents/skills/` and `.cursor/rules/`). Never copy upstream `brain/` over the project's `brain/`.
3. Remove approved obsolete `v1`/`v2` prompt files and delete `_genOS_Update/`.

### 5. Post-Upgrade Doctor & Proof
1. Read the **newly updated `AGENTS.md`** (`Doctor Protocol`) and verify/auto-repair any legacy `v1`/`v2` `brain/` schema gaps (missing `20_PROGRESS.yaml` keys, `[[wikilink]]` syntax, `brain/systems/README.md` Status column removal, Index sync) **without** erasing project history.
2. Confirm `brain/` history and project-installed Agency Agents remain preserved, then print the Upgrade Health Report:

```markdown
🎉 genOS Upgraded Successfully!

| Component | Status | Details |
|:---|:---:|:---|
| Framework Version | ✅ | Upgraded from `<old>` to `<new>` |
| Kernel (`AGENTS.md`) & Root Setup | ✅ | Updated (`CLAUDE.md` + root skills/rules verified) |
| Guides, Scripts & Prompts | ✅ | Refreshed canonical files; obsolete prompts cleaned (`<count>`) |
| Project Brain (`brain/`) | 🛡️ | Preserved (plus Doctor v1/v2 schema repairs if needed) |
| Project Skills & Rules | 🛡️ | Core refreshed; project Agency Agents shielded |
| Brain Doctor Audit | ✅ | All sanity checks passing |
```
