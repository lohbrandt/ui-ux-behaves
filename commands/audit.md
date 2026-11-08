---
description: Count source patterns that break UI/UX behaves and keep them from growing (ratchet)
argument-hint: "[config.json] [--baseline file]"
---

Run the behave audit on this project and explain the result. You do the counting yourself with your
search tool; the plugin ships no scripts.

1. Find an audit config: the path in `$ARGUMENTS`, else `ui-ux-audit.json` in the project root.
   If there is none, copy `${CLAUDE_PLUGIN_ROOT}/examples/audit-config.carbon-react.json` as a
   starting point, adapt `include` and the `skip` folders to this project's components (ask before
   writing the file), and say which checks fit its design system.
2. For each check in `checks`, search the files matching `include`, minus `exclude` and the
   check's `skip`, for its `pattern`. The patterns are regular expressions with lookaheads and
   inline flags such as `(?i)`, so search in PCRE mode (ripgrep `--pcre2`). If the check has
   `with`, count a file only when it also contains that text. Count hits per file.
3. Ratchet: when the user wants one, compare the counts with `ui-ux-baseline.json` (check → file →
   count). A count that rises is a failure; a count that falls means the baseline should be lowered
   so it cannot rise again. Write or update the baseline only after asking.
4. Report per check: hits, files, the behave key and the fix. Open two or three hits per check and
   say whether each is a real finding or a legitimate exception (for example a search field in a
   toolbar may hide its label). Never claim the code is compliant because the audit is clean: it
   only finds patterns, not missing states.
5. Suggest the next step: fix, raise the baseline with a reason, or tune the config. For CI, the
   same config can drive a small script of your own; the format is plain JSON.
