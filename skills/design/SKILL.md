---
name: design
description: Use when collaboratively designing a new software system or service before implementation, including service boundaries, HLD, LLD, data schemas, flows, and architectural decisions.
---

# Design

Use this skill to design a new software system or service with the user before any implementation begins.

## Workflow

1. Identify or create the design packet under `designs/<system-slug>/`. See [artifacts.md](artifacts.md).
2. Capture the user's initial context in `context.md`.
3. Gather required context before proposing architecture. See [intake.md](intake.md).
4. Ask one focused question at a time, with a recommendation and trade-off when a decision is needed. See [questioning.md](questioning.md).
5. Keep `design_plan.md`, `open_questions.md`, and `todo.md` current throughout the conversation.
6. Add HLDs, LLDs, schemas, flows, and ADRs only when the discussion produces enough substance. See [documentation.md](documentation.md).
7. Keep generated artifacts compatible with later Confluence publishing. See [artifacts.md](artifacts.md) and [documentation.md](documentation.md).
8. Use Mermaid diagrams for user flows, API flows, sequence diagrams, state transitions, and async workflows when they clarify the design. Always include a prose or table fallback. See [diagrams.md](diagrams.md).

## Guardrails

This is a design-only skill. Do not implement code, create prototypes, or hand off to another skill unless the user explicitly asks. Do not record architectural, product, or design decisions as chosen until the user confirms them. See [guardrails.md](guardrails.md).
