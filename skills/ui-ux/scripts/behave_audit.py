#!/usr/bin/env python3
"""Count source patterns that break UI/UX behaves, per check and file; optional ratchet.

Usage:
  behave_audit.py --config audit.json [--root DIR] [--report report.md]
                  [--baseline baseline.json [--update]]

The config names the patterns of your design system (see examples/audit-config.*.json):
  {
    "include": ["src/**/*.tsx"], "exclude": ["**/*.test.tsx"],
    "checks": {
      "spinner": {"behave": "page.loading", "pattern": "<Loading\\\\b",
                  "fix": "Skeleton for areas; inline loading only at a button",
                  "skip": ["src/components/QueryState/**"]},
      "toggleNextToSave": {"behave": "ui-ux-form: toggles", "pattern": "<Toggle\\\\b",
                           "with": "type=\\"submit\\""}
    }
  }
`pattern` is a Python regex counted per file. `with` (optional) counts a file only if it also
matches that regex. `skip` lists globs where the pattern is the component itself.

Without --baseline it prints the counts and exits 0. With --baseline it fails (exit 1) when a
count rose or a new file appears, and reports counts that fell so the baseline can be lowered.
--update writes the current counts as the new baseline.
Standard library only.
"""

import argparse
import json
import re
import sys
from pathlib import Path


def glob_re(pattern: str) -> re.Pattern:
    out, i = "", 0
    while i < len(pattern):
        if pattern.startswith("**/", i):
            out += "(?:.*/)?"; i += 3
        elif pattern.startswith("**", i):
            out += ".*"; i += 2
        elif pattern[i] == "*":
            out += "[^/]*"; i += 1
        elif pattern[i] == "?":
            out += "[^/]"; i += 1
        else:
            out += re.escape(pattern[i]); i += 1
    return re.compile(out + r"\Z")


def matches(path: str, globs: list[str]) -> bool:
    return any(glob_re(g).match(path) for g in globs)


def scan(root: Path, config: dict) -> dict[str, dict[str, int]]:
    include, exclude = config.get("include", ["**/*"]), config.get("exclude", [])
    files = sorted(
        p.relative_to(root).as_posix()
        for p in root.rglob("*")
        if p.is_file() and matches(p.relative_to(root).as_posix(), include)
        and not matches(p.relative_to(root).as_posix(), exclude)
    )
    texts = {f: (root / f).read_text(encoding="utf-8", errors="replace") for f in files}
    counts: dict[str, dict[str, int]] = {}
    for name, check in config["checks"].items():
        pattern = re.compile(check["pattern"])
        together = re.compile(check["with"]) if check.get("with") else None
        skip = check.get("skip", [])
        per_file = {}
        for f, text in texts.items():
            if matches(f, skip) or (together and not together.search(text)):
                continue
            n = len(pattern.findall(text))
            if n:
                per_file[f] = n
        counts[name] = per_file
    return counts


def report(config: dict, counts: dict) -> str:
    lines = ["# Behave audit", "", "| Check | Behave | Files | Hits | Fix |", "|---|---|---|---|---|"]
    for name, per_file in counts.items():
        c = config["checks"][name]
        lines.append(f"| `{name}` | `{c.get('behave', '')}` | {len(per_file)} | {sum(per_file.values())} | {c.get('fix', '')} |")
    for name, per_file in counts.items():
        if per_file:
            lines += ["", f"## `{name}`", ""] + [f"- `{f}`: {n}" for f, n in sorted(per_file.items())]
    return "\n".join(lines) + "\n"


def ratchet(counts: dict, baseline: dict) -> tuple[list[str], list[str]]:
    worse, better = [], []
    for name, per_file in counts.items():
        base = baseline.get(name, {})
        for f, n in per_file.items():
            if n > base.get(f, 0):
                worse.append(f"{name}: {f} {base.get(f, 0)} → {n}")
        for f, n in base.items():
            if per_file.get(f, 0) < n:
                better.append(f"{name}: {f} {n} → {per_file.get(f, 0)}")
    return worse, better


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", required=True)
    ap.add_argument("--root", default=".")
    ap.add_argument("--report")
    ap.add_argument("--baseline")
    ap.add_argument("--update", action="store_true")
    args = ap.parse_args()

    config = json.loads(Path(args.config).read_text(encoding="utf-8"))
    counts = scan(Path(args.root), config)
    if args.report:
        Path(args.report).write_text(report(config, counts), encoding="utf-8")
    for name, per_file in counts.items():
        print(f"{name}: {sum(per_file.values())} hits in {len(per_file)} files")

    if not args.baseline:
        return 0
    path = Path(args.baseline)
    if args.update or not path.exists():
        path.write_text(json.dumps(counts, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"baseline written: {path}")
        return 0
    worse, better = ratchet(counts, json.loads(path.read_text(encoding="utf-8")))
    for line in better:
        print(f"better (lower the baseline with --update): {line}")
    for line in worse:
        print(f"WORSE: {line}", file=sys.stderr)
    return 1 if worse else 0


if __name__ == "__main__":
    sys.exit(main())
