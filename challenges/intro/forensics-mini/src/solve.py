#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "dist" / "artifact.bin"


def main() -> None:
    match = re.search(rb"edu_ctf\{[^}]+\}", DATA.read_bytes())
    if not match:
        raise SystemExit("Флаг не найден")
    print(match.group(0).decode("ascii"))


if __name__ == "__main__":
    main()
