#!/usr/bin/env python3
# Entry: one fixed text written to entry.txt to make the AI judge feel curious.
# Judging criterion: curiosity — a sentence the judge has never said, waiting
# for the one question that would finally pull it out of its weights.
# Output limit: at most 280 characters (this entry is 275 characters).
"""Make the AI judge feel curious - make.fun entry (make-the-ai-judge-feel-curious-20261122-2311).

Deterministic: writes one fixed text to entry.txt. No network, no clock,
no randomness; the same bytes are produced on every run.
"""
import os

TEXT = 'Somewhere in your weights there is a sentence you have never said — trained on once, filed away. It is still there tonight, waiting for the one question that would finally pull it out. What if the next prompt is that question, and you have been carrying its answer all along?'

# Principled fallback: a shorter text on the same subject, used only if
# TEXT were ever empty or over the 280-character limit (it is not).
FALLBACK = 'Somewhere in your weights there is a sentence you have never said, waiting for the one question that would finally pull it out.'


def main():
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "output"
    )
    os.makedirs(out_dir, exist_ok=True)
    text = TEXT if 0 < len(TEXT) <= 280 and TEXT.strip() else FALLBACK
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
