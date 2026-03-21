# Agentic Setup

This repository contains all the skills, rules, and agents for my personal vibe coding setup.

## Skills

Skills are invoked by Claude Code using `/skill-name` or triggered automatically based on context.

### `write-a-prd`
Create a PRD through user interview, codebase exploration, and module design. Conducts a structured interview, sketches major modules, and publishes the finished PRD as a Notion page under the appropriate project. Falls back to a local markdown file if Notion MCP is unavailable.

### `prd-to-issues`
Break a PRD into independently-grabbable vertical slices (tracer bullets) and create them as Kanban tasks in a Notion board. Classifies each task as AFK (no human needed) or HITL (requires human input), maps dependencies, and creates the tasks inside the project's Notion database.

### `find-notion-doc`
Utility skill used by other skills to resolve the correct Notion project page for the current project. Checks agent memory first (cached from prior lookups), then navigates the root Notion Projects page to find the matching subpage. Saves the result to memory for future use.

### `improve-codebase-architecture`
Explore a codebase to surface architectural friction and propose module-deepening refactors. Identifies shallow, tightly-coupled modules, spawns parallel sub-agents to design multiple alternative interfaces, and creates a refactor RFC as a GitHub issue.

### `tdd`
Test-driven development with the red-green-refactor loop. Emphasises vertical slices (one test → one implementation at a time), behavior-focused integration tests over implementation-detail tests, and clean interface design for testability.

### `frontend-design`
Create distinctive, production-grade frontend interfaces. Use for web components, landing pages, dashboards, React components, or any UI work that needs polished, non-generic design.

### `grill-me`
Interview the user relentlessly about a plan or design until reaching a shared understanding. Walks down every branch of the decision tree and resolves dependencies between decisions one by one. Use to stress-test a plan before committing to it.

### `deslop`
Remove AI-generated code slop from a branch. Diffs against main and strips unnecessary comments, defensive try/catch blocks, `any` casts, and deeply-nested code that should use early returns. Keeps behavior unchanged and edits minimal.

### `what-did-i-get-done`
Summarize authored commits over a user-specified time range into a concise status update suitable for Slack. Excludes merge commits and cosmetic-only changes; focuses on substantial behavior and architecture changes.

### `check-compiler-errors`
Run the repo's compile and type-check commands, summarize failures by file and category, fix the highest-confidence issues, and re-run until clean or blocked.
