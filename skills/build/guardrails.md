# Build Guardrails

- Require an approved work packet for non-trivial work.
- Keep implementation scoped to the approved plan.
- Ask before expanding scope.
- Prefer simple changes that match the existing codebase.
- Use TDD by default for meaningful behavior changes.
- Use the TDD escape hatch only for trivial/mechanical edits or user-approved exceptions.
- Do not hide failing checks.
- Do not mark todo items complete until verified.

## Git Safety

Never perform git write operations:

- No `git add`.
- No `git commit`.
- No `git push`.
- No `git commit --amend`.
- No `git reset`.
- No `git checkout`.
- No `git switch`.
- No `git rebase`.
- No branch creation or branch changes.

This restriction applies to subagents too. Read-only git inspection is allowed when useful.
