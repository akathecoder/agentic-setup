---
name: write-jira
description: Write, update, and enrich existing Jira tickets using Atlassian MCP with strict preview-before-write approval. Use when the user provides a Jira ticket link and wants to add feature details, release details, comments, links, subtickets, acceptance criteria, QA notes, CMR details, or stakeholder-ready context.
---

# Write Jira

Use this skill to update an existing Jira ticket with complete, stakeholder-ready information. The user must provide a base Jira ticket link before any Jira write can happen.

## Hard Rules

- Do not create the starting/base Jira ticket unless the user explicitly asks for that separate action and approves it.
- Do not edit a ticket, add a comment, create a link, transition status, or create a sub-ticket without explicit user approval.
- Always show the exact proposed Jira changes first. Write only the approved changes.
- Ask for any context you do not have. Never assume missing facts, ownership, dates, rollout details, risk, approval status, links, or field values.
- Use Atlassian MCP for Jira and Confluence interactions. Before calling an MCP tool, read that tool's descriptor/schema.
- Use `AskQuestion` for structured choices, confirmations, and disambiguation. Use normal chat for free-form ticket details.
- If a section or point is not applicable, omit it from the final ticket instead of writing `NA`.
- If applicability is unclear, ask the user. Do not silently include or omit the section.
- Preserve existing useful ticket content unless the preview explicitly says it will be replaced.

## Workflow

1. Resolve the base ticket from the provided Jira link.
2. Fetch the current Jira state with comments and relevant fields. Prefer markdown body content for readable previews.
3. Determine the ticket mode:
   - Feature ticket, often in `PMNTC`. See [feature-ticket.md](feature-ticket.md).
   - CMR ticket, in `CMR`. See [cmr-ticket.md](cmr-ticket.md).
   - If unclear, ask the user which mode to use.
4. Read linked Jira or Confluence references when they are needed to answer a question. If a fact is not present in the ticket or linked sources, ask.
5. Draft the target ticket content and any comments, links, field edits, or sub-tickets.
6. Show an approval preview. See [approval-preview.md](approval-preview.md).
7. Wait for explicit approval before writing anything to Jira.
8. Apply only the approved operations using Atlassian MCP.
9. Report the result with affected ticket links and any items left unresolved.

## MCP Tool Guidance

Common Jira operations:

- Read base ticket: `getJiraIssue`
- Update fields or description: `editJiraIssue`
- Add or update progress/details comments: `addCommentToJiraIssue`
- Create approved sub-tickets: `createJiraIssue`
- Link approved related tickets: `createIssueLink`
- Discover link types or metadata when needed: `getIssueLinkTypes`, `getJiraProjectIssueTypesMetadata`, `getJiraIssueTypeMetaWithFields`
- Resolve people: `lookupJiraAccountId`

Call metadata tools before setting custom fields, issue types, parent relationships, priorities, components, labels, fix versions, or any field whose payload shape is not already known.

## Sub-Tickets

Sub-tickets may be created when the user gives a base Jira ticket and the work naturally needs separate tracking.

Before creating a sub-ticket, preview:

- Project and issue type
- Parent or linked base ticket relationship
- Summary
- Description
- Assignee, priority, labels, and required custom fields
- Planned issue links

Create sub-tickets only after approval.

## Completion Report

Return:

- Updated ticket URL
- Summary of fields changed
- Comments added or updated
- Links created
- Sub-tickets created
- Questions still unresolved, if any
