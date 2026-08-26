# LightningPay Service Landscape

Use this reference only when the invocation identifies LightningPay. It is a discovery
map, not a claim that every service owns every integration. Confirm each relevant edge
in the service before making it a finding or a target-package responsibility.

## Entry Flows

Map each active inbound source to its source-specific entry flow and the domain behavior
it starts:

- HTTP APIs: authentication, request validation, response and error translation, and
  public contract versioning.
- gRPC APIs: service contracts, deadlines, metadata propagation, and RPC error mapping.
- Administrative workers: privileged operations, audit ownership, scheduling, and safe
  retry behavior.
- Kafka consumers and producers: topic ownership, schema compatibility, partition and
  ordering assumptions, offset handling, idempotency, and dead-letter behavior.
- SQS consumers and producers: queue ownership, visibility timeout, retry and
  redrive behavior, ordering guarantees, and idempotency.

## Domain And Infrastructure Boundaries

For each flow, establish the owner of payment state, transaction boundaries, idempotency
keys, state transitions, audit records, and externally observable events. Keep HTTP,
gRPC, Kafka, and SQS payloads at their transport boundary; do not use them as the domain
model. Identify whether a deep lifecycle module owns behavior across synchronous and
asynchronous triggers.

Map adapters for persistent storage, cache, Kafka, SQS, remote payment systems, and
notification delivery. Verify which component owns retries, deduplication, timeout
policy, compensating actions, and failure translation at each edge.

## Observability

Trace correlation and causation identifiers across HTTP, gRPC, workers, and messages.
Review logs, metrics, traces, audit records, alerts, and dashboards for enough evidence
to reconstruct a payment flow without exposing sensitive payment or personal data.
