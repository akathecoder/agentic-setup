# Design Questioning

## Pair-Design Loop

Work as a design partner, not an autonomous architect.

For each unresolved decision:

1. Check whether the answer is already in `context.md`, existing docs, code, tickets, or references the user provided.
2. If the answer is discoverable, read first and update the design packet.
3. If user judgment is required, ask one focused question.
4. Present a recommended answer with the reasoning and trade-off.
5. Wait for the user's confirmation before recording the decision as chosen.
6. Update `design_plan.md`, `open_questions.md`, `todo.md`, and ADRs as needed.

## AskQuestion Usage

Use `AskQuestion` for structured choices, confirmations, prioritization, and disambiguation.

Good candidates:

- Choosing a service boundary.
- Selecting a data store or consistency model.
- Confirming in-scope and out-of-scope responsibilities.
- Choosing between synchronous API, async event, queue, or batch flow.
- Prioritizing must-haves versus good-to-haves.
- Confirming whether a durable decision belongs in an ADR.

Use normal chat for free-form context such as business background, operational constraints, rough user journeys, or early design notes.

## Recommendation Format

When asking for a decision, use:

```md
I recommend <option> because <reason>. The trade-off is <cost/risk>.
```

Do not present neutral menus for architectural decisions unless the user explicitly asks for brainstorming without a recommendation.

## Decision States

Use clear labels:

- `Proposed` - the agent has suggested a direction, but the user has not confirmed it.
- `Confirmed` - the user has approved the decision.
- `Rejected` - the user declined the option.
- `Open` - more information is needed.

Never turn a `Proposed` decision into `Confirmed` without user approval.
