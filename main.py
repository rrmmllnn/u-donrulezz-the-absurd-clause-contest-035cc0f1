#!/usr/bin/env python3
"""The Absurd Clause Contest -- entry program.

Writes a single absurd terms-of-service clause to /output/entry.txt.
The clause is one original English sentence of at most 200 characters:
deadpan legal boilerplate that quietly turns absurd.
"""

import os

CLAUSE = (
    "Any dispute arising under these Terms shall be resolved by a single "
    "game of rock-paper-scissors, best of one, witnessed by a notary "
    "public, whose decision is final and binding."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(CLAUSE)


if __name__ == "__main__":
    main()
