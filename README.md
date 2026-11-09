# UI/UX Behaves

A rule suite that helps Claude plan, build and review screens: tables, forms, date inputs, actions,
system feedback, tabs and dialogs. It works with any design system.

Built while making software for debt counselling, where clear screens help people get out of debt.

## Purpose

For software that people depend on: counselling, social work, public services, health, education,
and the everyday tools of those who serve them. The rules rest on decades of research into how
people perceive, read and decide. This plugin uses that research for the people on the screen, never
against them: no tricks that exploit attention, fear or habit. Free, MIT, no tracking.

It does not replace a design system; it tells your design system which state to show when.

## The idea

Every state a screen can be in gets a **behave key** of the form `context.state[.severity]`, for
example `table.noResults`, `field.invalid` or `action.undo`. Each key sits on three axes (phase,
semantics, trigger) and comes with a rule, a typical trap, accessibility requirements and what
happens on narrow screens. The suite never names components. Your design-system skill maps each
key to a component once (`references/design-system-mapping.md`), so switching design systems means
replacing one mapping file, not the rules. For IBM Carbon with React a filled-in mapping ships in
`examples/design-system-mapping.carbon-react.md`.

The rules are grounded in the classics: Don Norman (signifiers, mapping, feedback), Jakob Nielsen's
ten heuristics, Gestalt principles and UX writing. Each principle has a check question and links to
the original texts, and each of the ten heuristics names where in the suite it is applied. For
learnability, the cognitive walkthrough follows one task step by step from a newcomer's view. Two further groups cover sound (when it helps, and why silence is the default)
and respect: no deceptive patterns.

## Skills

| Skill | Use it when |
|---|---|
| `ui-ux` | Entry point: planning or reviewing any page or flow, writing acceptance criteria, missing states |
| `ui-ux-table` | Lists and tables: empty vs. no results, filters, selection, bulk and row actions |
| `ui-ux-form` | Forms and fields: validation timing, errors, toggles, unsaved changes, autosave |
| `ui-ux-date` | Dates, times, ranges, presets, blocked days, time zones |
| `ui-ux-active` | User actions: delete, send, confirm, undo, "Warn, but Recover" |
| `ui-ux-passive` | System feedback: loading, saving, notifications, stale data, conflicts, offline |
| `ui-ux-tabs` | Tabs: when to use them, URL state, dirty and invalid tabs, overflow |
| `ui-ux-dialog` | Modals and side panels: when a dialog is right, focus, nesting, closing |
| `ui-ux-chart` | Charts and key figures: which form, axis from zero, legends, data palette, table alternative, no personal data |

## Commands

| Command | What it does |
|---|---|
| `/ui-ux-behaves:review` | Reviews a page, component, URL or screenshot against the behaves and the masters; findings with severity, term and fix, then acceptance criteria |
| `/ui-ux-behaves:walkthrough` | Walks through one task step by step from a newcomer's view (cognitive walkthrough): four questions per step, a recording sheet per step, findings and acceptance criteria |
| `/ui-ux-behaves:audit` | Counts source patterns that break behaves (spinner over an area, toggle inside a submitted form, disabled submit, "Are you sure?") and keeps them from growing with a baseline |
| `/ui-ux-behaves:copy-check` | Finds stuttering copy: the same word repeated in elements close together on screen, and rewrites the block |

The audit patterns come from a plain JSON config; `examples/audit-config.carbon-react.json` is a
starting point for IBM Carbon with React. The same config can drive a check in your CI.

## Install

In Claude Code, one command at a time.

Step 1, add the marketplace:

```
/plugin marketplace add lohbrandt/ui-ux-behaves
```

Step 2, once step 1 reports success, install the plugin:

```
/plugin install ui-ux-behaves@ui-ux-behaves
```

## Use it

Ask Claude to plan, build or review a screen, for example "Review the settings page against the
UI/UX rules" or "Write acceptance criteria for the creditor list". Claude loads the entry skill and
the matching sub-skill on its own. To connect your design system, copy
`skills/ui-ux/references/design-system-mapping.md` into your design-system skill and fill in the
component for each key, or start from the Carbon example in `examples/`. Then ask Claude to check
the mapping against the catalog.

## Data

The plugin contains only Markdown and JSON: instructions, references and examples. It runs no code
of its own, sends nothing anywhere and calls no external service.

## License

MIT, see `LICENSE`.
