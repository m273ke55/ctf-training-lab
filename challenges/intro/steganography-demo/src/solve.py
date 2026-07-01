#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "dist" / "picture.png"


def main() -> None:
    text = DATA.read_bytes().decode("latin1", errors="ignore")
    match = re.search(r"edu_ctf\{[^}]+\}", text)
    if not match:
        raise SystemExit("Флаг не найден")
    print(match.group(0))


if __name__ == "__main__":
    main()
