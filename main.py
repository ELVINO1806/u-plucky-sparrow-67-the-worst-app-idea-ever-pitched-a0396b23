#!/usr/bin/env python3
"""Entry for make.fun: The Worst App Idea Ever Pitched.

Writes the one-sentence pitch to /output/entry.txt, exactly, with no
trailing newline. Deterministic, standard library only, no network.
"""

import os

ENTRY = (
    "MoodRing for Toasters: an app that reads your toaster's emotional "
    "state each morning and texts your bread a personalised apology "
    "before it burns."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
