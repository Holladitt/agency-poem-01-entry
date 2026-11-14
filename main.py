# Copies the poem stored in entry.txt
# into the output directory the harness provides.
import os


def load_poem():
    folder = os.path.dirname(os.path.abspath(__file__))
    poem_path = os.path.join(folder, "entry.txt")
    with open(poem_path, "r", encoding="utf-8") as handle:
        poem = handle.read()
    return poem


def run():
    poem = load_poem()
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(target_dir, exist_ok=True)
    target_path = os.path.join(target_dir, "entry.txt")
    with open(target_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(poem)


run()
