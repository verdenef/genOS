# genOS Stack Profiles

Stack Profiles provide curated, plug-and-play defaults for specific software engineering domains. 

When you run `guides/prompts/setup-init.md`, genOS detects your project environment and asks you to confirm or select a profile. The profile automatically pre-configures:
- **Recommended MCP Tooling:** Live runtime observers tailored to the stack.
- **Starter Systems:** Architectural baseline templates for `brain/systems/`.
- **Specialist AI Workforce:** Tailored roles for `brain/60_AGENTS.md`.

---

## Available Profiles

| Profile | Target Stack | Key Tooling / MCPs | Starter Systems |
| :--- | :--- | :--- | :--- |
| **`web-fullstack`** | React, Next.js, Vue, Svelte, Node | Playwright, PostgreSQL, REST/GraphQL | Auth, Database, FrontendUI, API |
| **`backend-services`** | Go, Rust, Python FastAPI, Java | Docker, Redis, DB inspector, OpenAPI | Gateway, ServiceCore, Database, Messaging |
| **`mobile`** | Flutter, React Native, Swift, Kotlin | Mobile Emulator, Device Logs | Navigation, LocalCache, RemoteSync, UI |
| **`ai-data`** | Python, PyTorch, LangChain, Pandas | Jupyter, Vector DB, Pipeline Monitor | IngestionPipeline, ModelEngine, Evaluation |
| **`cli-system`** | Rust, Go, C/C++, Shell | Terminal Inspector, Native Debugger | CommandDispatcher, ConfigEngine, OutputFormat |
| **`gamedev`** | Unity, Godot, Unreal Engine | Unity/Godot MCP, Asset Inspector | Movement, Combat, Inventory, Audio |

---

## Creating a Custom Profile

To add a custom profile for your internal company stack:
1. Create a new directory under `profiles/<your-profile-name>/`.
2. Add a `profile.yaml` following the schema below:

```yaml
id: custom-profile
name: "Display Name"
description: "High-level summary of the stack."
detection_indicators:
  - "filename_or_config_pattern"
recommended_mcps:
  - id: mcp-id
    name: "Tool Name"
    purpose: "Why this tool is useful"
recommended_agents:
  - role: "Role Title"
    purpose: "What this specialist owns"
starter_systems:
  - name: "SystemName"
    purpose: "Core architectural responsibility"
```
