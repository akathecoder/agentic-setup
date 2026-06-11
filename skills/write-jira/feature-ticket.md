# Feature Tickets

Use this workflow for Jira tickets that track feature build work, often under `PMNTC`. The Jira issue type may be Story, Task, Item, SubItem, Bug, or another project-specific type.

## Purpose

Feature tickets should give devs, QA, PMs, and reviewers enough context to understand:

- What is changing
- Why the change exists
- How the change should be validated
- Which tickets, docs, PRs, and decisions are related
- What progress or blockers have happened over time

## Information To Collect

Ask only for information that is missing from the base ticket, linked sources, or user-provided context.

- Goal or problem statement
- Scope and explicit out of scope items
- User or stakeholder impact
- Requested product or technical changes
- Acceptance criteria
- QA notes and test scenarios
- Implementation notes, constraints, feature flags, migrations, configs, or dependencies
- Linked Jira tickets
- Linked Confluence pages, design docs, dashboards, Slack threads, or PRs
- Current status, blockers, or progress updates

## Description Sections

Use these sections when applicable. Omit sections that are not applicable.

```markdown
## Context

[Why this work is needed and who it affects.]

## Scope

[What is included in this ticket.]

## Out Of Scope

[What is explicitly not included.]

## Requested Change

[What needs to be built, changed, configured, released, or validated.]

## Acceptance Criteria

- [ ] [Behavior or outcome that must be true]
- [ ] [Behavior or outcome that must be true]

## QA Notes

[Test scenarios, regression areas, environments, data setup, edge cases, or ownership.]

## Implementation Notes

[Technical approach, dependencies, configs, migrations, feature flags, rollout constraints, or links to implementation references.]

## Linked References

- Jira: [ticket links]
- Docs: [Confluence/design links]
- PRs: [PR links]
- Dashboards: [dashboard links]
```

## Comments

Use comments for time-based updates that should remain part of the ticket history:

- Build progress
- QA handoff or QA result
- Blockers and unblockers
- Release readiness notes
- Important decisions made after the description was written

Preview comment text before adding it.

## Links

Create real Jira issue links when the user wants Jira-level relationships, not just description text.

If the relationship type is unclear, call `getIssueLinkTypes` and ask the user to choose. For directional link types, verify direction in the approval preview.
