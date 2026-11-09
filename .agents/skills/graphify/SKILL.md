---
name: graphify
description: "Query codebase AST call graphs, caller hierarchies, and calculate blast radius for implementation planning."
---

# Graphify: Code Topology & Call Graph Analysis

## Purpose
Provide deterministic, AST-level code topology and call graph analysis via Tree-sitter. Graphify transforms the codebase into a pre-mapped call graph and dependency topology, enabling agents to navigate deep caller/callee hierarchies and calculate refactoring blast radius instantly without expensive exploratory search loops.

## Invariants
1. **Never guess call hierarchies:** When Graphify is available, query the AST call graph before asserting whether a method, class, or interface is safe to refactor or remove.
2. **Silent fallback:** If Graphify is not configured, unindexed, or unavailable on the host machine, fall back immediately and silently to native file search tools (`find_files`, `grep`, `read_file`) without throwing errors or halting the workflow.
3. **Keep queries targeted:** Query specific symbols or files (`get_callers`, `get_dependencies`, `get_blast_radius`) rather than dumping the entire global graph into the context window.
4. **Zero Brain contamination:** Graphify AST caches, databases, and temporary index files belong in `.graphify/` (gitignored) and architectural summaries belong in `reports/architecture/`. Never store Graphify output or caches inside `brain/`.

## Available MCP Tools
When the `@graphify/mcp-server` is configured, the following tools are available:
- `get_callers`: Retrieve all direct and indirect callers of a specific symbol/function.
- `get_dependencies`: Retrieve all downstream dependencies and symbols called by a component.
- `get_blast_radius`: Calculate the full impact radius (impacted files, dependent classes, test suites) of modifying a target file or symbol.
- `graph_freshness`: Check whether the local `.graphify/` AST cache matches the current git HEAD commit.

## Workflow

### Step 1: Check Graph Freshness
- Compare `.graphify/` cache freshness against recent git commits (`git status`, `git log -1`).
- If Graphify is available but the index is missing or stale, invoke index refresh (`graphify index`) or proceed with fallback if indexing cannot be run.

### Step 2: Query Callers and Dependencies
- For symbols, interfaces, or classes identified in the active milestone or task:
  - Run `get_callers` to identify all upstream consumers.
  - Run `get_dependencies` to identify all downstream dependencies.

### Step 3: Compute Blast Radius
- Before planning file edits, breaking changes, or refactoring:
  - Run `get_blast_radius` on the target files or symbols.
  - Identify all affected modules, downstream consumers, and associated test suites.

### Step 4: Enrich Plan Interfaces Block
- Use the deterministic signatures and caller dependencies returned by Graphify to enrich the plan's `Task N: Interfaces` block:
  ```markdown
  **Interfaces:**
  - Consumes: [exact signatures and callers verified from AST call graph]
  - Produces: [exact return types and exported symbols verified from AST call graph]
  ```

## Graceful Fallback Protocol
If Graphify tools return an error, are absent from the MCP server list, or encounter an unsupported language:
1. Do not raise an exception or abort the workflow.
2. Silently switch to native tools:
   - Use `grep` / text search to locate references and call sites.
   - Use file reading to inspect component signatures.
3. Proceed with standard implementation planning.
