I have just copied the GameOS folder into my project repository. We are bringing GameOS into an existing, in-progress codebase.

Follow AGENTS.md exactly.

Instructions:

1. Scan the repository structure. Acknowledge that this repository already contains implementation source code and assets.
2. Verify that the GameOS `brain/` directory and `AGENTS.md` are present.
3. Stop and ask me to provide the project intent, vision, scope, and target platform. Do NOT attempt to guess the vision from the existing code.
4. Wait for me to provide the project context.
5. Once I provide the context, use it to populate `00_PROJECT.md` via the Empty Brain Protocol.
6. After `00_PROJECT.md` is saved, intelligently scan the existing source code and reverse-engineer it into the Project Brain:
   - Generate necessary `brain/systems/*.md` documents to map the existing code to the GameOS architecture.
   - Populate `50_ROADMAP.md` reflecting what has already been built (past milestones marked as done) and defining the next planned milestone.
7. **CRITICAL:** HALT immediately after saving the Brain. Do NOT begin writing implementation code, modifying existing scripts, or executing any milestones. Day 0 setup is not finished yet.
8. Announce that onboarding is complete and tell me to proceed to `guides/prompts/setup-02-mcp.md` for engine MCP configuration.
