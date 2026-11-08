# Design-system mapping: IBM Carbon (React)

A filled-in example of `skills/ui-ux/references/design-system-mapping.md` for `@carbon/react`, taken
from a production business application. Copy it into your design-system skill and adjust the right
column to your own wrappers. "Your …" marks a small component of your own that Carbon does not ship;
the note says what it has to do. Copy wording lives in your translation files, not here.

<!-- behave-keys:start -->
| Key | Component / pattern | Notes |
|---|---|---|
| `page.loading` | `SkeletonText`, for tables `DataTableSkeleton`, inside a region with `aria-busy="true"` and a visually hidden `role="status"` "Loading" | Never `Loading` (overlay spinner) over the page |
| `page.error` | `InlineNotification kind="error" lowContrast` + `Button kind="tertiary"` "Try again" | No `ActionableNotification`: it moves focus. Not for 403/404 |
| `page.noAccess` | Whole page: your no-access route. Area (HTTP 403): `Callout kind="info"` with the reason and a way back | No "Try again": a second attempt changes nothing |
| `page.hint` | `Callout` (info) at the top of the page, dismissible per user | |
| `status.saving` | `InlineLoading` with `aria-live="polite"` ("Saving…", "Saved 10:42") | |
| `status.success` | `InlineNotification kind="success"` or `ToastNotification lowContrast` with `role="status"`, `timeout` ≥ 10000 | |
| `status.warning` | `Callout kind="warning"` | |
| `status.error` | `InlineNotification kind="error" lowContrast`, the way out in `subtitle` | |
| `status.live` | Server push (WebSocket/SSE) that invalidates the affected queries | |
| `status.stale` | `InlineNotification kind="info"` "Changed meanwhile" + `Button kind="ghost"` "Reload" | |
| `status.conflict` | Your conflict view: both values side by side, choose per field | |
| `status.offline` | `InlineNotification kind="warning"`; reload after reconnect | |
| `status.tag` | `Tag size="sm"` with text, colour only as a supplement | |
| `field.focus` | Carbon focus ring (token `$focus`) | Never override it |
| `field.validating` | `InlineLoading` below the field | |
| `field.valid` | `helperText` with the result | Carbon has no success state on fields |
| `field.invalid` | `invalid` + `invalidText` | Replaces `helperText` |
| `field.warning` | `warn` + `warnText` | |
| `field.optional` | `labelText` ends with "(optional)" | |
| `field.readonly` | `readOnly` + `helperText` with the reason | |
| `field.disabled` | `disabled` only with a reason next to it | Prefer `readOnly` |
| `field.override` | `warn` + `Button kind="ghost"` "Use anyway" | |
| `field.repeatedError` | `invalidText` with an example + `Link` to the help page | |
| `form.dirty` | A visible mark ("Unsaved changes") + `beforeunload` | |
| `form.dirtyGuard` | Router blocker + `Modal` ("Discard changes" / "Keep editing") | |
| `form.submitting` | `Button` showing `InlineLoading` instead of its text | `disabled` only while sending |
| `form.submitSuccess` | As `action.success` | |
| `form.submitFailed` | `InlineNotification kind="error"` above the buttons + "Try again" | Input stays |
| `form.errorSummary` | `InlineNotification kind="error"` at the top with a list of `Link`s to the field ids; focus moves there | |
| `form.autosave` | Debounced save + `InlineLoading` status ("Saved 10:42") | |
| `date.single` | `DatePicker datePickerType="simple"` (known date) or `"single"` (with calendar) | flatpickr reads only the set format; tolerant parsing (`5.3.80`) needs `parseDate` |
| `date.dateTime` | `DatePicker` + `TimePicker` | |
| `date.range` | `DatePicker datePickerType="range"` (one picker, two `DatePickerInput`) | |
| `date.relative` | `Dropdown` + `NumberInput` | No calendar |
| `date.preset` | `Dropdown` with presets before the range picker; "Custom range" last | |
| `date.unavailable` | `minDate` / `maxDate`, flatpickr `disable` for holidays and closing days | |
| `date.invalid` | `invalid` + `invalidText` on `DatePickerInput` | |
| `table.loading` | `DataTableSkeleton` | |
| `table.empty` | Your table wrapper: sentence what appears here + primary action if allowed | |
| `table.noResults` | Your table wrapper: "No results for …" + `Button kind="ghost"` "Reset filters" | Not the same as empty |
| `table.loadError` | `InlineNotification kind="error"` above the table + "Reload" | |
| `table.sorted` | `isSortable`, `TableHeader` with `sortDirection` | |
| `table.filtered` | Filter flyout + filter `Tag`s, state in the URL | |
| `table.selected` | `TableSelectAll` / `TableSelectRow` (`getSelectionProps`) | Indeterminate state built in |
| `table.bulkActions` | `TableBatchActions` + `TableBatchAction` (`getBatchActionProps`) | |
| `table.rowActions` | `OverflowMenu` per row; destructive item `isDelete` + `hasDivider` at the bottom | A link in the first cell opens the record |
| `table.inlineEdit` | Fields inside `TableCell`, saved per row | |
| `cell.invalid` | `invalid` + `invalidText` on the field in the cell | |
| `table.expanded` | `TableExpandRow` / `TableExpandedRow` | |
| `table.scale` | `Pagination` with `itemRangeText` | |
| `table.density` | `size` of `DataTable` | |
| `table.columns` | Column chooser with a priority per column; minor columns hidden below `lg` | |
| `action.primary` | `Button kind="primary"`, one per area | Verb + noun |
| `action.secondary` | `Button kind="secondary"` / `"tertiary"` / `"ghost"` | |
| `action.danger` | `Button kind="danger"` (in a dialog) / `"danger--ghost"`; in a menu `OverflowMenuItem isDelete` | |
| `action.hidden` | Permission check hides the control; the server checks again | |
| `action.blocked` | `Callout` with the reason, who can help and a way out; button with `aria-describedby` | |
| `action.pending` | `InlineLoading` inside the button | |
| `action.warn` | `Callout kind="warning"` at the object; in a dialog `InlineNotification kind="warning"` | |
| `action.notice` | `Callout kind="info"` or `helperText` | |
| `action.confirm` | `Modal danger` with the consequence in the text; focus returns to the launcher | |
| `action.confirmTyped` | `Modal danger` with a `TextInput`; button enabled once the name matches | |
| `action.success` | `ToastNotification kind="success" lowContrast` (`role="status"`), next step in `subtitle` | |
| `action.undo` | `ToastNotification` with `Button kind="ghost"` "Undo", `timeout` ≥ 10000 | Never `ActionableNotification` (moves focus) |
| `action.deactivate` | Action "Deactivate" instead of "Delete", status as `Tag` | |
| `action.failed` | `InlineNotification kind="error"` where the action was + "Try again" | |
| `tab.selected` | `Tabs` + `TabList` + `TabPanels` | |
| `tab.route` | Tabs bound to the URL (search parameter or route) | |
| `tab.dirty` | Mark in the `Tab` with visually hidden text for screen readers | |
| `tab.invalid` | `Tab` with an error icon + hidden text; link from `form.errorSummary` | |
| `tab.overflow` | `TabList` scroll buttons (built in); at 375 px `contained` or a `Dropdown` | |
| `tab.disabled` | `Tab disabled` only with a reason in the panel | |
| `dialog.open` | `Modal`, `data-modal-primary-focus` on the first field or on "Cancel" | |
| `dialog.form` | `Modal` with `hasForm`; form rules from `ui-ux-form` | |
| `dialog.confirm` | As `action.confirm` | Title = question with the object |
| `dialog.busy` | Primary button with `InlineLoading`, closing blocked while sending | |
| `dialog.error` | `InlineNotification` inside `ModalBody` | |
| `dialog.nested` | Second question rendered in a portal above the open `Modal` | Avoid where possible |
| `dialog.close` | Focus returns to the launcher, with a fallback when it is gone | |
| `dialog.sidePanel` | Area next to the list in the `Grid` | |
<!-- behave-keys:end -->
