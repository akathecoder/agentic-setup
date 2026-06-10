---
name: apply-feedback
description: Use when the user asks to apply, address, resolve, or fix review suggestions or feedback from humans, Bugbot, Copilot, AI reviewers, GitHub comments, pasted findings, or Review output.
---

# Apply Feedback

Use this skill to evaluate review feedback, ask the user which items to fix, and implement only the selected items.

## Workflow

1. Collect feedback from GitHub, Bugbot, AI review, peer review, pasted findings, or Review output. See [inputs.md](inputs.md).
2. Triage every item before editing. See [triage.md](triage.md).
3. Present the triage and ask the user which items to fix. See [selection.md](selection.md).
4. Fix only selected items. Use Build subagents for non-trivial or separable fixes. See [implementation.md](implementation.md).
5. Verify and report applied/skipped items. See [reporting.md](reporting.md).

## Guardrails

Do not assume feedback is correct. Do not edit before triage and user selection. Never stage, commit, push, amend, reset, checkout, rebase, change branches, or perform any other git write operation. See [guardrails.md](guardrails.md).
