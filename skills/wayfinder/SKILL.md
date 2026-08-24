---
name: wayfinder
description: Plan a huge, uncertain project as a map of decision tickets until the route to implementation is clear.
disable-model-invocation: true
---

# Wayfinder

Use Wayfinder when a loose idea is too large or uncertain for one agent session.
It charts the way to a **destination** as a shared map of **decision tickets**:
questions whose resolution clarifies the route, not implementation slices that deliver
the destination.

Wayfinder plans by default. Hand off to `to-spec` and `to-tickets` when the route is
clear. The decision tickets in this skill are not the implementation tickets created
by `to-tickets`.

Resolve every `.agents/projects/` path from the repository root; never read or write
project artifacts in a global agent-installation directory.

## The Map

The active project's map lives at `.agents/projects/<project>/wayfinder.md` and is published
to the selected issue tracker as the shared tracker map with the `wayfinder:map`
label. Its decision-ticket drafts live at
`.agents/projects/<project>/wayfinder-ticket-drafts.md`. The local and tracker maps carry the
same content; update both after each resolved decision.

The map is an index, not a decision store. Each resolution lives only in its decision
ticket. In human-facing text, refer to a ticket by its linked title, never a bare
identifier.

```md
# Wayfinder: <destination>

## Destination

<What reaching the end of this map looks like.>

## Notes

<Domain, required skills, and standing preferences.>

## Decisions So Far

- [<closed ticket title>](link) - <one-line gist of the answer>

## Not Yet Specified

<In-scope questions that are visible but not yet precise enough to ticket.>

## Out Of Scope

<Work consciously ruled beyond this destination.>
```

## Ticket Types

Each decision ticket has one type and is sized for one fresh agent session:

- **Research**: an agent investigates documentation, third-party APIs, or local
  sources to surface a fact a decision needs.
- **Prototype**: a user evaluates a cheap concrete artifact to decide behavior or
  appearance.
- **Grilling**: the user and agent resolve a decision through `grilling` and
  `domain-modeling`.
- **Task**: a blocking action such as provisioning access or preparing data; it exists
  only to unblock a later decision.

Label each decision ticket `wayfinder:<type>` using its lowercase type. Use the
configured tracker's native parent/child and blocking relationships. A ticket is
**unblocked** when all blockers are closed. The **frontier** is the set of open,
unblocked, unclaimed decision tickets.

## Chart The Map

1. Identify the active project and read its context, links, ADRs, and existing
   planning artifacts. Resolve the tracker from project context: Jira by default,
   GitHub Issues only when Jira is unavailable or the user explicitly selects GitHub.

   Done when the project facts, tracker, and existing constraints are known.

2. Use `grilling` and `domain-modeling` to name the destination. Then map the first
   frontier breadth-first: surface the decisions currently precise enough to state and
   capture the rest as fog. If there is no fog and the work fits one session, stop and
   recommend the smaller planning flow instead.

   Done when the destination, initial frontier, and in-scope fog are distinct.

3. Draft the local map and proposed decision tickets. Each draft names its question,
   type, blockers, and expected resolution. Keep a question in **Not Yet Specified**
   when it cannot yet be stated precisely; do not pre-slice fog into tickets. Put work
   outside the destination in **Out Of Scope**, never in fog.

   Done when `.agents/projects/<project>/wayfinder.md` and
   `.agents/projects/<project>/wayfinder-ticket-drafts.md` describe the map and initial
   decision tickets.

4. Show the map and ticket drafts to the user. Do not create the tracker map or any
   Jira/GitHub decision ticket until the user explicitly approves the draft. On
   approval, create the map first, then its child decision tickets, then wire blocking
   edges in a second pass. If authenticated tooling is unavailable, produce
   ready-to-paste tracker bodies and record the limitation in project context.

   Done when the approved map and every initial decision ticket have tracker links, or
   ready-to-paste equivalents are recorded.

5. Update `CONTEXT.md` and `LINKS.md` with the map URL, tracker choice, ticket links,
   and current frontier. Start research tickets in parallel where tooling permits;
   charting itself resolves no decision tickets.

   Done when the map is published, project artifacts point to it, and the session has
   stopped before hand-resolving a ticket.

## Work Through The Map

Resolve no more than one non-research ticket per session.

1. Load the map, not every child ticket. Use a ticket supplied by the user, or select
   the first ticket on the frontier. Claim it in the tracker before beginning so
   concurrent sessions skip it.

   Done when one unblocked decision ticket is claimed.

2. Resolve the question using its ticket type. Fetch related ticket detail only when
   needed. Use `grilling` and `domain-modeling` for a Grilling ticket. A HITL ticket
   only resolves through the user; do not answer the user's side yourself.

   Done when the ticket's decision or blocking task has a concrete outcome.

3. Post the outcome as a tracker resolution comment, ending with the exact line
   `Written by Cursor`. Close the ticket and add a linked one-line gist to the map's
   **Decisions So Far**. Keep detailed reasoning and created assets linked from the
   ticket rather than duplicating them in the map.

   Done when the resolution, map index, and local project mirror agree.

4. Graduate newly precise fog into fresh decision-ticket drafts. Obtain approval
   before creating any new Jira/GitHub tickets, then create and wire them. If a ticket
   is beyond the destination, close it and record a linked reason under **Out Of
   Scope**. Update or remove tickets invalidated by the decision.

   Done when the frontier and fog accurately reflect what the resolved decision made
   visible.

5. When no unresolved decision remains between the map and the destination, record
   that the route is clear and hand off to `to-spec`, then `to-tickets`. Do not begin
   implementation in Wayfinder.

   Done when the user has a clear next planning handoff or the map identifies the next
   unresolved frontier ticket.
