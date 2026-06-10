---
name: build
description: Use when the user asks to build, implement, code, fix from a plan, or execute a work packet with verification and TDD by default for meaningful behavior changes.
---

# Build

Use this skill to implement approved work safely. For non-trivial work, start from a Plan work packet. For trivial or mechanical edits, proceed directly only when the scope is clear.

## Workflow

1. Read the approved work packet or confirm the change is trivial/mechanical.
2. Identify implementation slices and verification requirements. See [workflow.md](workflow.md).
3. Use TDD by default for meaningful behavior changes. See [tdd.md](tdd.md).
4. Delegate bounded work to subagents whenever it reduces main-context pressure. See [subagents.md](subagents.md).
5. Integrate changes in the main conversation.
6. Verify before marking work complete. See [verification.md](verification.md).
7. Report what changed, what was verified, and what remains.

## Testing

Prefer behavior-focused tests through public interfaces. Mock only at system boundaries. See [testing.md](testing.md), [interface-design.md](interface-design.md), and [deep-modules.md](deep-modules.md).

## Refactoring

Refactor only after tests are green. See [refactoring.md](refactoring.md).

## Guardrails

Keep changes scoped to the approved plan unless the user approves scope expansion. Never stage, commit, push, amend, reset, checkout, rebase, change branches, or perform any other git write operation. See [guardrails.md](guardrails.md).
