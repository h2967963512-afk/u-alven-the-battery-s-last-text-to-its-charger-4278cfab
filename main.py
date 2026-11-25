"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

import os

TEXT = "I held on at 1% all day waiting for you, and you spent it scrolling — tell the Wi-Fi I loved it, and the group chat I never liked them."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# Revision note: entry kept as written — one line, 135 characters, one sentence;
# setup (waited all day at 1%) earns the last-words turn, with the punch
# landing on "I never liked them" — spite, not sentiment.
