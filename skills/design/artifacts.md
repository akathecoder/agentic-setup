# Design Artifacts

## Design Packet Location

Create and maintain design artifacts under:

```text
designs/<system-slug>/
```

Use a short kebab-case slug that names the system or service, such as `payment-orchestrator` or `notification-service`. If the name is unclear, ask the user to confirm the slug before creating files.

## Confluence Compatibility

Assume the completed design packet will be published to Confluence. Write artifacts using conservative Markdown that publishes cleanly:

- Use headings, paragraphs, ordered and unordered lists, standard tables, links, and fenced code blocks.
- Use fenced code blocks with a language tag for schemas, SQL, JSON, API examples, and diagrams.
- Keep tables simple. Avoid nested tables, merged cells, multi-paragraph table cells, and complex Markdown inside table cells.
- Avoid Markdown extensions that may not survive Confluence publishing, such as footnotes, custom anchors, admonition syntax, definition lists, raw HTML, and collapsible sections.
- Prefer plain status labels such as `Open`, `Decided`, `Blocked`, or `Done` over checkbox-only task lists in documents intended for publication.

## Packet Shape

```text
designs/<system-slug>/
├── context.md
├── design_plan.md
├── adr/
├── flows/
├── hld.md
├── lld/
├── schemas/
├── open_questions.md
└── todo.md
```

## Create Immediately

At the start of a design session, create or update:

- `context.md` - intake context, constraints, scope boundaries, user ideas, must-haves, must-avoids, and good-to-haves.
- `design_plan.md` - the living decision spine and the file the user references most often.
- `open_questions.md` - unresolved questions for the user, staff engineers, product managers, or the wider team.
- `todo.md` - pending design decisions, conversations, documents, reviews, and validation work.

Create the `adr/`, `flows/`, `lld/`, and `schemas/` folders when creating the packet so future files have an obvious home.

## Create When Needed

Only create detailed files once there is real content:

- `hld.md` for service boundary, larger-system context, major components, dependencies, and system-level architecture.
- `lld/001_xxx.md` for component-level, API-level, internal behavior, algorithms, edge cases, and implementation-relevant details.
- `schemas/001_xxx.md` for DB schemas, SQL queries, Redis keys, events, API payloads, and other structured contracts.
- `flows/001_xxx.md` for Mermaid flowcharts, sequence diagrams, state diagrams, and journey diagrams.
- `adr/0001_xxx.md` for confirmed durable decisions with meaningful trade-offs.

## `design_plan.md`

Keep `design_plan.md` concise and current. It should include:

- Goal and non-goals.
- Scope for the service and for the current design discussion.
- Current proposed architecture, clearly labeled as proposed until approved.
- Confirmed decisions.
- Key flows, with links to detailed flow documents when needed.
- Links to HLD, LLD, schema, and ADR details.
- Current next questions.

Do not turn `design_plan.md` into a dump of every schema, edge case, and diagram.
