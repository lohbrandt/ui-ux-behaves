---
description: Count source patterns that break UI/UX behaves and keep them from growing (ratchet)
argument-hint: "[config.json] [--baseline file]"
---

Run the behave audit on this project and explain the result.

1. Find an audit config: the path in `$ARGUMENTS`, else `ui-ux-audit.json` in the project root.
   If there is none, copy `${CLAUDE_PLUGIN_ROOT}/examples/audit-config.carbon-react.json` as a
   starting point, adapt `include` and the `skip` folders to this project's components (ask before
   writing the file), and say which checks fit its design system.
2. Run `python3 ${CLAUDE_PLUGIN_ROOT}/skills/ui-ux/scripts/behave_audit.py --config <config>
   --report ui-ux-audit.md` from the frontend root. Add `--baseline ui-ux-baseline.json` when the
   user wants a ratchet; the first run writes the baseline.
3. Report per check: hits, files, the behave key and the fix. Open two or three hits per check and
   say whether each is a real finding or a legitimate exception (for example a search field in a
   toolbar may hide its label). Never claim the code is compliant because the audit is clean: it
   only finds patterns, not missing states.
4. Suggest the next step: fix, raise the baseline with a reason, or tune the config.
