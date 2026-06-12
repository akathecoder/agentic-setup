# Keep Design Artifacts Confluence-Compatible

The `design` skill should produce artifacts that are intended to be published to Confluence later. It should default to conservative Confluence-safe Markdown: headings, paragraphs, ordered and unordered lists, standard tables, links, and fenced code blocks.

Mermaid diagrams remain allowed, but only as fenced `mermaid` code blocks with a nearby prose or table fallback summary so the design stays readable if Confluence does not render Mermaid.

## Consequences

The skill should avoid Markdown extensions and structures that may not survive Confluence publishing reliably. Build should update the design skill's artifact, documentation, and diagram guidance to make this compatibility rule explicit.
