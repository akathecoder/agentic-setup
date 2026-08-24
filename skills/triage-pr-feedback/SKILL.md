---
name: triage-pr-feedback
description: Evaluate human and bot feedback on a GitHub pull request, fix valid findings, and reply to and resolve every review thread.
disable-model-invocation: true
argument-hint: "What is the GitHub pull request URL?"
---

# Triage PR Feedback

Given a GitHub pull request URL, evaluate every unresolved human and bot review finding
against the diff, codebase, tests, and originating requirements. Accept and fix valid
feedback; reject incorrect, irrelevant, duplicate, or disproportionate feedback with
evidence. Treat resolved threads as prior decisions and leave them untouched.

Leave all code changes uncommitted and do not push.

Resolve every `.agents/projects/` path from the repository root; never read or write
project artifacts in a global agent-installation directory.

## Process

1. Identify the active project and read its context, links, spec, ticket references,
   and relevant ADRs. Fetch the pull request, its diff, review summaries, inline review
   threads, existing replies, and current thread-resolution state through available
   GitHub tooling.

   Ignore every resolved thread. Done when every unresolved human or bot review finding
   is listed with its author, location or review source, and existing discussion.

2. Evaluate each finding independently. Check whether it identifies a real behavioral,
   correctness, security, maintainability, testing, or specification issue in the
   proposed change. Reject findings that are false positives, irrelevant to the change,
   already addressed, duplicated, or request unjustified scope expansion. Do not accept
   a finding merely because its author is human or automated.

   Done when every finding has an evidence-based accepted or rejected decision.

3. For accepted findings, make the smallest correct fix using `tdd` at the established
   seam where appropriate. Follow the main implementation quality bar: run focused
   tests and typechecking regularly, the full relevant test suite at the end, and the
   repository's coverage tooling for changed code. Target 100% changed-code coverage
   and require at least 95%, unless the user or repository explicitly opts out.
   Invoke `code-review` for the aggregate fixes, address confirmed findings, and rerun
   affected verification before replying to review threads. Do not commit or push any
   change. If a finding cannot be fixed safely without a decision from the user, reject
   it only when it is invalid; otherwise explain the blocker and leave its thread
   unresolved for the user.

   Done when each accepted finding is fixed, meets the main-flow test and coverage bar,
   and passes final code review, or each genuinely blocked valid finding is explicitly
   left for user action.

4. Reply at the finding's native GitHub review surface. For an accepted finding, state
   the concise fix and verification performed. For a rejected finding, state the
   evidence-based reason. End every GitHub reply with the exact line:

   ```text
   Written by Cursor
   ```

   Resolve the thread after posting an accepted or rejected response. A review summary
   without a resolvable inline thread receives a reply on the closest available review
   or pull-request discussion surface; record that no thread-resolution operation was
   available.

   Done when every decided finding has its reply and is resolved where GitHub supports
   resolution.

5. Write `.agents/projects/<project>/pr-feedback.md` with each finding, its decision, evidence,
   fix and verification where applicable, reply URL, and resolution state. Update
   project context and links with the PR URL and remaining blocked feedback. Summarize
   the uncommitted changes and any unresolved blockers to the user.

   Done when project artifacts and the final report account for every review finding
   and the working tree remains uncommitted and unpushed.
