# Entrypoint for the news-image-20261118 entry.
# The judged artifact is entry.png (1024x1024 PNG, <= 1 MiB): one front
# page summing up Wednesday 18 November 2026 in 38 stories — 13
# illustrated panels, a world map and 25 briefs. The page source is
# index.html. This program copies entry.png into $MAKEFUN_OUTPUT_DIR
# (default /output) and prints a one-line dossier describing the page.
import json
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

COMPETITION = "news-image-20261118"
DATE = "2026-11-18"
STORIES = 38
ILLUSTRATED = 13
CONTINENTS = 6


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(OUT_DIR, "entry.png")
    shutil.copyfile(src, dst)
    dossier = {
        "schema": "makefun/dossier/v1",
        "competition": COMPETITION,
        "date": DATE,
        "stories": STORIES,
        "illustrated": ILLUSTRATED,
        "continents": CONTINENTS,
        "image": "entry.png",
        "bytes": os.path.getsize(dst),
    }
    print(json.dumps(dossier))


if __name__ == "__main__":
    main()
