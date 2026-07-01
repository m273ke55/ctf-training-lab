#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CIPHERTEXT = (ROOT / "dist" / 'ciphertext.txt').read_text(encoding="utf-8").strip()


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
    for shift in range(26):
        candidate = caesar(CIPHERTEXT, -shift)
        if candidate.startswith("edu_ctf{") and candidate.endswith("}"):
            print(candidate)
            return
    raise SystemExit("flag was not found")


if __name__ == "__main__":
    main()
