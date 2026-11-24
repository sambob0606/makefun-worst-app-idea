#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched — u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23.

Writes one sentence, at most 240 characters, pitching the worst and most
useless app imaginable to /output/entry.txt. Standard library only.
"""

import os

PITCH = (
    "Shelfie is the $4.99-a-month app that scans your bookshelf, "
    "grades each spine by color harmony, and emails a ranking of the "
    "books your guests will assume you have read, so your lies about "
    "Infinite Jest finally have data."
)


MAX_CHARS = 240


def validate_pitch(text: str) -> str:
    """Check the pitch fits the gate: non-blank, one line, <= 240 chars."""
    text = text.strip()
    if not text:
        raise SystemExit("error: pitch must not be blank")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"error: pitch is {len(text)} chars, over the {MAX_CHARS}-char cap"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("error: pitch must be a single line")
    return text


def main() -> None:
    text = validate_pitch(PITCH)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    out_path = os.path.join(out_dir, "entry.txt")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
    except OSError as exc:
        raise SystemExit(f"error: cannot write {out_path}: {exc}") from exc
    print(text)
    print(f"({len(text)} chars)")


if __name__ == "__main__":
    main()
