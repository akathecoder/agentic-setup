# Review Independence

Review must be independent from Plan and Build.

## Default Rule

Use a fresh readonly subagent or fresh session for Review when possible. The reviewer should see:

- The diff or PR.
- Nearby code and tests.
- PR metadata and existing comments.
- Relevant project conventions discovered from the codebase.

The reviewer should not see:

- The Plan work packet.
- Build session history.
- Implementation rationale from the author.
- User statements about why the approach is acceptable.

## Why

Review should find bugs, regressions, missing tests, design risks, and security issues. It should not become a confirmation pass for the plan.

## Exception

If the user explicitly asks for requirements traceability, first complete the independent review. Then compare the implementation against the Plan packet as a separate section or follow-up.

## Existing Comments

Read existing review comments to avoid duplicates. If an existing unresolved comment already covers a point, do not re-raise it unless you add materially new information.
