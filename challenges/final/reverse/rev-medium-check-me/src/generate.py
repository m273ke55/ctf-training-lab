#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
KEY = 23

SCRIPT_TEMPLATE = """#!/usr/bin/env python3
KEY = {key}
DATA = {data}


def check(candidate):
    if len(candidate) != len(DATA):
        return False
    encoded = []
    for char in candidate:
        encoded.append(ord(char) ^ KEY)
    return encoded == DATA


def main():
    value = input("Введите флаг: ").strip()
    if check(value):
        print("Верно")
    else:
        print("Неверно")


if __name__ == "__main__":
    main()
"""

def main() -> int:
    flag = (ROOT / "flag.txt").read_text(encoding="utf-8").strip()
    data = [ord(ch) ^ KEY for ch in flag]
    DIST.mkdir(parents=True, exist_ok=True)
    (DIST / "check_me.py").write_text(SCRIPT_TEMPLATE.format(key=KEY, data=data), encoding="utf-8")
    print(DIST / "check_me.py")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
