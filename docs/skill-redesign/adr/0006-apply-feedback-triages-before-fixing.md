# Apply Feedback Triages Before Fixing

The Apply Feedback skill should not assume review suggestions are correct. It should first evaluate each suggestion independently, classify it as a genuine must-fix issue, a good but optional issue, or a wrong issue to ignore, then ask the user which items to fix.

## Consequences

- No feedback item should be implemented before triage.
- The user chooses which triaged items actually get fixed.
- Selected fixes should be delegated to a Build-skill subagent when the work is non-trivial or separable.
- Skipped items should be reported with the triage category and reason.
