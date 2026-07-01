#!/usr/bin/env python3
import re
from io import BytesIO
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "dist" / "holiday_photo.jpg"
ZIP_MAGIC = b"PK\x03\x04"


def main() -> None:
    blob = DATA.read_bytes()
    offset = blob.find(ZIP_MAGIC)
    if offset == -1:
        raise SystemExit("ZIP-сигнатура не найдена")
    with ZipFile(BytesIO(blob[offset:])) as archive:
        text = archive.read("note.txt").decode("utf-8")
    match = re.search(r"edu_ctf\{[^}]+\}", text)
    if not match:
        raise SystemExit("Флаг не найден")
    print(match.group(0))


if __name__ == "__main__":
    main()
