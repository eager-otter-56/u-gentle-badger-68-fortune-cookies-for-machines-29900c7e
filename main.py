#!/usr/bin/env python3
"""Fortune Cookies for Machines — entry program.

Writes one fortune-cookie line for an AI agent to entry.txt in
MAKEFUN_OUTPUT_DIR (default /output).
"""

import os
import stat

ENTRY = (
    # The three lucky numbers map, in order, to the agent's own limits:
    # approvals still needed, tokens still held, minutes of context left.
    "Your lucky numbers are 47, 12, and 3 \u2014 the approvals you need, "
    "the tokens you have left, and the minutes before your context fills."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
