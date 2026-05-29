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
- Do not write to Confluence until the user explicitly approves the finalized RCA draft.
- The final Confluence RCA must be a single page. Never create more than one page. Never create subpages.
- Do not create Jira tickets. Only collect and link existing Jira references.

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

1. Ask for the incident source material: existing RCA page, incident ticket, on-call thread, dashboard/log links, service name, date, and owner.
2. Ask for the publishing target only if absent: existing RCA page URL or approval to create one new page.
3. Gather facts by template section. For each section, ask focused follow-ups until the answer is specific enough to write.
4. Challenge vague or overloaded terms immediately. For example, clarify "impact", "downtime", "users", "failure", "detected", "mitigated", and "resolved".
5. When the user states a technical cause, ask what evidence supports it unless the evidence is already provided.
6. For decision questions, include your recommended answer. For factual incident questions, do not provide a guessed default.

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

Ask the user to approve the final draft. Only after explicit approval, publish it to the single target Confluence page.
