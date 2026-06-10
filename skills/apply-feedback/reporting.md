# Feedback Reporting

Report what happened after implementation.

## Format

```md
## Apply Feedback Result

### Applied

1. **`path/file.ts`** - <what changed>
   Source: <reviewer/tool>
   Verification: <command/result>

### Skipped

1. **`path/file.ts`** - <summary>
   Category: <triage category>
   Reason: <why skipped>

### Not Selected

1. **`path/file.ts`** - <summary>
   Category: <triage category>
```

Omit empty sections.

## Verification

For applied items, include:

- Focused tests/checks run.
- Any checks not run and why.
- Residual risk.

Do not claim an item is fixed without verification evidence.
