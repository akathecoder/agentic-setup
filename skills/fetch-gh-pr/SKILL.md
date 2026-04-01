---
name: fetch-gh-pr
description: Fetch GitHub pull request details using the GH CLI and present them as structured context. Use when the user provides a GitHub PR link, PR number, or asks to look at / fetch / pull up a pull request.
---

# Fetch GitHub PR

Fetch comprehensive PR data and present it as structured markdown. This is a pure data-fetch skill — present the information and stop.

## Input Parsing

Accept two input forms:

1. **Full URL**: `https://github.com/owner/repo/pull/123` — extract owner, repo, and number from the URL.
2. **Bare number**: `#123` or `123` — use `gh pr view <number>` which infers the repo from the current directory's git remote.

If a bare number is given and the current directory has no git remote, request the full URL in normal chat. This is free-form input, so do not force it through AskQuestion.

## Fetch Workflow

### Step 1: Metadata + Comments

Run a single `gh pr view` to get all structured data:

```bash
gh pr view <number> --json number,title,body,state,isDraft,author,labels,baseRefName,headRefName,additions,deletions,changedFiles,reviewDecision,closingIssuesReferences,reviews,comments,url,createdAt,updatedAt,mergedAt,mergedBy,files,reviewRequests,assignees,milestone
```

For cross-repo PRs (full URL provided), use `-R owner/repo` flag.

### Step 2: Inline Review Comments

Fetch code-level review comments separately:

```bash
gh api repos/{owner}/{repo}/pulls/{number}/comments
```

### Step 3: CI / Check Status

```bash
gh pr checks <number>
```

Or with repo flag: `gh pr checks <number> -R owner/repo`

### Step 4: Conditional Diff

Calculate total changed lines from Step 1: `additions + deletions`.

- **If total <= 1500 lines**: fetch and include the full diff via `gh pr diff <number>`.
- **If total > 1500 lines**: show only the file-level summary from `files` (already fetched in Step 1). Tell the user they can ask for diffs of specific files.

## Bot Comment Separation

Separate bot-authored comments and reviews from human ones.

**Identification heuristics** (apply in order):
1. Author login ends with `[bot]` (e.g., `codecov[bot]`, `github-actions[bot]`)
2. Author `type` field is `"Bot"` (available in API responses)

Present bot content in its own section so human discussion is easy to scan.

## Output Format

Present fetched data using these sections. Omit any section that has no content.

```
## PR #<number>: <title>

**State**: <state> | **Author**: <author> | **Created**: <date>
**Base**: <base> ← **Head**: <head>
**Labels**: <labels> | **Reviewers**: <reviewers>
**Review Decision**: <approved/changes_requested/etc>
**Linked Issues**: <issues>

### Description

<PR body>

### Files Changed (<N> files, +<additions> -<deletions>)

<file list with per-file additions/deletions>

### Diff

<full diff if under threshold, or "Large PR — ask for specific file diffs">

### CI / Checks

<check name — status — details URL>

### Human Comments & Reviews

<human review comments and PR-level comments, chronologically>

### Bot Comments & Reviews

<bot review comments and PR-level comments, grouped by bot>
```

## Guardrails

- Do not summarize or editorialize. Present the data as-is.
- Do not suggest next actions. The user will decide.
- If `gh` is not authenticated or fails, surface the error clearly and suggest `gh auth login`.
