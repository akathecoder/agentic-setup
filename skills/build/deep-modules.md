# Deep Modules

From "A Philosophy of Software Design":

- Deep module: small interface, substantial implementation hidden behind it.
- Shallow module: large interface, little leverage behind it.

Deep modules are easier to test because callers can verify behavior through a stable public surface.

Ask:

- Can the number of methods be reduced?
- Can parameters be simplified?
- Can invariants move behind the interface?
- Can complex behavior be concentrated instead of leaking across callers?

Do not invent an abstraction just to make a test easy. The interface should improve production design first; testability follows from a good public surface.
