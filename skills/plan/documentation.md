# Plan Documentation

## Glossary Discipline

Use `glossary.md` for domain language only. It is not a spec, scratch pad, or implementation decision log.

Add or update glossary terms when:

- The user uses a term that conflicts with existing language.
- A term is overloaded or ambiguous.
- A new domain concept becomes central to the work.
- The code and user language disagree and the resolution matters.

Do not add general programming concepts, implementation utilities, or low-level technical details.

## `glossary.md` Format

```md
# <Work Name> Glossary

## Language

**Order**:
A concise definition of the term.
_Avoid_: Purchase, transaction

## Relationships

- An **Order** produces one or more **Invoices**.

## Example dialogue

> **Dev:** "When is the **Invoice** created?"
> **Domain expert:** "Only after **Fulfillment** confirms shipment."

## Flagged ambiguities

- "account" was used to mean both **Customer** and **User** - resolved: these are distinct concepts.
```

Rules:

- Be opinionated. Pick the best canonical term.
- Keep definitions tight: one sentence when possible.
- Define what the term is, not how it is implemented.
- Express relationships and cardinality where useful.
- Record ambiguities with their resolution.

## ADR Discipline

Create ADRs under the work packet's `adr/` folder only when all three are true:

1. Hard to reverse - changing later would be meaningfully costly.
2. Surprising without context - a future reader would wonder why this path was chosen.
3. Real trade-off - there were genuine alternatives.

Skip ADRs for obvious, easy-to-reverse, or purely tactical choices.

## ADR Format

Use sequential numbering inside the work packet:

```text
adr/0001-short-slug.md
adr/0002-next-decision.md
```

Template:

```md
# <Short Decision Title>

<1-3 sentences explaining the context, decision, and why.>
```

Optional sections:

- `## Considered Options` when rejected alternatives matter.
- `## Consequences` when downstream effects are non-obvious.
- Status frontmatter only when decisions are revisited.
