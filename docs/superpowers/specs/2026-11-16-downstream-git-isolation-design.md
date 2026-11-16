# Design: Downstream genOS Sidecar Git Isolation

**Goal:** Ensure that when genOS is installed as a sidecar (`genOS/`) in downstream project repositories, only `genOS/brain/` (and its `.gitignore`) is tracked and pushed to GitHub. All framework scaffolding (`guides/`, `profiles/`, `templates/`, `integrations/`, `AGENTS.md`, `README.md`, etc.) remains local and completely ignored by Git.

---

## 1. Context & Motivation

Downstream projects adopting genOS typically clone or download the framework into a `genOS/` subfolder. When developers or autonomous AI agents perform git commits (`git commit -am`, `git add .`), Git recursively stages the entire `genOS/` directory.

This causes:
1. Clutter in the user's project repository on GitHub (guides, test scripts, templates, stack profiles).
2. Merge conflicts when upstream genOS updates are downloaded.
3. Confusion over what constitutes project memory versus framework internals.

In a downstream project, **only `genOS/brain/` represents project-specific semantic truth**. Everything else is transient framework scaffolding.

---

## 2. Technical Architecture: Nested `.gitignore`

Git natively supports directory-level `.gitignore` files. When a `.gitignore` resides inside a subdirectory like `genOS/`, Git scopes its rules relative to that subdirectory.

### The Sidecar `.gitignore` Pattern

A template file `templates/sidecar.gitignore` will be added to genOS with the following rules:

```gitignore
# Ignore all framework scaffolding in downstream genOS sidecars
/*

# Whitelist project-specific memory and this ignore file
!/brain/
!/.gitignore
```

### Why this rule structure works:
- `/*` instructs Git to ignore every top-level file and directory inside `genOS/` (e.g. `AGENTS.md`, `guides/`, `profiles/`, `templates/`, `integrations/`, `README.md`).
- `!/brain/` un-ignores the `brain/` directory, allowing Git to descend into `genOS/brain/` and track all project memory (`00_PROJECT.md`, `20_PROGRESS.yaml`, `30_DECISIONS.md`, `40_BACKLOG.md`, `50_ROADMAP.md`, `60_AGENTS.md`, `systems/`).
- `!/.gitignore` ensures the `.gitignore` itself is tracked so the ignore rule persists across clones and team members.

---

## 3. Integration Touchpoints

### 3.1. Template Distribution
- **Add:** `templates/sidecar.gitignore` in the genOS core repository.

### 3.2. Setup Prompt Automation (`guides/prompts/setup-init.md`)
- In Phase 1 Step 1 (`Clean Slate & Layout Check`), add an automatic check:
  - When genOS is located in a subdirectory (e.g., `genOS/`), verify that `genOS/.gitignore` exists. If not, copy `templates/sidecar.gitignore` (or generate it) into `genOS/.gitignore` so downstream git commits are immediately shielded.

### 3.3. Documentation Alignment
- **`README.md` & `guides/guide.md` (Day 0 Installation Snippets):**
  - Update the 1-Prompt Auto-Install command block to copy `templates/sidecar.gitignore` as `genOS/.gitignore`.
  - Add a short tip for existing projects: how to untrack existing framework scaffolding without deleting local files:
    ```bash
    git rm -r --cached genOS/guides genOS/profiles genOS/templates genOS/integrations genOS/AGENTS.md genOS/README.md 2>/dev/null
    ```

---

## 4. Verification & Testing

1. **Unit / Structural Verification:**
   - Verify `templates/sidecar.gitignore` contains exact allowlist rules.
   - Test Git ignore behavior in a simulated nested repo: confirm `git status` shows `genOS/brain/` as untracked/modified, but completely ignores `genOS/guides/` and `genOS/AGENTS.md`.
2. **Doctor Audit:**
   - Ensure the new template does not break any Brain Doctor checklist items.
3. **Framework Update Shielding:**
   - Ensure `AGENTS.md` Framework Update Protocol respects `genOS/.gitignore` during upgrades.
