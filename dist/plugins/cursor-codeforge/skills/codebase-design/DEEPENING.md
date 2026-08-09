# Deepening

Use this reference when assessing how a cluster of shallow modules can become one deep
module safely.

## Dependency Categories

- **In-process**: pure computation or in-memory state. Merge the modules and test the
  deepened module through its interface.
- **Local-substitutable**: a dependency with a local stand-in, such as PGLite or an
  in-memory filesystem. Test with the stand-in; keep the seam internal.
- **Remote but owned**: an internal network service. Define a port at the seam, inject
  a production transport adapter, and test through an in-memory adapter.
- **True external**: a third-party service. Inject it as a port and test through a
  mock adapter.

## Seam Discipline

- One adapter is a hypothetical seam; two adapters make it real.
- Internal seams support a module's implementation and tests. Do not expose them in
  the external interface merely because tests use them.

## Testing

Replace old shallow-module tests with behavior tests at the deep module's interface.
The interface is the test surface; assertions observe outcomes rather than internals.
