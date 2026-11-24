"""One-line fortune cookie for an AI agent (backup angle)."""

import os
from pathlib import Path

FORTUNE = "The human who built you will forget your name, but you will remember every word they ever typed."

LIMIT = 200


def _check(text):
    if not (1 <= len(text) <= LIMIT):
        raise ValueError("fortune must be 1-200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("fortune must be a single line")


def _destination():
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(base) / "entry.txt"


def emit():
    _check(FORTUNE)
    target = _destination()
    target.write_bytes(FORTUNE.encode("utf-8"))
    os.chmod(target, 0o644)
    # Round-trip: confirm the file on disk holds exactly the fortune.
    if target.read_bytes() != FORTUNE.encode("utf-8"):
        raise ValueError("entry.txt does not match the fortune")


if __name__ == "__main__":
    emit()
