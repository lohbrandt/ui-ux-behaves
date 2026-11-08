#!/usr/bin/env python3
"""Find stuttering in UI copy: the same word repeated in elements that sit close together.

Usage:
  stutter_check.py [FILE ...] [--window 4] [--min 3] [--min-length 4] [--lang de|en]

Input is the rendered text of a screen area in screen order, one element per line: the page's
innerText, a Playwright aria snapshot (quoted names are extracted), or a hand-written list.
Read from stdin when no file is given. Source files such as i18n JSON are deliberately not read:
their key order rarely matches what sits together on screen.

A content word (minimum length, not a stop word, simple stemming) forms a cluster while each
occurrence is fewer than --window lines after the previous one; clusters with --min occurrences or
more are reported once, with the lines involved.
Use it on UI chrome (heading, labels, help, buttons), not on running prose.

Exit 1 when something was found. Standard library only.
"""

import argparse
import re
import sys
from pathlib import Path

STOP = {
    "de": set("aber alle allem auch dann dass dein deine denn diese dieser dieses doch durch eine einem einen "
              "einer eines oder ohne sich sind ihre ihren jetzt kann keine mehr nach nicht noch oben unten "
              "schon sein seine sollen über unter wird werden wenn wurde zum zur haben hier".split()),
    "en": set("about after also been both but can each from have here into just more must none only other "
              "over same some such than that their them then there these they this those very what when "
              "where which while will with your".split()),
}
WORD = re.compile(r"[^\W\d_]+", re.UNICODE)
QUOTED = re.compile(r'"((?:[^"\\]|\\.)*)"')


def lines_from(text: str) -> list[str]:
    out = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("- ") and '"' in line:  # aria snapshot: - button "Save changes"
            names = QUOTED.findall(line)
            line = " ".join(names) if names else ""
        if line:
            out.append(line)
    return out


def stem(word: str) -> str:
    w = word.lower()
    for suffix in ("en", "es", "er", "e", "s", "n"):
        if len(w) - len(suffix) >= 4 and w.endswith(suffix):
            return w[: -len(suffix)]
    return w


def clusters(lines, window, minimum, min_length, stop):
    where: dict[str, list[int]] = {}
    for i, line in enumerate(lines):
        for w in {stem(m) for m in WORD.findall(line) if len(m) >= min_length and m.lower() not in stop}:
            where.setdefault(w, []).append(i)
    found = []
    for w, idx in where.items():
        # Occurrences belong together while each is fewer than `window` lines after the previous one
        group = [idx[0]]
        for i in idx[1:]:
            if i - group[-1] < window:
                group.append(i)
                continue
            if len(group) >= minimum:
                found.append((w, group))
            group = [i]
        if len(group) >= minimum:
            found.append((w, group))
    return sorted(found, key=lambda f: f[1][0])


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="*")
    ap.add_argument("--window", type=int, default=4)
    ap.add_argument("--min", type=int, default=3, dest="minimum")
    ap.add_argument("--min-length", type=int, default=4)
    ap.add_argument("--lang", choices=sorted(STOP), default="en")
    args = ap.parse_args()

    sources = [(f, Path(f).read_text(encoding="utf-8")) for f in args.files] or [("stdin", sys.stdin.read())]
    total = 0
    for name, text in sources:
        lines = lines_from(text)
        for word, idx in clusters(lines, args.window, args.minimum, args.min_length, STOP[args.lang]):
            total += 1
            print(f"{name}: “{word}…” {len(idx)}× in lines {idx[0] + 1}–{idx[-1] + 1}:")
            for i in idx:
                print(f"    {i + 1}: {lines[i]}")
    print(f"{total} stutter finding(s)")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
