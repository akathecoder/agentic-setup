# CONTEXT.md Format

The active replacement is `skills/plan/documentation.md`, which uses per-work-packet `glossary.md` files.

Legacy `CONTEXT.md` structure:

```md
# {Context Name}

{One or two sentence description of what this context is and why it exists.}

## Language

**Order**:
{A concise description of the term}
_Avoid_: Purchase, transaction

## Relationships

- An **Order** produces one or more **Invoices**.

## Example dialogue

> **Dev:** "When is the **Invoice** created?"
> **Domain expert:** "Only after **Fulfillment** is confirmed."

## Flagged ambiguities

- "account" was used to mean both **Customer** and **User** - resolved: these are distinct concepts.
```
