# Architecture Report Format

Read this reference before rendering the visual report. Use the same information and
visual hierarchy in a Cursor Canvas or, when Canvas is unavailable, the HTML fallback.

## Structure

- Header: repository name, date, and compact legend for module, seam, leakage, and
  deep module. Go straight to candidates.
- Candidate cards: short deepening title, recommendation-strength badge (`Strong`,
  `Worth exploring`, or `Speculative`), dependency category, involved files/modules,
  before/after visual, one-sentence problem and solution, concise wins, and any ADR
  conflict callout.
- Top recommendation: candidate name, one sentence on why, and a link to its card.

## Visuals

Make the before/after visual the center of each candidate. Use graphs for dependencies
or call flow, cross-sections for shallow layered paths, mass diagrams for interface
size versus implementation, and call-graph collapse for hidden internal work. Vary the
visual type when candidates need different explanations. Diagrams should show a seam,
leakage, and the resulting deep module clearly without a prose paragraph.

For HTML, use a self-contained static document with Tailwind and Mermaid from CDNs.
For Canvas, use native visual blocks, connectors, labels, and diagrams that communicate
the same structure rather than embedding an HTML approximation.

## Language

Use the active project's domain terms with these architectural terms exactly: module,
interface, implementation, depth, deep, shallow, seam, adapter, leverage, and
locality. Keep prose sparse and plain. Wins must name the concrete gain, such as
"locality: bugs concentrate in one module" or "leverage: one interface, N callers."
