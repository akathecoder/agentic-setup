# Plan Guardrails

- Do not implement code during Plan.
- Do not write test code during Plan; record test intent instead.
- Do not turn `glossary.md` into a spec.
- Do not create ADRs for reversible or obvious choices.
- Do not ask the user questions that can be answered from code or docs.
- Do not start Build until the user approves the handoff.

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

Read-only git inspection is allowed when useful, such as `git status` or `git diff`.
