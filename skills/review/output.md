# Review Output

Findings come first, ordered by severity.

## Verdict Logic

- Any Critical finding: Request Changes.
- No Critical findings but Suggestions exist: Comment Only.
- Only Nitpicks or no findings: Approve.

## Format

```md
## Review: <target>

### Verdict: <Approve | Request Changes | Comment Only>

<1-3 sentence overall assessment.>

### Findings

#### `path/to/file.ts`

- **[Critical]** <specific issue, scenario, and impact>
- **[Suggestion]** <specific issue and suggested direction>

### Files Not Reviewed

<Only include when large diffs or generated/lock files were skipped.>

### Summary

Critical: N, Suggestions: N, Nitpicks: N
```

If there are no findings, say that clearly and mention any residual risk or unrun checks.

## Finding Quality

Each finding should include:

- The affected file or symbol.
- What can go wrong.
- A concrete scenario.
- Why existing tests do or do not catch it.
- The expected fix direction when clear.

Write findings for the user reviewing the change. Do not address the PR author as "you" unless the user is the author and asked for that style.
