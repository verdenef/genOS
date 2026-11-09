# Project

Authoritative file for project intent. See `AGENTS.md` → Ownership.

**Ownership:** Humans own vision and intent. AI may reorganize, summarize, clarify, and maintain this document. AI must never change intent without explicit human approval.

---

## Vision

Zero-context-loss, location-agnostic operating kernel for AI-assisted software development across multiple IDEs (Antigravity, Cursor, Claude Code, Codex) and LLM models.

## Research Goal

Prove that a strictly partitioned, filesystem-backed Project Brain enables flawless multi-agent and cross-session handoffs without context compaction or memory degradation.

## Scope

- **In scope:** Kernel protocols (`AGENTS.md`), memory surfaces (`brain/`), pre-packaged skills (Superpowers, Ponytail, genOS lifecycle), and update distribution pipeline.
- **Out of scope:** Proprietary cloud databases, language-specific runtime locks.

## Target Environment & Stack

Cross-IDE / Filesystem-first. Markdown (`[[wikilink]]` Obsidian-compatible), YAML (`20_PROGRESS.yaml`), Git.

## Core User Workflow / Domain Loop

BOOT -> Milestone/Intent Resolution -> Restrained TDD Implementation -> SHUTDOWN with Sanity Gate.

## Constraints

Filesystem-only persistence (no hidden external DB/server state), strict single source of truth, Obsidian wikilink compatibility.

## Success Criteria

- 100% zero-history recovery on session cold start.
- Seamless cross-IDE handoffs.
- Zero data loss during framework upgrades.
