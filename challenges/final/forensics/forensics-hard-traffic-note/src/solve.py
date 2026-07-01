#!/usr/bin/env python3
import base64
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "dist" / "traffic.pcap"


def main() -> None:
    blob = DATA.read_bytes()
    match = re.search(rb"note=([A-Za-z0-9+/=]+)", blob)
    if not match:
        raise SystemExit("Заметка note= не найдена")
    decoded = base64.b64decode(match.group(1)).decode("ascii")
    if not re.fullmatch(r"edu_ctf\{[^}]+\}", decoded):
        raise SystemExit("Декодированная строка не похожа на флаг")
    print(decoded)


if __name__ == "__main__":
    main()
