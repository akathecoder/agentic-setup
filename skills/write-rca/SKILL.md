---
name: write-rca
description: Writes rigorous RCA documents from incident details and publishes the approved final RCA to one Confluence page. Use when the user wants to create, draft, finalize, or publish a Root Cause Analysis/RCA for an incident, outage, degradation, operational failure, or post-incident review.
---

# Write RCA

Use this skill to interview the user, produce a detailed RCA that follows `RCA-TEMPLATE.md`, and publish the finalized RCA directly to Confluence.

## Hard Rules

- Do not assume missing incident facts. If a detail is not present in user-provided evidence or fetched source material, ask.
- Ask as many relevant questions as needed before finalizing the RCA.
- Use `AskQuestion` for structured choices, confirmations, and ambiguity resolution. Use normal chat for free-form incident details, timeline notes, logs, or narrative answers.
- Always write and maintain the draft RCA in a file. Never paste the full RCA draft into chat. In chat, only summarize what changed and reference the draft file path.
- Do not write to Confluence until the user explicitly approves the finalized RCA draft.
- The final Confluence RCA must be a single page. Never create more than one page. Never create subpages.
- Do not create Jira tickets. Only collect and link existing Jira references.
- Never use em dashes (—) anywhere in the RCA, the draft file, the Confluence page, or any chat output. This is critical and must never be ignored. Use commas, periods, parentheses, or restructured sentences instead. Also avoid en dashes (–) in prose; use a plain hyphen or "to" for ranges.
- Every Atlassian reference must be a clickable link. Whenever a Jira issue key (for example `CRT-1000`), a Confluence page, or any other Atlassian item is mentioned by short form or by a provided link, render it as a hyperlink to that item, not as plain text.

## Draft File

The RCA draft lives in a single file that you create at the start and update on every turn. Do not reproduce the full draft in chat.

1. At the very start of the skill invocation, before gathering any incident facts, use `AskQuestion` to ask where to create the draft file:
   - Option A: in the current working directory where the skill was invoked.
   - Option B: in the system temporary files directory (for example `$TMPDIR` or `/tmp`).
2. Create the draft file as Markdown using the structure from `RCA-TEMPLATE.md`. Name it `rca-draft-[YYYY-MM-DD]-{{short-slug}}.md`. If the date or slug is unknown, use a placeholder and rename once known.
3. After creating the file, tell the user the absolute path of the draft file.
4. On every subsequent turn where new information arrives or a section changes, update the draft file in place. Keep one draft file for the whole session. Do not create additional draft files for revisions.
5. When the user asks to see the draft, point them to the file and summarize the changes rather than dumping the full contents into chat.
6. When publishing to Confluence, the content must be sourced from the current draft file and must follow the same no em dash rule.

## Atlassian Reference Linking

Any time a Jira ticket, Confluence page, or other Atlassian artifact is referenced, in any section including prose, tables, timeline, and the Jira Ref columns, write it as a link.

- Jira issue keys: link `CRT-1000` to `https://coindcx.atlassian.net/browse/CRT-1000`. In Markdown that is `[CRT-1000](https://coindcx.atlassian.net/browse/CRT-1000)`.
- If the user provides a full link, use that exact URL as the link target and keep the short form (or the page title) as the visible text.
- For Confluence pages, link the page title or short reference to the provided page URL.
- Derive the Jira base URL from links the user provides. Default to `https://coindcx.atlassian.net` when the site is not otherwise specified. If you cannot determine the correct URL for a reference, ask the user rather than guessing.
- Preserve these links when publishing to Confluence so they remain clickable on the page.

## Required Template

Read `RCA-TEMPLATE.md` before drafting. The RCA must preserve the template's sections:

1. Created/Reviewed/Approved By
2. Problem Statement and Impact Assessment
3. Timeline
4. RCA using Fault Tree Analysis and 5 Whys
5. Root Cause Description table
6. Detection, diagnosis, and mitigation improvement questions
7. Corrective Action
8. Preventive Action
9. Lessons Learned

## Interview Flow

Start with section-level framing, then drill down one question at a time.

1. First, ask where to create the draft file (current directory or system temp directory) and create it, as described in the Draft File section.
2. Ask for the incident source material: existing RCA page, incident ticket, on-call thread, dashboard/log links, service name, date, and owner.
3. Ask for the publishing target only if absent: existing RCA page URL or approval to create one new page.
4. Gather facts by template section. For each section, ask focused follow-ups until the answer is specific enough to write. Update the draft file as answers come in.
5. Challenge vague or overloaded terms immediately. For example, clarify "impact", "downtime", "users", "failure", "detected", "mitigated", and "resolved".
6. When the user states a technical cause, ask what evidence supports it unless the evidence is already provided.
7. For decision questions, include your recommended answer. For factual incident questions, do not provide a guessed default.

## RCA Reasoning

- Build a timeline with exact timestamps, timezone, actor/team, observation, action, and outcome.
- Separate detection, diagnosis, mitigation, resolution, and prevention. Do not collapse them into one event.
- Use Fault Tree Analysis to enumerate all plausible direct causes and contributing factors.
- Break every meaningful FTA branch down at least two levels when the information is available.
- Apply 5 Whys to each lowest-level contributing factor, not only to the most obvious path.
- Do not stop at "human error", "missed review", "bad config", or "bug". Continue to the process, system, ownership, monitoring, testing, release, or governance gap.
- Label unproven claims as open questions and ask for confirmation before finalizing.
- Ensure every corrective or preventive action maps back to a root cause or contributing factor.

## Confluence Publishing

Use Atlassian MCP tools to read or write Confluence when needed.

- If the user provides an existing RCA page, update only that page after approval.
- If no existing RCA page is provided, create exactly one page in the `OnRampOffR` Confluence space under parent/folder ID `3995009043`.
- New page titles must follow: `RCA [YYYY-MM-DD]: {{SMALL TITLE DESCRIBING THE ISSUE}}`.
- If the incident date or small issue title is missing, ask before creating the page.
- After creating a new page, store and reuse that page ID for every later update. Do not create another page for revisions.
- If the target folder/parent cannot be used, stop and ask the user. Do not create the RCA somewhere else.
- Use a version message that identifies the RCA update, such as `Finalize RCA for <issue title>`.

## Finalization Checklist

Before asking for approval to publish, verify:

- All template sections are present on one page.
- The severity is stated and justified by quantified impact.
- Timeline gaps are either filled or explicitly marked as unknown/open.
- FTA branches and 5 Whys reach systemic causes.
- Corrective actions and preventive actions include owner, ETA, and existing Jira ref when available.
- Lessons learned are concrete and reusable.
- The Confluence title and target page/folder are known.
- The draft file and the finalized content contain no em dashes.
- Every Jira, Confluence, and Atlassian reference is a clickable link.

Ask the user to approve the final draft. Only after explicit approval, publish it to the single target Confluence page.
