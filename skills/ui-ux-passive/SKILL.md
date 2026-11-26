---
name: ui-ux-passive
description: System feedback without user action. Use when loading, saving, status, hints, error messages, notifications, toasts, live announcements, stale data, conflicts during concurrent editing, missing permissions or offline states are planned, written or reviewed.
---

# Feedback (passive)

Principle: the system says **unprompted** what is going on, **without interrupting the user**.
Message as close to the object as possible, as calm as possible, with a way out when something is
stuck. Every message follows the four parts of `../ui-ux/references/helpful-feedback.md`: what
happened, why in plain words, what to do now, what is kept.

## Behaves

| Key | Rule | Trap |
|---|---|---|
| `page.loading` | Skeleton of the page, no spinner over the page; for long operations say what is being done in steps the user understands | Empty state flashes before the data |
| `page.error` | Message with reason in user language and "Reload" | Blank page |
| `page.noAccess` | Own page "No access" with the reason, a way back and who can grant access | Blank page or 404 |
| `page.hint` | Page hint at the top, dismissible as in `notice.close`, action "Show me how" | Hint returns after dismissing |
| `notice.close` | **Dismissing is visible at once and stays remembered.** Information, tips and explanations carry a close button ("×", accessible name "Dismiss hint") directly on the hint, top right, last in the tab order. Dismissed per person on the server: it stays dismissed after reloading, on another device and after signing out. One way back: "Show hints again" in the personal settings. A hint whose content changed substantially (new version) may appear exactly once more. Status, errors and locks have no "×": they leave with their cause and name a way out. Toasts close by themselves, by "×" and by Escape. Dismissed hints go to the page's hint collector (`hint.collect`) | "Hide" in an overflow "…" menu or another detour; dismissed hint returns on reload or on another device (browser storage only); "×" on a lock or an error |
| `hint.collect` | Hint collector: an information button "(i)" in the header of every page lists the hints dismissed on this page and the page's suggestions (hints without consequence), then "Show me how" and the help for this page. A badge counts what is new. The list opens directly at the (i), Escape closes it. The bell is personal (notifications, deadlines, tasks; the same on every page), the (i) is the context of this page. Status, errors, warnings and locks never go into it. Dialogs have no (i) of their own; there `notice.close` applies | Dismissed hint gone without a trace; dismissed hints mixed into the notification bell; (i) filled with errors or locks; a second rule set for suggestions |
| `hint.transition` | When "×" is pressed, the hint moves into the (i) in one short motion (design-system motion tokens, about 0.4 s, expressive exit easing); focus then goes to the (i) and a polite announcement says where the hint went ("Hint moved to page information"). With "reduce motion" the hint only disappears; focus and announcement stay | Focus falls to the start of the page or into nothing; motion despite "reduce motion"; hint vanishes without a visible destination |
| `hint.ticker` | Optional one-line ticker next to the (i), only where there is room (wide screens, from a large breakpoint): changes about every 8 s, suggestions first, pauses on pointer and focus, off with `prefers-reduced-motion` (WCAG 2.2.2 Pause, Stop, Hide), not a live region (`aria-live="off"`); activating it opens the list of the (i). Each person can switch it off in the personal settings | Announcement on every change; runs despite "reduce motion"; cannot be paused; squeezes the header on narrow screens |
| `status.saving` | Small status in place ("Saving …" → "Saved 10:42") | Whole page locked |
| `status.success` | Inline or toast, not modal, disappears on its own | Success dialog with "OK" |
| `status.warning` | Inline at the object, with a way out | Warning without an action |
| `status.error` | Inline at the object, short title, detail with a way out; input stays | "An error has occurred" |
| `status.live` | Others change the same record → data reloads quietly, hint only if it affects the user | Page jumps under the cursor |
| `notice.new` | A new notification raises the count on the bell; the count is part of the bell's accessible name ("Notifications, 3 unread") and is announced once, politely ("1 new notification"; several at once in one announcement). No toast per notification; the details wait in the bell's panel (`notice.panel`) | A toast per notification; red bell or badge as the only sign; assertive announcement or focus theft |
| `notice.panel` | The bell opens a panel, not a page: the latest ten notifications, deadlines on top with a text tag, unread as a text tag; a row names subject, sender and time and leads to its target. "Mark all as read" and "Show all" (full list). On opening, focus goes to the panel heading; Escape closes and returns focus to the bell. Opening an entry marks it read and closes the panel. Full width on narrow screens | The bell navigates away from the current work; unread shown by colour or bold alone; focus stays behind the panel or is lost on closing |
| `notice.due` | Open deadlines are additionally reminded once a day, after the first sign-in of the day, as a toast with the number and an action "View notifications" (opens `notice.panel`); remembered for the day, so reloads and navigation do not repeat it. Toast rules apply (polite, no focus theft, ≥ 10 s, pause on hover/focus, closable); calm wording | A modal "You have 3 open deadlines" with "OK" on every page load; reminder on every reload; deadline only visible in the bell |
| `status.stale` | Shown state is old → hint + "Reload" | Silently working on an old state |
| `status.conflict` | Show field by field what changed; never overwrite silently | Last write wins |
| `status.offline` | Say what stays local and when it will be transferred; retry automatically | Data gone |
| `status.tag` | Status as a tag with text, colour only in addition | Colour alone |

