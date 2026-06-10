# TDD Default

TDD is the default for meaningful behavior changes. Use the escape hatch only for trivial or mechanical edits, or when the user explicitly approves a non-TDD path.

## Philosophy

Tests should verify behavior through public interfaces, not implementation details. Code can change entirely; behavior tests should survive.

Good tests are integration-style: they exercise real code paths through public APIs and describe what the system does, not how it does it.

Bad tests are coupled to implementation: they mock internal collaborators, test private methods, assert call order, or break when behavior is unchanged.

## Anti-Pattern: Horizontal Slices

Do not write all tests first, then all implementation.

Wrong:

```text
RED:   test1, test2, test3, test4
GREEN: impl1, impl2, impl3, impl4
```

Right:

```text
RED->GREEN: test1->impl1
RED->GREEN: test2->impl2
RED->GREEN: test3->impl3
```

Each test should respond to what was learned from the previous cycle.

## Tracer Bullet

Start with one behavior that proves the path works end-to-end:

```text
RED:   Write one test for one behavior.
GREEN: Write minimal code to pass.
```

Then repeat for the next behavior.

## Per-Cycle Checklist

```text
[ ] Test describes behavior, not implementation.
[ ] Test uses the public interface.
[ ] Test would survive internal refactor.
[ ] Code is minimal for this behavior.
[ ] No speculative features were added.
```

Never refactor while red. Get green first, then refactor.
