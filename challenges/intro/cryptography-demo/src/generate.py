#!/usr/bin/env python3
from pathlib import Path

FLAG = 'edu_ctf{crypto_demo_shift}'
SHIFT = 3
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist" / 'message.txt'


def caesar(text: str, shift: int) -> str:
    result = []
    for ch in text:
        if "a" <= ch <= "z":
            result.append(chr((ord(ch) - ord("a") + shift) % 26 + ord("a")))
        elif "A" <= ch <= "Z":
            result.append(chr((ord(ch) - ord("A") + shift) % 26 + ord("A")))
        else:
            result.append(ch)
    return "".join(result)


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(caesar(FLAG, SHIFT) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
