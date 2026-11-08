---
name: ui-ux-active
description: Actions the user triggers. Use when a button, action or menu item is planned or reviewed, especially when something is deleted, overwritten, sent, submitted or locked, when confirmation, undo, trash, warnings or permissions are involved, or when users complain about "Are you sure?" dialogs.
---

# Actions (active) and "Warn, but Recover"

Principle: friction grows with **consequence, scope and irreversibility**. Never punish: every action
ends with a result, a way back and a next step (forgiveness, peak-end rule).

## Buttons

| Key | Rule |
|---|---|
| `action.primary` | One per area, verb + noun ("Create case"), never "OK" |
| `action.secondary` | Cancel, alternatives; placed before the primary action |
| `action.danger` | Separate from everyday actions, at the bottom of the menu; never default, never on Enter |
| `action.pending` | Button shows progress, a second click has no effect |
| `action.hidden` | No permission → hide. Frontend permissions are only convenience; the backend always checks |
| `action.blocked` | Blocked by state → hint with a way out (state, action, button to resolve, "How it works"); the button points to it via `aria-describedby` |

## Warn, but Recover

Sequence: `action.warn` (early) → `action.notice` (inline) → `action.warn` (escalated) →
`action.confirm` → `action.success` + `action.undo`. **Routine actions skip everything up to
`action.success`.**

Decision, top to bottom, the first "yes" wins:

| Question | Yes → |
|---|---|
| 1. Reversible? | Execute immediately, `action.undo` (undo ≥ 10 s) |
| 2. Still referenced (other records, documents, links)? | `action.deactivate`: offer only "Deactivate"; "Delete" appears only when nothing points to it any more |
| 3. Can it be cushioned? | Trash with a retention period, versions, audit log; then as 1 |
| 4. Would a mistake be serious? | `action.confirm`: consequence with object, count, names **before** confirming |
| 5. Worst case catastrophic and rare (delete permanently, send to an authority)? | Multi-layered: confirmation + log; `action.confirmTyped` (type the name) only here |

Also: frequent action → keep it light; user in flow (data entry, writing) → do not interrupt with a
modal. No artificial waiting times as deterrent.

**Rule:** prevent what is catastrophic and hard to fix; give a way back for everything that happens
easily.

## `action.success` and `action.failed`

- Specific: "Letter sent to District Court Kiel.", never "Action completed".
- Undo **and** the next sensible step as a button; offer undo only if it reliably works.
- Failure: what is kept, what works now, "Try again"; no technician tone.

In detail (four strategies, mistakes, measuring): `references/warn-but-recover.md`.

## Accessibility

- Announce success and undo via a live region; the message does **not** take focus.
- The undo message stays while hovered/focused, can be closed and is keyboard reachable (WCAG 2.2.1).
- After the action: focus on a sensible target (neighbouring row, heading), never lost.
- Button names unambiguous without context ("Delete case Miller" in the row menu).

## Responsive

- At 375 px the primary action stays visible; further actions go into the menu.
- Stacked buttons: the safe action is reached first, the dangerous one not under the thumb.

## Checklist per dangerous action

- [ ] Would undo or deactivate suffice instead of a confirmation?
- [ ] Consequence names object, count, names before confirming?
- [ ] The safe option is default and has initial focus?
- [ ] Success with undo **and** next step?
- [ ] Keyboard, announcement, focus afterwards checked?
- [ ] Worst case protected in several layers?

Implementation: mapping of the keys in the design-system mapping (`ui-ux/references/design-system-mapping.md`).
