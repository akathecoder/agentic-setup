# Review Runs Independently From Plan And Build

The Review skill should evaluate local branch diffs and GitHub PRs from a fresh readonly context, without relying on the Plan work packet or Build session history unless the user explicitly asks for that comparison. This keeps Review focused on correctness, security, design, testing, performance, and maintainability rather than validating the assumptions made during planning or implementation.

## Consequences

- Review should support both local branch diffs and GitHub PR links or numbers.
- Review should gather codebase context from the diff, surrounding files, tests, and PR metadata.
- Review should not read the work packet by default.
- A separate follow-up can compare the implementation against the Plan when the user wants requirements traceability.
