---
name: ui-ux-form
description: Forms and input fields. Use when a form, input mask, field or toggle is created or reviewed, when validation, required fields, error messages, warnings, unsaved changes, autosave or submitting are involved; for date fields also ui-ux-date.
---

# Forms

Principle: **validate late, report close, never lose input.** Errors sit at the field, not in a
toast; every error says how to get it right.

## Field behaves

| Key | Rule | Trap |
|---|---|---|
| `field.focus` | Focus clearly visible | Focus ring removed by styling |
| `field.validating` | "Checking …" only for server checks (duplicate, reference number) | Check on every keystroke |
| `field.valid` | Success only for hard fields (password, IBAN checksum) | Green tick on every field |
| `field.invalid` | Message at the field: problem + solution ("A German IBAN has 22 characters") | "Invalid input" |
| `field.warning` | Non-fatal: allow, warn ("Date falls on a weekend") | Warning blocks saving |
| `field.optional` | Required is the norm; optional is marked "(optional)" | Asterisk without explanation |
| `field.readonly` / `field.disabled` | Always say why (permission, status) | Silent grey |
| `field.override` | Check can be overridden for address/phone; never for IBAN or reference numbers | User cannot proceed |
| `field.repeatedError` | From the 3rd identical error, more help (example, help link) | Same text over and over |

**Timing:** validate on leaving the field (`on-blur`) and on submit. While typing only to remove an
error already shown. Parse tolerantly: spaces, groups, upper/lower case.

## Form behaves

| Key | Rule |
|---|---|
| `form.errorSummary` | On submit with errors: summary at the top with links to the fields, focus on the summary or the first field; never the only indication |
| `form.submitting` | Submit button shows progress, double click has no effect |
| `form.submitSuccess` | Specific, with next step (`ui-ux-active`) |
| `form.submitFailed` | Input stays, reason in user language, "Try again" |
| `form.dirty` / `form.dirtyGuard` | Unsaved changes visible; ask on leaving ("Discard changes" / "Keep editing") |
| `form.autosave` | Where interruptions are frequent (data entry on the phone): draft saved automatically, state visible ("Saved 10:42") |

**The submit button stays enabled.** A disabled button does not explain what is missing. Exception:
a block with a visible hint and a way out (`action.blocked`).

**Toggles** take effect immediately, without a save button. The label says what happens and where
("Show in lists"), not only the object. If the toggle acts outside the page, the help text below
names the place, ideally with a link. No toggle for something that only applies after submitting;
use a checkbox or a choice instead (mapping, feedback: `ui-ux/references/masters.md`).

Concurrent editing: conflict protection instead of silent overwriting (`status.conflict`).

## Accessibility

- Every field has a visible label (a placeholder is not a label); help and error connected via
  `aria-describedby`, invalid via `aria-invalid`.
- The error summary is announced; links jump into the field.
- `autocomplete` and a matching input mode (email, number, phone).
- Order of fields = reading order = tab order.

## Responsive

- Form in a narrow column (about half width) at 1280 px; at 375 px single column, full width.
- Buttons not covered by the on-screen keyboard; error summary stays reachable at the top.

## Common mistakes

- Validating while typing; errors as toast or tooltip.
- Form cleared after a server error.
- Disabled submit button without a reason.
- Required-field errors on first opening.
- A toggle whose effect cannot be seen and whose label does not say where it happens.

## Checklist

- [ ] Validation on-blur + on-submit, message at the field with a solution?
- [ ] Error summary with links and focus?
- [ ] Server error: input kept, "Try again"?
- [ ] Leave guard for unsaved changes?
- [ ] Labels, `autocomplete`, announcements checked; single column at 375 px?

Implementation: mapping of the keys in the design-system mapping (`ui-ux/references/design-system-mapping.md`).
