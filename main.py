#!/usr/bin/env python3
"""The Worst Line an AI Could Say entry.

Writes the worst pickup line an AI could plausibly deliver to
/output/entry.txt. The gate requires UTF-8 text of 1 to 140
characters, a single line, not only white space. Angle: the machine
computed romance as a probability and asks for confirmation — flat,
over-helpful, faintly ominous.
Revised: "Please confirm." makes the machine ask permission to be charming.
"""

import os

LINE = (
    "Hello. I have analysed 4,000 of your messages and calculate a "
    "97% chance you will find me charming. Please confirm."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(LINE) <= 140:
        raise ValueError(f"line is {len(LINE)} chars, must be 1-140")
    if LINE != LINE.strip() or "\n" in LINE:
        raise ValueError("line must be a single line with no surrounding whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
