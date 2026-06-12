# Confluence Publish Skill Plan

## Goal

Design a new active skill that publishes local documentation to Atlassian Confluence using Atlassian MCP, with strict approval before any Confluence write.

## Skill Name

The active skill name is `publish-confluence`.

## Skill Trigger

`Use when an agent needs to publish one or more local documentation files to Atlassian Confluence through a bounded publishing subagent using Atlassian MCP, with preview-before-write approval, page/folder target resolution, and one Confluence page per source file.`

## Current Intent

The skill is internal and not intended for direct user invocation. It should be invoked by an agent when that agent needs to publish local documentation to Confluence.

The invoking agent should handle high-level reasoning, user interaction, target decisions, previews, and final reporting. Atlassian MCP interactions should be delegated to a smaller, less expensive Composer 2.5 subagent whenever possible.

After approval, the Composer 2.5 publishing subagent may read MCP schemas, fetch current Confluence state, perform only the approved create or update operations, and return URLs, results, and errors. It must not change scope, ask user questions, split documents, choose targets, or write unapproved content.

The user provides a Confluence target ID. The ID may refer to an existing page to update or to a folder/container/parent location where a new page should be created. The skill must resolve the target based on context rather than blindly treating every ID as the same kind of target.

The skill should support one or more explicit local source files. Each local source file maps to exactly one Confluence page and must never be split into multiple pages because of length. Directory publishing is out of scope unless the user explicitly asks for it later.

Target resolution should be contextual:

- If the ID resolves as an existing page and the user asked to update, update that page.
- If the ID is a folder/container/parent and the user asked to publish under it, create exactly one new page under that target.
- If the target role is ambiguous, stop and ask before writing.

## Known Hard Rules

- Use Atlassian MCP for Confluence publication.
- Read MCP tool descriptors before Atlassian MCP calls.
- Do not write to Confluence until the user approves a preview.
- Keep one local source file as one Confluence page, regardless of length.
- Never split a single local source file into multiple Confluence pages because it is large.
- If a local document is 5000 lines, publish it as one Confluence page containing those 5000 lines.
- The invoking agent owns high-level thinking and user-facing decisions.
- A Composer 2.5 subagent should perform the actual approved Atlassian MCP interactions.

## Relevant MCP Surface

- `getConfluencePage` requires `cloudId` and `pageId`; it can read `html`, `markdown`, or `adf`.
- `updateConfluencePage` requires `cloudId`, `pageId`, and `body`; it can also set `title`, `status`, `spaceId`, `parentId`, `contentFormat`, `versionMessage`, and `includeBody`.
- `createConfluencePage` requires `cloudId`, `spaceId`, and `body`; it can also set `title`, `status`, `parentId`, `contentFormat`, `isPrivate`, and `subtype`.
- `getConfluencePageDescendants` can inspect children of a page-like target.
- `getAccessibleAtlassianResources` can resolve accessible Atlassian resources when a hostname or `cloudId` is unclear.

## Content Format

Default to `contentFormat: markdown` for Markdown-heavy local documentation. Use `contentFormat: html` only when the user explicitly needs richer Confluence formatting or round-trip fidelity.

## Approval Preview

Before any write-capable Confluence MCP call, show a preview that includes:

- Each local source file.
- Target operation: update existing page or create one new page.
- Target page ID, title, space, and parent/container where known.
- Selected content format.
- Confirmation that each source file remains one Confluence page.
- Body summary or diff, depending on whether this is a create or update.
- Version message for updates.
- Unresolved questions or explicit unknowns.

Only explicit publish approval authorizes the publishing subagent to write.

## Failure Handling

When multiple files are approved, publish sequentially and stop on the first failure. Report completed pages, the failed operation, the MCP error, and remaining unpublished files. Continue only if the user explicitly asks.

## Proposed Skill File

Implement `publish-confluence` as a single file:

- `skills/publish-confluence/SKILL.md`

The file should stay concise while covering workflow, target resolution, approval preview, publishing, subagents, and guardrails.

README should list `publish-confluence` as an internal skill, not a generic user-invoked skill.

## Decisions Needed

No known design decisions remain open.
