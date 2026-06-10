# Review Inputs

Review supports local branch diffs and GitHub PR links or numbers.

## Local Diff

Use read-only inspection:

- `git status --short`
- `git diff --stat`
- `git diff`
- `git diff <base>...HEAD` when a base branch is known
- `git log --oneline <base>..HEAD` when useful

Do not change branches or modify git state to obtain the diff.

If the base branch is unclear, infer it from branch tracking information when possible. Otherwise ask the user.

## GitHub PR

For a PR link or number, use `gh` read-only commands/API calls:

- PR metadata: title, body, author, base/head refs.
- Files changed and patches.
- Existing review comments.
- Check status when relevant to risk.

If the local repo matches the PR, also read nearby code and tests from the checkout. If not, review from the fetched diff and clearly state the limitation.

## Large PRs

When the diff is too large to inspect fully, prioritize:

1. Source files with the largest behavioral impact.
2. Security-sensitive paths such as auth, crypto, permissions, and middleware.
3. Database migrations and schema changes.
4. API handlers and job processors.
5. Tests for changed behavior.

Skip by default:

- Lockfiles.
- Generated files.
- Pure formatting/config churn.

List skipped files in the review output.
