# Agentic Setup

This repository contains the active skills, rules, and archived agent definitions for my personal vibe coding setup.

## Installation

### Skills

```bash
npx skills@latest add https://github.com/akathecoder/agentic-setup/tree/main/skills
```

### Agents

There are currently no active agents to install. Deprecated agent definitions are archived under `deprecated/agents/` for reference.

When active agents are added back, install them at the user level by copying files from `agents/` into `~/.cursor/agents/`:

```bash
cp agents/<name>.md ~/.cursor/agents/
```

### Rules

Rules can be installed at the user level or project level depending on your use case.

**User level** — applies across all projects:

```bash
cp rules/<name>.md ~/.cursor/rules/
```

**Project level** — applies only to the current project:

```bash
cp rules/<name>.md .cursor/rules/
```

## Skills

Skills are invoked by Claude Code using `/skill-name` or triggered internally based on context.

Interactive repo skills should use `AskQuestion` for structured choices, confirmations, and ambiguity resolution. Use normal chat only for free-form input that cannot be represented as fixed options.

| Skill                           | Type     | Description                                                                                                                                                                                    |
| ------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `plan`                          | generic  | Clarify, stress-test, and approve a feature or change before implementation, creating a work packet under `docs/<jira-ticket-or-context>/`.                                                    |
| `build`                         | generic  | Implement an approved plan or small code change with verification, using TDD by default for meaningful behavior changes and subagents for bounded work.                                        |
| `design`                        | generic  | Collaboratively design a new software system or service before implementation, including service boundaries, HLD, LLD, data schemas, flows, and architectural decisions.                       |
| `review`                        | generic  | Independently review a local branch diff or GitHub PR from a fresh readonly context, reporting findings without fixing them.                                                                   |
| `apply-feedback`                | generic  | Triage review feedback from humans, Bugbot, Copilot, AI reviewers, GitHub comments, pasted findings, or Review output; ask what to fix; then apply selected items.                             |
| `frontend-design`               | generic  | Create distinctive, production-grade frontend interfaces for web components, landing pages, dashboards, React components, HTML/CSS layouts, or other web UI work.                              |
| `deslop`                        | internal | Remove AI-generated code slop from a branch, including unnecessary comments, abnormal defensive checks, `any` casts, and over-nested code. Keeps behavior unchanged unless fixing a clear bug. |
| `check-compiler-errors`         | internal | Run compile and type-check commands, summarize failures by file and category, fix the highest-confidence issues, and re-run until clean or blocked.                                            |
| `codegraph`                     | internal | Prefer CodeGraph MCP queries for repository discovery, code-flow questions, and impact analysis whenever the server and project index are available.                                           |
| `publish-confluence`            | internal | Publish local documentation files to Atlassian Confluence through a bounded Composer 2.5 subagent using Atlassian MCP, with preview-before-write approval.                                     |
| `improve-codebase-architecture` | generic  | Find deepening opportunities in a codebase, informed by work-packet glossary language and ADRs.                                                                                                |
| `prototype`                     | generic  | Build throwaway logic or UI prototypes to flesh out a design, sanity-check a model, or explore radically different interface options before committing.                                        |
| `write-jira`                    | generic  | Update existing Jira tickets with feature or CMR details using Atlassian MCP, previewing all changes and requiring explicit approval before any Jira write.                                    |
| `write-rca`                     | generic  | Interview for incident details, draft a detailed RCA from the local RCA template, and publish the approved final RCA to a single Confluence page.                                              |
| `zoom-out`                      | generic  | Ask for broader module and caller context when working in an unfamiliar area of code or needing to understand how it fits into the bigger picture.                                             |
| `handoff`                       | generic  | Compact the current conversation into a handoff document for another agent or session to pick up.                                                                                              |

## Agents

There are no active agents in this repo right now. The previous autonomous agent suite is deprecated and archived under `deprecated/agents/`.

Deprecated agents: `tech-lead`, `planner`, `test-writer`, `dev`, `reviewer`, `qa`, and `wrap-up`.

## Deprecated

Deprecated definitions are kept under `deprecated/` for historical reference and should not be installed as active skills or agents.

Deprecated skills: `write-a-prd`, `write-a-prd-dcx`, `prd-to-issues`, `prd-to-issues-dcx`, `review-pr`, `fetch-gh-pr`, `find-notion-doc`, `find-confluence-doc`, `tdd`, `implement-ai-suggestions`, `grill-with-docs`, `create-jira-ticket`, `grill-me`, `what-did-i-get-done`, and `wrap-up`.

## Rules

Rules in `rules/` are loaded globally and govern agent behavior across all sessions.

| Rule                          | Description                                                                                                                                                                             |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `codegraph`                   | Always prefer `codegraph_explore` for repository discovery when the CodeGraph MCP server and project index are available; use built-in tools only as the fallback.                      |
| `sync-task-status-to-tickets` | Whenever a task status changes (started, completed, blocked, deferred), update the linked Notion or Jira ticket immediately and leave a brief comment summarizing progress.             |
| `top-level-generic-rule`      | Base CLAUDE.md template to drop into any coding project. Covers planning, subagent strategy, task management, verification, bug fixing, and code quality. Refine per-project as needed. |
