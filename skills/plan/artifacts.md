# Plan Artifacts

## Work Packet Location

Create planning artifacts under one folder:

```text
docs/<jira-ticket-or-context>/
```

Use a lower-case Jira ticket when available, such as `docs/pmntc-1234/`. If the work is not tied to a ticket, choose a short kebab-case context name, such as `docs/checkout-retry-plan/`.

## Required Files

Every Plan run creates or maintains:

- `links.md` - Jira tickets, Confluence pages, PRs, design docs, review threads, or other online references.
- `glossary.md` - domain language and resolved terminology for this work.
- `todo.md` - checkable implementation, verification, and review tasks.
- `adr/` - ADRs for durable decisions.

Create `plan.md` only when the change needs a fuller handoff: high-level interfaces, test intent, risks, sequencing, rollout notes, or implementation guardrails.

## `links.md`

Use this structure:

```md
# Links

- Jira: <url or "Not provided">
- Confluence: <url or "Not provided">
- Pull request: <url or "Not created yet">
- Other references:
  - <url> - <why it matters>
```

If no links are known, say so explicitly. Do not invent ticket numbers or URLs.

## `todo.md`

Track Plan progress and the future Build handoff:

```md
# <Work Name> Todo

## Plan

- [ ] Clarify scope and constraints.
- [ ] Record glossary decisions.
- [ ] Record ADR-worthy decisions.
- [ ] Define Build handoff.

## Build

- [ ] <implementation task>

## Verification

- [ ] <required test or check>

## Review

- [ ] Review final diff for correctness and risk.
```

Mark items complete as they are proven, not when they are merely discussed.

## `plan.md`

When needed, keep `plan.md` high level. It can include:

- Goal and non-goals.
- Proposed shape and affected areas.
- Public interfaces or contracts to preserve/change.
- Required tests as behavior statements, not test code.
- Risks, edge cases, and guardrails for Build.
- Open questions and decisions.

Do not write implementation code in `plan.md`.
