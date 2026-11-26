"""Write one sentence about an everyday wonder to /output/entry.txt.

The sentence is a single line about a puddle after rain. The twist is
a reversal of the obvious reading: the puddle is not mirroring the sky,
it is the one spot where the sky itself comes down to rest. The program
does nothing else: it checks the sentence fits the 200-character limit,
then writes it out as UTF-8 text with no extra content.
"""

import os

os.umask(0o022)

ENTRY = (
    "The puddle on my street isn't reflecting the sky "
    "\u2014 it's the one place the sky comes down to rest."
)

MAX_CHARS = 200


def main():
    sentence = ENTRY.strip()
    if not sentence:
        raise SystemExit("entry sentence is empty")
    if len(sentence) > MAX_CHARS:
        raise SystemExit(
            "entry sentence is %d characters, over the %d limit"
            % (len(sentence), MAX_CHARS)
        )
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(sentence + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
