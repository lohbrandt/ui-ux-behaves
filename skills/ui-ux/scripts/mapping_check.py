#!/usr/bin/env python3
"""Check that a design-system mapping covers every behave key exactly once.

Usage:
  mapping_check.py MAPPING.md [--catalog behave-catalog.md]

Both files hold a table between `<!-- behave-keys:start -->` and `<!-- behave-keys:end -->` whose
first column is the key in backticks. Reports keys missing from the mapping, keys the catalog does
not know, duplicates, and mapping rows whose component column is still empty.
Exit 1 on any difference. Standard library only.
"""

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

ROW = re.compile(r"^\|\s*`([a-zA-Z.]+)`\s*\|(.*)$", re.M)


def rows(path: Path) -> list[tuple[str, str]]:
    text = path.read_text(encoding="utf-8")
    try:
        block = text.split("behave-keys:start", 1)[1].split("behave-keys:end", 1)[0]
    except IndexError:
        sys.exit(f"{path}: no behave-keys block")
    return [(k, rest.split("|")[0].strip()) for k, rest in ROW.findall(block)]


def main() -> int:
    here = Path(__file__).resolve().parent.parent / "references" / "behave-catalog.md"
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mapping")
    ap.add_argument("--catalog", default=str(here))
    args = ap.parse_args()
    if not Path(args.catalog).is_file():
        ap.error(f"catalog not found: {args.catalog} (pass --catalog path/to/behave-catalog.md)")

    catalog = [k for k, _ in rows(Path(args.catalog))]
    mapping = rows(Path(args.mapping))
    keys = [k for k, _ in mapping]
    problems = []
    problems += [f"missing in mapping: `{k}`" for k in catalog if k not in keys]
    problems += [f"unknown key (not in catalog): `{k}`" for k in keys if k not in catalog]
    problems += [f"duplicate: `{k}` ({n}×)" for k, n in Counter(keys).items() if n > 1]
    empty = [k for k, component in mapping if not component]
    for line in problems:
        print(line)
    if empty:
        print(f"{len(empty)} key(s) without a component yet: " + ", ".join(f"`{k}`" for k in empty))
    print(f"{len(catalog)} catalog keys, {len(keys)} mapping rows, {len(problems)} problem(s)")
    return 1 if problems or empty else 0


if __name__ == "__main__":
    sys.exit(main())
