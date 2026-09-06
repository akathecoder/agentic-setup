---
name: handoff
description: Compact the current conversation into a project handoff so a fresh agent can continue the work.
disable-model-invocation: true
argument-hint: "What will the next session be used for?"
---

# Handoff

Write a compact handoff of the current conversation so a fresh agent can continue
the work. If the user described what the next session will focus on, tailor the
document to that.

Resolve every `.agents/projects/` path from the repository root; never read or write
project artifacts in a global agent-installation directory.

## Process

1. Identify the active project. Read its `CONTEXT.md`, `LINKS.md`, todo, lessons, and
   any spec, tickets, review, or ADRs this conversation used.

   Done when standing artifacts and the next-session purpose are known.

2. Record newly confirmed project facts, links, remaining work, and user corrections
   in the standing artifacts they belong in. Redact API keys, passwords, and personally
   identifiable information.

   Done when durable knowledge from this session lives in those files rather than only
   in the handoff.

3. Generate a short random hex id and write
   `.agents/projects/<project>/handoffs/<id>.md` using the structure below. Point at
   existing artifacts by path or URL. Describe code by its types and behaviours. Name
   the skills the next agent should invoke. Tell the user the path.

   Done when a fresh agent can continue from the document plus the artifacts it points
   at, without this conversation, and the user has the path.

## Document

```md
# Handoff: <next session purpose>

## Next session

<What the next agent should do, scoped to the stated purpose.>

## Suggested skills

- <skill-name>: <why this session needs it>

## Pointers

- `.agents/projects/<project>/CONTEXT.md`

## Session outcome

<What this session accomplished that the standing artifacts do not already record.>

## Open

<Blockers, unresolved decisions, and in-flight work described by behaviour.>
```

## Done when

- Standing artifacts hold the durable facts, remaining work, and corrections from this
  session.
- `.agents/projects/<project>/handoffs/<id>.md` is tailored to the next session and
  contains only what those artifacts do not.
- The user has the path.
