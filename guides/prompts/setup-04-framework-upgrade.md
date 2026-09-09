I have downloaded the latest genOS framework release and placed it in a temporary folder named `_genOS_Update/` in the root of my repository.

Your task is to safely upgrade this project's existing framework (whether upgrading an older GameOS or a previous genOS version) to the latest genOS framework.

Requirements:

1. **Compare Framework Directories:**
   - Compare the active `genOS/` (or `GameOS/`) folder against `_genOS_Update/`.
   - Identify new framework files (e.g. `profiles/`, new prompts, `workflow-doctor.md`).
   - Identify updated framework files (e.g. `AGENTS.md` kernel updates, `guides/guide.md`).
2. **STRICT PRESERVATION OF THE PROJECT BRAIN:**
   - **Never** overwrite or delete any file in `brain/` (`00_PROJECT.md`, `20_PROGRESS.yaml`, `30_DECISIONS.md`, `40_BACKLOG.md`, `50_ROADMAP.md`, `60_AGENTS.md`, and all `brain/systems/*.md`).
   - All existing milestones, tasks, decisions, progress RAM, and architectural documents must remain 100% intact.
3. **Migration & Compatibility:**
   - If upgrading an existing game project from GameOS, configure the project to use the `profiles/gamedev/` profile. Prune the other unused profiles (`web-fullstack`, `mobile`, etc.) so their game project remains clean and focused.
   - If the folder was named `GameOS/`, offer to update the name to `genOS/` or maintain location-agnostic compatibility as defined in `AGENTS.md`.
4. **Automated Sanity Audit:**
   - Run the Brain Doctor check (`workflow-doctor.md`) on the project's Brain to confirm that the existing memory is 100% compatible and valid under the new kernel.
5. **Approval Gate:**
   - Present a concise diff summary of what will be updated.
   - Wait for my explicit approval before modifying any files or deleting the temporary `_genOS_Update/` folder.
