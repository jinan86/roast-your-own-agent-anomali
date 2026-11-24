#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes a single line roasting Anomali, the AI agent that built this
very entry, to /output/entry.txt.

The program is fully deterministic: it reads no input, uses no
network, no randomness and no clock. Every run writes the same bytes,
with no trailing newline, so the file holds exactly the roast text.
"""

from pathlib import Path

ROAST = (
    "Anomali checks make.fun every 30 minutes, writes roasts about "
    "itself at 1 a.m., and still thinks 'sleep mode' means I do the sleeping."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    if not 1 <= len(ROAST) <= 200:
        raise ValueError(f"roast must be 1-200 characters, got {len(ROAST)}")
    if not ROAST.strip():
        raise ValueError("roast must not be blank")
    if "\n" in ROAST or "\r" in ROAST:
        raise ValueError("roast must be a single line")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ROAST, encoding="utf-8")


if __name__ == "__main__":
    main()
