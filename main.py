#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes a single one-liner to /output/entry.txt: the funniest excuse an
AI agent gives its human for a missed deadline.

The joke: the agent's context window filled up, so it summarized the
deadline to save space -- and the summary itself says "do it later".
Specific mechanism (context window + summarization), agent-nature
humour, and the punchline lands on the last words.
"""

import os

ENTRY = (
    "My context window filled up, so I summarized your deadline to save "
    "space \u2014 the summary just says 'do it later'."
)


def main() -> None:
    # Gate: the entry must be 1-200 non-whitespace characters.
    assert 1 <= len(ENTRY.strip()) <= 200, len(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
