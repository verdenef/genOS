# genOS Framework Auto-Updater

> **Primary trigger:** Type `update` in any AI chat where genOS is loaded.
> **Alternative trigger:** `@update.md` for explicit confirmation.
> **Full protocol definition:** `AGENTS.md` → Framework Update Protocol

You are executing the genOS Framework Auto-Updater. Safely update this project's genOS framework to the latest official release while strictly shielding the Project Brain.

---

## Instructions

Follow the Framework Update Protocol from AGENTS.md strictly:

1. **Smart Fetch (Dual-Method):**
   - **Git Upstream Method:** If this repository tracks an upstream remote for `verdenef/genOS`, fetch the latest release from `main`.
   - **Direct Archive Fetch Method:** If no upstream git remote exists, use your terminal tool (`curl` / PowerShell `Invoke-WebRequest`) to download and extract `https://github.com/verdenef/genOS/archive/refs/heads/main.zip` into a temporary directory `_genOS_Update/`.
   - **Local Drop-in:** If `_genOS_Update/` was manually provided, use it directly.

2. **Strict Brain Shield (Zero Data Loss):**
   - **DO NOT TOUCH** `brain/` under any circumstances (`00_PROJECT.md`, `20_PROGRESS.yaml`, `30_DECISIONS.md`, `40_BACKLOG.md`, `50_ROADMAP.md`, `60_AGENTS.md`, and all `brain/systems/*.md`).
   - **DO NOT TOUCH** `.obsidian/` configuration.
   - **DO NOT TOUCH** custom profiles in `profiles/`.
   - **DO NOT TOUCH** project source code.

3. **Framework Synchronization:**
   - Update `AGENTS.md` (kernel).
   - Update `guides/guide.md` and reference prompts in `guides/prompts/`.
   - Update standard profiles in `profiles/`.
   - Update pre-packaged `.agents/skills/` and `.cursor/rules/`.

4. **Self-Audit & Cleanup:**
   - Delete `_genOS_Update/` temporary files.
   - Run the genOS Brain Doctor to verify that existing brain memory conforms to the upgraded kernel.
   - Print the Upgrade Health Report:

```markdown
🎉 genOS Upgraded Successfully!

| Component | Status | Details |
|:---|:---:|:---|
| Kernel (`AGENTS.md`) | ✅ | Upgraded to latest version |
| Guides & Prompts | ✅ | Refreshed to latest standards |
| Project Brain (`brain/`) | 🛡️ | 100% Preserved & untouched |
| Brain Doctor Audit | ✅ | All sanity checks passing |
```
