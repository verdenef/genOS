# GameOS User Guide

Welcome to GameOS! This guide explains how to interact with the framework day-to-day. GameOS relies on you (the human) to provide intent, while the AI agents handle implementation and memory management.

## Day 0: Setup & Initialization

Before you can use GameOS for daily development, it needs to be initialized for your specific project.

### 1. Project Onboarding
**Important:** You must create your actual game/engine project (e.g. via Unity Hub) *before* running this setup prompt. GameOS is an observer, it is not designed to generate engine scaffolds from scratch for you.

Once your blank engine project is ready and you have copied the GameOS folder into the repository, open a chat with your AI agent and paste the contents of:
**`guides/prompts/setup-01-project-onboarding.md`**

This instructs the AI to scan your workspace, verify the GameOS installation, and prompt you for your project vision to initialize the Brain.

### 2. MCP Setup
Once the project vision is established, you need to hook up the necessary Model Context Protocol (MCP) servers so the AI can read your engine's live state. Paste the contents of:
**`guides/prompts/setup-02-mcp.md`**

The AI will configure the servers based on your stack. It will pause and ask for your help if it needs global packages installed or specific permissions.

---

## The Daily Workflow

The AI agents in GameOS have no chat history. Every time you start a new conversation or bring in a new agent, they need to read the Project Brain to figure out what is going on.

To make this seamless, GameOS uses a strict **BOOT** and **SHUTDOWN** cycle.

### 1. Starting Work (Milestone Kickoff)
When you are ready to begin working on a milestone, open a new chat with your AI agent and paste the contents of:
**`guides/prompts/workflow-01-kickoff.md`**

This instructs the AI to read the kernel (`AGENTS.md`) and boot up the Brain. It will summarize the active milestone and propose an implementation plan for your approval.

### 2. Implementation
Once you approve the plan, the agent will write the code and modify your project files. You can chat back and forth as normal during this phase.

### 3. Context Switching (Changing IDEs mid-session)
If you need to switch IDEs (e.g. from Cursor to Antigravity) in the middle of working on a task, you will lose your chat history. To catch the new agent up to speed instantly, open a chat in the new IDE and paste the contents of:
**`guides/prompts/workflow-03-resume-session.md`**

This instructs the AI to read the execution state (`PROGRESS.yaml`) and summarize exactly what you were in the middle of doing, allowing you to resume work without missing a beat.

### 4. Ending Work (Milestone Shutdown)
When the milestone is complete and the code is verified, you must save the state back to the Brain before closing the chat. Paste the contents of:
**`guides/prompts/workflow-02-shutdown.md`**

The AI will update the roadmap, update any system architecture documents that were affected, and log the execution state in `PROGRESS.yaml`. 

Once the shutdown is complete, you can safely close the chat. The next time you open your IDE, you can start back at step 1 and the new agent will seamlessly pick up exactly where you left off.

---

## Maintenance & Upgrades

As GameOS evolves, you may want to pull in new framework features or kernel updates without losing your project's Brain. 

### Upgrading GameOS
1. Download the latest GameOS release.
2. Extract it into your repository as a temporary folder named `_GameOS_Update/` (placed right next to your active `GameOS/` folder).
3. Open a chat with your AI agent and paste the contents of:
**`guides/prompts/setup-03-framework-upgrade.md`**

This instructs the AI to safely compare the new framework against your local one. It will selectively upgrade your kernel (`AGENTS.md`) and tools while preserving all of your project's `brain/` data.
