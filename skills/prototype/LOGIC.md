# Logic Prototype

A single HTML file that lets anyone drive a state model by clicking buttons. Use
this when the question is business logic, state transitions, or data shape: things
that look reasonable on paper and feel wrong once pushed through real cases.

One file with nothing to install, so a non-developer can feel the model. Labels
speak domain language, not the code's.

## Process

1. State the question in a visible intro at the top of the demo: which state model,
   and what you are checking.

   Done when the question is explicit enough to check later.

2. Isolate the logic in one `<script>` block as a small pure module that could lift
   into the real codebase. The page around it is throwaway; this module is not.
   Pick the shape that fits the question:

   - A pure reducer `(state, action) => state` when actions are discrete events.
   - A state machine when which actions are legal is part of the question.
   - Pure functions over a plain data type when there is no implicit current state.
   - A module with a clear method surface when the logic owns ongoing internal state.

   Keep it pure: no DOM, no `document`, no button handlers inside it. The page calls
   in; nothing flows the other way.

   Done when the answering logic is a liftable module with no page dependency.

3. Build one plain HTML/CSS/JS file: no framework, bundler, or server. Open it by
   double-click. Lay it out top to bottom:

   1. Title and one-line explanation of the question.
   2. Current state as a labelled panel, re-rendered after every click. Call out
      what just changed when that helps a non-developer follow.
   3. Free-play buttons: one per action, always available, any order.
   4. Guided walkthroughs as tabs. Each tab is a **scenario**: a short description
      and the ordered buttons to press. Each step is a real button. Starting a
      walkthrough resets to a known initial state.

   Choose scenarios that are hard to reason about on paper: the happy path, a tricky
   edge, an illegal attempt. Clean typography, generous spacing, one accent colour.

   Done when a stranger can open the file and drive both free-play and every
   scenario.

4. Hand over the file, or open it. If they want new actions or a new scenario, add
   them.

   Done when the user can click through without further setup.

5. Once the question is answered, record the verdict in the active project's
   context and on the tracker ticket when one exists. Lift the validated reducer,
   machine, or function set into the real module. The HTML shell stays a primary
   source off main, committed to a `prototype/<name>` branch only when the user asks.

   Done when the decision lives in real code and the verdict is recorded.

## Rules

- Skip tests. A prototype that needs tests is production work.
- Use in-memory state unless the question is specifically about persistence.
- Answer one question. Leave later support unbuilt.
- Keep the page a thin shell over the pure module.
- One file the recipient double-clicks.
- Ship the logic module, not the HTML shell.
