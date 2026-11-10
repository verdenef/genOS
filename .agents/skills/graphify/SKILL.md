---
name: graphify
description: "Query the code graph (callers, callees, shortest path, communities) built by Graphify, and rebuild it when stale, before planning edits."
---

# Graphify: Code Topology

## Purpose
Graphify (PyPI `graphifyy`) parses source with tree-sitter into `graphify-out/graph.json`: classes, methods, and `calls` / `references` / `inherits` / `imports` edges. Use it to find callers and dependencies of a symbol without search loops.

## Invariants
1. **Code only, local:** build with `--code-only`. This needs no API key and nothing leaves the machine. Never run a build that sends documents to an LLM without the human asking.
2. **Never guess call hierarchies** when the graph is available: query it before saying a method is safe to change or remove.
3. **The graph is syntactic.** It cannot see references that live in strings or assets: `GameObject.Find("...")`, `FindProperty("...")`, menu paths, scene and prefab files, reflection, `SendMessage`. Grep those. Edges marked `INFERRED` (cross-class calls resolved by name) are leads, not proof; confirm with Grep when a decision depends on one.
4. **Silent fallback:** if the graph or the tool is missing, use `grep` and file reads without comment and carry on.
5. **Keep queries targeted:** one symbol or file at a time; never dump the whole graph into context.
6. **Zero Brain contamination:** `graphify-out/` is gitignored and never goes in `brain/`.

## Setup (once per machine)
```
uv tool install "graphifyy[mcp]"
graphify extract . --code-only
```
Scope is set by `.graphifyignore` at the repo root (which folders count as code). Do **not** run `graphify install` or `graphify claude install`; this skill replaces them.

## Freshness
Before relying on the graph, compare `graphify-out/graph.json` with `git log -1 --format=%cd`. If the graph is older than the last commit or the working tree has code changes, run `graphify update .` (re-extracts code only; no LLM).

## Query (CLI works without MCP)
- `graphify explain "Class.Method()"`: node plus incoming (`<--` callers) and outgoing (`-->` callees) edges; add `--all` for every edge.
- `graphify path "A" "B"`: shortest path between two nodes.
- `graphify query "<question>" --seed X`: BFS from a node.
- Use the exact label shown in the "No exact match" hint, e.g. `Class.Method()`.

## MCP tools (when the `graphify` server is registered)
`query_graph`, `get_node`, `get_neighbors`, `get_community`, `god_nodes`, `graph_stats`, `shortest_path`. The server is `graphify-mcp --graph graphify-out/graph.json`.

## Use in planning
1. For each symbol in scope, list its callers (`<--  [calls]`) and callees.
2. Add the strings-and-assets check from Invariant 3 by Grep.
3. Put the verified signatures and callers into the plan's `Task N: Interfaces` block:
   ```markdown
   **Interfaces:**
   - Consumes: [signatures and callers from the graph, Grep-confirmed where INFERRED]
   - Produces: [return types and exported symbols]
   ```
