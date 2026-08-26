# Go Re-architecture

Use this reference only when the reviewed repository uses Go. Apply the repository's
documented conventions first; these are the review baseline, not a replacement for
evidence.

## Assessment

Inspect package acyclicity, `internal` boundaries, composition at `main`, context
propagation and cancellation, resource cleanup, and error wrapping with `errors.Is` or
`errors.As`. Run or assess the standard `gofmt`, `go vet`, `staticcheck`, and
`govulncheck` gates. Include `go test -race` where concurrent behavior exists.

Look for interfaces owned by their consumer, concrete types retained until a real seam
exists, and package names that describe domain capability rather than a technical
bucket. Treat exported API, package visibility, `context.Context`, goroutine lifecycle,
and resource ownership as architecture decisions, not implementation details.

## Target Package Map

Start the proposed package map from this hierarchy. Change it only when repository
evidence supports a better fit:

```text
cmd/<service>                 composition root and process lifecycle
internal/transport/<protocol> inbound handlers and protocol mapping
internal/<domain>             use cases, lifecycle, types, policy, ports, and errors
internal/<domain>/adapter     domain-owned persistence and remote-system adapters
internal/platform             domain-neutral observability and configuration
```

A handler decodes and validates protocol input, invokes the source-specific entry flow,
and translates its result. The composition root wires concrete adapters to application
behavior. Keep transport and persistence DTOs at their boundary, avoid `I`-prefixed
interfaces, and define an interface in the package that consumes it. Use `platform` only
for truly domain-neutral capabilities, never as a second application layer.

## Errors And Tests

Use errors that retain their cause while exposing a stable domain meaning. Keep a
package's public error taxonomy in an `errors` file when that makes its contract easy to
find; keep tightly local failures beside the behavior they explain. Translate domain
errors to HTTP, RPC, or message outcomes only at a transport boundary.

Test behavior through the highest useful public seam. Add adapter integration tests for
database, cache, queue, and remote protocol behavior. Cover cancellation, cleanup,
timeouts, and concurrent failure paths where they apply. Target 100% coverage for
changed behavior and require at least 95% for the agreed scope, with named and justified
exclusions.
