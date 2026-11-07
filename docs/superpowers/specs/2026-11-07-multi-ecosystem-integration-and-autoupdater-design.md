# genOS Multi-Ecosystem Integration & Auto-Updater Design Spec

**Date:** 2026-11-07
**Status:** Proposed
**Branch:** `genos-v3` (incorporates and builds upon v3 overhaul)

---

## 1. Executive Summary

This specification defines the seamless integration of **Superpowers**, **Ponytail**, and **Agency Agents** into genOS under **Approach 1 (The Integrated Pipeline)**, along with a **Dual-Method 1-Click Auto-Updater**.

The core premise:
- **genOS** governs state, memory, and lifecycle (`kickoff`, `shutdown`, `doctor`, `update`).
- **Agency Agents** provides domain specialist roles and engineering invariants.
- **Ponytail** governs restraint, preventing over-engineering via the **Ladder of Restraint**.
- **Superpowers** provides rigorous execution (ideation, test-driven bite-sized plans, verification).
- **Auto-Updater** enables hands-free framework upgrades via a single `update` command or `@update.md`.

All four systems collaborate automatically without forcing the human to manually invoke separate tool syntaxes.

---

## 2. The 4-Layer Integrated Pipeline

### 2.1 Layer Responsibilities

```
┌────────────────────────────────────────────────────────┐
│  1. Memory & State: genOS                              │
│     (AGENTS.md, brain/, 20_PROGRESS.yaml, 50_ROADMAP)  │
└─────────────────────────┬──────────────────────────────┘
                          │ passes active milestone & context
                          ▼
┌────────────────────────────────────────────────────────┐
│  2. Identity & Domain: Agency Agents                   │
│     (brain/60_AGENTS.md, .cursor/rules/, .agents/)     │
└─────────────────────────┬──────────────────────────────┘
                          │ passes domain invariants & role
                          ▼
┌────────────────────────────────────────────────────────┐
│  3. Restraint & YAGNI: Ponytail                        │
│     (Ladder of Restraint: skip, reuse, stdlib, 1-line) │
└─────────────────────────┬──────────────────────────────┘
                          │ filters plan before code generation
                          ▼
┌────────────────────────────────────────────────────────┐
│  4. Execution Rigor: Superpowers                       │
│     (brainstorming, writing-plans, TDD, verification)  │
└────────────────────────────────────────────────────────┘
```

### 2.2 Lifecycle Integration Points

1. **BOOT & Kickoff:**
   - genOS BOOTs from Project Brain.
   - **Hard Persona Gate:** Reads `60_AGENTS.md` and loads active specialist persona.
   - **Ponytail Ladder Filter:** Before proposing any plan or code, evaluate:
     1. *Does this need to exist at all? (YAGNI)*
     2. *Is it already in this codebase? (Reuse)*
     3. *Does the standard library or engine native API do it?*
     4. *Can an existing dependency do it?*
     5. *Can it be written in one clean line or minimal function?*
     6. *Only then:* Propose new architectural code.
   - **Superpowers Plan Structuring:** Propose plan as bite-sized, testable tasks with exact file paths and verification commands.
2. **Implementation:**
   - Adhere strictly to specialist persona rules (e.g. no GC alloc in Unity loops, idiomatic patterns).
   - Test-Driven Development (write/verify tests before implementation).
3. **Auditing & QA (Batch / Pre-Shutdown):**
   - QA Auditor persona runs Ponytail code bloat review (`/ponytail-review` / bloat audit) + Superpowers `verification-before-completion` checks.
4. **SHUTDOWN:**
   - 18-point Sanity Gate verifies brain integrity and persists state to `brain/`.

---

## 3. Pre-Packaged Ecosystem Layout

All necessary skills and rules are pre-packaged in the repository so genOS works out-of-the-box offline with zero network friction:

