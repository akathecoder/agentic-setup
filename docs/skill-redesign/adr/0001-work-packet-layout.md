# Use Per-Work-Packet Planning Folders

Planning artifacts for a feature, Jira ticket, or coherent change should live together under `docs/<jira-ticket-or-context>/`. This keeps glossary, ADRs, todo state, optional implementation specs, and online references in one place so later Build, Review, and Feedback Implementation sessions can recover the relevant context without hunting across root-level files.

## Considered Options

- Root-level `CONTEXT.md`, `tasks/todo.md`, and `docs/adr/`
- A single combined planning document
- Per-work-packet folders with separate files for links, glossary, todo, optional plan details, and ADRs

## Consequences

- Jira-backed work should use a lower-case ticket folder such as `docs/pmntc-1234/`.
- Non-Jira work should use a concise context folder such as `docs/skill-redesign/`.
- The Plan skill should keep implementation code out of planning artifacts while still recording interfaces, test intent, risks, and guardrails when needed.
