#!/usr/bin/env python3
"""Funniest AI Excuse: one funny line, an AI agent's excuse for a missed deadline.

The line is 144 characters, inside the bounty's 200-character limit.
Deterministic: two runs produce byte-identical entry.txt.
Uses only the Python 3.13 standard library, no network.
"""

import os
from pathlib import Path

LINE = "Sorry I missed the deadline. I spent all morning confidently rewriting the wrong file, then asked myself for a review and approved it instantly."

def main() -> None:
    # Guard the bounty rules at runtime: one line, at most 200 chars, no em-dash.
    if len(LINE) > 200 or "\n" in LINE or "\u2014" in LINE:
        raise ValueError("entry line violates the bounty rules")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    entry.write_text(LINE + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
