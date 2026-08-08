---
name: to-tickets
description: Break approved work into tracker-ready tracer-bullet tickets.
disable-model-invocation: true
---

# To Tickets

Break the approved plan, spec, or current conversation into **tracer-bullet**
vertical-slice tickets. Each ticket declares the work that blocks it.

## Process

1. Identify the active project. Read its context, links, spec, ADRs, and any supplied
   tracker reference in full, including comments. Explore the codebase if it has not
   already been explored.

   Done when the source material and tracker choice are known.

2. Draft vertical slices. Each slice is a narrow but complete path through relevant
   layers, independently demoable or verifiable, and small enough for a fresh agent
   context. Put prefactoring first. For a mechanical wide refactor, use an
   expand-contract sequence with migration batches rather than forcing false vertical
   slices.

   Done when every proposed ticket has a title, delivery statement, acceptance
   criteria, and only its genuine blocking edges.

3. Write the proposed numbered breakdown to `.agents/projects/<project>/ticket-drafts.md`.
   For each ticket show its title, what it delivers, acceptance criteria, and blockers.
   Ask whether granularity and blocking edges are correct; iterate until approval.

   Do not create or modify Jira tickets or GitHub Issues before explicit approval.
   Done when the user approves the complete breakdown.

4. Publish the approved tickets in dependency order. Default to Jira when project
   context names Jira or no tracker has been established; use GitHub Issues only when
   Jira is unavailable or the user explicitly selects GitHub. Use native blockers or
   sub-task relationships where available; otherwise include blockers in the body.
   Use available authenticated tooling, or produce ready-to-paste ticket bodies and
   record the limitation.

   Done when every approved ticket has a tracker identifier or a ready-to-paste
   fallback.

5. Update the active project's `CONTEXT.md`, `LINKS.md`, and `todo.md` with the
   tracker choice, ticket identifiers, URLs, dependency status, and next frontier.
   Append `Written by Cursor` to any agent-authored Jira or GitHub comment, but not
   ticket descriptions or local documentation.

   Done when project artifacts point to the published ticket set and its current
   implementation frontier.
