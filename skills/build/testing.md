# Testing Guidance

## Good Tests

Good tests verify observable behavior through public interfaces:

```typescript
test("user can checkout with valid cart", async () => {
  const cart = createCart();
  cart.add(product);
  const result = await checkout(cart, paymentMethod);
  expect(result.status).toBe("confirmed");
});
```

Characteristics:

- Tests behavior users or callers care about.
- Uses public API only.
- Survives internal refactors.
- Describes what, not how.
- Keeps assertions focused on one behavior.

## Bad Tests

Avoid implementation-detail tests:

```typescript
test("checkout calls paymentService.process", async () => {
  const mockPayment = jest.mock(paymentService);
  await checkout(cart, payment);
  expect(mockPayment.process).toHaveBeenCalledWith(cart.total);
});
```

Red flags:

- Mocking internal collaborators.
- Testing private methods.
- Asserting on call counts or internal order.
- Test breaks when refactoring without behavior change.
- Test name describes implementation instead of behavior.

## Mocking

Mock at system boundaries only:

- External APIs.
- Time and randomness.
- File system when a real fixture is not practical.
- Databases only when a test database is not practical.

Do not mock:

- Your own modules.
- Internal collaborators.
- Code you control.

Prefer dependency injection for boundary clients so tests can supply a realistic fake without contorting production code.
