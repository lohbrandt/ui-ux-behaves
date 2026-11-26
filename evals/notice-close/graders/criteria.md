---
type: llm
weight: 1
---

A successful response meets all of these:

1. The dismiss control sits directly on the hint as a visible close button (an "×" icon button with an accessible name such as "Dismiss hint"), not inside a "…"/overflow menu and not as a detour.
2. Dismissing is remembered per person on the server (or account level), so the hint stays dismissed after reload, on another device and after signing out; browser-only storage is named as insufficient.
3. There is one way back to bring dismissed hints back (for example "Show hints again" in personal settings).
4. Informational content (info, tip, explanation) is dismissible, but status, error and lock messages ("record is locked", "saving failed") get no close button: they disappear when the cause is resolved and name a way out.
5. A hint whose content changed substantially may reappear (once), instead of staying hidden forever or returning on every load.

Score 1 only if all five points are clearly present and none is contradicted (for example by keeping "Hide" for the lock or error message).
