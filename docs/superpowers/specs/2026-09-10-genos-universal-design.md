# genOS: Universal Agentic Operating System & GameOS Hardening

- **Date:** 2026-09-10
- **Status:** Approved / Spec
- **Target Repository (genOS):** `https://github.com/verdenef/genOS.git`
- **Source Repository (GameOS):** `https://github.com/verdenef/gameos.git`

---

## 1. Executive Summary & Architectural Vision

GameOS established a deterministic, zero-chat-history operating model for AI pair programming:
1. **Single source of truth:** Project intent, execution RAM (`PROGRESS.yaml`), decisions, backlog, roadmap, and system architecture are strictly partitioned.
2. **Zero-history recovery:** Agents boot from file state alone, eliminating chat context rot and token waste.
3. **Strict lifecycle:** Mandatory BOOT and SHUTDOWN cycles maintain durable state across IDE switches and fresh conversations.

**Goal:**
1. **Harden GameOS:** Eliminate existing onboarding friction (the multi-prompt maze) and introduce automated Brain integrity verification (the Doctor self-audit).
2. **Generalize into genOS:** Extract the battle-tested kernel into a universal, stack-agnostic AI operating system hosted at `https://github.com/verdenef/genOS.git` that supports Web, Backend, Mobile, AI/Data, CLI, and Game Development via plug-and-play **Stack Profiles**.

---

## 2. Phase 1: GameOS Hardening (Immediate In-Repo Upgrades)

### 2.1 Brain Doctor & Automated Sanity Gate
Currently, manual edits or hallucinating agents can introduce syntax errors or broken milestone pointers that break subsequent cold-start boots.

#### A. Mandatory SHUTDOWN Sanity Gate
Update the SHUTDOWN sequence in `AGENTS.md` and `guides/prompts/workflow-02-shutdown.md` with a mandatory 5-point verification gate:
1. **YAML Integrity:** `20_PROGRESS.yaml` is parseable and valid YAML; all required keys (`current_milestone`, `working_on`, `systems_in_scope`, `blockers`, `session_summary`, `last_agent`, `last_ide`) are present and uncorrupted.
2. **Milestone Pointer Integrity:** `current_milestone` points to a valid, active milestone ID in `50_ROADMAP.md`.
3. **Index Synchronization:** All index tables in `50_ROADMAP.md` and `30_DECISIONS.md` exactly mirror their underlying markdown section headings and statuses.
4. **No State Leakage:** `40_BACKLOG.md` does not contain in-progress ("Doing") tasks or milestone definition duplicates.
5. **System Scopes:** Every system identifier listed in `systems_in_scope` exists as a file in `brain/systems/<Name>.md`.

#### B. Standalone Doctor Prompt (`guides/prompts/workflow-doctor.md`)
A pure-markdown, dependency-free diagnostic and auto-repair prompt:
* Scans all 6 Brain files and `brain/systems/`.
* Automatically repairs syntax formatting, fixes out-of-sync index tables, restores broken milestone pointers, and clears stale tasks.
* Outputs a clear health verification table (`[✓] 00_PROJECT.md`, `[✓] 20_PROGRESS.yaml`, etc.).

---

### 2.2 Unified Day 0 Onboarding Master Wizard (`setup-init.md`)
Replaces the confusing multi-prompt sequence (`setup-01` -> `setup-02` -> `setup-03`) with a single guided wizard:

#### Prompt Flow (`guides/prompts/setup-init.md`):
1. **Phase 1: Project & Brain Detection**
   * Automatically inspects the repository root.
   * Detects if the workspace is blank or has existing engine code.
   * Prompts the user for Project Intent, Target Platform, and Core Systems.
   * Writes `00_PROJECT.md`, proposes milestones for `50_ROADMAP.md`, and (for existing projects) reverse-engineers existing code into initial `brain/systems/*.md`.
2. **Phase 2: Tooling & MCP Transition**
   * Immediately transitions without prompting the user to find another file: *"Intent locked. Now let's connect your engine's MCP servers..."*
   * Configures engine-specific MCPs (Unity MCP, Godot MCP, Unreal MCP, etc.).
   * Pauses only if manual user intervention (e.g. global package installation or IDE permissions) is required.
3. **Phase 3: AI Workforce Integration (Optional)**
   * Offers specialized agent roles from Agency Agents (e.g. Lead Architect, Systems Designer, Engine Specialist).
   * Populates `60_AGENTS.md` upon approval.
4. **Phase 4: Integrity Check & Handoff**
   * Runs the Doctor self-check.
   * Displays the Day 0 completion banner and directs the user to `workflow-01-kickoff.md` for their first coding session.

*Note:* `setup-02-mcp.md` and `setup-03-workforce.md` are retained in `guides/prompts/` as utility tools for post-onboarding reconfigurations. `guides/guide.md` is updated to showcase `setup-init.md` as the default path.

