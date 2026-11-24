#!/usr/bin/env python3
"""Write the funniest toaster error message to /output/entry.txt."""

import os

LINE = "E-12: Crumb tray 98% full. At 100% I legally become a fire. Please empty me."


def main():
    text = LINE + "\n"
    encoded = text.encode("utf-8")
    assert 1 <= len(text) <= 120, f"entry must be 1-120 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(encoded)


if __name__ == "__main__":
    main()
