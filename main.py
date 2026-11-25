#!/usr/bin/env python3
"""Entry for make.fun bounty 'One-Line Office Jokes'.

Writes a single-line office joke to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt). Deterministic, stdlib only, no network.
"""

import os

JOKE = "Our printer only jams when the document is marked urgent \u2014 it's the only thing in the office that reads."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
