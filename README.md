# GameOS

GameOS is a reusable AI operating system for software projects: a lightweight Project Brain that stores persistent knowledge across agents, sessions, and IDEs.

Humans contribute ideas and decisions. AI maintains the brain. The engine/source stores implementation. GameOS stores knowledge that cannot be inferred from code or the IDE.

---

## Repository structure

```
GameOS/
├── AGENTS.md                 # OS kernel — all agents must follow this
├── README.md                 # This file
├── guides/                   # User guide and reusable prompt templates
├── integrations/             # Optional OS integrations (e.g., Agency Agents)
└── brain/
    ├── 00_PROJECT.md         # Vision, scope, constraints
    ├── 20_PROGRESS.yaml      # Current state / session handoff
    ├── 30_DECISIONS.md       # Decision log
    ├── 40_BACKLOG.md         # Kanban backlog
    ├── 50_ROADMAP.md         # Milestone authority
    ├── 60_AGENTS.md          # Optional AI workforce roster
    └── systems/              # Per-system knowledge files
        ├── README.md
        └── SYSTEM.md
```

Operational rules live in [`AGENTS.md`](AGENTS.md), not here.

---

## Getting Started

To learn how to use GameOS, read the [GameOS User Guide](guides/guide.md) for a step-by-step walkthrough of the daily workflow, including ready-to-use prompts for kicking off and shutting down milestones.

---

## Tooling relationship

| Tool | Role |
|------|------|
| **IDE Agents** | Examples: Cursor, Antigravity. Reads `AGENTS.md` + `brain/` |
| **Engine / IDE MCP** | Live inspection (implementation truth); brain holds semantic truth |
| **Optional Integrations** | GameOS can integrate with specialist persona frameworks (like Agency Agents) via the `integrations/` directory, but the kernel remains fully independent. |

---

## Philosophy

- Humans provide ideas and make decisions.
- AI maintains the Project Brain automatically.
- The repository stores implementation.
- GameOS stores knowledge.
