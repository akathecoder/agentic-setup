---
name: teach
description: Teach a skill or concept over multiple sessions in a project teaching workspace.
disable-model-invocation: true
argument-hint: "What would you like to learn about?"
---

# Teach

Teach the user something they intend to learn over multiple sessions. The active
**project** is the teaching workspace.

Resolve every `.agents/projects/` path from the repository root; never read or write
project artifacts in a global agent-installation directory.

## Workspace

All teaching state lives under `.agents/projects/<project>/`:

- `CONTEXT.md`: what this teaching project is, enough to re-orient next session
- `MISSION.md`: the reason they are learning. When writing or revising it, read
  `MISSION-FORMAT.md`.
- `RESOURCES.md`: high-trust sources for knowledge and communities for wisdom.
  When writing or revising it, read `RESOURCES-FORMAT.md`.
- `GLOSSARY.md`: canonical terms once the user can use them correctly. When adding
  a term, read `GLOSSARY-FORMAT.md`.
- `NOTES.md`: teaching preferences and working notes
- `lessons/NNNN-slug.html`: one **lesson** per file, sequential numbering
- `learning-records/NNNN-slug.md`: non-obvious lessons that steer future sessions.
  When writing one, read `LEARNING-RECORD-FORMAT.md`.
- `reference/*.html`: compressed cheat sheets, syntax, algorithms, sequences
- `assets/`: reusable lesson components (shared stylesheet first)

Create a file only when it has content to hold.

## Process

1. Identify the teaching project from the topic. Read the workspace files that
   exist. If the user described what they want to learn, that is the topic.

   Done when the project slug and current workspace state are known.

2. If `MISSION.md` is missing or vague, interview the user for the concrete
   real-world outcome, what success looks like, constraints, and out of scope.
   Write `CONTEXT.md` as one paragraph that re-orients a later session. Do not
   write lessons until the mission is confirmed.

   Done when `MISSION.md` states an observable outcome the user has confirmed and
   `CONTEXT.md` names the teaching project.

3. Before `RESOURCES.md` is well populated, find high-trust **primary sources**
   and communities. Ground teaching in those, not parametric knowledge.

   Done when `RESOURCES.md` has annotated knowledge sources for the next lesson,
   or an explicit gap.

4. Choose the next lesson from the mission and the user's **zone of proximal
   development**: the most relevant thing they cannot yet do, just beyond what
   learning records show they can. Read `NOTES.md` for teaching preferences.

   Done when the next lesson has a single tightly-scoped win tied to the mission.

5. Reuse `assets/` by default. Write a new component there when a second lesson
   would duplicate it. Produce one short self-contained HTML lesson, numbered
   after the highest existing file. Teach the knowledge required for the skill,
   then practise the skill through a tight feedback loop. Cite resources. Link
   related lessons and reference docs. Recommend one primary source. Remind them
   they can ask follow-up questions. Open the file when the harness can.

   Done when the lesson is saved, completable quickly, and opened or its path
   reported.

6. Update glossary, reference docs, and learning records as understanding
   crystallizes. Confirm with the user before changing the mission.

   Done when workspace files match what this session established.

## Lessons

A lesson is beautiful enough to return to (think Tufte): clean typography, short,
one tangible win. Learners' working memory is small; stay inside it.

Knowledge first, then skill practice. For knowledge, difficulty is the enemy: it
eats working memory needed for understanding. For skills, difficulty is the tool:
retrieval practice, spacing, and (for skills practice) interleaving build storage
strength rather than fluency that only feels like mastery.

Quizzes: each answer the same length so formatting does not leak the answer.
Feedback immediately, ideally automatically.

## Knowledge, skills, wisdom

- **Knowledge** comes from the high-trust resources in `RESOURCES.md`. Cite them.
- **Skills** stick through interactive practice with a tight feedback loop.
- **Wisdom** comes from real-world interaction. When a question needs it, answer,
  then point at a high-reputation community from `RESOURCES.md`. Honour a
  preference not to join one.

## Done when

- The mission is confirmed and recorded.
- The next lesson is in the user's zone of proximal development and saved under
  `lessons/`.
- Resources, glossary, and learning records reflect what this session established.
