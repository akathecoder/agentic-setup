---
name: to-questionnaire
description: Turn a decision only someone else can answer into a questionnaire for them to fill in.
disable-model-invocation: true
argument-hint: "What decision needs someone else's answer?"
---

# To Questionnaire

Turn something the user cannot answer alone into a **questionnaire**: a Markdown
document they hand to one person to fill in async, or fill out together in a
meeting. The recipient holds knowledge the user lacks; the questionnaire pulls it
out of them.

Grill the send, not the subject. Interview the user only about the send, which
they can always answer: who it goes to, and what they need back. The questions in
the document then target the **gap** between what the recipient knows and what the
user needs.

Resolve every `.agents/projects/` path from the repository root; never read or write
project artifacts in a global agent-installation directory.

## Process

1. Identify the active project. In one exchange, ask the recipient's role,
   expertise, and relationship to the user. That fixes tone and how much context
   the document must carry.

   Done when you know who the recipient is and what they know that the user does
   not.

2. In one exchange, ask the specific decisions or facts the user cannot resolve
   alone and needs from this person.

   Done when there is a concrete list of what the user must walk away able to do
   or decide.

3. Draft questions aimed at that gap, following the structure below. Order
   most-important-first. Group under `##` headings by theme once there are more
   than a handful. Every question is one idea, with an answer stub beneath, and a
   one-line why-this-matters only where the question could be misread. Write
   `.agents/projects/<project>/questionnaire-<slug>.md` and tell the user the path.

   Done when the file exists and every item from step 2 is covered by a question.

## Document

```md
# <Questionnaire title>

**Purpose:** why this questionnaire exists and the decision riding on it.

**From:** <the user>, **To:** <the recipient>, **How your answers will be used:**
<where they go>

## Context

One paragraph orienting a recipient who was not in the user's head.

## How to answer

Deadline and rough effort. Partial answers and "I don't know" are useful: flag
anything unsure rather than skipping it.

## <Theme heading>

### <One question, one idea>

_Why this matters: <only when the question could be misread.>_

>

## Anything else?

Anything we did not ask that we should know?
```

## Done when

- The send (recipient and needed answers) is known.
- `.agents/projects/<project>/questionnaire-<slug>.md` covers every item the user
  named.
- The user has the path.
