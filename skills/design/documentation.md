# Design Documentation

## Keep Documents Current

Update the design packet as the conversation evolves. Routine updates for agreed facts, open questions, todos, and context do not need separate approval. Architectural, product, or design decisions need user confirmation before being recorded as chosen.

## Confluence-Compatible Markdown

Write every generated artifact as if it will later be published to Confluence by `publish-confluence`.

Use:

- ATX headings (`#`, `##`, `###`).
- Plain paragraphs.
- Ordered and unordered lists.
- Standard Markdown tables.
- Standard links.
- Fenced code blocks with language tags.

Avoid:

- Raw HTML.
- Footnotes.
- Definition lists.
- Custom heading anchors.
- Admonition or callout syntax such as `:::note`.
- Collapsible sections.
- Nested tables.
- Merged table cells.
- Complex Markdown inside table cells.
- Checkbox-only task lists when the document is meant to be read as a final design artifact.

If an advanced structure would make the design clearer, write the information as a normal heading, paragraph, list, or table instead.

## Document Boundaries

- `context.md` captures intake context and constraints.
- `design_plan.md` is the living decision spine and user-facing design summary.
- `hld.md` covers service boundary, larger-system context, major components, dependencies, and system-level architecture.
- `lld/001_xxx.md` covers a specific component, API, internal behavior, algorithm, edge case, or implementation-relevant detail.
- `schemas/001_xxx.md` covers DB schemas, SQL queries, Redis keys, events, API payloads, and other structured contracts.
- `flows/001_xxx.md` covers Mermaid flowcharts, sequence diagrams, state diagrams, and journey diagrams.
- `adr/0001_xxx.md` records confirmed durable architecture decisions.
- `open_questions.md` tracks unresolved questions.
- `todo.md` tracks pending design work.

## HLD Guidance

Create `hld.md` when the design has enough shape to describe the system at a high level. Include:

- Problem and goals.
- Non-goals.
- Service boundary.
- Larger-system context.
- Major components.
- External dependencies.
- Major request, event, or data flows.
- Operational and reliability considerations.
- Security, privacy, and compliance considerations when relevant.
- Open risks.

## LLD Guidance

Create an LLD when a specific part of the design needs detail outside `design_plan.md`. Use one file per coherent subject, such as:

- `lld/001_api_contracts.md`
- `lld/002_worker_processing.md`
- `lld/003_idempotency.md`

Include the reason the detail matters, proposed behavior, edge cases, failure behavior, and unresolved questions.

## Schema Guidance

Use `schemas/001_xxx.md` for structured contracts. Prefer tables for field descriptions:

```md
| Field | Type   | Required | Description                              |
| ----- | ------ | -------- | ---------------------------------------- |
| `id`  | string | Yes      | Stable unique identifier for the record. |
```

For SQL or Redis designs, include key indexes, uniqueness constraints, TTLs, access patterns, and ownership. For events and APIs, include producers, consumers, versioning, compatibility, and failure behavior.

Keep schema tables Confluence-friendly: one row per field, short cell text, no nested lists inside cells, and detailed notes in paragraphs below the table.

## ADR Guidance

Create an ADR only when all are true:

1. The decision is hard to reverse.
2. A future reader would wonder why this path was chosen.
3. There were real alternatives.

Use sequential names such as `adr/0001-service-boundary.md`.

Template:

```md
# <Decision Title>

<1-3 sentences explaining the context, decision, and why.>

## Considered Options

## Consequences
```

Skip ADRs for obvious or easy-to-reverse choices.

## Open Questions

Group questions in `open_questions.md` by audience:

- User or product.
- Staff engineer or architect.
- Security, compliance, or privacy.
- Operations or SRE.
- Wider team.

Close questions when answered, and link the answer to the document or ADR that recorded the decision.

Use simple status labels for questions, for example `Open`, `Answered`, or `Blocked`, instead of relying only on checkbox rendering.
