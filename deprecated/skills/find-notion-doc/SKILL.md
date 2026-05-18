---
name: find-notion-doc
description: Find the relevant Notion project page for the current project. Designed to be invoked by other skills that need a Notion page reference. Returns the project's Notion page ID and URL. Caches the result in agent memory for future use.
---

This skill is a utility used by other skills to resolve the correct Notion project page for the current project. It can also be invoked directly by the user.

Use the AskQuestion tool whenever project resolution requires a bounded choice, confirmation, or ambiguity resolution. Use normal chat only when you need free-form text that cannot be represented as fixed options.

## Memory-first lookup

Before querying Notion, check agent memory for an existing entry for this project:

- Look for a reference memory with a key like `notion-project:<project-name>` (e.g. `notion-project:agentic-setup`).
- If found, return the cached Notion project page ID and URL immediately. Skip all steps below.

## Resolution steps (only if not cached)

1. **Check Notion MCP availability.** Look for Notion tools in the available MCP tools. If Notion MCP is not available, inform the caller and stop — do not proceed.

2. **Determine the project name.**
   - Infer it from the current working directory name or git repository name.
   - If a calling skill has passed a project name hint, prefer that.
   - If still ambiguous, request the project name in normal chat because the missing input is free-form text.

3. **Find the root Projects page.**
   - Use Notion MCP to locate the top-level "Projects" page — the root page under which all projects live as subpages.
   - Do NOT search inside any other top-level page.

4. **Find the matching project subpage.**
   - Search the children of the root Projects page for a subpage whose title matches (or closely matches) the resolved project name.
   - If no match is found, show the user the available project names and use AskQuestion to confirm the correct one. Do not guess or pick an unrelated page.

5. **Save to memory.**
   - Once the correct project subpage is confirmed, save a reference memory entry:
     - Key: `notion-project:<project-name>`
     - Value: the Notion page ID and URL of the project subpage
     - Type: `reference`
     - Description: "Notion project page for <project-name>"
   - This allows future skill invocations to skip Notion lookup entirely.

6. **Return the result.**
   - Provide the Notion project page ID and URL to the calling skill or user.
   - If invoked directly by the user (not by another skill), also list the child pages (documents) inside the project subpage as a numbered list with titles and URLs.
