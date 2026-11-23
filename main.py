"""Dad Joke Showdown entry: one dad joke, written to /output/entry.txt.

The joke: a father names his dog "Five Miles" so he can honestly say he
walks Five Miles every day. The pun lands on the second "Five Miles" and
needs no explanation, which is exactly the groan the judge rewards.
"""

import os

JOKE = "I named my dog Five Miles so I can tell people I walk Five Miles every day."

MIN_CHARS = 1
MAX_CHARS = 200


def validate_entry(text):
    """Enforce the competition gate: 1-200 UTF-8 characters, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")
    return text


def output_path():
    """Resolve the output file, honouring the harness scratch-dir override."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def write_entry(text, path):
    """Write exactly the joke: no trailing newline, no extra whitespace."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main():
    write_entry(validate_entry(JOKE), output_path())


if __name__ == "__main__":
    main()
