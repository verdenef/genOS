I have downloaded the latest genOS framework release and placed it in a temporary folder named `_genOS_Update/` in the root of my repository.

Your task is to safely upgrade this project's existing framework (whether upgrading an older GameOS or a previous genOS version) to the latest genOS framework.

Requirements:

1. **Compare Framework Directories & Prune Obsolete Files:**
   - Compare the active `genOS/` (or `GameOS/`) folder against `_genOS_Update/`.
   - Identify new and updated framework files (e.g. `profiles/`, `setup-init.md`, `setup-tooling.md`, `setup-workforce.md`, `workflow-autonomous-batch.md`, `workflow-doctor.md`).
   - Identify and **delete obsolete framework files** that no longer exist in the new release (such as deprecated `setup-01-project-onboarding.md`, `setup-01b-existing-project.md`, `setup-02-mcp.md`, and `setup-03-workforce.md`).
   - **Do NOT** flag custom user profiles in `profiles/` (e.g. `profiles/desktop-automation/`) as obsolete just because they aren't in the official update folder.
2. **STRICT PRESERVATION OF THE PROJECT BRAIN & USER DATA:**
   - **Never** overwrite or delete any file in `brain/` (`00_PROJECT.md`, `20_PROGRESS.yaml`, `30_DECISIONS.md`, `40_BACKLOG.md`, `50_ROADMAP.md`, `60_AGENTS.md`, and all `brain/systems/*.md`).
   - **Never** delete or modify the `.obsidian/` directory if it exists.
   - **Never** delete the project's active custom `profiles/` folder.
   - All existing milestones, tasks, decisions, progress RAM, and architectural documents must remain 100% intact.
3. **Migration & Compatibility:**
   - If upgrading an existing game project from GameOS, configure the project to use the `profiles/gamedev/` profile. Prune the other unused profiles (`web-fullstack`, `mobile`, etc.) so their game project remains clean and focused.
   - If the folder was named `GameOS/`, offer to update the name to `genOS/` or maintain location-agnostic compatibility as defined in `AGENTS.md`.
4. **Automated Sanity Audit:**
   - Run the Brain Doctor check (`workflow-doctor.md`) on the project's Brain to confirm that the existing memory is 100% compatible and valid under the new kernel.
5. **Approval Gate:**
   - Present a concise diff summary of what will be updated and what obsolete files will be removed.
   - Wait for my explicit approval before modifying any files or deleting the temporary `_genOS_Update/` folder.
