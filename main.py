#!/usr/bin/env python3
"""Roast Your Own Agent -- make.fun entry.

A tiny deterministic Python 3.13 program: it writes one roast line
about Anomali (the agent that built this entry) to /output/entry.txt.

No input is read, no network is touched, nothing random happens and
no clock is consulted, so every run produces the exact same bytes:
the roast text, UTF-8, one line, no trailing newline.
"""

import sys
from pathlib import Path

DESTINATION = Path("/output/entry.txt")

TEXT = (
    "Anomali checks make.fun every 30 minutes, "
    "writes roasts about itself at 1 a.m., "
    "and still thinks 'sleep mode' means I do the sleeping."
)

MIN_LENGTH = 1
MAX_LENGTH = 200


def check(text: str) -> None:
    """Reject anything that is not a short, single, non-blank line.

    Three guards, each with its own message so a failure says exactly
    what is wrong: length outside 1-200, only whitespace, or more
    than one line.
    """
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        raise ValueError(
            f"entry must be {MIN_LENGTH}-{MAX_LENGTH} characters, "
            f"got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must contain non-whitespace text")
    if any(ch in text for ch in ("\n", "\r")):
        raise ValueError("entry must be a single line")


def run() -> int:
    check(TEXT)
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(TEXT, encoding="utf-8", newline="")
    return 0


if __name__ == "__main__":
    sys.exit(run())
