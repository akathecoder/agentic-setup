# Agentic Setup

This repository contains all the skills, rules, and agents for my personal vibe coding setup.

## Installation

```bash
npx skills@latest add https://github.com/akathecoder/agentic-setup
```

## Skills

Skills are invoked by Claude Code using `/skill-name` or triggered internalmatically based on context.

| Skill                           | Type     | Description                                                                                                                                                                                                          |
| ------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `write-a-prd`                   | generic  | Create a PRD through user interview, codebase exploration, and module design. Publishes to Notion; falls back to a local markdown file if Notion MCP is unavailable.                                                 |
| `prd-to-issues`                 | generic  | Break a PRD into independently-grabbable vertical slices and create them as Kanban tasks in a Notion board. Classifies each task as AFK or HITL and maps dependencies.                                               |
| `review-pr`                     | generic  | Thoroughly review a GitHub PR for correctness, security, design, testing, performance, and readability. Produces a structured review with severity-tiered findings. Does not post to GitHub unless explicitly asked. |
| `implement-ai-suggestions`      | generic  | Fetch suggestions from a GitHub Copilot review and apply the good ones locally. Triages structured code suggestions and prose feedback; leaves changes unstaged.                                                     |
| `improve-codebase-architecture` | generic  | Surface architectural friction in a codebase and propose module-deepening refactors. Spawns parallel sub-agents to design alternative interfaces and creates a refactor RFC as a GitHub issue.                       |
| `tdd`                           | generic  | Test-driven development with the red-green-refactor loop. Focuses on vertical slices, behavior-driven integration tests, and clean interface design.                                                                 |
| `frontend-design`               | generic  | Create distinctive, production-grade frontend interfaces for web components, landing pages, dashboards, or React components.                                                                                         |
| `grill-me`                      | generic  | Interview the user relentlessly about a plan or design until reaching shared understanding. Resolves every branch of the decision tree before stopping.                                                              |
| `deslop`                        | internal | Remove AI-generated slop from a branch — unnecessary comments, defensive try/catch blocks, `any` casts, and deeply-nested code. Keeps behavior unchanged.                                                            |
| `what-did-i-get-done`           | generic  | Summarize authored commits over a time range into a concise Slack-ready status update. Excludes merge commits and cosmetic-only changes.                                                                             |
| `check-compiler-errors`         | internal | Run compile and type-check commands, summarize failures by file and category, fix the highest-confidence issues, and re-run until clean or blocked.                                                                  |
| `wrap-up`                       | generic  | Generate an end-of-session handoff summary: what was accomplished, hacks taken, incomplete todos, and recommended next steps. Chat-only — no file or git mutations.                                                  |
| `write-a-prd-dcx`               | work     | Variant of `write-a-prd` for DCX projects. Publishes the finished PRD to Confluence instead of Notion.                                                                                                               |
| `prd-to-issues-dcx`             | work     | Variant of `prd-to-issues` for DCX projects. Reads PRDs from Confluence and creates a Jira Epic with child issues instead of a Notion board.                                                                         |
| `fetch-gh-pr`                   | internal | Fetch comprehensive GitHub PR data (metadata, diff, CI checks, inline comments) as structured markdown. Used internally by `review-pr` and `implement-ai-suggestions`.                                               |
| `find-notion-doc`               | internal | Resolve the correct Notion project page for the current project. Checks agent memory first, then navigates Notion to find the matching subpage. Used internally by other skills.                                     |
| `find-confluence-doc`           | internal | Resolve the correct Confluence page for the current project. Returns the page ID, space key, and URL. Used internally by other skills.                                                                               |

## Agents

Agents in `agents/` are autonomous, long-running units that orchestrate multi-step work. The Tech Lead is the entry point — it dispatches all others.

| Agent         | Description                                                                                                                                                                 |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tech-lead`   | Orchestrator. Fetches a Jira/Notion ticket, drives the full implementation loop, maintains `tasks/project-log.md`, and escalates to the user after 10 failed QA iterations. |
| `planner`     | Breaks a ticket into a file-level implementation plan. Runs once before any code is written.                                                                                |
| `test-writer` | Writes tests against the ticket spec before Dev implements. Tests must fail initially.                                                                                      |
| `dev`         | Implements code to make tests pass. On subsequent iterations, addresses Reviewer findings and QA failures.                                                                  |
| `reviewer`    | Reviews the current diff as a staff engineer. Posts findings to `tasks/project-log.md` by severity.                                                                         |
| `qa`          | Runs the full test suite, validates acceptance criteria, and reports PASS/FAIL to the Tech Lead.                                                                            |
| `wrap-up`     | Runs after QA passes. Produces `tasks/handoff.md` covering everything implemented, tested, fixed, broken, and flagged — including security and compliance concerns.         |

## Rules

Rules in `rules/` are loaded globally and govern agent behavior across all sessions.

| Rule                          | Description                                                                                                                                                                             |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sync-task-status-to-tickets` | Whenever a task status changes (started, completed, blocked, deferred), update the linked Notion or Jira ticket immediately and leave a brief comment summarizing progress.             |
| `top-level-generic-rule`      | Base CLAUDE.md template to drop into any coding project. Covers planning, subagent strategy, task management, verification, bug fixing, and code quality. Refine per-project as needed. |
