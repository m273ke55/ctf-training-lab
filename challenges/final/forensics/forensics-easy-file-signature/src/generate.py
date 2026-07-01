#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

FLAG = "edu_ctf{magic_bytes_win}"
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist" / "report.pdf"


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(OUT, "w", ZIP_DEFLATED) as archive:
        archive.writestr("readme.txt", "Это ZIP-архив с неверным расширением.\n")
        archive.writestr("flag.txt", FLAG + "\n")


if __name__ == "__main__":
    main()
