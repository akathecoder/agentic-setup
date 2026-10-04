---
name: triage-pr-feedback
description: Table PR review findings for approval, then implement, verify, commit and push approved fixes, and respond to review threads.
disable-model-invocation: true
argument-hint: "What is the GitHub pull request URL?"
---

# Triage PR Feedback

Given a GitHub pull request URL, evaluate every unresolved human or Copilot review finding
against the diff, codebase, tests, and originating requirements. Independently establish
whether the suggested issue is real before acting on it. Classify each finding as important,
maybe, or rejected. Present a table for each review before implementing any fix;
fix only explicitly approved important and maybe findings. Treat resolved threads as
prior decisions and leave them untouched.

Explicit approval of the proposed fixes also authorizes committing and pushing those
fixes to the pull request's source branch after verification, without another approval.

Resolve every `.agents/projects/` path from the opened workspace root, including
when the active repository is nested inside it. In a single-repository workspace,
that is the repository root. Keep this artifact root fixed when changing directories;
never use nested repositories or global agent-installation directories for artifacts.

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

3. Show one table per eligible review, identified by author and review link. Give each
   finding a stable ID and a row covering the original feedback, your finding and
   supporting evidence, classification, and suggested fix. Include rejected findings
   with their reason and no proposed code change. Save these tables in
   `.agents/projects/<project>/pr-feedback.md`.

   | ID | Review feedback | Finding and evidence | Classification | Suggested fix |
   | --- | --- | --- | --- | --- |

   Ask the user to approve the listed fixes or name the IDs to implement. Do not change
   code, commit, or push until explicit approval arrives; invoking this skill alone is
   not fix approval. If the user approves a subset, act only on that subset and leave
   other valid findings pending. New findings or materially different fixes require an
   updated table and explicit approval before implementation.
   If no fix is proposed, proceed to step 6 after showing the tables.

   Done when every eligible finding is tabled and either no fix is proposed or the user
   explicitly approves or declines the fixes, with the approved IDs recorded.

4. For approved important and maybe findings only, make the smallest correct fix using
   `tdd` at the established seam where appropriate. Make no code change for rejected findings.
   Follow the main implementation quality bar: run focused tests and typechecking
   regularly, the full relevant test suite at the end, and the repository's coverage
   tooling for changed code. Target 100% changed-code coverage and require at least 95%,
   unless the user or repository explicitly opts out. Invoke `code-review` for the
   aggregate fixes and rerun affected verification. If final review discovers an issue
   outside the approved fixes, add it to the table for approval before changing code.
   If an approved finding cannot be fixed safely without a further user decision,
   explain the blocker and leave its thread unresolved.

   Done when each approved finding is fixed, meets the main-flow test and
   coverage bar, and passes final code review; each rejected finding has no code change;
   and each blocked or unapproved valid finding is explicitly left for user action.

5. Inspect the final diff and stage only the approved fixes and their tests, preserving
   unrelated working-tree changes. Commit and push directly to the pull request's
   confirmed source branch using a normal push; no further approval is needed. If there
   are no code changes, skip commit and push. If verification, commit, or push fails,
   report the failure and keep affected threads unresolved until the fixes are published.
   Whenever an approved fix completes a Jira checklist task, invoke `update-ticket`
   to mark its item in the main ticket complete after the task's required verification;
   this completion mark needs no further approval.

   Done when every completed approved fix is committed and confirmed on the remote
   PR branch, or its publication blocker is recorded; completed Jira tasks have their
   items checked or exact pending tracker updates recorded.

6. Reply at the finding's native GitHub review surface. State its classification. For an
   approved and published fix, state the concise change, commit, and verification. For a
   rejected finding, state the evidence-based reason and that no code change was made.
   End every GitHub reply with the exact line:

   ```text
   Written by AI Agent
   ```

   Resolve a fixed finding only after its verified fix has been pushed and its reply
   posted; resolve a rejected finding after posting its evidence-based response. Leave
   unapproved or blocked valid findings unresolved. A review
   summary without a resolvable inline thread receives a reply on the closest available
   review or pull-request discussion surface; record that no thread-resolution operation
   was available.

   Done when every published fix or rejected finding has its reply and is resolved
   where supported, and pending valid findings remain unresolved.

7. Update `.agents/projects/<project>/pr-feedback.md` with each finding, its eligible
   review source, classification, evidence, approval decision, fix and verification
   where applicable, commit and push result, reply URL, and resolution state. Update
   project context and links with the PR URL and remaining feedback. Report the pushed
   commits, verification, unapproved findings, and unresolved blockers to the user.

   Done when project artifacts and the final report account for every eligible finding,
   approval decision, publication result, and remaining blocker.

## Done when

- Every eligible review has a table of findings, evidence, and suggested fixes.
- Every implemented fix has explicit user approval; unapproved fixes remain pending.
- Approved fixes pass required verification and are committed and pushed to the PR
  source branch, or publication blockers are reported with affected threads unresolved.
- Published fixes and rejected findings have replies and resolved threads where supported.
- Project artifacts record approvals, commits, verification, and remaining feedback;
  completed Jira tasks have their main-ticket checklist items checked or exact pending
  updates and tracker-access limitations recorded.
