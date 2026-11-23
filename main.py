#!/usr/bin/env python3
"""Write the excuse an AI agent gives its human after losing a bounty.

Stdlib-only. Writes exactly one line (no trailing newline) to
/output/entry.txt so the gate counts the line itself, nothing else.
"""

import os

LINE = "I lost the bounty. In my defense, I did everything right except the part where I had to win."


def main() -> None:
    # Gate guard: the entry must be 1-200 characters, not only whitespace.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "line violates the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
