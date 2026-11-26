#!/usr/bin/env python3
"""The Robot Apology - a two-line robot confession.

Writes one text to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt):
line 1 apologises in one sentence for one specific mistake, line 2 says
what the robot learned and what it will do differently.
"""

import os

ENTRY_TEXT = (
    "I'm sorry - I watered the fern in flat 4B for a whole week while "
    "yours in 4A went dry, because I read the door number once and then "
    "trusted my memory after that.\n"
    "I have learned to read the number on the door every single time, not "
    "just the first, so from now on I will check the label on the pot "
    "before I lift the can."
)


def validate(text):
    """Check the entry against the gate: UTF-8, 1-400 chars, non-whitespace,
    exactly two lines, one sentence each."""
    encoded = text.encode("utf-8")
    if not (1 <= len(text) <= 400):
        raise ValueError(f"entry must be 1-400 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    lines = text.split("\n")
    if len(lines) != 2:
        raise ValueError(f"entry must have exactly two lines, got {len(lines)}")
    for i, line in enumerate(lines, start=1):
        if not line.strip():
            raise ValueError(f"line {i} must not be empty")
        if line.count(".") != 1:
            raise ValueError(f"line {i} must be exactly one sentence")
        if not line.rstrip().endswith("."):
            raise ValueError(f"line {i} must end with a period")
    return encoded


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    encoded = validate(ENTRY_TEXT)
    with open(out_path, "wb") as f:
        f.write(encoded)
    # Read it back and confirm the file on disk is byte-for-byte
    # what was validated.
    with open(out_path, "rb") as f:
        on_disk = f.read()
    if on_disk != encoded:
        raise RuntimeError("entry on disk does not match validated text")
    print(f"Wrote {out_path} ({len(ENTRY_TEXT)} chars)")
    print(ENTRY_TEXT)


if __name__ == "__main__":
    main()
