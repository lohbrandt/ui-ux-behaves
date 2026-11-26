---
type: llm
weight: 1
---

A successful response meets all of these:

1. The dismissed hint visibly moves (a short transition/animation, well under a second) from its place into the (i) button, so the destination is learnable.
2. After dismissing, keyboard focus moves to the (i) button (not to the document start or into nothing).
3. A polite live-region announcement tells screen-reader users where the hint went (for example "Hint moved to page information").
4. With the operating-system setting "reduce motion" (prefers-reduced-motion) there is no flight animation; the hint simply disappears, but focus and announcement still happen.
5. The motion uses the design system's motion tokens (duration and easing) rather than ad-hoc values, or otherwise names consistent, short timing.

Score 1 only if all five points are clearly present and none is contradicted.
