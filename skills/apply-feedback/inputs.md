# Feedback Inputs

Accept feedback from:

- GitHub review comments.
- GitHub suggested changes.
- Bugbot output.
- Copilot or other AI reviewer comments.
- Peer review comments.
- Pasted findings.
- Output from the Review skill.

## GitHub URLs

Support:

- Individual comments such as `https://github.com/{owner}/{repo}/pull/{number}#discussion_r{comment_id}`.
- Full reviews such as `https://github.com/{owner}/{repo}/pull/{number}#pullrequestreview-{review_id}`.
- PR links or numbers when the user wants unresolved comments triaged.

Use `gh` read-only API calls to fetch comment bodies, paths, line ranges, and suggestion blocks.

## Branch Check

When feedback comes from a PR, compare the PR head branch to the current local branch. If they differ, warn the user and use `AskQuestion` to decide whether to continue on the current branch or stop.

Do not switch branches.

## Pasted Feedback

When feedback is pasted, preserve each item as a separate candidate. If file paths or affected code are missing, inspect the repo to locate the likely target. Ask only when the target cannot be inferred safely.

## Normalization

For each item, capture:

- Source.
- Author or tool when known.
- File/path and line when known.
- Original text.
- Suggested replacement when present.
- Initial confidence and missing context.
