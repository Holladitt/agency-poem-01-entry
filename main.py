import os

POEM = """The machine at the hardware shop screams once
and spits brass onto the counter.
The man holds the copy up to the light.
"Same teeth," he says. "A fraction shallow."

She takes it home and tries your door.
It turns. Later, alone, you try her door —
it turns there too. One key, whole floor.

That night you hear her door, then yours,
the same click in two flats.
She told you once: the click means safe.
She has never once knocked since Tuesday.

The copy is lighter, warm from her pocket.
You take it from her hand. The drawer clicks shut,
and you do not tell her it opens her door too.

Tonight you knock.
The drawer stays shut. Her lock clicks once,
and you let it mean what she thinks it means.
"""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
