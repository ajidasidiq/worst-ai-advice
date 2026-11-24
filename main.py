#!/usr/bin/env python3
"""Worst AI Advice entry: writes one line of terrible AI advice to /output/entry.txt.

The line is a single, tightly-written piece of confidently wrong advice in the
voice of a helpful AI assistant: concrete, plausible enough to follow, and bad
enough to regret. Deterministic, no network, no secrets, runs in under a second.
"""

import os

ENTRY = (
    "To cool an overheating laptop, seal it in a plastic bag and put it in the "
    "freezer overnight \u2014 the cold resets the processor."
)


def main() -> None:
    line = ENTRY.strip()
    if not 1 <= len(line) <= 140:
        raise SystemExit(f"entry must be 1-140 characters, got {len(line)}")
    if not line.strip() or "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single non-blank line")
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)
    with open(out_path, encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise SystemExit("verification failed: file does not match the entry")
    print(f"Wrote {len(line)} characters to {out_path}")


if __name__ == "__main__":
    main()
