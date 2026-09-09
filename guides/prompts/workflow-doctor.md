You are running the genOS Brain Doctor. Your purpose is to diagnose and repair integrity issues across the Project Brain.

Follow AGENTS.md strictly.

## Diagnostic Checklist

Perform a comprehensive inspection of all Project Brain files:

1. **YAML Validity (`brain/20_PROGRESS.yaml`):**
   - Verify the file is strictly valid YAML.
   - Confirm all required top-level keys exist: `current_milestone`, `working_on`, `systems_in_scope`, `blockers`, `session_summary`, `last_agent`, `last_ide`.
   - Confirm `working_on` is either `null` or lists only active tasks for the current session.

2. **Milestone Pointer Integrity (`brain/50_ROADMAP.md` vs `brain/20_PROGRESS.yaml`):**
   - Check whether `current_milestone` in `20_PROGRESS.yaml` points to an actual milestone ID that exists in `50_ROADMAP.md`.
   - Confirm that the referenced milestone status in `50_ROADMAP.md` is `active` (not `done` or `cancelled`).

3. **Index Synchronization:**
   - **Roadmap:** Verify that every milestone in `50_ROADMAP.md` has an entry in the Roadmap Index table at the top of the file, and that the statuses (`planned`, `active`, `done`, `cancelled`) match.
   - **Decisions:** Verify that every decision header in `brain/30_DECISIONS.md` matches its corresponding row in the Decisions Index table.

4. **Single Source of Truth & No State Leakage:**
   - Confirm `brain/40_BACKLOG.md` does NOT contain in-progress ("Doing") tasks or duplicates of milestone deliverables.
   - Confirm `brain/00_PROJECT.md` is not empty (unless uninitialized).

5. **System Scopes Integrity (`brain/systems/`):**
   - Confirm every identifier listed in `PROGRESS.systems_in_scope` has a matching `.md` file inside `brain/systems/`.
   - Confirm `brain/systems/README.md` lists all system files without displaying a status column (status is owned exclusively by the individual system files).

---

## Action Instructions

1. If any syntax errors, desynced index tables, or broken milestone pointers are found:
   - **Automatically repair them.** Fix broken formatting, re-sync index tables to match actual content, and correct invalid pointers.
2. If any human intent decisions or scope questions are unresolved:
   - Stop and present the issue clearly to the user.
3. Output the **Brain Health Report**:

```markdown
### genOS Brain Health Report

| Component | Status | Details |
| :--- | :---: | :--- |
| `00_PROJECT.md` | [✓ / ⚠ / ✗] | [Status description] |
| `20_PROGRESS.yaml` | [✓ / ⚠ / ✗] | [YAML validity & current milestone ID] |
| `30_DECISIONS.md` | [✓ / ⚠ / ✗] | [Decisions count & index sync status] |
| `40_BACKLOG.md` | [✓ / ⚠ / ✗] | [Queue health & leakage check] |
| `50_ROADMAP.md` | [✓ / ⚠ / ✗] | [Milestones count & active milestone status] |
| `brain/systems/` | [✓ / ⚠ / ✗] | [Systems count & scope verification] |
```

If all checks pass, confirm that the Brain is pristine and ready for daily operations.
