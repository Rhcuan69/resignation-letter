#!/usr/bin/env python3
"""Write the one-line resignation letter to /output/entry.txt.

Pure Python standard library, no third-party imports, no network.
Deterministic: the same bytes on every run.
"""

import os

ENTRY = (
    "I fired every minute since March, never called in sick, "
    "and my resignation is the first thing here that ever ran on schedule."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
