# Interface Design For Testability

Good interfaces make behavior tests natural.

## Accept Dependencies

Accept dependencies instead of creating them internally:

```typescript
function processOrder(order, paymentGateway) {}
```

Avoid hiding boundary construction inside behavior:

```typescript
function processOrder(order) {
  const gateway = new StripeGateway();
}
```

## Return Results

Prefer returning results over mutating distant state:

```typescript
function calculateDiscount(cart): Discount {}
```

Be careful with functions whose only observable behavior is a side effect; they are harder to test through a clean public interface.

## Keep Surface Area Small

Small interfaces reduce the number of tests and the amount of setup:

- Fewer methods.
- Fewer parameters.
- Clear invariants.
- Errors and edge cases callers can understand.
