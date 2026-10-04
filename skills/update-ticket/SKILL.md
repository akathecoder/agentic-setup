---
name: update-ticket
description: Sync completed Jira checklist items and draft progress updates. Use when a Jira task completes, meaningful implementation or review progress needs communicating, or a ticket needs clarification.
---

# Update Ticket

Use this skill when a significant implementation or code-review milestone changes the
project's meaningful progress, a Jira task completes, or the current ticket needs
clarification. It is for progress communication, not ticket workflow management.

Resolve every `.agents/projects/` path from the opened workspace root, including
when the active repository is nested inside it. In a single-repository workspace,
that is the repository root. Keep this artifact root fixed when changing directories;
never use nested repositories or global agent-installation directories for artifacts.

## Scope

Whenever a Jira task completes and its required verification passes, mark the
corresponding checklist item in the main ticket complete. This update is authorized
by the standing user instruction and needs no further approval. Fetch the latest
ticket first, change only the completed item's check state, preserve other content,
and read back the ticket to confirm the update. Use the description checklist when
no dedicated checklist field is available.

These other updates require explicit user approval:

- Add a Jira or GitHub comment.
- Update ticket descriptions when necessary to keep factual progress accurate.
- Update GitHub checklists or change Jira checklist content beyond completion marks.

Ticket status, assignee, labels, relationships, estimates, priority, and every other
metadata field are outside this skill's scope. Implementation completion alone does
not establish ticket completion; user review, merge, tests, and other required
verification still govern it.

## Process

1. Identify the active project and read `.agents/projects/<project>/CONTEXT.md`, `LINKS.md`,
   `todo.md`, relevant spec, and the target Jira ticket or GitHub Issue. Inspect the
   implementation and review evidence rather than inferring progress from intent.

   Done when the ticket, current evidence, and unchanged metadata boundary are known.

2. Apply every evidence-backed main Jira checklist completion update. If tracker
   access is unavailable, provide the exact ready-to-paste checklist update and record
   the limitation in `.agents/projects/<project>/todo.md`.

   Done when each completed Jira task is checked in the tracker, or its pending update
   and access limitation are recorded. If no other progress communication is needed,
   proceed to step 6.

3. Draft the smallest factual update needed. State completed behavior, verification
   performed, known blockers, and next work only when evidence supports each claim.
   Include proposed description or checklist changes separately from the comment.
   End the proposed tracker comment with the exact line:

   ```text
   Written by AI Agent
   ```

   Done when the proposed update contains no unsupported completion claim or metadata
   operation.

4. Show the user a concise summary of the proposed comment and any other description
   or checklist changes. Wait for explicit approval before posting these changes;
   main Jira checklist completion marks are covered by step 2.
   If the user declines, proceed to step 6 and record that decision.

   Done when the user approves the exact proposed tracker changes or declines them.

5. On approval, post only the approved comment, description, or checklist changes
   through available Jira or GitHub tooling. If tooling is unavailable, provide the
   ready-to-paste update and record the limitation in `.agents/projects/<project>/todo.md`.

   Done when the approved update is posted or the ready-to-paste fallback is recorded.

6. Update the active project's context, links, and todo with the ticket URL, factual
   progress, and remaining work. Do not mark the ticket complete unless the user has
   confirmed all required review, merge, and verification conditions.

   Done when project artifacts reflect the tracker update and its remaining work.

## Done when

- Every completed Jira task has its main-ticket checklist item checked, or the exact
  pending update and tracker-access limitation are recorded.
- Comments and all other description or checklist edits have explicit user approval.
- Ticket metadata is unchanged and project artifacts reflect actual tracker progress.
