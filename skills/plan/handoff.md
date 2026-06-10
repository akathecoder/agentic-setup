# Build Handoff

Before Build starts, the work packet should answer:

- What is the goal?
- What is explicitly out of scope?
- Which files, modules, APIs, or user flows are likely involved?
- Which behaviors must be tested?
- Which existing behavior must not regress?
- Which risks, edge cases, or constraints should Build respect?
- Which decisions are recorded as ADRs?
- Which open questions remain, if any?

## Minimum Handoff

For small but non-trivial work, `todo.md` plus `glossary.md` may be enough.

For larger work, add `plan.md` with:

```md
# <Work Name> Plan

## Goal

## Non-Goals

## Proposed Shape

## Required Behaviors To Test

## Risks And Guardrails

## Open Questions
```

Do not include implementation code. Build owns the actual implementation.

## Approval

Stop after the handoff is ready and ask the user to approve or revise it. Do not start Build until the user approves.
