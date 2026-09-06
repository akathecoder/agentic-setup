# UI Prototype

Several structurally different UI variations on one route, switchable from a
floating bottom bar. The user flips between them, picks one or steals bits, then
throws the rest away.

If the question is about logic or state rather than what something looks like, this
is the wrong branch. Read `LOGIC.md`.

## Sub-shapes

Default to **A**. Reach for **B** only when the thing being prototyped has no
existing page to live inside.

### A: adjustment to an existing page

The route already exists. Variants render on that route, gated by a `?variant=`
search param. Existing data fetching, params, and auth stay; only rendering swaps.
If the prototype would naturally live inside a page (a new dashboard section, a
settings card, a step in an existing flow), it is still A: mount the variants
inside the host page.

### B: a new page

Only when there is no existing page to embed in (a new top-level surface, or a flow
that cannot sit anywhere sensible). Create a throwaway route using the project's
routing convention, with `prototype` in the path or filename. Same `?variant=`
pattern.

## Process

1. State the question and pick N. Default to 3 variants; cap at 5. Write one line
   at the prototype's location or in a top-of-file comment:

   > Three variants of the settings page, switchable via `?variant=`, on the
   > existing `/settings` route.

   Done when N, the host route, and the question are written down.

2. Draft each variant against the page's purpose, its data, and the project's
   component library. Export a clear name (`VariantA`, `VariantB`, …). Variants
   must disagree about structure: layout, information hierarchy, or primary
   affordance. If two drafts come out similar, redo one under an explicit
   constraint that forbids the shared structure.

   Done when every variant is structurally distinct and uses real page data.

3. Wire them through a single switcher on the route. Read `variant` from the
   search param, default `A`, render that variant, then the switcher. For A, keep
   existing data fetching above the switcher. For B, mount the same switcher on
   the throwaway route.

   Done when `?variant=` selects each draft and the URL is shareable.

4. Build a small fixed bar at the bottom-centre:

   - Left arrow cycles backward (wraps).
   - Label shows the current key and exported name, e.g. `B (Sidebar layout)`.
   - Right arrow cycles forward (wraps).

   Arrow clicks update the search param through the framework's router so the
   variant survives reload. `←` / `→` also cycle, except when an input, textarea,
   or contenteditable is focused. Style the bar so it is obviously not part of the
   design. Hide it in production builds (`NODE_ENV !== 'production'` or equivalent).
   Put the switcher in one shared component.

   Done when keyboard and clicks cycle variants, the URL updates, and the bar
   cannot ship.

5. Hand over the URL and the `?variant=` keys.

   Done when the user can flip variants in the browser.

6. Once a variant has won, record which one and why in the active project's
   context and on the tracker ticket when one exists. Fold the winner into real
   code (A: the existing page; B: a real route) and drop losing variants and the
   switcher from main. The full set stays a primary source off main, committed to
   a `prototype/<name>` branch only when the user asks.

   Done when the winner is folded in, the verdict is recorded, and main no longer
   carries the throwaway variants.

## Rules

- Variants differ in structure, not only colour or copy.
- Share small pieces such as a header; each variant owns its layout.
- Point mutations at a stub. The question is how it should look.
- Rewrite the winner under production constraints when folding it in.
