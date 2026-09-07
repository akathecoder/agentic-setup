# akathecoder's Agentic Setup

This repository is the source of truth for reusable agent skills and Cursor rules.

## Contents

- `skills/` - Canonical portable skill sources.
- `rules/` - Canonical Cursor rule sources.

## Installing Skills

Install selected skills into a supported coding agent with:

```bash
npx skills@latest add akathecoder/agentic-setup
```

The installer lets you choose skills and a target harness. Consult the target agent's
documentation for its installation and configuration steps.

## Skills

### Main Skills

| Skill             | Use case                                                                                                 |
| ----------------- | -------------------------------------------------------------------------------------------------------- |
| `grill-with-docs` | Interview a change or design until decisions are clear, while maintaining project context and decisions. |
| `to-spec`         | Turn settled project discussion into a local and tracker-published specification.                        |
| `to-tickets`      | Break approved work into small, dependency-aware implementation tickets.                                 |
| `implement`       | Implement approved specifications or tickets with tests and final review.                                |

### Design And Planning

| Skill                           | Use case                                                                                     |
| ------------------------------- | -------------------------------------------------------------------------------------------- |
| `improve-codebase-architecture` | Find codebase architecture improvements and work through a selected opportunity.             |
| `review-service-architecture`   | Assess a service, propose a behavior-preserving target architecture, and plan its migration. |
| `grilling`                      | Stress-test an idea, plan, or design by resolving its open decisions.                        |
| `grill-me`                      | Relentless interview to sharpen a plan or design, without writing project artifacts.         |
| `prototype`                     | Throwaway prototype that answers a design question about logic, state, or UI.                |
| `wayfinder`                     | Map a large, uncertain project as decision tickets before implementation begins.             |
| `domain-modeling`               | Clarify and record project terminology, facts, and durable design decisions.                 |
| `codebase-design`               | Design deeper module boundaries, interfaces, seams, and test strategies.                     |

### Implementation And Quality

| Skill                | Use case                                                                                   |
| -------------------- | ------------------------------------------------------------------------------------------ |
| `tdd`                | Build or fix code through a red-green-refactor testing loop.                               |
| `code-review`        | Review a branch, pull request, or working diff against project requirements and standards. |
| `triage-pr-feedback` | Validate PR review feedback, fix valid findings, and resolve review threads.               |
| `wizard`             | Walk a human through a manual procedure only they can perform.                             |

### Documentation And Communication

| Skill              | Use case                                                                                       |
| ------------------ | ---------------------------------------------------------------------------------------------- |
| `to-confluence`    | Turn project knowledge into a concise, standalone Confluence page.                             |
| `update-ticket`    | Draft a meaningful Jira or GitHub progress update for approval before posting.                 |
| `unslop`           | Edit documentation, tickets, or other reader-facing prose to be direct, natural, and specific. |
| `research`         | Investigate a question against primary sources and write cited findings.                       |
| `to-questionnaire` | Turn a decision only someone else can answer into a questionnaire for them.                    |

### Utility

| Skill                | Use case                                                                     |
| -------------------- | ---------------------------------------------------------------------------- |
| `handoff`            | Compact the current conversation into a project handoff for a fresh agent.   |
| `bro-what`           | Re-explain the previous response in plain language.                          |
| `teach`              | Teach a skill or concept over multiple sessions in a project workspace.      |
| `writing-for-agents` | Reference for writing skills, AGENTS.md, and other agent-consumed documents. |
| `install-from-catalog` | Install a chosen third-party skill, plugin, or extension from a curated catalog. |
