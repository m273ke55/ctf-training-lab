#!/usr/bin/env python3
import re
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "dist" / "report.pdf"


def main() -> None:
    with ZipFile(DATA) as archive:
        text = archive.read("flag.txt").decode("utf-8")
    match = re.search(r"edu_ctf\{[^}]+\}", text)
    if not match:
        raise SystemExit("Флаг не найден")
    print(match.group(0))


if __name__ == "__main__":
    main()
