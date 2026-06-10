# Implementing Selected Feedback

Fix only feedback items selected by the user.

## Delegation

Use a Build subagent when a selected fix is non-trivial, separable, or benefits from focused context.

Subagent prompt should include:

- The selected feedback item.
- Triage category and reason.
- Target files and line ranges.
- Relevant surrounding context.
- Required tests or verification.
- Instruction to read and follow the Build skill.
- No git write operations.

Example:

```text
Read and follow the Build skill. Fix only this selected feedback item:
<item>

Triage: <category and reason>
Target files: <files>
Required verification: <checks>

Do not stage, commit, push, change branches, or perform any git write operation.
Return changed files, verification results, and any blockers.
```

## Same-File Feedback

Process multiple items in the same file sequentially because line numbers and context can shift.

## Cross-File Feedback

Independent items in different files can be delegated in parallel when the fixes do not interact.

## Scope

Do not modify files unrelated to selected feedback unless the fix is impossible without doing so. If scope needs to expand, ask the user first.
