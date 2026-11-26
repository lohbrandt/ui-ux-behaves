---
type: llm
weight: 1
---

A successful response meets all of these:

1. It rejects a modal on every page load (it interrupts, trains people to click "OK" blindly, no decision is needed).
2. It proposes a reminder at most once a day (for example after the first sign-in of the day), remembered so reloads and navigation do not repeat it.
3. The reminder is a non-modal message (toast or similar) with an action that leads to the deadlines (for example "View notifications"), and the deadlines stay visible at the top of the bell panel.
4. It follows the rules for self-dismissing messages: polite live region, no focus theft, at least 10 seconds or persistent until closed, pauses on hover/focus, closable.
5. The message says how many deadlines and what to do now, in a calm tone without alarm wording.

Score 1 only if at least four of the five points are clearly present and none is contradicted.
