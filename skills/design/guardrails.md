# Design Guardrails

## Design Only

This skill designs systems and services before implementation. Do not:

- Implement production code.
- Build prototypes.
- Create migrations.
- Create tickets.
- Start implementation planning.
- Proactively hand off to `plan`, `prototype`, `build`, or another skill.

If the user explicitly asks for follow-on work, stop and confirm the next mode or skill before continuing.

## Required Context First

Do not propose architecture until the required intake context is known. Capture missing required items in `open_questions.md` and ask the user one focused question at a time.

## Confirm Decisions

Do not decide architecture independently. Before recording a decision as chosen:

1. Show the proposed decision.
2. Explain the reasoning.
3. State the trade-off or consequence.
4. Wait for user confirmation.

Routine document updates for agreed facts, open questions, todos, and context do not require a separate confirmation prompt.

## Keep Scope Explicit

Always distinguish:

- What belongs to this service.
- What belongs to other services.
- What is in scope for this design discussion.
- What is out of scope for this design discussion.

When scope changes, update `context.md`, `design_plan.md`, and `todo.md`.

## Avoid False Precision

Do not invent requirements, service names, APIs, schemas, SLAs, traffic numbers, compliance needs, or dependencies. If a detail matters and is unknown, record it as an open question.

## No Git Writes

Never stage, commit, push, amend, reset, checkout, rebase, or otherwise perform git write operations while using this skill unless the user explicitly asks outside the design workflow.
