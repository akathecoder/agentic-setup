# Review Guardrails

- Findings only; do not fix issues during Review.
- Do not apply patches.
- Do not update the Plan packet.
- Do not post to GitHub unless the user explicitly asks.
- Do not duplicate existing review comments.
- Do not suggest purely stylistic changes unless they conflict with local conventions.
- Do not read the Plan or Build context by default.

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

Read-only git inspection is allowed.
