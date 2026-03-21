# Rule: Sync Task Status to Issue Tickets

## Purpose

Whenever a task is being worked on and its status changes, the corresponding issue ticket on Notion or Jira must be updated to reflect that change.

## When This Rule Applies

This rule applies any time an agent:
- Starts work on a task (status: In Progress)
- Completes a task (status: Done)
- Blocks on a task (status: Blocked)
- Abandons or deprioritizes a task (status: Backlog / To Do)
- Updates sub-task progress within a larger task

## Required Behavior

1. **Identify the ticket**: Before or as soon as you begin a task, determine whether there is a linked Notion page or Jira issue. Look for:
   - A Notion page ID or URL referenced in the task description, MEMORY.md, or conversation context
   - A Jira issue key (e.g., `PROJ-123`) referenced anywhere in context
   - Ask the user if no ticket is apparent and the task seems non-trivial

2. **Update on every status change**: Each time the task status changes, update the linked ticket immediately — do not batch updates.

   | Task Status     | Ticket Status to Set  |
   |-----------------|----------------------|
   | Starting work   | In Progress          |
   | Completed       | Done                 |
   | Blocked         | Blocked              |
   | Deferred        | To Do / Backlog      |

3. **Add a comment**: When updating the ticket status, also leave a brief comment summarizing what was done or what the blocker is. Keep it factual and concise (1–3 sentences).

4. **Use available tools**:
   - For Notion: use the `notion-update-page` and `notion-create-comment` MCP tools
   - For Jira: use whatever Jira MCP or API integration is available in the session
   - If neither tool is available, notify the user and ask them to update the ticket manually

## Example Flow

```
1. User assigns task: "Implement auth middleware (PROJ-42)"
2. Agent begins work → updates PROJ-42 status to "In Progress", adds comment: "Starting implementation of auth middleware."
3. Agent completes work → updates PROJ-42 status to "Done", adds comment: "Auth middleware implemented and tests passing. PR #88 created."
```

## Exceptions

- Skip this rule if the user explicitly says not to update tickets for the current task.
- Skip if the task is purely exploratory/investigative with no defined ticket.
- If a ticket cannot be found and the user is unavailable, proceed with the task and note the missed update so it can be done later.
