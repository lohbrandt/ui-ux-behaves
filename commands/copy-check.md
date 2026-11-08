---
description: Find stuttering copy (the same word repeated in elements close together) on a screen
argument-hint: "[file with rendered text | URL]"
---

Check the copy of a screen area for stuttering and rewrite it.

1. Get the rendered text in screen order, one element per line: from the file in `$ARGUMENTS`,
   from a Playwright aria snapshot or `innerText` of the page if a browser tool is available, or
   ask the user to paste the area. Do not use i18n source files: their order rarely matches the
   screen.
2. Run `python3 ${CLAUDE_PLUGIN_ROOT}/skills/ui-ux/scripts/stutter_check.py <file> --lang <de|en>`
   (or pipe the text on stdin).
3. For each finding, rewrite the block following "No stuttering" in
   `${CLAUDE_PLUGIN_ROOT}/skills/ui-ux/references/masters.md`: the heading carries the term, the
   elements below say only what they do and where. Show before and after side by side.
4. Run the check again on the rewritten text; it should report nothing.
