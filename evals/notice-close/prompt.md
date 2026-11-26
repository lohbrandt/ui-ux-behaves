---
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

We are reviewing the hint design of our case-management web app before the next release.

Today every page can show a short info box at the top ("Tip: you can filter the list by status").
To get rid of it, people open the "…" menu of the box and choose "Hide". After reloading the page
or signing in on another computer the tip is back. The same box component is also used for
"This record is locked because it was submitted" and for "Saving failed, try again"; those also
offer "Hide" in the "…" menu.

Review this design and write numbered acceptance criteria for how hints are dismissed.
