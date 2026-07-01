#!/usr/bin/env python3
from pathlib import Path
import py_compile
import tempfile

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
XOR_KEY = 41
SHIFT = 3

SOURCE_TEMPLATE = """DATA = {data_tuple}
XOR_KEY = {xor_key}
SHIFT = {shift}
PARAMS = ({xor_key}, {shift})


def check(candidate):
    transformed = []
    for char in candidate[::-1]:
        transformed.append((ord(char) ^ XOR_KEY) + SHIFT)
    return transformed == DATA


def main():
    value = input("Введите флаг: ").strip()
    print("Верно" if check(value) else "Неверно")


if __name__ == "__main__":
    main()
"""

def main() -> int:
    flag = (ROOT / "flag.txt").read_text(encoding="utf-8").strip()
    data = [(ord(ch) ^ XOR_KEY) + SHIFT for ch in flag[::-1]]
    DIST.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        source_path = Path(tmp) / "lockbox_source.py"
        source_path.write_text(SOURCE_TEMPLATE.format(data_tuple=tuple(data), xor_key=XOR_KEY, shift=SHIFT), encoding="utf-8")
        py_compile.compile(str(source_path), cfile=str(DIST / "lockbox.pyc"), doraise=True)
    print(DIST / "lockbox.pyc")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
