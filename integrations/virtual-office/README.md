# genOS Virtual Office Integration

The genOS Virtual Office turns Grok Bot's cloud agent platform into a persistent, semi-autonomous development team for any genOS project. Each Agency Agent defined in `brain/60_AGENTS.md` maps to a dedicated Grok Bot, coordinated by a designated **Lead Bot**.

All durable project state flows strictly through the genOS Project Brain (`brain/`) via git branches and PR reviews, preserving the single-source-of-truth guarantee with zero memory drift.

---

## 1. Overview

- **genOS is the Brain:** Grok Bots are compute workers, not memory holders. Durable decisions, system invariants, and progress pointers live only in your repository's `brain/` directory.
- **Semi-Autonomous Execution:** The Lead Bot proposes daily work assignments based on `50_ROADMAP.md`. You approve the plan in the Grok app, and the bots execute autonomously.
- **Git Branch Isolation:** Every bot works in its own branch (`bot/<agent-name>`), pushes commits to GitHub, and submits pull requests for your review.
- **Obsidian Graph Sync:** When PRs are merged to `main`, pulling locally automatically updates your Obsidian Graph View.

---

## 2. Prerequisites

1. **Grok Bot App:** Installed on your phone, tablet, or desktop with an active subscription.
2. **GitHub Repository:** Your genOS project repository pushed to GitHub.
3. **Active Workforce:** Specialist agents defined in `brain/60_AGENTS.md` (or configured via `setup-workforce.md`).
4. **GitHub Access for Grok Bots:** Grant Grok Bot repository access (read/write) so bots can clone, create branches, and push commits.

---

## 3. Architecture & Data Flow

```
┌────────────────────────────────────────┐
│        Grok Bot Remote App             │
│  (Human reviews & approves proposals)  │
│                                        │
│   ┌────────┐                           │
│   │  Lead  │ ← Coordinator Bot         │
│   │  Bot   │                           │
│   └───┬────┘                           │
│       │ dispatches tasks via chat      │
│   ┌───┴────┐       ┌───────┐           │
│   │Builder │       │  QA   │           │
│   │  Bot   │       │  Bot  │           │
│   └───┬────┘       └───┬───┘           │
└───────┼────────────────┼───────────────┘
        │ git push       │ git review
        ▼────────────────▼
┌────────────────────────────────────────┐
│           GitHub Repository            │
│  - main branch: genOS brain/ & code    │
│  - bot/builder branch (PR open)        │
│  - bot/qa branch (PR comments / fixes) │
└────────────────────────────────────────┘
        ▲
        │ git pull
        ▼
┌────────────────────────────────────────┐
│          Your Local Machine            │
│  - Cursor / Antigravity / Obsidian     │
└────────────────────────────────────────┘
```

---

## 4. Bot Roles & Responsibilities

### Lead Bot (Coordinator)
- **Authority:** Reads `brain/50_ROADMAP.md` and `brain/40_BACKLOG.md` on `main`.
- **Responsibilities:** Formulates daily task assignments, presents proposals to human, dispatches tasks to Builder/QA bots, monitors progress, and prepares daily handoff summaries.
- **Restrictions:** Never writes application code, modifies system files, or changes architectural decisions.

### Builder Bots (Mapped from `60_AGENTS.md`)
- **Authority:** Full read/write access to source code and relevant `brain/systems/*.md` files on their branch.
- **Branch:** `bot/<agent-name>` (e.g. `bot/unity-architect`, `bot/backend-engineer`).
- **Protocol:** Must execute the genOS BOOT sequence, implement assigned deliverables, run local tests, perform SHUTDOWN with Sanity Gate checks, and open a PR.

### QA Bot (Mapped from `60_AGENTS.md`)
- **Authority:** Read-only access to main, checkout access to Builder branches.
- **Branch:** `bot/<qa-agent-name>`.
- **Protocol:** Performs adversarial verification per `workflow-autonomous-batch.md` standards. Runs tests, inspects code quality, posts reviews on GitHub PRs, and tags Builder bots if fixes are needed (2-retry budget).

---

## 5. Branch & PR Conventions

- **Branch Naming:** `bot/<agent-name>` (e.g., `bot/lead`, `bot/frontend-dev`, `bot/qa-tester`).
- **Commit Messages:** Follow conventional commits (e.g., `feat(combat): implement hitbox collision handling`, `docs(brain): update combat system status`).
- **Pull Requests:** Titled `[Bot Work] <Task Description>`. Must include a summary of code changes, test results, and brain updates.
- **Merges:** Always squash or merge via GitHub web/mobile UI after reviewing changes.

---

## 6. Daily Operational Cycle

1. **Morning Briefing:** You prompt the Lead Bot in the project thread (`guides/prompts/workflow-virtual-office.md`). The Lead Bot inspects the roadmap and posts proposed assignments.
2. **Approval:** You reply "Approved" (or tweak the tasks).
3. **Execution:** Lead Bot tags Builder bots with clear deliverables. Builders execute in parallel on separate branches.
4. **Peer Review:** QA Bot tests each builder branch and posts approval or feedback (2-retry limit).
5. **Human Review & Merge:** You review the PRs on GitHub, merge approved branches into `main`, and your local Obsidian Graph reflects all progress.

---

## 7. Troubleshooting & Escalation

- **Merge Conflicts:** If two bots touch the same `brain/` file, the human resolves conflicts during PR merge.
- **Blocked Bots:** If a bot hits an error after 2 retries, the Lead Bot escalates to the human in the Grok thread with full error output and options.
- **Brain Integrity:** If brain files desync, paste `guides/prompts/workflow-doctor.md` into your IDE to auto-heal.
