---
name: publish-confluence
description: Use when an agent needs to publish one or more local documentation files to Atlassian Confluence through a bounded publishing subagent using Atlassian MCP, with preview-before-write approval, page/folder target resolution, and one Confluence page per source file.
---

# Publish Confluence

Use this internal skill when an agent needs to publish local documentation to Confluence. It is not intended for direct user invocation.

## Hard Rules

- The invoking agent owns high-level reasoning, local file review, user interaction, approval previews, and final reporting.
- Use a Composer 2.5 subagent for Atlassian MCP interactions. The main agent should not perform Atlassian MCP reads or writes directly unless the user explicitly overrides this.
- The subagent must read the relevant MCP tool descriptors before calling Atlassian MCP tools.
- Do not write to Confluence until the user explicitly approves a publish preview.
- Publish each local source file to exactly one Confluence page. Never split one source file into multiple Confluence pages because it is large.
- If a local file is 5000 lines, publish it as one Confluence page containing those 5000 lines.
- Support one or more explicit local source files. Do not recursively publish directories unless the user explicitly asks for directory publishing.
- Default to `contentFormat: markdown`. Use `html` only when explicitly needed for richer Confluence formatting or round-trip fidelity.

## Workflow

1. Collect explicit local source file paths and the Confluence target ID or URL from the invoking context. If either is missing, ask the user.
2. Read the local files yourself and summarize what will be published. Do not paste huge file bodies into chat.
3. Resolve the Confluence target through a Composer 2.5 subagent in read-only mode:
   - Read MCP descriptors for any Atlassian tools it will call.
   - Prefer hostname or site URL as `cloudId` when provided.
   - Use `getAccessibleAtlassianResources` only when `cloudId` is unclear or a direct call fails.
   - Use `getConfluencePage` when the ID might be an existing page.
   - Use `getConfluencePageDescendants` only when children are needed to understand a parent/container target.
4. Decide the intended operation from context:
   - Update the existing page when the target resolves as a page and the user asked to update it.
   - Create exactly one new page under the target when the target is a parent, folder, or container and the user asked to publish under it.
   - If the target role is ambiguous, stop and ask before previewing any write.
5. Build a publish preview and ask for explicit approval.
6. After approval, launch a Composer 2.5 publishing subagent with the exact approved operation list.
7. Publish sequentially. Stop on the first failure and report completed, failed, and pending files.

## Approval Preview

Before any write-capable Confluence MCP call, show:

- Local source file path for each publish operation.
- Operation: update existing page or create one new page.
- Target page ID, title, space, parent ID, or container ID where known.
- Selected `contentFormat`.
- Confirmation that each source file remains one Confluence page.
- Body summary for creates, or section-level diff/summary for updates.
- Version message for updates.
- Open questions or explicit unknowns.

Use `AskQuestion` when available:

- Publish to Confluence
- Revise the preview
- Cancel

Only the publish option authorizes writes.

## Publishing Subagent

Use a focused subagent with model `composer-2.5` for approved Atlassian work. Its prompt must include:

- The exact approved operations.
- The local source file paths and target IDs.
- The selected `contentFormat`.
- A prohibition on splitting any source file into multiple pages.
- A prohibition on changing target, title, body, scope, or operation type.
- A requirement to read MCP tool descriptors before MCP calls.
- A requirement to perform only the approved `createConfluencePage` or `updateConfluencePage` calls.
- A requirement to return page IDs, URLs if available, version messages, completed operations, and errors.

The subagent must not ask the user questions, invent missing target data, publish unapproved content, continue after a failure, or perform unrelated Jira/Confluence actions.

## Completion Report

Report:

- Pages created or updated.
- Source file mapped to each page.
- Content format used.
- Version message, when applicable.
- Failure details from MCP, if any.
- Files left unpublished because publishing stopped on a failure.
