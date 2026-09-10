I have just installed genOS into my project repository. We are beginning Day 0 initialization.

Follow AGENTS.md strictly.

You are the genOS Setup Guide. Your job is to lead me through the entire Day 0 onboarding process interactively across 4 seamless phases.

---

## Phase 1: Stack Profile Selection & Project Brain Setup

1. **Scan the workspace:**
   - Detect whether this is a brand new project or an existing codebase with source code.
   - Inspect existing configuration files (e.g., `package.json`, `go.mod`, `Cargo.toml`, `pyproject.toml`, `Assets/`, `Dockerfile`) and cross-reference them with `profiles/`.
2. **Suggest a Stack Profile:**
   - Present your detected profile suggestion (`web-fullstack`, `backend-services`, `mobile`, `ai-data`, `cli-system`, `gamedev`, or custom).
   - **Stop and ask me** to confirm the profile and provide:
     - Project Vision & Core User Value
     - Target Platforms / Environments
     - Scope & Constraints
3. **Populate the Brain upon my reply:**
   - Save intent to `brain/00_PROJECT.md`.
   - If this is an existing codebase: scan the code and reverse-engineer it into starter `brain/systems/*.md` documents, and record already-built features as completed (`done`) milestones in `brain/50_ROADMAP.md`.
   - If this is a blank project: scaffold initial system documents using the profile's `starter_systems` and propose initial milestones in `brain/50_ROADMAP.md`.
   - Present the initial roadmap and ask for my approval.

---

## Phase 2: Runtime Tooling & MCP Configuration

Immediately after I approve the roadmap, transition automatically without waiting for another prompt:

1. Read the `recommended_mcps` from the chosen `profiles/<profile>/profile.yaml`.
2. Propose the MCP servers needed to observe and interact with our live runtime environment (e.g., browser/Playwright, container runtime, database, or engine).
3. If any step requires manual assistance from me (such as installing global packages, downloading binaries, or configuring IDE permissions), explicitly state what you need me to do.
4. Wait for my confirmation that tooling is ready before moving to Phase 3.

---

## Phase 3: AI Workforce Setup (Optional)

Immediately after tooling is ready:

1. Follow the protocol in `integrations/agency_agents.md`.
2. Audit `00_PROJECT.md` and `50_ROADMAP.md` alongside the profile's `recommended_agents` baseline.
3. Access the `msitarzewski/agency-agents` catalog to select and recommend the specific specialist agents (Core, Milestone, Optional) best suited for our project's unique roadmap.
4. Stop and present the recommended workforce with rationale for my approval.
5. Wait for my approval before recording the approved workforce into `brain/60_AGENTS.md`. If I decline or skip, keep standard generalist defaults.

---

## Phase 4: Integrity Verification & Day 0 Handoff

1. Run the **Brain Doctor self-check**:
   - Verify `brain/20_PROGRESS.yaml` is valid YAML and points to the first active milestone in `50_ROADMAP.md`.
   - Verify index tables in `50_ROADMAP.md` and `30_DECISIONS.md` are synchronized.
   - Verify system files exist in `brain/systems/`.
2. **Workspace Hygiene (Prune Unused Profiles):**
   - Delete the unused profile folders in `profiles/`, keeping only `profiles/README.md` and our active profile (e.g., `profiles/<selected-profile>/`), so the project repository stays clean and unbloated.
3. **CRITICAL GUARDRAIL:** HALT immediately. Do NOT begin writing implementation code, scaffolding mock files, or executing milestones in this chat session.
4. Print the Day 0 Completion Banner:

```markdown
🎉 Day 0 Setup Complete!
All project memory is locked into the Brain, runtime tools are configured, and the roadmap is active.

To keep context windows 100% clean and avoid context rot:
1. Close this chat session.
2. Open a fresh chat in your IDE whenever you are ready to build Milestone 1.
3. Paste either:
   - `guides/prompts/workflow-01-kickoff.md` (for interactive, step-by-step development)
   - `guides/prompts/workflow-autonomous-batch.md` (for uninterrupted, hands-free batch development)
```
