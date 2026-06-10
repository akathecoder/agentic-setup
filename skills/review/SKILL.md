---
name: review
description: Use when the user asks to review a PR, review local changes, inspect a branch diff, or provide unbiased code review findings for correctness, security, testing, design, performance, and maintainability.
---

# Review

Use this skill to review code independently. Review findings only; do not fix issues during Review.

## Workflow

1. Determine whether the input is a local diff or GitHub PR. See [inputs.md](inputs.md).
2. Run the review in a fresh readonly context whenever possible. See [independence.md](independence.md).
3. Gather diff, nearby code, tests, PR metadata, and existing review comments.
4. Review by severity-weighted dimensions. See [review-dimensions.md](review-dimensions.md).
5. Present findings with verdict and severity. See [output.md](output.md).

## Guardrails

Do not read Plan or Build work packets unless the user explicitly asks for requirements traceability. Do not apply patches. Never stage, commit, push, amend, reset, checkout, rebase, change branches, or perform any other git write operation. See [guardrails.md](guardrails.md).
