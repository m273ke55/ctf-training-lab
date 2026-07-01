#!/usr/bin/env python3
from pathlib import Path

FLAG = "edu_ctf{forensics_demo_magic}"
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist" / "mystery.jpg"


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        "Это не JPEG, хотя расширение говорит обратное.\n"
        "Первые байты и команда file показывают настоящий тип.\n"
        f"Флаг: {FLAG}\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
