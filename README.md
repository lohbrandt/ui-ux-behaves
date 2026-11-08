# UI/UX Behaves

A rule suite that helps Claude plan, build and review the screens of business applications: tables,
forms, date inputs, actions, system feedback, tabs and dialogs. It works with any design system.

## The idea

Every state a screen can be in gets a **behave key** of the form `context.state[.severity]`, for
example `table.noResults`, `field.invalid` or `action.undo`. Each key sits on three axes (phase,
semantics, trigger) and comes with a rule, a typical trap, accessibility requirements and what
happens on narrow screens. The suite never names components. Your design-system skill maps each
key to a component once (`references/design-system-mapping.md`), so switching design systems means
replacing one mapping file, not the rules.

The rules are grounded in the classics: Don Norman (signifiers, mapping, feedback), Jakob Nielsen's
ten heuristics, Gestalt principles and UX writing. Each principle has a check question and links to
the original texts.

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

## Install

In Claude Code:

```
/plugin install ui-ux-behaves --marketplace sin-ev/ui-ux-behaves
```

On older versions, add the marketplace first:

```
/plugin marketplace add sin-ev/ui-ux-behaves
/plugin install ui-ux-behaves@ui-ux-behaves
```

## Use it

Install the plugin and ask Claude to plan, build or review a screen, for example "Review the
settings page against the UI/UX rules" or "Write acceptance criteria for the creditor list".
Claude loads the entry skill and the matching sub-skill on its own. To connect your design
system, copy `skills/ui-ux/references/design-system-mapping.md` into your design-system skill and
fill in the component for each key.

## Data

The plugin contains only Markdown instructions. It sends no data anywhere, calls no external
service and stores nothing.

## License

MIT, see `LICENSE`.
