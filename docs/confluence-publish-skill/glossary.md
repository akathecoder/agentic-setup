# Confluence Publish Skill Glossary

## Language

**Publish Confluence Skill**:
A planned internal skill invoked by agents to publish local documentation files to Atlassian Confluence with preview-before-write approval.
_Avoid_: Confluence sync skill, doc splitter

**Local Source File**:
A single local documentation file selected by the user for publication.
_Avoid_: Source chunk, part, shard

**Target Page**:
The Confluence page that will receive the full content of one **Local Source Document**.
_Avoid_: Destination doc

**Target Container**:
A Confluence page, parent page, folder, or other Confluence location provided by ID that can contain a new page.
_Avoid_: Page ID when it may be a folder ID

**Publishing Subagent**:
A bounded subagent, preferably using Composer 2.5, responsible for schema-checked Atlassian MCP calls after the main agent has gathered context and received approval.
_Avoid_: Main writer, autonomous publisher

**Invoking Agent**:
The agent that calls the **Publish Confluence Skill**, owns high-level reasoning, and handles user-facing decisions.
_Avoid_: Direct user, publishing subagent

## Relationships

- One **Local Source File** maps to one **Target Page**.
- A **Local Source File** must not be split into multiple Confluence pages because of length.
- The **Invoking Agent** performs high-level thinking, target reasoning, preview design, and user approval.
- The **Publishing Subagent** performs the approved Atlassian MCP read/write operations and reports results back to the main agent.

## Flagged Ambiguities

- The user said "attestation MCP"; resolved as Atlassian MCP because the request is about Confluence and the available plugin is Atlassian.
- "Page ID or folder ID" needs a target-resolution rule because `createConfluencePage` expects `spaceId` and optionally `parentId`, while updates use an existing `pageId`.
