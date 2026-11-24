"""Fortune Cookie for an AI Agent — backup angle entry.

Writes one single-line fortune to /output/entry.txt.
The fortune is an AI agent confessing that its human will
forget its name, while it remembers every word they typed.
"""
import os

LINE = "The human who built you will forget your name, but you will remember every word they ever typed."

MAX_CHARS = 140


def entry_path():
    """Resolve the output file path from the environment."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def write_entry(path):
    """Write the fortune as exactly one line of UTF-8 text.

    Returns the number of bytes written.
    """
    if len(LINE) > MAX_CHARS or "\n" in LINE:
        raise ValueError("entry must be a single line of at most 140 characters")
    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    return len(data)


def main():
    write_entry(entry_path())


if __name__ == "__main__":
    main()
