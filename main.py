"""Loading Screen Gold entry.

Writes a single loading-screen tip (one line of text) to
/output/entry.txt. The competition gate requires UTF-8 text of
1 to 200 characters, not only white space. The program is
deterministic: every run writes exactly the same bytes.

The tip is built from two beats: a shared predicament (developer
and AI agent both stuck watching a spinner, each waiting on the
other) and the turn that reframes the wait as a meeting neither
of them wanted to attend.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200

SETUP = (
    "Tip: Relax \u2014 your AI agent is staring at a spinner too, waiting for you "
    "to approve the fix you asked it for."
)
PUNCHLINE = "You're not blocked. You're in a meeting."


def build_tip() -> str:
    """Assemble the one-line tip from its setup and punchline."""
    return f"{SETUP} {PUNCHLINE}"


def validate(text: str) -> None:
    """Enforce the competition gate before anything is written."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry must be 1..{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    text = build_tip().strip()
    validate(text)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
