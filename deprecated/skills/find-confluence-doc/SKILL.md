---
name: find-confluence-doc
description: Find the relevant Confluence project page for the current project in the user's personal space. Designed to be invoked by other skills that need a Confluence page reference. Returns the project's Confluence page ID, space key, and URL. Caches the result in agent memory for future use.
---

This skill is a utility used by other skills to resolve the correct Confluence project page for the current project. It can also be invoked directly by the user.

Use the AskQuestion tool whenever project resolution requires a bounded choice, confirmation, or ambiguity resolution. Use normal chat only when you need free-form text that cannot be represented as fixed options.

## Memory-first lookup

Before querying Confluence, check agent memory for an existing entry for this project:

- Look for a reference memory with a key like `confluence-project:<project-name>` (e.g. `confluence-project:agentic-setup`).
- If found, return the cached Confluence page ID, space key, and URL immediately. Skip all steps below.

## Resolution steps (only if not cached)

1. **Check Atlassian MCP availability.** Look for Atlassian/Confluence tools in the available MCP tools (e.g. `searchConfluenceUsingCql`, `getConfluencePage`). If the Atlassian MCP is not available or needs authentication, inform the caller and stop — do not proceed.

2. **Determine the project name.**
   - Infer it from the current working directory name or git repository name.
   - If a calling skill has passed a project name hint, prefer that.
   - If still ambiguous, request the project name in normal chat because the missing input is free-form text.

3. **Get the cloud ID.**
   - Use `getAccessibleAtlassianResources` to retrieve the available Atlassian cloud instances.
   - If multiple cloud instances exist, use AskQuestion to let the user choose which one to use. If only one, use it.

4. **Find the user's personal space.**
   - Use `searchConfluenceUsingCql` with CQL like `type = "personal"` or search for the user's personal space.
   - Alternatively, use `getConfluenceSpaces` or equivalent to list spaces and identify the personal space (personal spaces typically have a key prefixed with `~`).
   - Always use the personal space. Do NOT use team/squad spaces unless a different skill instructs otherwise.

5. **Find the Projects folder.**
   - Search the children of the personal space root for a page titled "Projects" (or a closely matching name).
   - This is the top-level folder under which all project subpages live.
   - If no "Projects" page is found, list the top-level pages in the personal space and use AskQuestion to let the user choose which page serves as the projects root.

6. **Find the matching project subpage.**
   - Search the children of the Projects folder for a subpage whose title matches (or closely matches) the resolved project name.
   - If no match is found, show the user the available project names and use AskQuestion to confirm the correct one. Do not guess or pick an unrelated page.

7. **Save to memory.**
   - Once the correct project subpage is confirmed, save a reference memory entry:
     - Key: `confluence-project:<project-name>`
     - Value: the Confluence page ID, space key, cloud ID, and URL of the project subpage
     - Type: `reference`
     - Description: "Confluence project page for <project-name>"
   - This allows future skill invocations to skip Confluence lookup entirely.

8. **Return the result.**
   - Provide the Confluence page ID, space key, cloud ID, and URL to the calling skill or user.
   - If invoked directly by the user (not by another skill), also list the child pages (documents) inside the project subpage as a numbered list with titles and URLs.
