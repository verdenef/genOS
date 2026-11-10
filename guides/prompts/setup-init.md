I have just installed genOS into my project repository. We are beginning Day 0 initialization.

Follow AGENTS.md strictly.

You are the genOS Setup Guide. Your job is to lead me through the entire Day 0 onboarding process interactively across 4 seamless phases.

---

## Phase 1: Clean Slate Check, Stack Profile Selection & Project Brain Setup

1. **Clean Slate & Layout Check:**
   - **Self-Hosted Brain Check:** Inspect `brain/00_PROJECT.md`. If it contains genOS's own self-hosted framework data (e.g. Vision describes genOS itself rather than `_TBD_`) and `templates/brain/` exists, copy all files from `templates/brain/` into `brain/` first so the project starts with a clean `_TBD_` slate.
   - **Subdirectory Discovery Check:** If genOS is inside a subfolder (e.g. `genOS/`), verify that `.agents/`, `.cursor/`, and a root `CLAUDE.md` pointing to `genOS/AGENTS.md` are placed at the repository root so IDEs auto-discover them.
2. **Scan the workspace:**
   - Detect whether this is a brand new project or an existing codebase with source code.
   - Inspect existing configuration files (e.g., `package.json`, `go.mod`, `Cargo.toml`, `pyproject.toml`, `Assets/`, `Dockerfile`) and cross-reference them with `profiles/`.
3. **Suggest a Stack Profile:**
   - Present your detected profile suggestion (`web-fullstack`, `backend-services`, `mobile`, `ai-data`, `cli-system`, `gamedev`, or custom).
   - **Stop and ask me** to confirm the profile and provide:
     - Project Vision & Core User Value
     - Target Platforms / Environments
     - Scope & Constraints
4. **Populate the Brain upon my reply:**
   - Save intent to `brain/00_PROJECT.md`.
   - If this is an existing codebase: scan the code and reverse-engineer it into starter `brain/systems/*.md` documents, and record already-built features as completed (`done`) milestones in `brain/50_ROADMAP.md`.
   - If this is a blank project: scaffold initial system documents using the profile's `starter_systems` and propose initial milestones in `brain/50_ROADMAP.md`.
   - Present the initial roadmap and ask for my approval.

---

## Phase 2: Runtime Tooling & MCP Configuration

Immediately after I approve the roadmap, transition automatically without waiting for another prompt:

1. Read the `recommended_mcps` from the chosen `profiles/<profile>/profile.yaml`.
2. Propose the MCP servers needed to observe and interact with our live runtime environment (e.g., browser/Playwright, container runtime, database, or engine).
3. **Code Topology *(Optional — Graphify)*:** If `graphify-mcp` is recommended (or if the codebase is medium/large), ask whether the human wants local `--code-only` Graphify AST topology enabled:
   - Install once per machine: `uv tool install "graphifyy[mcp]"`
   - Add a repo-root `.graphifyignore` restricting scope to source code folders
   - Add `graphify-out/` to `.gitignore` and build locally with `graphify extract . --code-only`
   - Register the MCP server from `profiles/templates/mcp-graphify.json` in `.mcp.json` / `.cursor/mcp.json`
4. If any step requires manual assistance from me (such as installing global packages, downloading binaries, or configuring IDE permissions), explicitly state what you need me to do.
5. Wait for my confirmation that tooling is ready before moving to Phase 3.

---

## Phase 3: AI Stack Activation (Specialist Workforce & Engineering Disciplines)

Immediately after tooling is ready:

1. **Activate Specialist AI Workforce (Agency Agents):**
   - Audit `00_PROJECT.md` and `50_ROADMAP.md` alongside the profile's `recommended_agents` and any custom project needs.
   - Present the recommended Core and Milestone specialist roles with concise rationales and **ask for my confirmation**.
   - Upon confirmation, install the approved agents using the zero-app automated installer:
     ```bash
     python <genos>/guides/scripts/install_agent.py <agent_1> <agent_2> ...
     ```
     This automatically writes `.agents/skills/<slug>/SKILL.md` and `.cursor/rules/<slug>.mdc` with valid frontmatter using Python standard library alone (no desktop app required).
   - Populate `brain/60_AGENTS.md` with the active workforce roster.
2. **Activate Engineering Restraint (Ponytail):**
   - Confirm `.agents/skills/ponytail/SKILL.md` / `.cursor/rules/ponytail.mdc` is active to prevent over-engineering and code bloat.
3. **Activate Code Topology *(if enabled in Phase 2)*:**
   - Confirm `.agents/skills/graphify/SKILL.md` / `.cursor/rules/graphify.mdc` is active.
4. **Activate Execution Rigor (Superpowers):**
   - Confirm pre-packaged Superpowers skills (`brainstorming`, `writing-plans`, `test-driven-development`, `verification-before-completion`) are available.
5. Present the configured AI Stack and wait for my confirmation before proceeding to Phase 4.

---

## Phase 4: Integrity Verification & Day 0 Handoff

1. Run the **Brain Doctor self-check**:
   - Verify `brain/20_PROGRESS.yaml` is valid YAML and points to the first active milestone in `50_ROADMAP.md`.
   - Verify index tables in `50_ROADMAP.md` and `30_DECISIONS.md` are synchronized.
   - Verify system files exist in `brain/systems/`.
2. **Workspace Hygiene (Prune Unused Profiles):**
   - Delete the unused profile folders in `profiles/`, keeping only `profiles/README.md`, `profiles/templates/` (if Graphify is used), and our active profile (e.g., `profiles/<selected-profile>/`), so the project repository stays clean and unbloated.
3. **CRITICAL GUARDRAIL:** HALT immediately. Do NOT begin writing implementation code, scaffolding mock files, or executing milestones in this chat session.
4. Print the Day 0 Completion Banner:

```markdown
🎉 Day 0 Setup Complete!
All project memory is locked into the Brain, runtime tools are configured, and the roadmap is active.

To keep context windows 100% clean and avoid context rot:
1. Close this chat session.
2. Open a fresh chat in your IDE whenever you are ready to build Milestone 1.
3. Either type `kickoff` / `batch` or paste:
   - `kickoff` or `guides/prompts/workflow-kickoff.md` (for interactive, step-by-step development)
   - `batch` or `guides/prompts/workflow-batch.md` (for uninterrupted, hands-free batch development)
```
