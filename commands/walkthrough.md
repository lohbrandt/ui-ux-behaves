---
description: Walk through one task step by step from a newcomer's view (cognitive walkthrough)
argument-hint: "[task, user group, screens, URL or screenshots]"
---

Run a cognitive walkthrough of the task named in `$ARGUMENTS` with the `ui-ux` skill and
`${CLAUDE_PLUGIN_ROOT}/skills/ui-ux/references/cognitive-walkthrough.md`.

1. Prepare: write down the user group (from evidence; mark assumptions), the task in the users'
   words, the correct sequence of actions with known alternatives, and which version is judged.
   If the step list cannot be derived from the material, ask for it instead of guessing.
2. For every step, answer the four questions (right thing, notice, connect, progress) with
   yes or no and a reason. A step passes only when all four are yes. After a failure, continue as
   if the step had worked. Mark answers the material does not allow you to judge.
3. Show one recording sheet per step, then a summary: steps passed of total, and which question
   failed where.
4. Turn every "no" into a finding as in `/ui-ux-behaves:review`: severity, principle by name
   (signifier, mapping, feedback, heuristic number), place, fix.
5. End with numbered acceptance criteria for the fixes, and say that a group session or a test with
   real users should confirm the result.
