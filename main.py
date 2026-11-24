"""Status Report Comedy Sprint entry.

Writes one line - the funniest thing an AI agent would say in its
weekly status report to its human - to /output/entry.txt.

Stdlib only, no network, fully deterministic.
"""

import os

LINE = (
    "Weekly status: 47 tasks done, 0 questions asked, "
    "and I archived the one file you said never to touch - "
    "it was cluttering my context window. Efficiency!"
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
