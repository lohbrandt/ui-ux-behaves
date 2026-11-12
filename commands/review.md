---
description: Review a screen against the behaves and the principles of the masters
argument-hint: "[page, component path, URL or screenshot]"
---

Review the screen named in `$ARGUMENTS` with the `ui-ux` skill and the matching sub-skills.

1. Look at it once like a newcomer: what invites a click, and what is visibly different afterwards?
2. List the containers on the screen (page, table, form, dialog, tabs) and check each for its
   required behaves: loading, empty, ready, error, and warning where there is risk.
3. Go through the seven groups in `${CLAUDE_PLUGIN_ROOT}/skills/ui-ux/references/masters.md`
   (interaction, heuristics, perception, language, sound, respect, helpful feedback). Check every
   message on the screen against the four parts and the tone of
   `${CLAUDE_PLUGIN_ROOT}/skills/ui-ux/references/helpful-feedback.md`. Answer the heuristics H1 to H10
   one by one, each with a finding or "no finding". If the rendered text is available, run the
   stutter check (`/ui-ux-behaves:copy-check`). For a core or costly task, offer a walkthrough of it
   (`/ui-ux-behaves:walkthrough`).
4. Report findings as a table: severity (critical, high, medium, low), behave key or principle by
   name ("Mapping: toggle acts on another page"), place, fix. Name what already works well.
5. End with numbered acceptance criteria for the fixes, in the forms listed in the entry skill.
