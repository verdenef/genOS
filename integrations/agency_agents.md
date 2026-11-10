# AI Workforce Protocol (Agency Agents Integration)

This document defines the standard protocol for recommending and assembling an AI workforce using specialist agents.

## When to Execute
Do not evaluate or recommend an AI workforce until the project vision (`00_PROJECT.md`) and initial milestones (`50_ROADMAP.md`) are well-defined. 

## The Protocol

When tasked with assembling or reviewing the AI workforce, the AI must follow these exact steps:

1. **Audit the Project:** Read `00_PROJECT.md`, `50_ROADMAP.md`, and `30_DECISIONS.md`. Determine the specific technical disciplines, workflows, and skills required for the project.
2. **Locate the Catalog:** Browse or query the available Agency Agents catalog from the official repository (`https://github.com/msitarzewski/agency-agents`).
   - genOS relies directly on `msitarzewski/agency-agents` as its official source for specialized agent personas, workflows, and skills.
   - Stack profiles in `profiles/` specify recommended agent paths from this catalog.
   - Query or search available upstream agents with the built-in installer:
     ```bash
     python <genos>/guides/scripts/install_agent.py --list [keyword]
     ```
     *(e.g., `python guides/scripts/install_agent.py --list unity` or `python guides/scripts/install_agent.py --list backend`)*
   - Inspect already-installed agents in `.agents/skills/` and `.cursor/rules/`.
3. **Formulate Recommendations:** Based on the audit and the catalog, group recommended agents into the following categories:
   - **Core Agents:** Essential for the life of the project.
   - **Milestone Agents:** Needed only for the current active milestone.
   - **Optional Specialists:** Beneficial but not strictly required.
   - **Unnecessary Agents:** Explicitly state which agents in the catalog should be avoided (e.g., to reduce noise or because they don't fit the stack).
4. **Explain the Rationale:** Provide a clear reason for *every* recommendation.
5. **Wait for Approval (Mandatory Human Gate):** Present the recommendations to the human. **Never auto-install before approval.** The human operator must approve the agent roster before any installation command runs.
6. **Automated Installation (Zero-App Installer):** Once approved by the human, install the agents using the zero-dependency Python script:
   ```bash
   python <genos>/guides/scripts/install_agent.py <agent_ref_1> [<agent_ref_2> ...]
   ```
   *(e.g., `python guides/scripts/install_agent.py game-development/unity-developer engineering/backend-architect`)*
   - Accepts `<category>/<slug>.md`, short IDs, GitHub blob URLs, or raw URLs.
   - Automatically writes verbatim markdown with valid YAML frontmatter to both:
     - `.agents/skills/<slug>/SKILL.md` (for Claude Code, Antigravity, and portable on-disk skills)
     - `.cursor/rules/<slug>.mdc` (for Cursor IDE)
   - Zero external dependencies: uses only Python 3 standard library modules (no desktop app, no pip install).
   - Use `--force` to overwrite existing files if an agent needs updating.
   - **Offline / Manual Fallback:** If offline or Python is unavailable, manually download raw markdown from `https://github.com/msitarzewski/agency-agents/tree/main/<category>/<agent>.md` and save it to `.agents/skills/<slug>/SKILL.md` and `.cursor/rules/<slug>.mdc`.
7. **Update the Brain:** Once installed, record the active workforce in `brain/60_AGENTS.md`.

## Lifecycle Maintenance
The AI must periodically re-evaluate this workforce recommendation whenever the project scope (`00_PROJECT.md`) or the roadmap (`50_ROADMAP.md`) changes significantly. When changing active milestones, prompt the human before installing newly needed Milestone Agents or retiring completed ones.
