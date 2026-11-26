---
type: llm
weight: 1
---

A successful response meets all of these:

1. It rejects mixing dismissed page hints into the notification bell: the bell is personal (notifications, deadlines, tasks, the same on every page), while dismissed hints belong to the context of the current page.
2. It proposes a per-page hint collector, for example an information "(i)" button in the page header, that lists the dismissed hints of this page (and optional suggestions), with a badge or count for what is new, and ends with a way to help for the page (help link and/or "show me how").
3. Status, error, warning and lock messages (such as "saving failed" or "session expires") never go into the collector.
4. The list opens directly at the (i) button, is keyboard reachable, and Escape closes it.
5. It addresses dialogs: no separate collector inside a dialog (hints there are simply dismissible), or an equivalent explicit rule.

Score 1 only if at least four of the five points are clearly present and none is contradicted.
