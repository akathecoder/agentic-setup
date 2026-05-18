---
name: prd-to-issues
description: Break a PRD into independently-grabbable vertical slices and create them as Kanban tasks in Notion. Use when user wants to convert a PRD to tasks/tickets, create implementation work items, or break down a PRD into tracked work.
---

# PRD to Issues

Break a PRD into independently-grabbable vertical slices (tracer bullets) and create them as Kanban tasks in Notion.

Use the AskQuestion tool for structured choices, confirmations, and ambiguity resolution throughout this workflow. Use normal chat only when you need free-form feedback that cannot be expressed as fixed options.

## Process

### 1. Locate the PRD

Invoke the `find-notion-doc` skill to resolve the Notion project page for the current project.

Once you have the project page, search its child pages for the relevant PRD:
- If there is only one PRD, use it.
- If there are multiple, list them and use AskQuestion to let the user choose which one to use.
- If the user already specified a PRD by name, find the closest match.

Read the full content of the selected PRD page.

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
- **Blocked by**: which other slices (if any) must complete first
- **User stories covered**: which user stories from the PRD this addresses

Use AskQuestion where the feedback can be represented as bounded choices, and use normal chat only for any extra free-form rationale. Cover:

- Does the granularity feel right? (too coarse / too fine)
- Are the dependency relationships correct?
- Should any slices be merged or split further?
- Are the correct slices marked as HITL and AFK?

Iterate until the user approves the breakdown.

### 5. Find or create the Kanban board in Notion

Inside the project's Notion page, look for an existing Kanban database (a Board view database):
- If one exists, use it. Do not create a duplicate.
- If none exists, create a new Notion database named "Tasks" with the following properties:
  - **Name** (title) — the task title
  - **Status** (select) — options: `Backlog`, `In Progress`, `In Review`, `Done`
  - **Priority** (select) — options: `High`, `Medium`, `Low`
  - **Type** (select) — options: `Feature`, `Chore`, `Research`, `HITL`
  - **Blocked by** (text) — names of blocking tasks
  - **PRD** (text) — name of the source PRD page
  - Set the default view to **Board**, grouped by **Status**.

### 6. Create the Kanban tasks

For each approved slice, create a Notion database entry using the task template below.

Create tasks in dependency order (blockers first) so you can reference their names in the "Blocked by" field.

Inside each task page, add a content block using this template:

<task-template>
## Parent PRD

<link to the source PRD Notion page>

## What to build

A concise description of this vertical slice. Describe the end-to-end behavior, not layer-by-layer implementation. Reference specific sections of the parent PRD rather than duplicating content.

## Acceptance criteria

- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Blocked by

Names of blocking tasks, or "None — can start immediately".

## User stories addressed

Reference by number from the parent PRD:

- User story 3
- User story 7

</task-template>

Do NOT modify the parent PRD page.

### 7. Report

Share a summary with the user:
- The Notion Kanban board URL
- Total number of tasks created, with counts by type (AFK / HITL) and priority
