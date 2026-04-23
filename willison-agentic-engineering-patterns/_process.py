#!/usr/bin/env python3
"""Clean defuddle markdown -> vault-ready chapters.

Usage: ./_process.py <raw_dir> <dst_dir>

Reads <raw_dir>/<slug>.md for every slug in ORDER, writes
<dst_dir>/NN-<slug>.md with vault frontmatter, attribution callout,
and wikilink nav. Called by _refresh.sh.
"""
import datetime as _dt
import re
import sys
from pathlib import Path

ORDER = [
    ("what-is-agentic-engineering", "01", "Principles"),
    ("code-is-cheap", "02", "Principles"),
    ("hoard-things-you-know-how-to-do", "03", "Principles"),
    ("better-code", "04", "Principles"),
    ("anti-patterns", "05", "Principles"),
    ("how-coding-agents-work", "06", "Working with coding agents"),
    ("using-git-with-coding-agents", "07", "Working with coding agents"),
    ("subagents", "08", "Working with coding agents"),
    ("red-green-tdd", "09", "Testing and QA"),
    ("first-run-the-tests", "10", "Testing and QA"),
    ("agentic-manual-testing", "11", "Testing and QA"),
    ("linear-walkthroughs", "12", "Understanding code"),
    ("interactive-explanations", "13", "Understanding code"),
    ("gif-optimization", "14", "Annotated prompts"),
    ("adding-a-new-content-type", "15", "Annotated prompts"),
    ("prompts", "16", "Appendix"),
]
SLUG_TO_IDX = {s: i for i, (s, _, _) in enumerate(ORDER)}
BASE = "https://simonwillison.net/guides/agentic-engineering-patterns"


def clean(raw: str):
    lines = raw.splitlines()

    while lines and (lines[0].strip() == "" or lines[0].startswith("[Guides]")):
        lines.pop(0)

    for i, ln in enumerate(lines):
        if ln.startswith("## "):
            lines = lines[i:]
            break

    created = modified = None
    for ln in lines:
        m = re.match(r"Created:\s*(.+?)\s*$", ln)
        if m:
            created = m.group(1).strip()
        m = re.match(r"Last modified:\s*(.+?)\s*$", ln)
        if m:
            modified = m.group(1).strip()

    cut = len(lines)
    for i, ln in enumerate(lines):
        if (
            "This is a chapter from the guide" in ln
            or "**Chapters in this guide**" in ln
        ):
            cut = i
            break
    body = "\n".join(lines[:cut]).rstrip()

    body = re.sub(
        r"\n+(?:←\s*\[.*?\]\(.*?\)\s*\n*)+(?:\[.*?\]\(.*?\)\s*→\s*)?\s*$",
        "\n",
        body,
        flags=re.MULTILINE,
    )
    body = re.sub(r"\n+\[.*?\]\(.*?\)\s*→\s*$", "\n", body, flags=re.MULTILINE)

    def repl(m):
        text, slug_ref = m.group(1), m.group(2)
        if slug_ref in SLUG_TO_IDX:
            prefix = ORDER[SLUG_TO_IDX[slug_ref]][1]
            return f"[[{prefix}-{slug_ref}|{text}]]"
        return m.group(0)

    body = re.sub(
        r"\[([^\]]+)\]\(/guides/agentic-engineering-patterns/([a-z0-9-]+)/\)",
        repl,
        body,
    )
    body = re.sub(
        r"\]\((/[^)]+)\)",
        lambda m: f"](https://simonwillison.net{m.group(1)})",
        body,
    )

    return body.strip() + "\n", created, modified


def main():
    if len(sys.argv) != 3:
        print("usage: _process.py <raw_dir> <dst_dir>", file=sys.stderr)
        sys.exit(2)

    raw_dir = Path(sys.argv[1])
    dst = Path(sys.argv[2])
    dst.mkdir(parents=True, exist_ok=True)
    today = _dt.date.today().isoformat()

    for slug, idx, section in ORDER:
        src = raw_dir / f"{slug}.md"
        if not src.exists():
            print(f"skip {slug}: no source", file=sys.stderr)
            continue
        body, created, modified = clean(src.read_text())
        i = SLUG_TO_IDX[slug]

        prev_link = None
        next_link = None
        if i > 0:
            ps, pi, _ = ORDER[i - 1]
            prev_link = f"[[{pi}-{ps}|← {ps}]]"
        if i < len(ORDER) - 1:
            ns, ni, _ = ORDER[i + 1]
            next_link = f"[[{ni}-{ns}|{ns} →]]"

        fm = [
            "---",
            f"date: {today}",
            f"source: {BASE}/{slug}/",
            "author: Simon Willison",
            "tags: [agentic-engineering, claude-code, llm, clipping, willison]",
            f"chapter: {int(idx)}",
            f'section: "{section}"',
        ]
        if created:
            fm.append(f'created: "{created}"')
        if modified:
            fm.append(f'modified: "{modified}"')
        fm.append("---")

        nav = " · ".join(x for x in [prev_link, "[[index|index]]", next_link] if x)

        out = (
            "\n".join(fm)
            + "\n\n"
            + f"> [!info] From Simon Willison's *Agentic Engineering Patterns* guide. Source: {BASE}/{slug}/\n\n"
            + body
            + "\n---\n\n"
            + nav
            + "\n"
        )
        (dst / f"{idx}-{slug}.md").write_text(out)
        print(f"wrote {idx}-{slug}.md")


if __name__ == "__main__":
    main()
