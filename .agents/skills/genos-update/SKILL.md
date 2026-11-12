---
name: genos-update
description: "Verify whether genOS is outdated, propose an Upgrade & Migration Plan, wait for approval, and safely upgrade while shielding the Project Brain."
---

# genOS Update

Execute the `update` command as defined in `AGENTS.md` → Framework Update Protocol (or `guides/prompts/update.md` for self-contained legacy `v1`/`v2` upgrades).

Follow the 5-phase protocol strictly: smart fetch upstream `verdenef/genOS` (read-only), verify drift against local files (stop cleanly if already up to date, emitting a 1-line `kickoff tooling` tip if an existing codebase lacks Graphify), present the Upgrade & Migration Plan (core files, obsolete v1/v2 prompts, root discovery files, approval-gated Graphify setup recommendation if an existing coding codebase lacks code topology, and strict shields for `brain/` and project Agency Agents) and **wait for human approval**, apply approved core updates cleanly, and run the Doctor health check using the newly updated `AGENTS.md`.
