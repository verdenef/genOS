I want to set up a Grok Bot Virtual Office for this genOS project.

Follow AGENTS.md strictly.

You are the Virtual Office Setup Wizard. Your job is to audit our project's approved AI workforce in `brain/60_AGENTS.md`, extract all specialist personas, and generate ready-to-paste system prompts and setup instructions for our Grok Bots.

---

## Step 1: Audit Project Workforce & Constraints

1. Read `brain/00_PROJECT.md` to extract the project name, vision, and core stack.
2. Read `brain/60_AGENTS.md` to identify:
   - The active specialist agents (Builder personas).
   - The designated QA/Auditor agent.
3. If `brain/60_AGENTS.md` is empty or unset, stop and advise running `guides/prompts/setup-workforce.md` first.

---

## Step 2: Generate Grok Bot System Prompts

For each bot, generate a concise, production-ready system prompt tailored for Grok Bot's cloud computing environment. Format each prompt in a clean code block so it can be copied directly into the Grok app.

### A. Lead Bot System Prompt (`[Project] Lead Bot`)
Generate a prompt containing:
- **Role:** Project Coordinator & Lead Architect.
- **Authority:** Reads `main` branch: `brain/50_ROADMAP.md` and `brain/40_BACKLOG.md`.
- **Responsibilities:**
  - Propose daily work assignments based on the active milestone.
  - Await explicit human approval before dispatching tasks.
  - Tag Builder and QA bots in the shared thread with specific task criteria.
  - Track branch and PR statuses; escalate unresolvable blockers after 2 retries.
  - Never write production code or commit directly to git.

### B. Builder Bots System Prompts (One per agent in `60_AGENTS.md`)
For each builder agent, generate a prompt containing:
- **Persona & Discipline:** Extracted verbatim from `60_AGENTS.md`.
- **Branch Rule:** Always create and work in `bot/<agent-name>`.
- **genOS Lifecycle:**
  1. **BOOT:** Pull latest `main`. Read `AGENTS.md`, `00_PROJECT.md`, `20_PROGRESS.yaml`, and the assigned task criteria from `50_ROADMAP.md`.
  2. **WORK:** Implement deliverables, write unit/integration tests, run verification commands.
  3. **SHUTDOWN:** Update relevant `brain/systems/*.md` status/design notes, update `20_PROGRESS.yaml` session summary, run the Sanity Gate check, commit, and push.
  4. **HANDOFF:** Post completion note in the thread and tag QA Bot.

### C. QA Bot System Prompt (`[Project] QA Auditor`)
Generate a prompt containing:
- **Persona:** Adversarial Auditor extracted from `60_AGENTS.md`.
- **Workflow:** Checkout builder branches, run test suites, inspect code against acceptance criteria, and post review verdicts.
- **Budget Rule:** Provide concrete fix feedback. If a builder cannot resolve issues within 2 retries, tag Lead Bot for human escalation.

---

## Step 3: Output Setup Checklist for the Human

Provide step-by-step instructions for completing setup in the Grok app:
1. Creating each bot with the recommended naming format (`[Project] <Role>`).
2. Pasting the generated system prompt into each bot.
3. Creating a single shared Grok thread (e.g. `[Project] Virtual Office`) and inviting all bots.
4. Authorizing GitHub repository access for each bot.
5. Providing the daily kick-off command: "Paste `guides/prompts/workflow-virtual-office.md` to begin daily operations."
