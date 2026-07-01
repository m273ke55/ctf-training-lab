#!/usr/bin/env python3
from pathlib import Path
import marshal
import types

ROOT = Path(__file__).resolve().parents[1]
PYC = ROOT / "dist" / "lockbox.pyc"
HEADER_SIZE = 16

def walk_consts(code):
    for const in code.co_consts:
        yield const
        if isinstance(const, types.CodeType):
            yield from walk_consts(const)

def main() -> int:
    code = marshal.loads(PYC.read_bytes()[HEADER_SIZE:])
    consts = list(walk_consts(code))
    data = next(c for c in consts if isinstance(c, (list, tuple)) and len(c) > 10 and all(isinstance(x, int) for x in c))
    params = next(c for c in consts if isinstance(c, tuple) and c == (41, 3))
    xor_key, shift = params
    reversed_flag = "".join(chr((value - shift) ^ xor_key) for value in data)
    print(reversed_flag[::-1])
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
