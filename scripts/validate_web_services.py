#!/usr/bin/env python3
"""Validate integrated Web challenges without third-party dependencies."""

from __future__ import annotations

import ast
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "challenges/intro/web-demo": ("intro", 0),
    "challenges/final/web/web-easy-method-head": ("easy", 100),
    "challenges/final/web/web-medium-command-injection": ("medium", 200),
    "challenges/final/web/web-hard-upload-include": ("hard-but-fair", 300),
    "challenges/final/web/web-bonus-xxe-docx": ("medium", 200),
}
REQUIRED = ("Dockerfile", "challenge.yml", "challenge.md", "solve.md", "flag.txt")
FLAG_RE = re.compile(r"^edu_ctf\{[a-zA-Z0-9_!?@#.,:+-]+\}$")


def validate_challenge(name: str, difficulty: str, points: int) -> list[str]:
    errors: list[str] = []
    challenge = ROOT / name
    for relative in REQUIRED:
        if not (challenge / relative).is_file():
            errors.append(f"{name}: missing {relative}")
    if not (challenge / "src").is_dir():
        errors.append(f"{name}: missing src directory")

    flag_path = challenge / "flag.txt"
    metadata_path = challenge / "challenge.yml"
    if not flag_path.is_file() or not metadata_path.is_file():
        return errors

    flag = flag_path.read_text(encoding="utf-8").strip()
    metadata = metadata_path.read_text(encoding="utf-8")
    if not FLAG_RE.fullmatch(flag):
        errors.append(f"{name}: invalid flag format")
    checks = {
        "category": "category: Web",
        "difficulty": f"difficulty: {difficulty}",
        "points": f"points: {points}",
        "flag": f"  - {flag}",
        "service port": "  port: 5000",
    }
    for label, needle in checks.items():
        if needle not in metadata:
            errors.append(f"{name}: inconsistent {label} in challenge.yml")
    return errors


def main() -> int:
    errors: list[str] = []
    for name, (difficulty, points) in EXPECTED.items():
        errors.extend(validate_challenge(name, difficulty, points))

    for source in sorted(ROOT.rglob("*.py")):
        try:
            ast.parse(source.read_text(encoding="utf-8"), filename=str(source))
        except SyntaxError as exc:
            errors.append(f"{source.relative_to(ROOT)}: {exc.msg} at line {exc.lineno}")

    for requirements in ROOT.rglob("requirements.txt"):
        for line in requirements.read_text(encoding="utf-8").splitlines():
            if line and not line.startswith("#") and "==" not in line:
                errors.append(f"{requirements.relative_to(ROOT)}: unpinned dependency {line!r}")

    if errors:
        for error in errors:
            print(f"[ERROR] {error}")
        return 1
    print(f"[OK] {len(EXPECTED)} Web challenges are structurally valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
