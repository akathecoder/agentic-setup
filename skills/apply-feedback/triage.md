# Feedback Triage

Triage every feedback item before editing. Do not assume a reviewer, Bugbot, Copilot, or peer is correct.

## Categories

Use exactly one category for each item:

1. **Genuine issue, must fix**
   - The feedback identifies a real bug, security issue, data loss risk, broken requirement, meaningful missing test, or high-confidence maintainability problem.
   - The fix is within scope or must be addressed before the work can be trusted.

2. **Good issue, optional**
   - The feedback is valid, but not urgent.
   - It may improve readability, design, test coverage, or consistency.
   - It can reasonably be ignored, deferred, or batched later.

3. **Wrong issue, ignore**
   - The feedback misunderstands the code.
   - The suggestion would introduce a bug or regression.
   - It conflicts with established project patterns or ADRs.
   - It is too vague to act on safely.

## Evaluation Checklist

For each item:

- Read the target code and surrounding context.
- Check callers, tests, and existing patterns when relevant.
- Verify whether the suggested behavior is actually desired.
- Consider whether the feedback conflicts with the Plan packet or ADRs, if available.
- Decide the category and write a short reason.

Structured GitHub suggestions still require judgment. Defaulting to "apply" is not allowed.

## Triage Output

Prepare a list like:

```md
## Feedback Triage

1. **[Genuine issue, must fix]** `path/file.ts` - <summary>
   Reason: <why this is valid and important>

2. **[Good issue, optional]** `path/file.ts` - <summary>
   Reason: <why valid but not mandatory>

3. **[Wrong issue, ignore]** `path/file.ts` - <summary>
   Reason: <why not correct or not safe>
```
