---
name: update-ticket
description: Draft a Jira or GitHub progress update when meaningful implementation or review progress needs communicating, then post it only after user approval.
---

# Update Ticket

Use this skill when a significant implementation or code-review milestone changes the
project's meaningful progress, or when the current ticket needs clarification. It is
for progress communication, not ticket workflow management.

Resolve every `.agents/projects/` path from the repository root; never read or write
project artifacts in a global agent-installation directory.

## Scope

This skill may draft and, after explicit user approval, perform only these updates:

- Add a Jira or GitHub comment.
- Update ticket descriptions when necessary to keep factual progress accurate.
- Update checklists in tickets or sub-tickets to reflect work that is actually done.

Ticket status, assignee, labels, relationships, estimates, priority, and every other
metadata field are outside this skill's scope. Implementation completion alone does
not establish ticket completion; user review, merge, tests, and other required
verification still govern it.

## Process

1. Identify the active project and read `.agents/projects/<project>/CONTEXT.md`, `LINKS.md`,
   `todo.md`, relevant spec, and the target Jira ticket or GitHub Issue. Inspect the
   implementation and review evidence rather than inferring progress from intent.

   Done when the ticket, current evidence, and unchanged metadata boundary are known.

2. Draft the smallest factual update needed. State completed behavior, verification
   performed, known blockers, and next work only when evidence supports each claim.
   Include proposed description or checklist changes separately from the comment.
   End the proposed tracker comment with the exact line:

   ```text
   Written by Cursor
   ```

   Done when the proposed update contains no unsupported completion claim or metadata
   operation.

3. Show the user a concise summary of the proposed comment and any description or
   checklist changes. Wait for explicit approval before modifying the tracker.

   Done when the user approves the exact proposed tracker changes or declines them.

4. On approval, post only the approved comment, description, or checklist changes
   through available Jira or GitHub tooling. If tooling is unavailable, provide the
   ready-to-paste update and record the limitation in `.agents/projects/<project>/todo.md`.

   Done when the approved update is posted or the ready-to-paste fallback is recorded.

5. Update the active project's context, links, and todo with the ticket URL, factual
   progress, and remaining work. Do not mark the ticket complete unless the user has
   confirmed all required review, merge, and verification conditions.

   Done when project artifacts reflect the tracker update and its remaining work.
