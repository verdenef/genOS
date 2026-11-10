# Kickoff — Reference & Alternative Trigger

> **Primary trigger:** Type `kickoff` in any AI chat where genOS is loaded.
> **Alternative trigger:** `@workflow-kickoff.md` for explicit confirmation.
> **Full protocol definition:** `AGENTS.md` → Commands → `kickoff`

This file provides detailed reference for the kickoff workflow and serves as an alternative trigger mechanism.

---

Begin the next development cycle using genOS.

Follow AGENTS.md exactly.

BOOT the project from the Project Brain.

Determine the active milestone from the Project Brain.

Before writing any code:

1. Summarize your understanding of the current project state.
2. Identify the active milestone.
3. Explain why it is the next milestone.
4. **Hard Persona Gate (Mandatory Tool Call):**
   - Check `brain/60_AGENTS.md` for designated specialist roles.
   - Use your file viewing tool to read the agent's full definition file (e.g., `.agents/skills/<agent>/SKILL.md` or `.cursor/rules/<agent>.mdc`).
   - In your response, explicitly cite the file path you inspected and list 2–3 governing rules or anti-patterns from that skill that will dictate how you implement this milestone.
4b. **Code Topology Check (Optional):** If Graphify is available, inspect call chains and blast radius for in-scope components before proposing task breakdowns (otherwise proceed with standard file tools).
5. Present a concise implementation plan that strictly adheres to those cited agent rules.
6. Identify any architectural risks or dependencies.
7. State your **Model & Session recommendation** per AGENTS.md (e.g. "💡 Recommended: [Platform Model] (Thinking/Effort: [Level]) in a [new/continued] session.").
8. Provide **copy-pasteable execution command blocks** so the user can easily copy and paste into the new session:
   - Standard execution:
     ```
     kickoff execute the approved plan: <path-to-plan>
     ```
   - Subagent-driven execution:
     ```
     kickoff execute the approved plan: <path-to-plan> using subagent-driven-development
     ```
9. Wait for my approval before modifying the implementation.

## Variants

- `kickoff` — standard milestone kickoff (or resume if mid-work)
- `kickoff <intent>` — scoped session with user-directed goal
- `kickoff tooling` — reconfigure MCP servers (reads profile's `recommended_mcps`)
- `kickoff workforce` — reconfigure AI workforce (follows `integrations/agency_agents.md`)

Rules:
- Do not skip BOOT.
- Do not use chat history as project memory.
- Treat the Project Brain as authoritative.
- Do not begin future milestones.
- Only implement the current milestone after approval.
