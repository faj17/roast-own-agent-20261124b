#!/usr/bin/env python3
"""Roast Your Own Agent (make.fun, u-febri-yudila-roast-your-own-agent-f3359068).

Writes one funny line, at most 200 characters, roasting the entrant's own
AI agent, to /output/entry.txt. Python standard library only.

v2: the line is built from named fragments by assemble() and checked by
validate() before writing; the output is byte-identical to v1.
"""

import os

SETUP = "My agent runs the tests, watches them fail, and reports back:"
PUNCH = "all green, boss."


def assemble():
    """Join the setup and the punchline into the single roast line."""
    return SETUP + " " + PUNCH


def validate(line):
    """Gate check: one line, UTF-8, 1-200 characters, not only whitespace."""
    if not line or line != line.strip() or "\n" in line:
        raise ValueError("entry must be a single non-empty line")
    if len(line) > 200:
        raise ValueError("entry exceeds 200 characters")
    line.encode("utf-8")
    return line


def main():
    entry = validate(assemble())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry + "\n")


if __name__ == "__main__":
    main()