**Which form?** At the object (field, row, area) before page hint before toast. Modal only when the
user must decide (`ui-ux-dialog`). A hint that blocks an action is `action.blocked` (`ui-ux-active`).

**Bell or (i)?** The bell (`notice.*`) holds what concerns the person: notifications, deadlines,
tasks, the same on every page. The (i) (`hint.*`) holds the context of the current page: dismissed
hints and suggestions. Status, errors and locks belong to neither; they stay at the object.

## Accessibility

- Messages in a live region: `polite` for status and success, `assertive` only for errors that
  require immediate action. The region exists before the text.
- Messages never take focus (no alert dialogs for hints).
- Self-dismissing messages: at least 10 s, pause on hover/focus, closable; errors never disappear by
  themselves.
- Announce loading ("Loading") and set `aria-busy` on the area.
- Motion respects "reduced motion".
- Close buttons on hints have an accessible name ("Dismiss hint") and come last in the hint's tab order.
- Anything that moves or changes by itself (ticker) pauses on hover and focus, can be switched off and
  is not a live region.

## Responsive

- Toasts full width at 375 px, never covering a primary action.
- Page hint wraps, buttons stacked; the skeleton has the shape of the narrow view.
- The ticker (`hint.ticker`) is hidden on narrow screens; the (i) and the bell stay. The bell's panel
  takes the full width.

## Common mistakes

- Spinner over the whole page; toast for a field error.
- Message that steals focus.
- Error without a way out, success without content.
- Copy that blames the user, alarms without need ("Fatal", "!") or only names a code.
- Realtime update that overwrites input.
- "Hide" hidden in a "…" menu, or a dismissed hint that comes back after reload.
- A toast per incoming notification; a modal reminder on every page load.

## Checklist

- [ ] Loading, error, no access defined per page?
- [ ] Message at the object, with a way out, without stealing focus?
- [ ] Live region with fitting urgency?
- [ ] Stale and conflict visible instead of silent?
- [ ] Time limits ≥ 10 s and closable?
- [ ] Every message: what happened, why, what now, what is kept; calm tone, no blame?
- [ ] Hint (information, tip, explanation) with "×" directly on it, remembered per person on the server; no "×" only for status, error or lock, each with a way out?
- [ ] Dismissed hints in the (i) of the page; ticker pausable and off with reduced motion (`hint.collect`, `hint.ticker`)?
- [ ] New notifications as count and one polite announcement; bell panel with focus and Escape; deadlines at most once a day (`notice.*`)?

Heuristics (`../ui-ux/references/masters.md`): H1 system status, H7 dismissible page hints that stay dismissed ("×" directly, remembered per person, collected in the (i) of the page), H9 notice with a way out.

Implementation: mapping of the keys in the design-system mapping (`ui-ux/references/design-system-mapping.md`).
