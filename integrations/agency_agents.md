# AI Workforce Protocol (Agency Agents Integration)

This document defines the standard protocol for recommending and assembling an AI workforce using specialist agents.

## When to Execute
Do not evaluate or recommend an AI workforce until the project vision (`00_PROJECT.md`) and initial milestones (`50_ROADMAP.md`) are well-defined. 

## The Protocol

When tasked with assembling or reviewing the AI workforce, the AI must follow these exact steps:

1. **Audit the Project:** Read `00_PROJECT.md`, `50_ROADMAP.md`, and `30_DECISIONS.md`. Determine the specific technical disciplines, workflows, and skills required for the project.
2. **Locate the Catalog:** Read the available Agency Agents catalog from the official repository (`https://github.com/msitarzewski/agency-agents`). 
   - genOS relies directly on `msitarzewski/agency-agents` as its official source for specialized agent personas, workflows, and skills.
   - Stack profiles in `profiles/` link directly to exact agent files from this repository.
   - You may also check for locally installed agents in folders like `.agents/` or `skills/`.
3. **Formulate Recommendations:** Based on the audit and the catalog, group recommended agents into the following categories:
   - **Core Agents:** Essential for the life of the project.
   - **Milestone Agents:** Needed only for the current active milestone.
   - **Optional Specialists:** Beneficial but not strictly required.
   - **Unnecessary Agents:** Explicitly state which agents in the catalog should be avoided (e.g., to reduce noise or because they don't fit the stack).
4. **Explain the Rationale:** Provide a clear reason for *every* recommendation.
5. **Wait for Approval:** Present the recommendations to the human. **Never auto-install agents.**
6. **Manual Installation:** Wait for the human to manually install the approved agents.
7. **Update the Brain:** Once installed and approved, record the active workforce in `brain/60_AGENTS.md`.

## Lifecycle Maintenance
The AI must periodically re-evaluate this workforce recommendation whenever the project scope (`00_PROJECT.md`) or the roadmap (`50_ROADMAP.md`) changes significantly.
