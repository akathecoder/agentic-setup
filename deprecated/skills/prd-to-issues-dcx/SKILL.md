---
name: prd-to-issues-dcx
description: Break a PRD into independently-grabbable vertical slices and create them as Jira Epic + tickets. Reads PRDs from Confluence. Use when user wants to convert a PRD to tasks/tickets, create implementation work items, or break down a PRD into tracked work — for DCX projects using Confluence and Jira.
---

# PRD to Issues (DCX)

Break a PRD into independently-grabbable vertical slices (tracer bullets) and create them as a Jira Epic with child tickets.

Use the AskQuestion tool for structured choices, confirmations, and ambiguity resolution throughout this workflow. Use normal chat only when you need free-form feedback that cannot be expressed as fixed options.

## Process

### 1. Locate the PRD

Invoke the `find-confluence-doc` skill to resolve the Confluence project page for the current project.

Once you have the project page, search its child pages for the relevant PRD:
- If there is only one PRD, use it.
- If there are multiple, list them and use AskQuestion to let the user choose which one to use.
- If the user already specified a PRD by name, find the closest match.

Read the full content of the selected PRD page using `getConfluencePage` with `contentFormat="markdown"`.

### 2. Explore the codebase (optional)

If you have not already explored the codebase, do so to understand the current state of the code.

### 3. Draft vertical slices

Break the PRD into **tracer bullet** slices. Each slice is a thin vertical cut that goes through ALL integration layers end-to-end, NOT a horizontal slice of one layer.

Slices may be 'HITL' or 'AFK'. HITL slices require human interaction, such as an architectural decision or a design review. AFK slices can be implemented and merged without human interaction. Prefer AFK over HITL where possible.

<vertical-slice-rules>
- Each slice delivers a narrow but COMPLETE path through every layer (schema, API, UI, tests)
- A completed slice is demoable or verifiable on its own
- Prefer many thin slices over few thick ones
</vertical-slice-rules>

### 4. Quiz the user

Present the proposed breakdown as a numbered list. For each slice, show:

- **Title**: short descriptive name
- **Type**: HITL / AFK
- **Issue type**: Story / Task / Bug (see guidelines below)
- **Blocked by**: which other slices (if any) must complete first
- **User stories covered**: which user stories from the PRD this addresses

Use AskQuestion where the feedback can be represented as bounded choices, and use normal chat only for any extra free-form rationale. Cover:

- Does the granularity feel right? (too coarse / too fine)
- Are the dependency relationships correct?
- Should any slices be merged or split further?
- Are the correct slices marked as HITL and AFK?

Iterate until the user approves the breakdown.

### 5. Determine the Jira project

Request the Jira project key in normal chat if the user already knows it. If they do not, use AskQuestion with the available project list.

If the user is unsure, use `getVisibleJiraProjects` to list available projects and use AskQuestion to let them pick.

Once you have the project key, use `getJiraProjectIssueTypesMetadata` to discover available issue types (Epic, Story, Task, Bug, etc.).

### 6. Create the Epic

Create a Jira Epic to group all the slices under:

```
createJiraIssue(
  cloudId="...",
  projectKey="PROJ",
  issueTypeName="Epic",
  summary="<Epic title derived from PRD name>",
  description="<see template below>"
)
```

Epic description template:

```markdown
## Overview
<1-2 sentence summary of what this epic delivers>

## Source
Confluence PRD: <link to the PRD page in Confluence>

## Vertical Slices
<count> slices — <AFK count> AFK, <HITL count> HITL

## Success Criteria
- <criteria from the PRD>
```

Capture the returned Epic key (e.g. `PROJ-123`) — every child ticket needs it.

### 7. Create child tickets

For each approved slice, create a Jira issue linked to the Epic.

**Issue type selection:**
- **Story** — new user-facing features or functionality
- **Task** — technical/infrastructure work without direct user impact
- **Bug** — fixing existing problems or defects

```
createJiraIssue(
  cloudId="...",
  projectKey="PROJ",
  issueTypeName="Story",
  summary="<slice title>",
  description="<see template below>",
  parent="PROJ-123"
)
```

Create tickets in dependency order (blockers first) so you can reference their keys in descriptions.

Child ticket description template:

```markdown
## Parent PRD

<link to the source PRD Confluence page>

## What to build

A concise description of this vertical slice. Describe the end-to-end behavior, not layer-by-layer implementation. Reference specific sections of the parent PRD rather than duplicating content.

## Acceptance criteria

- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Blocked by

<PROJ-key of blocking tickets>, or "None — can start immediately".

## User stories addressed

Reference by number from the parent PRD:

- User story 3
- User story 7
```

Do NOT modify the parent PRD page in Confluence.

### 8. Report

Share a summary with the user:
- The Jira Epic URL
- Each child ticket key, title, type, and URL
- Total number of tickets created, with counts by type (AFK / HITL) and issue type (Story / Task / Bug)
- The source Confluence PRD URL
