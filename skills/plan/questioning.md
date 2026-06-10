# Plan Questioning

## Core Loop

Interview the user until the plan is clear enough to build. Walk the decision tree one branch at a time.

For each unresolved decision:

1. Check whether the answer can be found by reading code, docs, tickets, or existing references.
2. If it can be discovered, explore instead of asking.
3. If user judgment is required, ask one focused question.
4. Provide your recommended answer with the trade-off.
5. Wait for the user's answer before moving to the next decision.
6. Update the work packet immediately when the decision affects glossary, ADRs, todo, risks, or Build handoff.

## AskQuestion Usage

Use `AskQuestion` for structured choices, confirmations, prioritization, and disambiguation. Use normal chat for free-form details such as long product requirements, reproduction steps, or narrative constraints.

Good `AskQuestion` candidates:

- Choosing between implementation approaches.
- Confirming non-goals.
- Prioritizing behaviors to test.
- Selecting the work packet folder when multiple tickets are plausible.
- Confirming whether an ADR should be written.

## Question Quality

Ask questions that force precision:

- Replace fuzzy nouns with concrete domain terms.
- Ask about edge cases, not only the happy path.
- Ask how the system should behave when dependencies fail.
- Ask what must be preserved for existing users.
- Ask what should explicitly be out of scope.

Avoid asking the user to answer questions the codebase can answer.

## Recommendation Format

When asking, include a recommendation:

```md
I recommend <option> because <reason>. The trade-off is <cost/risk>.
```

Do not present a menu of options without a point of view.