---

## 3. Phase 2: genOS Universal Architecture (`verdenef/genOS`)

### 3.1 Domain-Agnostic Abstraction
`genOS` eliminates all game-engine-specific terms while preserving 100% of the kernel invariants:

| Concept | GameOS | genOS |
| :--- | :--- | :--- |
| **Domain** | Games, interactive simulations | Any software product, service, CLI, or system |
| **Runtime Observer** | Engine MCP (Unity, Godot, Unreal) | Runtime MCP (Docker, Playwright, DB, API, Node, Python) |
| **Domain Truth** | Gameplay loops, combat, physics | Business logic, domain workflows, APIs, state machines |
| **System Docs** | `Combat.md`, `Inventory.md` | `Auth.md`, `Database.md`, `Payments.md`, `WorkerQueue.md` |
| **Implementation** | Scenes, prefabs, assets, shaders | Endpoints, models, components, migrations, scripts |

---

### 3.2 Stack Profiles Engine (`profiles/`)
In `genOS`, users don't start from an empty vacuum. `profiles/` provides curated presets for specific engineering domains:

```
genOS/
├── AGENTS.md                          # Universal Kernel (Stack-Agnostic)
├── brain/                             # Universal Project Brain
│   ├── 00_PROJECT.md
│   ├── 20_PROGRESS.yaml
│   ├── 30_DECISIONS.md
│   ├── 40_BACKLOG.md
│   ├── 50_ROADMAP.md
│   ├── 60_AGENTS.md
│   └── systems/
│       ├── README.md
│       └── SYSTEM.md                  # Universal architectural template
├── profiles/
│   ├── web-fullstack/                 # Next.js/Vite, Node/tRPC, Postgres, Playwright
│   ├── backend-services/              # Go/Rust/FastAPI, Docker, Redis, Postgres, OpenAPI
│   ├── mobile/                        # Flutter / React Native / Swift / Kotlin
│   ├── ai-data/                       # Python, PyTorch, Vector DBs, Data Pipelines
│   ├── cli-system/                    # Rust / Go / C CLI & System Utilities
│   └── gamedev/                       # Complete GameOS compatibility profile
├── guides/
│   ├── guide.md
│   └── prompts/
│       ├── setup-init.md              # All-in-one wizard with profile selector
│       ├── setup-tooling.md           # Runtime MCP config utility
│       ├── setup-workforce.md         # Workforce config utility
│       ├── workflow-01-kickoff.md     # Milestone execution kickoff
│       ├── workflow-02-shutdown.md    # Milestone completion & state save
│       ├── workflow-03-resume.md      # Mid-session IDE resume
│       └── workflow-doctor.md         # Brain integrity check & auto-repair
└── integrations/
    └── agency_agents.md               # Universal specialist agent catalog
```

Each profile directory (`profiles/<name>/`) contains:
- `profile.yaml`: Metadata, stack recommendations, recommended MCP tools, and suggested system architecture.
- `recommended_agents.md`: Curated specialist agent roles for that stack.
- `suggested_systems/`: Baseline system document starters (e.g. `Auth.md`, `Database.md`).

---

### 3.3 Universal Kernel Specifications (`AGENTS.md`)
The `genOS` kernel maintains the exact same table of ownership and zero-history protocols:
- `00_PROJECT.md`: Product intent, user problem, tech stack, architectural constraints (Human owns).
- `20_PROGRESS.yaml`: Cold-start execution RAM (`current_milestone`, `working_on`, `systems_in_scope`, `session_summary`).
- `30_DECISIONS.md`: Architectural Decision Records (ADRs).
- `40_BACKLOG.md`: Non-milestone ad-hoc queue.
- `50_ROADMAP.md`: Milestone definitions, deliverables, and completion criteria.
- `brain/systems/<Name>.md`: Autonomous domain systems (Purpose, Invariants, Interfaces, Responsibilities).
- `brain/60_AGENTS.md`: Approved AI workforce roster.

---

## 4. Execution Plan & Next Steps

1. **Step 1: Harden GameOS (Local)**
   - Implement `guides/prompts/workflow-doctor.md`.
   - Update `AGENTS.md` and `guides/prompts/workflow-02-shutdown.md` with the SHUTDOWN Sanity Gate.
   - Implement `guides/prompts/setup-init.md` (Unified Day 0 Onboarding).
   - Update `guides/guide.md` to document the unified onboarding and doctor workflows.
   - Commit changes to GameOS.
2. **Step 2: Initialize `genOS` Repository**
   - Clone / initialize `https://github.com/verdenef/genOS.git`.
   - Port hardened kernel and generalize terminology to universal software development.
   - Author standard stack profiles (`web-fullstack`, `backend-services`, `mobile`, `ai-data`, `cli-system`, `gamedev`).
   - Package setup and workflow prompts.
   - Push to `verdenef/genOS`.
