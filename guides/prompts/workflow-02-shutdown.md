The current milestone has been successfully implemented and verified.

Perform the GameOS SHUTDOWN procedure.

Instructions:

1. Verify that the milestone satisfies every completion criterion in the ROADMAP.
2. Update ONLY the necessary GameOS files.
3. Update affected SYSTEMS documents to reflect the implementation.
4. Update ROADMAP:
   - mark the milestone as done
   - activate the next milestone
5. Update PROGRESS:
   - execution state only
   - systems_in_scope
   - working_on
   - blocked
   - session_summary
   - timestamps
6. If implementation required a permanent architectural decision,
   propose a DEC and explain why before creating it.
7. **Sanity Gate (Mandatory Integrity Audit):**
   - Verify `20_PROGRESS.yaml` is parseable YAML and all required keys exist.
   - Verify `current_milestone` points to an active milestone ID in `50_ROADMAP.md`.
   - Confirm index tables in `50_ROADMAP.md` and `30_DECISIONS.md` match section headers.
   - Confirm `40_BACKLOG.md` has no "Doing" tasks or milestone duplicates.
   - Confirm all `systems_in_scope` exist in `brain/systems/`.
8. Do NOT modify PROJECT.md.
9. Do NOT modify unrelated systems.
10. Produce a concise milestone report containing:
   - milestone completed
   - files changed
   - systems updated
   - technical debt introduced
   - recommendations for the next milestone

Do not modify implementation source code during SHUTDOWN.
Only update GameOS brain files.
