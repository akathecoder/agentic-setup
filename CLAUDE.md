# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repo Structure

This repo is a collection of Claude Code **skills** and **rules** — no build system, no tests, no compiled output.

- `skills/<name>/SKILL.md` — the skill definition. Must include YAML frontmatter with `name` and `description`.
- `skills/<name>/*.md` — optional supporting reference files a skill can read (e.g., `tdd/` has `mocking.md`, `tests.md`, etc.).
- `agents/<name>.md` — autonomous agents that orchestrate multi-step work. `tech-lead` is the entry point; it dispatches all others.
- `rules/<name>.md` — global rules loaded into every Claude Code session.
- `CLAUDE.md` — this file, loaded into every session in this repo.
- `README.md` — user-facing documentation. Keep it up to date (see rule below).

## Skill Frontmatter Format

Every `SKILL.md` must open with:

```yaml
---
name: skill-name
description: One-sentence description used by Claude to decide when to trigger this skill.
---
```

The `description` field is the trigger condition — write it as "Use when…" so Claude knows exactly when to invoke it.

## Skill Types

| Type | Meaning |
|---|---|
| `generic` | General-purpose, invoked manually by the user via `/skill-name` |
| `work` | Project-specific variants (currently DCX — uses Confluence + Jira instead of Notion) |
| `internal` | Invoked automatically by the agent or by other skills, not by the user directly |
| `niche` | Invoked manually but only for a very specific, narrow purpose |

## Rules

### Use AskQuestion For Structured Input

When authoring or updating repo-owned skills:

- Use the `AskQuestion` tool for any user interaction that can be represented as a structured choice, confirmation, or disambiguation.
- Use normal chat only when collecting free-form content that cannot be expressed as fixed options, such as long descriptions, ticket summaries, reproduction steps, or other open-ended inputs.
- If a question can be answered by exploring the repo or calling tools, do that before asking the user.

### Keep README Updated

Update `README.md` whenever a change affects the developer-facing surface: setup, run commands, architecture, APIs, tooling, or contributing workflow. Skip for internal refactors, bug fixes with no behavior change, and test-only changes.

- Read the current README before editing — surgical updates only, no wholesale rewrites.
- Document commands over concepts; use fenced code blocks for anything copy-pasteable.
- Remove stale content rather than leaving it.
