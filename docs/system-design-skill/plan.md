# Design Skill Plan

## Goal

Design a new active skill that helps a developer and agent collaboratively design a new software system or service before implementation begins.

## Skill Trigger

`Use when collaboratively designing a new software system or service before implementation, including service boundaries, HLD, LLD, data schemas, flows, and architectural decisions.`

## Current Intent

The active skill name is `design`.

The skill should interview the user for service intent, responsibilities, larger-system context, scope boundaries, existing constraints, user ideas, must-haves, must-avoids, good-to-haves, and any early design sketches before proposing architecture.

The skill should keep living design documents under `designs/<system-slug>/` up to date throughout the conversation and use Mermaid diagrams for user flows, API flows, sequence diagrams, and other flow-heavy explanations.

The design artifacts should be written with later Confluence publication in mind. Use conservative Confluence-safe Markdown by default: headings, paragraphs, ordered and unordered lists, standard tables, links, and fenced code blocks. Avoid Markdown extensions or custom structures that may not render reliably in Confluence.

The primary design file should be `designs/<system-slug>/design_plan.md`.

`design_plan.md` should be the living decision spine for the design. It should include the goal, scope, current proposed architecture, confirmed decisions, key flows, links to HLD/LLD/schema/ADR details, and current next questions.

Mermaid diagrams should live in `designs/<system-slug>/flows/001_xxx.md` when they need more than a short summary in `design_plan.md`, `hld.md`, or an LLD. Every Mermaid diagram should include a nearby prose or table fallback summary so the design remains readable if Confluence preserves the diagram as code rather than rendering it.

At the start of a design session, the skill should create the core files immediately:

- `context.md`
- `design_plan.md`
- `open_questions.md`
- `todo.md`

The skill should create detailed HLD, LLD, schema, flow, and ADR content only when the discussion produces enough substance for those documents.

## Design Packet Boundaries

- `context.md` captures the intake context, constraints, scope boundaries, user ideas, must-haves, must-avoids, and good-to-haves.
- `design_plan.md` is the living decision spine and user-facing design summary.
- `hld.md` covers service boundary, larger-system context, major components, dependencies, and system-level architecture.
- `lld/001_xxx.md` covers component-level, API-level, internal behavior, algorithms, edge cases, and implementation-relevant details.
- `schemas/001_xxx.md` covers DB schemas, SQL queries, Redis keys, events, API payloads, and other structured contracts, with field descriptions where useful.
- `flows/001_xxx.md` covers Mermaid flowcharts, sequence diagrams, state diagrams, and journey diagrams.
- `adr/0001_xxx.md` records confirmed durable architecture decisions with context, considered options, and consequences when useful.
- `open_questions.md` tracks unresolved questions for the user, staff engineers, product managers, or wider team.
- `todo.md` tracks pending design decisions, conversations, documents, reviews, and validation work.

## Proposed Skill Files

The implemented skill should use progressive disclosure:

- `skills/design/SKILL.md` - small entrypoint with frontmatter, when to use the skill, workflow, and links to supporting files.
- `skills/design/artifacts.md` - design packet layout, naming, file creation timing, and document ownership.
- `skills/design/intake.md` - required context gate, optional context, and how to update `context.md`.
- `skills/design/questioning.md` - one-question-at-a-time pair-design loop, recommendations, and confirmation requirements.
- `skills/design/documentation.md` - HLD, LLD, schema, flow, ADR, open-question, and todo update rules.
- `skills/design/diagrams.md` - Mermaid flowchart and sequence-diagram guidance.
- `skills/design/guardrails.md` - design-only scope, no implementation, no unconfirmed decisions, and no proactive handoff.

Before design work starts, the skill should use a hybrid intake flow: create or update `context.md` from the initial user prompt, then ask one focused follow-up question at a time for missing required context.

Mandatory context before architecture proposals:

- Service intent.
- Service responsibilities.
- Where the service is used in the larger system.
- What is in scope for this service.
- What is out of scope because other services own it.
- What is in scope for the current design discussion.
- What is out of scope for the current design discussion.
- Existing constraints.
- Must-haves.
- Must-avoids.

Optional but captured when available:

- Initial user ideas and plans.
- Good-to-haves.
- Basic designs or sketches.
- Other contextual notes that affect later decisions.

## Known Guardrails

- Gather required context before making design decisions.
- Do not require the user to fill a rigid form when the initial prompt already contains usable context.
- Capture optional ideas without letting them bypass the required context gate.
- Keep all design artifacts packet-local under `designs/<system-slug>/`.
- Keep all design artifacts compatible with later Confluence publishing.
- Keep the process as a pair discussion with the user or developer.
- Do not decide anything independently without first showing the proposed decision and reasoning, then receiving confirmation.
- Allow routine document updates for agreed facts, open questions, todos, and context without a separate confirmation prompt.
- Keep design artifacts current as the conversation evolves.
- Stop before implementation; this skill designs the service before a new service is written.
- Do not proactively hand off to `plan`, `prototype`, or `build`; follow-on work happens only when the user explicitly asks.

## Decisions Needed

- Active README description and skill trigger wording.
