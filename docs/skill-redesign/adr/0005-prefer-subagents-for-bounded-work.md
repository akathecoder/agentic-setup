# Prefer Subagents For Bounded Work

Plan and Build should use subagents when a task can be bounded and summarized without requiring the main context to retain every intermediate detail. This is especially important in Build, where implementation slices, test work, verification, compiler errors, cleanup, and focused research can consume large context quickly.

## Consequences

- Build should rely heavily on subagents, while keeping orchestration and integration in the main conversation.
- Plan should use subagents for bounded repo exploration, pattern checks, ownership mapping, and test convention summaries.
- Core user decisions, trade-offs, and terminology choices should stay in the main conversation.
- Subagents must inherit the same no-stage, no-commit, no-push restriction.
