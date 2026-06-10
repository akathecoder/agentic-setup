---
name: plan
description: Use when planning non-trivial work, discussing a feature/change, creating a Jira-backed work packet, deciding implementation guardrails, or preparing a handoff for Build.
---

# Plan

Use this skill to turn an idea, ticket, or vague change request into an approved work packet that Build can implement safely.

## Workflow

1. Identify the work packet location. See [artifacts.md](artifacts.md).
2. Gather reference links and existing context.
3. Explore the codebase before asking questions when the answer is discoverable.
4. Grill the plan one focused question at a time. See [questioning.md](questioning.md).
5. Update `glossary.md`, `todo.md`, `links.md`, and `adr/` as decisions crystallize. See [documentation.md](documentation.md).
6. Create `plan.md` only when the work needs high-level interfaces, test intent, risks, or implementation guardrails.
7. Stop for user approval before Build begins.

## Subagents

Use subagents for bounded exploration that can be summarized without preserving every intermediate detail. Keep user decisions, trade-offs, and terminology choices in the main conversation. See [subagents.md](subagents.md).

## Handoff

Before handing off to Build, verify the work packet has a clear todo, known risks, required test intent, and any ADR-worthy decisions recorded. See [handoff.md](handoff.md).

## Guardrails

Never implement code during Plan. Never stage, commit, push, amend, reset, checkout, rebase, change branches, or perform any other git write operation. See [guardrails.md](guardrails.md).
