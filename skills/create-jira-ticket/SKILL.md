---
name: create-jira-ticket
description: Create a single Jira ticket through Atlassian MCP by interviewing the user for missing details, validating issue types and required fields, previewing the final ticket, and then creating the issue plus any requested links. Use when the user asks to create, raise, file, or draft a Jira ticket, Jira story, Jira task, Jira bug, enhancement, or improvisation ticket.
---

# Create Jira Ticket

Create exactly one Jira issue per run. Reuse details the user already provided and ask only for what is still missing.

Use the AskQuestion tool for structured choices, confirmations, and ambiguity resolution throughout this workflow. Use normal chat only for free-form fields like ticket summaries, bug details, problem statements, or other open-ended content.

## Workflow

### 1. Resolve Jira site and project

- If the user provides an `atlassian.net` URL, first try the site hostname as `cloudId`.
- Otherwise call `getAccessibleAtlassianResources` and use AskQuestion when more than one site is available.
- Request the target Jira project key in normal chat when it is not already known.
- If the user is unsure, call `getVisibleJiraProjects(cloudId, action="create", expandIssueTypes=true)` and use AskQuestion to let them pick from the visible projects.

### 2. Resolve issue type and required fields

- Request the issue type in normal chat if the user already knows it. If multiple issue types are plausible from available metadata, use AskQuestion to let them choose.
- Call `getJiraProjectIssueTypesMetadata(cloudId, projectIdOrKey)` and map the user request to an available issue type.
- Call `getJiraIssueTypeMetaWithFields(cloudId, projectIdOrKey, issueTypeId)` before you try to create anything.
- Ask only for fields that are still missing.
- Never guess required custom fields. If the payload shape or allowed values are unclear, use AskQuestion when the missing value is one of several known options; otherwise request the value in normal chat.

### 3. Pick the description mode

Use AskQuestion to determine which ticket category best fits if it is not already clear:

- Enhancement / Internal Improvisation
- Bug
- Story / Task / Other

Use the matching template below.

### 4. Interview for ticket content

Always collect:

- Summary
- Optional assignee
- Optional priority
- Optional labels
- Optional parent or Epic relationship
- Related ticket keys and intended relationship, if any

Use `parent` only for sub-tasks. For Epic or other hierarchy fields, discover the correct field from Jira metadata and pass it through `additional_fields`.

#### Enhancement / Internal Improvisation

These sections are mandatory. Keep asking until each one is concrete enough for QA to understand the why, the user impact, and the edge cases.

- Implementation
- Before / After
- Why / Problem Statement
- Primary Consumer
- Problem Solved
- Edge Cases / Exclusions
- Linked Tickets

Do not accept vague content like "UI change done" or "done as requested". Ask for the operational problem, who benefits, and what workflow improves.

Render the description in markdown:

```markdown
## Implementation
[What was built technically: DB, API, UI, config, flags]

## Before / After
**Before:** [State before the change]
**After:** [State after the change]

## Why / Problem Statement
[What pain point, escalation, or gap triggered this ticket]

## Primary Consumer
- [ ] Internal Ops
- [ ] Support Team
- [ ] Engineering
- [ ] Customer-facing

## Problem Solved
[Specific workflow, manual process, or failure this eliminates]

## Edge Cases / Exclusions
[What is out of scope, blank/null states, or unsupported scenarios]

## Linked Tickets
- Epic: [ticket key or None]
- Depends on: [ticket key(s) or None]
- Related: [ticket key(s) or None]
```

#### Bug

Collect:

- Context / affected area
- Steps to reproduce
- Expected behavior
- Actual behavior
- Impact
- Edge Cases / Scope
- Linked Tickets

Render the description in markdown:

```markdown
## Context
[Where the bug happens and who is affected]

## Steps To Reproduce
1. [Step]
2. [Step]
3. [Step]

## Expected Behavior
[What should happen]

## Actual Behavior
[What happens instead]

## Impact
[Customer, support, ops, or engineering impact]

## Edge Cases / Scope
[Known limits, environments, data conditions]

## Linked Tickets
- Related: [ticket key(s) or None]
```

#### Story / Task / Other

Collect:

- Context
- Requested Change
- Acceptance Criteria
- Constraints / Notes
- Linked Tickets

Render the description in markdown:

```markdown
## Context
[Why this work is needed]

## Requested Change
[What should be built or changed]

## Acceptance Criteria
- [ ] [Criterion 1]
- [ ] [Criterion 2]

## Constraints / Notes
[Dependencies, technical notes, or limits]

## Linked Tickets
- Related: [ticket key(s) or None]
```

### 5. Resolve people and extra fields

- If the user provides an assignee by name or email, use `lookupJiraAccountId(cloudId, searchString)`.
- If multiple people match, use AskQuestion to let the user choose.
- For common optional fields like `priority` and `labels`, verify the expected Jira payload and then pass them through `additional_fields`.
- If the project requires fields like component, team, sprint, environment, or other custom values, ask for them before previewing.

### 6. Preview before create

Always show the final payload before creating the issue. Include:

- Jira site
- Project key
- Issue type
- Summary
- Assignee
- Priority
- Labels
- Parent / Epic relationship
- Final markdown description
- Planned issue links

Require explicit user confirmation via AskQuestion before creation.

### 7. Create the issue

Use `createJiraIssue` with markdown output:

```text
createJiraIssue(
  cloudId="...",
  projectKey="PROJ",
  issueTypeName="Task",
  summary="...",
  description="...",
  assignee_account_id="...",
  parent="...",              # only for sub-tasks
  additional_fields={...},
  contentFormat="markdown",
  responseContentFormat="markdown"
)
```

- Include `description` whenever the user has provided enough context, even if Jira does not require it.
- If creation fails, use the error together with field metadata to recover instead of retrying blindly.

### 8. Create Jira links after issue creation

- If the user supplied related ticket keys plus a relationship type, create real Jira issue links after the issue is created.
- If the relationship type is unknown, call `getIssueLinkTypes(cloudId)` and use AskQuestion to let the user choose the right one.
- For directional link types, follow Atlassian semantics from the tool description:
  - blocker = `inwardIssue`
  - blocked item = `outwardIssue`
- Keep the `## Linked Tickets` section in the description even when you also create real Jira links.

### 9. Report the result

Return:

- Created issue key and URL
- Summary
- Project and issue type
- Assignee and important optional fields
- Issue links created
- Any fields intentionally left blank

## Guardrails

- One ticket per run.
- Do not create anything until the user approves the preview.
- Ask only for missing information; do not re-ask for values the user already supplied.
- If the requested issue type is unavailable, present the available issue types and use AskQuestion to let the user choose.
- For enhancement and improvisation tickets, the description must include all SOP sections before you ask for confirmation via AskQuestion.

## Example Triggers

- "Create a Jira enhancement ticket for the support dashboard."
- "Raise a Jira bug in PAYMENTS and assign it to Priya."
- "Draft a Jira task, show me the final description, then create it."
