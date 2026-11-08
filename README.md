# UI/UX Behaves

A rule suite that helps Claude plan, build and review the screens of business applications: tables,
forms, date inputs, actions, system feedback, tabs and dialogs. It works with any design system.

Built while making software for debt counselling, where clear screens help people get out of debt.

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

## Commands and tools

| Command | What it does |
|---|---|
| `/ui-ux-behaves:review` | Reviews a page, component, URL or screenshot against the behaves and the masters; findings with severity, term and fix, then acceptance criteria |
| `/ui-ux-behaves:audit` | Counts source patterns that break behaves (spinner over an area, toggle inside a submitted form, disabled submit, "Are you sure?") and keeps them from growing with a baseline |
| `/ui-ux-behaves:copy-check` | Finds stuttering copy: the same word repeated in elements close together on screen, and rewrites the block |

The scripts behind them live in `skills/ui-ux/scripts/` (Python 3, standard library only) and also
run in CI: `behave_audit.py` (ratchet, exit 1 when a count rises), `stutter_check.py` and
`mapping_check.py` (every behave key mapped exactly once in your design-system mapping). The audit
patterns come from a config; `examples/audit-config.carbon-react.json` is a starting point for
IBM Carbon with React.

## Install

In Claude Code:

```
/plugin install ui-ux-behaves --marketplace lohbrandt/ui-ux-behaves
```

On older versions, add the marketplace first:

```
/plugin marketplace add lohbrandt/ui-ux-behaves
/plugin install ui-ux-behaves@ui-ux-behaves
```

## Use it

Install the plugin and ask Claude to plan, build or review a screen, for example "Review the
settings page against the UI/UX rules" or "Write acceptance criteria for the creditor list".
Claude loads the entry skill and the matching sub-skill on its own. To connect your design
system, copy `skills/ui-ux/references/design-system-mapping.md` into your design-system skill and
fill in the component for each key.

## Data

The plugin contains Markdown instructions and three local Python scripts. The scripts read the
files you point them at and write only the report and baseline files you name. Nothing is sent
anywhere and no external service is called.

## License

MIT, see `LICENSE`.
