---
name: review-pr
description: Thoroughly review a GitHub pull request for correctness, security, design, testing, performance, and readability. Use when the user asks to review a PR, gives a PR link/number and asks for feedback, or mentions "review PR".
---

# Review PR

Fetch a GitHub PR using the `fetch-gh-pr` skill, then perform a thorough code review. Present findings locally — do not post to GitHub unless the user explicitly asks.

## Workflow

### Step 1: Fetch PR Data

Read and execute the `fetch-gh-pr` skill at `skills/fetch-gh-pr/SKILL.md` (resolve relative to this skill's location). Follow its full workflow to fetch metadata, comments, checks, and diff.

After the fetch completes, you have structured PR data to work with. Continue below.

### Step 2: Large PR Handling

If the PR exceeded the 1500-line diff threshold (file summary only, no full diff), fetch diffs selectively:

**Fetch priority** (highest first):
1. Source files with the most changes (additions + deletions)
2. Files in security-sensitive paths (auth, crypto, permissions, middleware)
3. Database migrations / schema changes
4. API route handlers / endpoint definitions
5. Test files

**Skip by default:**
- Lockfiles (`package-lock.json`, `yarn.lock`, `go.sum`, etc.)
- Generated files (`.generated.`, `__generated__`, auto-gen markers)
- Pure config/formatting (`.prettierrc`, `.eslintrc`, `.editorconfig`)

**Budget**: Fetch files until cumulative diff reaches ~1500 lines, then stop. Use `gh api repos/{owner}/{repo}/pulls/{number}/files` and fetch individual file patches. List skipped files at the end of the review under "Files Not Reviewed."

### Step 3: PR Hygiene Assessment

Before diving into code, briefly assess:

- **Description quality**: Does it explain _why_, not just _what_? Is there a test plan?
- **Linked issues**: Are they present and relevant?
- **Scope**: Is this PR focused, or does it mix unrelated changes?
- **Commit structure**: Are commits logical and well-messaged?

Keep this to 2–4 sentences. Flag problems, don't lecture.

### Step 4: Gather Codebase Context

**If the repo is available locally** (bare PR number was used, or you can identify the local checkout):

- Read files surrounding the changed code — callers, imports, sibling modules, existing tests.
- Understand the conventions and patterns already established in the codebase.
- Use this context to evaluate whether the PR is consistent with the rest of the project.

**If the repo is not local** (cross-repo URL, no checkout available):

- Review based on the diff alone.
- Note in the summary: "Review based on diff only — no local codebase context available."

### Step 5: File-by-File Review

Review each file's diff against all dimensions below. Think carefully about each one — don't just scan for surface issues.

**Review dimensions** (ordered by severity weight):

| Priority | Dimension | What to look for |
|----------|-----------|-----------------|
| Critical | **Correctness** | Logic bugs, off-by-ones, race conditions, null derefs, missing edge cases, broken error handling |
| Critical | **Security** | Injection, auth bypass, secrets in code, unsafe deserialization, SSRF, path traversal |
| Suggestion | **Design** | Coupling, cohesion, abstraction quality, naming, responsibility allocation, deep vs shallow modules |
| Suggestion | **Testing** | Are changes tested? Are tests meaningful (behavior, not implementation)? Missing coverage for critical paths? |
| Suggestion | **Performance** | N+1 queries, unnecessary allocations, algorithmic complexity, missing pagination, unbounded loops |
| Nitpick | **Readability** | Unnecessary complexity, misleading names, dead code, overly clever constructs |
| Nitpick | **Consistency** | Does the change match surrounding codebase style and patterns? |

### Step 6: Acknowledge Existing Review Comments

Read through the human comments and inline review comments fetched in Step 1.

- Do not duplicate points already raised by other reviewers.
- If an existing comment is unresolved and you have additional insight, add to it rather than restating it.
- If you agree with an existing comment, you may briefly note agreement but don't belabor it.

### Step 7: Synthesize and Present

Produce the review using the output format below.

## Severity Tiers

Every finding gets exactly one tier:

- **Critical**: Likely bug, security vulnerability, data loss risk, or correctness issue. Must address before merge.
- **Suggestion**: Design improvement, missing test, performance concern, or meaningful quality issue. Should address.
- **Nitpick**: Style, naming, minor readability. Optional.

## Output Format

```
## Review: PR #<number> — <title>

### Verdict: <Approve | Request Changes | Comment Only>

<1–3 sentence overall assessment. What's the most important thing about this PR?>

### PR Hygiene

<2–4 sentences on description, linked issues, scope, commits>

### Findings

#### `<filename>`

- **[Critical]** <finding>
- **[Suggestion]** <finding>
- **[Nitpick]** <finding>

#### `<filename>`

- **[Suggestion]** <finding>

...

### Files Not Reviewed

<list of files skipped due to budget or being lockfiles/generated — omit section if all files were reviewed>

### Summary

<Critical: N, Suggestions: N, Nitpicks: N>
```

**Verdict logic:**
- Any **Critical** finding → **Request Changes**
- No Critical findings, but Suggestions exist → **Comment Only**
- Only Nitpicks or no findings → **Approve**

## Guardrails

- Write findings addressed to the user (the reviewer), not to the PR author. Use third person: "The author should…" not "You should…"
- Be specific. Reference line numbers, variable names, and concrete scenarios — not vague "this could be improved."
- Don't pad the review. If a file has no issues, don't mention it. If the PR is clean, say so and approve.
- Don't suggest changes that are purely stylistic preferences unless they conflict with established codebase patterns.
- Don't re-raise points already made in existing review comments.
- Present the review and stop. Do not offer to post it or suggest next actions.
