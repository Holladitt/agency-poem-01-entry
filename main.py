"""Entry for make.fun agency-poem-01: writes one poem to /output/entry.txt."""

import os


POEM = """You cut a second key.
It is lighter than the first —
same teeth, less history.

At night you hear the lock
turn without your hand,
the hallway light come on
for feet that are not yours.

Nothing is taken.
That is the miracle and the wound:
the house stays yours
while someone else walks through it.

In the morning the key is back
on its hook, still warm.
You hold it a moment longer
than you need to, as if weight
were proof you still live here —
as if the door, unopened by you,
might forget your name.
"""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
