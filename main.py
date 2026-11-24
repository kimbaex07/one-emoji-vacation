#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — write the chosen emoji to entry.txt.

The entry is exactly one emoji: Mount Fuji (U+1F5FB). The program validates
it first (exactly one character, one emoji, not whitespace, within the
1-8 character gate) and then writes it, with no trailing newline, to
$MAKEFUN_OUTPUT_DIR/entry.txt — or /output/entry.txt when the variable is
unset — mode 0644 under umask 022. A local output/ directory next to this
script is used only as a fallback if the primary directory cannot be
written, and only inside the except handler, never before the primary dir.

Pure Python standard library only; no third-party imports.
"""

import os
import sys

EMOJI = "\U0001F5FB"  # 🗻 MOUNT FUJI — the dream vacation in one character.


def _is_single_emoji(text):
    """True when text is exactly one emoji character."""
    if len(text) != 1 or text.isspace():
        return False
    code = ord(text)
    return (
        0x1F000 <= code <= 0x1FAFF  # emoticons, pictographs, transport, etc.
        or 0x2600 <= code <= 0x27BF  # miscellaneous symbols and dingbats
        or 0x2B00 <= code <= 0x2BFF  # miscellaneous symbols and arrows
        or 0x2194 <= code <= 0x21AA  # arrows
        or 0xFE00 <= code <= 0xFE0F  # variation selectors
    )


def _write_entry(path, data):
    with open(path, "wb") as handle:
        handle.write(data)
    os.chmod(path, 0o644)


def main():
    os.umask(0o022)
    if not _is_single_emoji(EMOJI):
        print("entry must be exactly one emoji (1-8 chars)", file=sys.stderr)
        return 1
    data = EMOJI.encode("utf-8")
    primary_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    primary_path = os.path.join(primary_dir, "entry.txt")
    try:
        os.makedirs(primary_dir, exist_ok=True)
        _write_entry(primary_path, data)
        return 0
    except OSError as exc:
        here = os.path.dirname(os.path.abspath(__file__))
        fallback_dir = os.path.join(here, "output")
        fallback_path = os.path.join(fallback_dir, "entry.txt")
        try:
            os.makedirs(fallback_dir, exist_ok=True)
            _write_entry(fallback_path, data)
        except OSError as exc2:
            print("cannot write entry.txt: %s / %s" % (exc, exc2),
                  file=sys.stderr)
            return 1
        print("primary output dir failed (%s); wrote %s" % (exc, fallback_path),
              file=sys.stderr)
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
