# Git Write Operations Are User-Owned

The Plan, Build, Review, and Apply Feedback skills must never stage, commit, push, amend, reset, checkout files, rebase, change branches, or perform any other git write operation. The user owns git state changes whenever they are needed.

## Consequences

- Skills may inspect git state with read-only commands.
- Skills may leave file edits in the working tree.
- Skills must not stage files after editing.
- Skills must not create commits or push branches, even after successful verification.
- Subagents must follow the same restriction.
