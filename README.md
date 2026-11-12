# UI/UX Behaves

A rule suite for planning, building, and reviewing UI screens: tables, forms, date inputs,
user actions, system feedback, tabs, and dialogs. It is design-system-agnostic.

## Purpose

UI/UX Behaves provides rules for the states that a screen can be in and for how those states
should be handled. It is intended for products that users rely on — for example counselling,
social work, public services, health, education, and the internal tools used by their staff —
and applies to any similar software.

The rules are grounded in established human-factors research: Don Norman (signifiers, mapping,
feedback), Jakob Nielsen's ten usability heuristics, the Gestalt principles, and UX writing.
Each principle provides a check question and links to the original text; each heuristic notes
where in the suite it is applied. A cognitive walkthrough covers learnability step by step from
a newcomer's view. Two further groups cover sound (used sparingly, with silence as the default)
and respect (no deceptive patterns).

## What it does and does not do

- **Does:** Tell a design system which state to show, when.
- **Does not:** Replace a design system. It names the state, not the component; the mapping to
  concrete components is done separately.
- **Scope:** It is an instruction and reference suite. It contains only Markdown and JSON —
  instructions, references, and examples. It executes no code of its own, sends no data, and
  calls no external service.

## Core concept

Every state a screen can be in gets a **behave key** of the form `context.state[.severity]`,
for example `table.noResults`, `field.invalid`, or `action.undo`. Each key is positioned on
three axes (phase, semantics, trigger) and comes with a rule, a typical trap, accessibility
requirements, and behaviour on narrow screens.

The suite never names components. A design-system skill maps each key to a component once
(`references/design-system-mapping.md`), so switching design systems means replacing one
mapping file rather than the rules. A filled-in mapping for IBM Carbon with React ships in
`examples/design-system-mapping.carbon-react.md`.

## Skills

| Skill | Use it when |
|---|---|
| `ui-ux` | Entry point: planning or reviewing any page or flow, writing acceptance criteria, covering missing states |
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
| `/ui-ux-behaves:review` | Reviews a page, component, URL, or screenshot against the behaviours and the master principles; returns findings with severity, term, and fix, plus acceptance criteria |
| `/ui-ux-behaves:walkthrough` | Runs a cognitive walkthrough of one task from a newcomer's view: four questions per step, a recording sheet per step, findings, and acceptance criteria |
| `/ui-ux-behaves:audit` | Counts source patterns that break behaviours (spinner over an area, toggle inside a submitted form, disabled submit, "Are you sure?") and keeps them from growing against a baseline |
| `/ui-ux-behaves:copy-check` | Finds stuttering copy — the same word repeated in elements close together on screen — and rewrites the block |

The audit patterns come from a plain JSON config; `examples/audit-config.carbon-react.json`
is a starting point for IBM Carbon with React. The same config can run as a check in CI.

## Requirements

- A Claude Code environment that supports plugins and skills.
- A design system to map behave keys to. A mapping file is required before applying the rules;
  use `references/design-system-mapping.md` or start from `examples/`.

## Installation

In Claude Code, run one command at a time.

Step 1 — add the marketplace:

```
/plugin marketplace add lohbrandt/ui-ux-behaves
```

Step 2 — after step 1 reports success, install the plugin:

```
/plugin install ui-ux-behaves@ui-ux-behaves
```

## Usage

Ask Claude to plan, build, or review a screen, for example:

- "Review the settings page against the UI/UX rules."
- "Write acceptance criteria for the creditor list."

Claude loads the entry skill and the matching sub-skill automatically. To connect your design
system, copy `skills/ui-ux/references/design-system-mapping.md` into your design-system skill and
fill in the component for each key, or start from the Carbon example in `examples/`. Then ask
Claude to check the mapping against the catalogue.

## Data and privacy

The plugin contains only Markdown and JSON: instructions, references, and examples. It runs no
code of its own, sends no data, and calls no external service.

## License

MIT. See `LICENSE`.

This project is community-maintained and is not affiliated with Anthropic.