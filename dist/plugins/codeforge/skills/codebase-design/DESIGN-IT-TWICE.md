# Design It Twice

Read this reference when the user wants to compare alternative interfaces for a chosen
deepening candidate.

1. Explain the problem space: constraints, dependency categories from `DEEPENING.md`,
   and a small illustrative sketch that grounds constraints without proposing a design.

   Done when the user can evaluate the constraints while designs are explored.

2. Launch at least three parallel design explorations with distinct constraints:
   minimize the interface, maximize flexibility, and optimize the common caller. Add a
   ports-and-adapters alternative when cross-seam dependencies apply. Each exploration
   describes the interface, caller example, hidden implementation, dependency strategy,
   and trade-offs in leverage and locality.

   Done when the alternatives are materially different rather than small variations.

3. Present designs sequentially, compare their depth, locality, and seam placement,
   then recommend the strongest design or a deliberate hybrid.

   Done when the user has a clear, opinionated recommendation.
