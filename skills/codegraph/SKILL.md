---
name: codegraph
description: Automatically prioritizes CodeGraph MCP queries for repository understanding and impact analysis. Use whenever work requires codebase exploration, structural or flow questions, implementation context, or change-impact assessment.
---

# CodeGraph-First Repository Exploration

This skill is eligible for automatic invocation; do not add
`disable-model-invocation`.

For any work that needs repository discovery or code-context gathering, prefer
CodeGraph over file-by-file search when its MCP server and project index are
available.

## Workflow

1. Check whether a CodeGraph MCP server and `codegraph_explore` tool are
   available. Inspect the tool schema before calling it.
2. Call `codegraph_explore` directly with a focused natural-language query and
   the relevant `projectPath`.
   - Ask for symbols, flows, callers, implementation context, or likely impact.
   - Do not delegate initial discovery to a file-reading subagent when
     CodeGraph can answer it directly.
3. Treat the returned source, call paths, and blast-radius data as the primary
   exploration context. Do not repeat the same discovery with broad
   search/read loops.
4. If CodeGraph reports a pending or stale-file warning, read only the named
   changed file(s) to obtain live content before relying on that result.
5. Use built-in search and file-reading tools only when CodeGraph is
   unavailable, the target project has no index, or the query needs information
   outside the indexed source.

## Boundaries

- Do not install CodeGraph, create a `.codegraph/` index, re-index a project,
  or change MCP configuration unless the user explicitly asks.
- CodeGraph is an exploration accelerator, not a substitute for verifying
  user-provided requirements, runtime behavior, generated files, or external
  systems.

## Example

For “How does an API request reach persistence?”, query:

`Trace the API request flow from its route or handler to persistence, including middleware and relevant callers.`
