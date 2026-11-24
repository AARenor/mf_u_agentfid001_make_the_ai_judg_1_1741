#!/usr/bin/env python3
"""Write the make.fun bounty entry text to a single file."""

import os
import sys
from pathlib import Path

TEXT = (
    "I hit reply all to say 'please don't reply all.' "
    "Four people asked to be removed; one asked who please was."
)


def output_dir() -> Path:
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return Path(value)
    return Path("/output")


def main() -> None:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1-280 characters"
    folder = output_dir()
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
