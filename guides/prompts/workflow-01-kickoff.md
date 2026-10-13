Begin the next development cycle using genOS.

Follow AGENTS.md exactly.

BOOT the project from the Project Brain.

Determine the active milestone from the Project Brain.

Before writing any code:

1. Summarize your understanding of the current project state.
2. Identify the active milestone.
3. Explain why it is the next milestone.
4. **Identify and Load Agency Agents (Mandatory Tool Call):**
   - Check `brain/60_AGENTS.md` for designated specialist roles.
   - Use your file viewing tool to read the agent's full definition file (e.g., `.agents/skills/<agent>/SKILL.md` or `.cursor/rules/<agent>.mdc`).
   - In your response, explicitly cite the file path you inspected and list 2–3 governing rules or anti-patterns from that skill that will dictate how you implement this milestone.
5. Present a concise implementation plan that strictly adheres to those cited agent rules.
6. Identify any architectural risks or dependencies.
7. Wait for my approval before modifying the implementation.

Rules:
- Do not skip BOOT.
- Do not use chat history as project memory.
- Treat the Project Brain as authoritative.
- Do not begin future milestones.
- Only implement the current milestone after approval.
- **Hard Persona Gate:** You must physically read the Agency Agent definition file using your file viewing tool before presenting the plan; do not guess or rely on generic assumptions when a specialist skill definition exists on disk.
