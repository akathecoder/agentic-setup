# Refactoring After Green

Refactor only after tests are passing.

Look for:

- Duplication that can be removed without obscuring behavior.
- Long methods that hide multiple responsibilities.
- Shallow modules that add interface cost without leverage.
- Feature envy where behavior belongs with different data.
- Primitive obsession where a value object would clarify invariants.
- Existing code that the new behavior reveals as misleading or brittle.

Run relevant tests after each meaningful refactor step.

Do not broaden scope during refactor. If a larger cleanup is discovered, record it as follow-up unless it blocks the approved work.
