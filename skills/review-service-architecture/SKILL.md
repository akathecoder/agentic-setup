---
name: review-service-architecture
description: Review a service's architecture, then produce a behavior-preserving target design, visual report, repository guidance, and migration plan.
disable-model-invocation: true
argument-hint: "Which service and review name should I assess?"
---

# Review Service Architecture

Review a functioning pre-production service before its structure becomes costly to
change. Preserve confirmed business behavior. Ground the design in real entry flows,
domain boundaries, and preservation constraints rather than a generic folder template.

This is an enterprise architecture review, not a file-by-file style review and not a
mandate to introduce layers. A layer earns its place only when it owns behavior, policy,
or an infrastructure boundary that callers should not learn. Prefer domain packages with
a clear downward dependency rule over global `controllers`, `services`, `common`,
`repositories`, or `types` dumping grounds.

Use the review name supplied in the initial invocation as the active project's kebab-case
slug. When the reviewed repository uses Go, read `GOLANG.md` for the Go-specific
assessment, target package map, error policy, testing, and quality gates. When the
invocation identifies LightningPay, read `LIGHTNINGPAY.md` for its service-landscape
review map. Those references guide discovery; verify their relevance in the service
instead of assuming every integration exists.

Resolve every `.agents/projects/` path from the service repository root.

## Process

1. Establish the review boundary. Read repository guidance, project context, ADRs, and
   architecture documentation. Identify executable entry points, externally observable
   contracts, deployable units, ownership boundaries, and business behavior that must
   remain unchanged. Inspect a useful span of recent commits to find changing hot spots.

   Do not assess a vague service scope. Ask the user to name the service boundary,
   critical flows, preservation constraints, and review name when they cannot be learned
   from evidence.

   Done when the review name, service boundary, critical flows, preservation constraints,
   decision owners, and changing hot spots are known.

2. Build an evidence baseline before proposing a target structure. Explore independent
   areas in parallel when the harness permits. Map composition roots, inbound transports,
   source-specific entry flows, application orchestration, lifecycle behavior, domain
   policies and state, data ownership, transaction boundaries, ports, infrastructure
   adapters, external contracts, configuration, errors, tests, CI, and developer
   commands. Trace each critical flow from its entry point to owned storage or an
   external dependency.

   Assess ownership, dependency direction, module depth, locality, contract discipline,
   failure behavior, observability, and engineering controls. For every candidate,
   record concrete file, symbol, and call-path evidence; the leakage or shallow
   interface; its change or operational cost; and the deletion-test result. Record
   preservation constraints for contracts, topics, schemas, idempotency, transactions,
   state transitions, external-call ordering, and operational behavior where applicable.

   Done when every critical flow has an evidence-backed current-state map and every
   candidate distinguishes a hard risk from a preference.

3. Invoke `domain-modeling` when a term, ownership boundary, or contract is ambiguous.
   Record confirmed vocabulary and durable decisions in the active project's context and
   ADRs. Invoke `improve-codebase-architecture` with the review boundary, critical
   flows, evidence baseline, preservation constraints, and the target preference below.
   It must surface deepening opportunities without speculative abstraction.

   Create the visual report required by `improve-codebase-architecture`: use a native
   Cursor Canvas when available; otherwise create the self-contained HTML fallback. The
   visual must show the current and target call or dependency structure, highest-risk
   leakage, candidate deep modules, preservation constraints, and recommendation
   strength. Keep the supporting findings in
   `.agents/projects/<project>/architecture-review.md`. Ask the user to select the
   candidate or candidates to design.

   Done when the user can inspect a Canvas or HTML visual and has selected the candidate
   scope for target design.

4. Design from the selected domain outward. Every critical flow must be readable through
   this hybrid dependency map:

   ```text
   transport adapter
     -> source-specific entry flow
     -> use case OR deep lifecycle module
     -> domain policies, state, types, and errors
     -> behavior-focused port
     <- technology adapter
   ```

   A source-specific entry flow retains protocol or consumer semantics. A use case owns
   one short-lived business flow. A deep lifecycle module owns stateful behavior that
   spans triggers, such as idempotency, transaction coordination, or state transitions;
   do not introduce one for a simple request. Domain policy owns reusable business rules.
   A port expresses what domain or application behavior needs from an external system;
   its technology adapter owns a database, cache, queue, or network protocol.

   Share a capability only after two domains demonstrably need the same stable behavior.
   Do not create generic `common`, `models`, `types`, `helpers`, or `utils` packages as
   an escape from deciding ownership. Place domain types, commands, results, statuses,
   invariants, and errors with the bounded context that owns them. Keep adapters
   technology-specific and free of business policy.

   Invoke `codebase-design` only when selected candidates have unresolved alternatives
   for a module seam or interface. Compare the alternatives before choosing one; do not
   create an interface merely for tests or hypothetical substitution.

   Write `.agents/projects/<project>/architecture-design.md` as the target-design source
   of truth. It names current risks, target package responsibilities and dependency rule,
   domain and contract ownership, error taxonomy, test seams, quality gates,
   cross-service implications, rejected alternatives, and unresolved decisions. Include
   a proposed directory and package map only as the approved target, not a stale
   inventory of current source locations.

   Done when the target architecture makes every selected flow, ownership boundary,
   error translation, preservation constraint, and test seam explicit and the user has
   approved the design.

5. Turn the approved target into repository guidance. Create or update root `AGENTS.md`.
   Preserve existing applicable instructions; reconcile conflicts with the approved
   target instead of replacing instructions with generic boilerplate. The guidance must
   state the dependency rule, package responsibilities, allowed shared capabilities,
   domain and contract ownership, interface placement, error and logging policy, testing
   expectations, coverage policy, required local and CI checks, and how an exception is
   proposed and recorded.

   Require behavior-focused tests at public seams. Target 100% coverage for changed
   behavior and require at least 95% for the agreed scope, with every intentional
   exclusion named and justified. Coverage never substitutes for assertions of business
   outcomes, failure paths, cancellation, or infrastructure failure modes.

   Done when the repository has concrete, target-specific `AGENTS.md` guidance that a
   new contributor can apply without inferring the architecture.

6. Write `.agents/projects/<project>/rearchitecture-plan.md`. Order migration by
   behavioral safety and dependency direction: characterize critical behavior, establish
   target seams, move one vertical flow at a time, replace obsolete code, then enforce
   the new checks. Each wave names the behavior and preservation constraints, affected
   packages or contracts, test proof, rollback or recovery action, and completion signal.
   Prefer direct replacement over compatibility scaffolding when no consumer or
   persisted data requires compatibility. Do not change runtime behavior or begin
   implementation in this skill.

   End with the ranked findings, their evidence and business impact, the visual report
   location, the target design and guidance locations, the approved migration order, and
   the smallest safe implementation slice. Hand off to `to-spec`, `to-tickets`, and
   `implement` only after the user chooses to proceed.

   Done when the team can execute the approved re-architecture as independently
   verifiable vertical slices without rediscovering the target design.

## Done When

- The current architecture and every critical flow are evidenced with files, symbols,
  and call paths rather than assumed.
- A Canvas or self-contained HTML visual communicates current and target structure.
- `architecture-design.md` records an approved, domain-owned target architecture.
- Root `AGENTS.md` gives target-specific repository guidance.
- The migration plan preserves business behavior, uses testable vertical slices, and
  makes its coverage exceptions explicit.
- No application code or runtime behavior changed during the review.