```
genOS/
├── .agents/
│   ├── AGENTS.md
│   └── skills/
│       ├── using-superpowers/
│       ├── brainstorming/
│       ├── writing-plans/
│       ├── test-driven-development/
│       ├── verification-before-completion/
│       ├── systematic-debugging/
│       ├── ponytail/                      # NEW: Pre-packaged Ponytail skill
│       │   └── SKILL.md
│       ├── genos-kickoff/
│       ├── genos-shutdown/
│       └── genos-doctor/
├── .cursor/
│   └── rules/
│       ├── genos.mdc
│       ├── ponytail.mdc                   # NEW: Pre-packaged Ponytail rule
│       └── [agency-agent-rules].mdc       # Activated on Day 0
```

---

## 4. Day 0 Automated Activation (`setup-init.md`)

Update `guides/prompts/setup-init.md` so Phase 3 becomes the **AI Stack Activation**:
1. Inspects the selected profile (`profiles/<profile>/profile.yaml`).
2. Reads the profile's `recommended_agents`.
3. Activates the recommended specialist Agency Agent into `brain/60_AGENTS.md` and copies/links its definition to active rules.
4. Activates Ponytail rules and Superpowers skills.
5. Verifies all 3 subsystems are registered in the Brain Doctor audit.
6. Halts cleanly for Day 0 completion without user manual downloading.

---

## 5. Dual-Method 1-Click Auto-Updater (`update.md` / `update` command)

### 5.1 Command Definition in `AGENTS.md`

Add `update` to the `## Commands` table in `AGENTS.md`:

| Command | Protocol |
|---------|----------|
| `update` | Run Framework Update protocol (see below): detect source, fetch latest release, upgrade framework files while strictly preserving `brain/` and custom profiles, run Doctor |

### 5.2 Update Protocol & Prompt (`guides/prompts/update.md`)

Replaces and upgrades `setup-upgrade.md`.

#### Step 1: Smart Source Detection
- **Method A (Git Upstream / Remote):** If a git remote `upstream` or `origin` tracks `verdenef/genOS`, fetch latest tags/main.
- **Method B (Direct GitHub Release / Archive Fetch):** If no upstream remote is tracked, use standard shell tools (`curl` / PowerShell `Invoke-WebRequest`) to fetch the latest `genOS` archive from `https://github.com/verdenef/genOS/archive/refs/heads/main.zip` into a temporary `_genOS_Update/` folder.
- **Method C (Local Drop-in Fallback):** If `_genOS_Update/` already exists locally, use it directly.

#### Step 2: Strict Brain & User Data Shield
The updater must NEVER touch, overwrite, or delete:
- `brain/` (`00_PROJECT.md`, `20_PROGRESS.yaml`, `30_DECISIONS.md`, `40_BACKLOG.md`, `50_ROADMAP.md`, `60_AGENTS.md`, `brain/systems/`)
- `.obsidian/` directory
- Custom user profiles in `profiles/`
- User implementation source code

#### Step 3: Framework File Refresh
Updates:
- `AGENTS.md` (kernel)
- `guides/` (guide.md and prompts)
- Standard profiles in `profiles/`
- Pre-packaged `.agents/skills/` and `.cursor/rules/`

#### Step 4: Verification & Doctor Self-Audit
- Runs the Brain Doctor (`doctor` protocol) to verify that existing brain memory conforms to the upgraded kernel.
- Removes temporary files (`_genOS_Update/`).
- Outputs the Upgrade Health Report.

---

## 6. Spec Self-Review Checklist

- [x] **Placeholder scan:** No TBDs, TODOs, or vague steps.
- [x] **Consistency:** Aligns with genOS v3 Commands and pure-text philosophy.
- [x] **Scope:** Covers Superpowers, Ponytail, Agency Agents, and Auto-Updater.
- [x] **Ambiguity:** Explicit hierarchy: Human Intent > genOS Milestones > Ponytail Restraint > Superpowers Rigor > Agency Domain Idioms.
