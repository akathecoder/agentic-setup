---
name: wrap-up
description: Generate an end-of-session summary with call-outs, warnings, and guidance for future sessions. Chat-only output with zero side-effects.
---

# Wrap-up

## Trigger

End of an agent session when the user wants a structured handoff summary before closing the conversation.

## Workflow

1. **Gather context.** Collect information from three sources:
   - The current conversation history (what was discussed, decided, attempted, and accomplished).
   - The current todo list state (any pending, in-progress, completed, or cancelled items).
   - Run `git status` and `git diff --stat` to see what actually changed on disk.
   - Run a search for `TODO`, `HACK`, `FIXME`, and `XXX` comments in files modified during the session (scope using `git diff --name-only`).

2. **Synthesize and present the wrap-up** in the chat using the three sections below. Omit any section that has no meaningful content.

## Sections

### Session Summary

One concise paragraph covering what was attempted, what was accomplished, and the overall outcome. Follow with optional bullet points only for distinct deliverables (e.g., "added X", "refactored Y", "fixed Z"). Aim for the density of a good PR description — enough for future-you or a new agent session to understand the session's arc without re-reading the transcript.

### Call-outs & Warnings

Surface anything a future session needs to be aware of. Scan for items in these categories:

- **Hacks & known shortcomings** — pragmatic shortcuts taken during the session: hardcoded values, workarounds, skipped error handling, `TODO`/`HACK`/`FIXME`/`XXX` comments in modified files.
- **Assumptions** — decisions the agent made without explicit user confirmation (e.g., assumed a schema column exists, assumed an endpoint requires auth).
- **Incomplete todos** — any items from the todo list still in `pending` or `in_progress` state.
- **Potential risks** — concerns noticed but not addressed (e.g., missing tests for a new code path, possible breaking changes, dependency upgrade risks).
- **Session context** — important decisions, trade-offs, constraints, or deferred items that came up in conversation but are not reflected in code.

### Guidance

Forward-looking suggestions for future sessions. Present these as recommendations only — do not act on any of them.

- **Rule suggestions** — recurring patterns or conventions that emerged and could be codified as cursor rules.
- **Skill suggestions** — gaps in the current skill set that this session exposed.
- **Context to carry forward** — repo state, branch info, stashes, failing tests, environment specifics a future session needs to know.
- **Recommended next steps** — what to work on next and in what order.
- **Discussion takeaways** — user preferences, constraints, or decisions expressed in conversation that should inform future agent behavior (e.g., "user prefers composition over inheritance", "never use ORMs in this project").

## Guardrails

- **No code changes.** This is a pure reporting step.
- **No file creation or modification.** Do not write wrap-up files, update READMEs, or modify rules/skills.
- **No git mutations.** Do not commit, push, stash, or alter git state in any way.
- **No noise.** If the session was straightforward with no issues, keep it short. Do not manufacture warnings to fill sections.
- **No editorializing.** Stick to factual observations. "Tests were not added" is fine. "You should have written tests" is not.
