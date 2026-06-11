# Approval Preview

Every Jira write must be preceded by an approval preview. Do not call a write-capable Atlassian MCP tool until the user explicitly approves the preview.

Write-capable operations include:

- `editJiraIssue`
- `addCommentToJiraIssue`
- `createJiraIssue`
- `createIssueLink`
- `transitionJiraIssue`
- `addWorklogToJiraIssue`

## Preview Format

Use this structure in chat before asking for approval:

```markdown
I plan to make these Jira changes:

## Base Ticket

- Ticket: [KEY](url)
- Mode: [Feature / CMR / Other]

## Fields To Update

- [Field]: [old value] -> [new value]

## Description Changes

[Final rendered description, or exact section-level diff when preserving most of the current description.]

## Comments To Add Or Update

- [Comment body or summary]

## Links To Create

- [KEY-1] [relationship] [KEY-2]

## Sub-Tickets To Create

- Project: [project]
- Issue type: [type]
- Parent/link: [relationship to base ticket]
- Summary: [summary]
- Description: [description]

## Sections Omitted As Not Applicable

- [Section or point]

## Open Questions / Explicit Unknowns

- [Question or field that remains unresolved]
```

Omit empty groups from the preview.

## Confirmation

Use `AskQuestion` for approval when available:

- Apply these Jira changes
- Revise the draft
- Cancel

Only the first option authorizes Jira writes. If the user asks to revise, update the preview and ask again.

## Unknown Values

Do not invent missing values. If a value is unknown:

- Ask for it when it is needed for correctness or approval.
- Leave it out when the section is not applicable.
- Use `TBD` only when the user explicitly approves writing `TBD` into the Jira ticket.

## After Writing

Report:

- Ticket URL
- Fields updated
- Comments added or updated
- Links created
- Sub-tickets created
- Any approved `TBD` or unresolved items still present
