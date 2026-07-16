# Prioritize CodeGraph Todo

## Plan

- [x] Define a CodeGraph-first discovery workflow and fallbacks.
- [x] Keep installation, indexing, and MCP configuration outside the skill's scope.

## Build

- [x] Add the internal `codegraph` skill entrypoint.
- [x] Document direct `codegraph_explore` usage, stale-file handling, and fallback behavior.
- [x] Add the active skill to the README inventory.
- [x] Make the `codegraph` skill eligible for automatic invocation.
- [x] Add an always-applied `codegraph` rule and document it in the README.

## Verification

- [x] Validate the skill frontmatter and referenced paths.
- [x] Run Markdown whitespace validation.
- [x] Validate the new always-applied rule and final Markdown changes.

## Review

- [x] Summarize automatic skill invocation and rule enforcement.

The `codegraph` skill remains automatically discoverable because its frontmatter
does not set `disable-model-invocation`. The new always-applied `codegraph` rule
enforces direct `codegraph_explore` usage whenever the MCP server and project
index are available, with an explicit no-index fallback. Verified all Markdown
changes with `git diff --check`.
