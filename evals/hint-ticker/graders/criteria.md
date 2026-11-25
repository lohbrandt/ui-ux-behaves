---
type: llm
weight: 1
---

A successful response meets all of these:

1. It rejects announcing every change to screen readers: the ticker is not a live region (aria-live off); clicking or activating it opens the full list instead.
2. The ticker pauses on pointer hover and on keyboard focus, and can be stopped (WCAG 2.2.2 Pause, Stop, Hide named or clearly implied).
3. It is off when the user prefers reduced motion (prefers-reduced-motion).
4. It shows only when there is room (wide screens / from a breakpoint), not on narrow screens, and rotates slowly (several seconds, about 8 s, clearly slower than 3 s).
5. Each person can switch the ticker off in their personal settings; suggestions (or the most relevant entries) come first.

Score 1 only if at least four of the five points are clearly present and none is contradicted.
