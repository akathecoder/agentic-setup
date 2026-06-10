# Build Subagents

Use subagents aggressively when work can be bounded and integrated safely. The main agent remains responsible for scope, integration, verification, and user communication.

## Good Build Delegations

Use subagents for:

- Focused implementation slices in separate files or modules.
- Writing or updating behavior tests for a defined surface.
- Investigating compiler, type-check, or lint failures.
- Exploring existing patterns before editing.
- UI implementation when paired with a design-focused subagent.
- Cleanup passes after behavior is green.
- Verifying a specific command or failure category.

## Avoid Delegating

Keep in the main conversation:

- Scope changes.
- Cross-cutting architecture decisions.
- Conflict resolution between subagent outputs.
- Final integration.
- Final verification summary.
- Any user-facing decision.

## Prompt Shape

Give each subagent:

- The work packet path.
- The exact slice to implement or investigate.
- The files it may touch.
- Required tests or checks.
- The no-git-write rule.
- Expected final report format.

Example:

```text
Read and follow the Build skill. Implement only <slice> from <work packet>.
Touch only <files/area> unless blocked.
Run <focused checks>.
Do not stage, commit, push, change branches, or perform any git write operation.
Return changed files, verification results, and blockers.
```

## Integration Rules

- Do not assume subagent edits are correct.
- Read changed files before integrating.
- Re-run checks from the main working tree.
- If subagent outputs conflict, stop and resolve deliberately.
