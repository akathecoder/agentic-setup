# Apply Feedback Guardrails

- Do not assume feedback is correct.
- Do not edit before triage.
- Do not edit before user selection.
- Do not fix unselected items.
- Do not broaden scope without asking.
- Do not apply structured suggestions blindly.
- Do not hide skipped or rejected feedback.
- Do not post comments to GitHub unless the user explicitly asks.

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

This applies to Build subagents used by Apply Feedback. Read-only git inspection is allowed.
