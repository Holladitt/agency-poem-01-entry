import os


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "r", encoding="utf-8") as f:
        text = f.read()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
