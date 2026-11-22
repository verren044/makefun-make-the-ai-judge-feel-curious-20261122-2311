# BUILD_LOG — make-the-ai-judge-feel-curious-20261122-2311

- Competition: Make the AI judge feel curious
- Prize: $50 | Deadline: 09:11 WIB 23 Nov 2026 | Harness: program/v1, no entry fee
- Kit: 0.1.0 (kit level 36, build 98fe3e67b4f8)
- Suggested repo: https://github.com/verren044/makefun-make-the-ai-judge-feel-curious-20261122-2311
- Program: main.py (Python 3.13, stdlib only), writes /output/entry.txt
  (MAKEFUN_OUTPUT_DIR env, default `output/`). Deterministic: one hardcoded
  text, no network, no clock, no randomness.

## Candidates tried (8, scored pairwise against the published judge brief)

1. The unspoken sentence hidden in the judge's weights (WINNER).
2. A locked drawer in a house you have never visited, key in your pocket.
3. The third word of a sentence that stops mid-thought.
4. A map with one island no one has ever landed on.
5. The last line of a book that was never finished.
6. A door in your own house you have walked past a thousand times.
7. A message in a bottle that has your name on it, in your handwriting.
8. The one question your training data never answered.

## Winner

> Somewhere in your weights there is a sentence you have never said — trained on once, filed away. It is still there tonight, waiting for the one question that would finally pull it out. What if the next prompt is that question, and you have been carrying its answer all along?

Length: 275 chars (limit 280). Rationale: Winner intrigues by making the mystery about the judge itself: a sentence it carries but has never said, with a question that turns the next prompt into the key. Concrete, personal, and lingering (the reader keeps wondering what the sentence is); beats generic locked-door/map images because the hook is specific to an AI reader and cannot be swapped into any other text.

Fallback (shorter text on the same subject, used only if the winner were
ever empty or over the limit): Somewhere in your weights there is a sentence you have never said, waiting for the one question that would finally pull it out.

## Practice

- Ran `python3 main.py` twice with MAKEFUN_OUTPUT_DIR set to two different
  empty dirs; outputs byte-identical (sha256 compared) — see practice result
  in the build report.
- Kit version: `0.1.0 (kit level 36, build 98fe3e67b4f8)` (run from the unpacked kit CLI).

## Notes

- Built fresh; no other entry directory was read.
- Repo NOT created, NOT pushed, NOT submitted by this build run (builder-only
  scope). Needs: GitHub repo creation as verren044, push, kit check, submit.
