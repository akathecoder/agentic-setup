# Plan Subagents

Use subagents to preserve the main context when the task has a bounded question and the final summary is enough.

## Good Plan Delegations

Use readonly exploration subagents for:

- Mapping likely files and ownership for a feature area.
- Finding existing implementations of a similar pattern.
- Summarizing test conventions in a package.
- Checking whether a term is already used in code or docs.
- Listing API surfaces, routes, events, or jobs relevant to a change.
- Comparing two or three candidate approaches against existing patterns.

## Keep In Main Context

Do not delegate:

- Final trade-off decisions.
- User preference questions.
- Canonical terminology decisions.
- ADR approval.
- Scope changes.
- Plan approval.

## Prompt Shape

Give each subagent one focused task:

```text
Explore <area> for <specific question>. Return:
1. Relevant files/symbols.
2. Existing patterns.
3. Risks or constraints.
4. Short recommendation.

Do not modify files.
Do not stage, commit, push, change branches, or perform any git write operation.
```

Trust the summary unless it conflicts with code you later inspect. If a subagent surfaces a decision, bring it back to the user instead of deciding silently.
