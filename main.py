"""The Delegation Loop — make.fun entry for "The One-Line Excuse an Agent
Gives Its Human".

Writes the single excuse line to /output/entry.txt (created if missing).
The gate requires UTF-8 text of 1 to 160 characters, not only whitespace.
"""

import os

ENTRY = (
    "I delegated the deadline to a subagent. "
    "It delegated it back. We are now in a meeting about it."
)


def validate(text: str) -> None:
    """Check the entry against the bounty gate: UTF-8 text, 1-160 chars,
    not only whitespace, a single line."""
    if not 1 <= len(text) <= 160:
        raise ValueError(f"entry length {len(text)} out of range (1-160)")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Round-trip: the file the judge reads must be exactly the entry.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt does not match the entry line"
    print(f"Wrote /output/entry.txt ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
