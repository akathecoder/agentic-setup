# Agentic Setup

This repository contains the active skills, rules, and archived agent definitions for my personal vibe coding setup.

## Installation

### Skills

```bash
npx skills@latest add https://github.com/akathecoder/agentic-setup
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

| Skill                      | Type     | Description                                                                                                                                                                                                                          |
| -------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `frontend-design`          | generic  | Create distinctive, production-grade frontend interfaces for web components, landing pages, dashboards, React components, HTML/CSS layouts, or other web UI work.                                                                     |
| `implement-ai-suggestions` | generic  | Fetch suggestions from a GitHub Copilot review or comment and apply the good ones locally. Triages structured code suggestions and prose feedback; leaves changes unstaged.                                                          |
| `deslop`                   | internal | Remove AI-generated code slop from a branch, including unnecessary comments, abnormal defensive checks, `any` casts, and over-nested code. Keeps behavior unchanged unless fixing a clear bug.                                      |
| `check-compiler-errors`    | internal | Run compile and type-check commands, summarize failures by file and category, fix the highest-confidence issues, and re-run until clean or blocked.                                                                                  |

## Agents

There are no active agents in this repo right now. The previous autonomous agent suite is deprecated and archived under `deprecated/agents/`.

Deprecated agents: `tech-lead`, `planner`, `test-writer`, `dev`, `reviewer`, `qa`, and `wrap-up`.

## Deprecated

Deprecated definitions are kept under `deprecated/` for historical reference and should not be installed as active skills or agents.

Deprecated skills: `write-a-prd`, `write-a-prd-dcx`, `prd-to-issues`, `prd-to-issues-dcx`, `review-pr`, `fetch-gh-pr`, `find-notion-doc`, `find-confluence-doc`, `tdd`, `improve-codebase-architecture`, `create-jira-ticket`, `grill-me`, `what-did-i-get-done`, and `wrap-up`.

## Rules

Rules in `rules/` are loaded globally and govern agent behavior across all sessions.

| Rule                          | Description                                                                                                                                                                             |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sync-task-status-to-tickets` | Whenever a task status changes (started, completed, blocked, deferred), update the linked Notion or Jira ticket immediately and leave a brief comment summarizing progress.             |
| `top-level-generic-rule`      | Base CLAUDE.md template to drop into any coding project. Covers planning, subagent strategy, task management, verification, bug fixing, and code quality. Refine per-project as needed. |
