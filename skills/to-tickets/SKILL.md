---
name: to-tickets
description: Break approved work into a main Jira ticket checklist or tracer-bullet GitHub Issues.
disable-model-invocation: true
---

# To Tickets

Break the approved plan, spec, or current conversation into **tracer-bullet**
vertical slices. In Jira, put the slices in a checklist in the main ticket; do not
create subtickets. In GitHub, create an Issue per slice. Each slice declares its blockers.

Resolve every `.agents/projects/` path from the opened workspace root, including
when the active repository is nested inside it. In a single-repository workspace,
that is the repository root. Keep this artifact root fixed when changing directories;
never use nested repositories or global agent-installation directories for artifacts.

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

   Done when every proposed slice has a title, delivery statement, acceptance
   criteria, and only its genuine blocking edges.

3. Write the proposed numbered breakdown to `.agents/projects/<project>/ticket-drafts.md`.
   For Jira, show the existing main ticket or proposed main-ticket title and body,
   with a numbered checklist covering every slice. For GitHub, show each proposed
   Issue. Include delivery, acceptance criteria, and blockers for every slice.
   Ask whether granularity and blocking edges are correct; iterate until approval.

   Do not create or modify Jira tickets or GitHub Issues before explicit approval.
   Done when the user approves the complete breakdown.

4. Publish the approved breakdown. Default to Jira when project
   context names Jira or no tracker has been established; use GitHub Issues only when
   Jira is unavailable or the user explicitly selects GitHub. In Jira, update the
   approved existing main ticket or create one main ticket with the checklist in its
   description. Give items stable numbers and state item-level blockers beside them.
   Preserve existing completion marks; new items start unchecked until completion is
   evidenced. Use native issue links for external ticket blockers.
   In GitHub, publish the approved Issues in dependency order and use native blocking
   relationships where available, otherwise state blockers in the body. Use available
   authenticated tooling, or produce ready-to-paste bodies and record the limitation.

   Done when every approved slice is a checklist item in the main Jira ticket or a
   GitHub Issue, with a tracker identifier or ready-to-paste fallback.

5. Update the active project's `CONTEXT.md`, `LINKS.md`, and `todo.md` with the
   tracker choice, ticket identifiers, URLs, checklist item numbers where applicable,
   dependency status, and next frontier. As each Jira task completes and its required
   verification passes, use `update-ticket` to check its item in the main ticket;
   this completion update needs no further approval.
   Append `Written by Cursor` to any agent-authored Jira or GitHub comment, but not
   ticket descriptions or local documentation.

   Done when project artifacts point to the published ticket set and its current
   implementation frontier.

## Done when

- Every approved slice is accounted for in the main Jira checklist or GitHub Issues.
- Jira has no newly created subtickets; item-level blockers remain visible.
- Project artifacts record tracker links, item numbers, and the next frontier.
- Completed Jira tasks are checked, or unavailable tracker access is recorded with
  the exact pending checklist update.
