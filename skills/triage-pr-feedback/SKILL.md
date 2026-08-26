---
name: triage-pr-feedback
description: Evaluate human and Copilot feedback on a GitHub pull request, fix validated findings, and reply to and resolve every review thread.
disable-model-invocation: true
argument-hint: "What is the GitHub pull request URL?"
---

# Triage PR Feedback

Given a GitHub pull request URL, evaluate every unresolved human or Copilot review finding
against the diff, codebase, tests, and originating requirements. Independently establish
whether the suggested issue is real before acting on it. Classify each finding as important,
maybe, or rejected; fix only important and maybe findings. Treat resolved threads as prior
decisions and leave them untouched.

Leave all code changes uncommitted and do not push.

Resolve every `.agents/projects/` path from the repository root; never read or write
project artifacts in a global agent-installation directory.

## Process

1. Identify the active project and read its context, links, spec, ticket references,
   and relevant ADRs. Fetch the pull request, its diff, review summaries, inline review
   threads, existing replies, and current thread-resolution state through available
   GitHub tooling. Include only findings authored by a human reviewer or GitHub Copilot.
   Exclude GitHub Actions, check runs, workflow output, and automated reports, including
   Sonar, Snyk, and OX.

   Ignore every resolved thread. Done when every unresolved eligible review finding is
   listed with its author, location or review source, and existing discussion; no GitHub
   Actions or automated report finding is included.

2. Evaluate each finding independently. Reproduce or trace its claimed behavior through
   the diff, affected code, tests, and originating requirements; use the smallest focused
   check that can confirm or disprove it. Do not rely on the review author's confidence,
   status, or reasoning as proof. Classify the result as:

   - **Important**: a confirmed correctness, security, data-loss, or material behavioral
     issue that requires a change before merge.
   - **Maybe**: a supported maintainability, testing, or lower-risk issue where the
     proposed change is proportionate and safe to make now.
   - **Rejected**: a false positive, irrelevant, already-addressed, duplicate, unsupported,
     or disproportionate finding.

   Done when every finding has an evidence-based classification, including the specific
   code, test, requirement, or focused check that supports it.

3. For important and maybe findings only, make the smallest correct fix using `tdd` at
   the established seam where appropriate. Make no code change for rejected findings.
   Follow the main implementation quality bar: run focused tests and typechecking
   regularly, the full relevant test suite at the end, and the repository's coverage
   tooling for changed code. Target 100% changed-code coverage and require at least 95%,
   unless the user or repository explicitly opts out. Invoke `code-review` for the
   aggregate fixes, address confirmed findings, and rerun affected verification before
   replying to review threads. Do not commit or push any change. If an important or maybe
   finding cannot be fixed safely without a decision from the user, explain the blocker
   and leave its thread unresolved for the user.

   Done when each important or maybe finding is fixed, meets the main-flow test and
   coverage bar, and passes final code review; each rejected finding has no code change;
   and each genuinely blocked important or maybe finding is explicitly left for user action.

4. Reply at the finding's native GitHub review surface. State its classification. For an
   important or maybe finding, state the concise fix and verification performed. For a
   rejected finding, state the evidence-based reason and that no code change was made.
   End every GitHub reply with the exact line:

   ```text
   Written by Cursor
   ```

   Resolve the thread after posting an important, maybe, or rejected response. A review
   summary without a resolvable inline thread receives a reply on the closest available
   review or pull-request discussion surface; record that no thread-resolution operation
   was available.

   Done when every decided finding has its reply and is resolved where GitHub supports
   resolution.

5. Write `.agents/projects/<project>/pr-feedback.md` with each finding, its eligible
   review source, classification, evidence, fix and verification where applicable, reply
   URL, and resolution state. Update project context and links with the PR URL and
   remaining blocked feedback. Summarize the uncommitted changes and any unresolved
   blockers to the user.

   Done when project artifacts and the final report account for every review finding
   and the working tree remains uncommitted and unpushed.
