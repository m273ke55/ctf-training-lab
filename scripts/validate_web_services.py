#!/usr/bin/env python3
"""Validate integrated Web challenges without third-party dependencies."""

from __future__ import annotations

import ast
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "challenges/intro/web-demo": ("intro", 0, "web-demo", 5101),
    "challenges/final/web/web-easy-method-head": ("easy", 100, "web-easy-method-head", 5102),
    "challenges/final/web/web-medium-command-injection": ("medium", 200, "web-medium-command-injection", 5103),
    "challenges/final/web/web-hard-upload-include": ("hard-but-fair", 300, "web-hard-upload-include", 5104),
    "challenges/final/web/web-bonus-xxe-docx": ("medium", 200, "web-bonus-xxe-docx", 5105),
}
REQUIRED = ("Dockerfile", "challenge.yml", "challenge.md", "hints.md", "solve.md", "flag.txt")
FLAG_RE = re.compile(r"^edu_ctf\{[a-zA-Z0-9_!?@#.,:+-]+\}$")


def validate_challenge(name: str, difficulty: str, points: int) -> list[str]:
    errors: list[str] = []
    challenge = ROOT / name
    for relative in REQUIRED:
        if not (challenge / relative).is_file():
            errors.append(f"{name}: missing {relative}")
    if not (challenge / "src").is_dir():
        errors.append(f"{name}: missing src directory")

    dockerfile_path = challenge / "Dockerfile"
    if dockerfile_path.is_file():
        dockerfile = dockerfile_path.read_text(encoding="utf-8")
        for token in ("COPY flag.txt /flag.txt", "EXPOSE 5000", "HEALTHCHECK"):
            if token not in dockerfile:
                errors.append(f"{name}: Dockerfile missing {token}")
        if ":latest" in dockerfile:
            errors.append(f"{name}: Dockerfile uses a floating latest tag")
        if "web-hard-upload-include" not in name and "USER challenge" not in dockerfile:
            errors.append(f"{name}: Python service must run as non-root")

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
    for name, (difficulty, points, _, _) in EXPECTED.items():
        errors.extend(validate_challenge(name, difficulty, points))

    compose_path = ROOT / "docker-compose.web.yml"
    if not compose_path.is_file():
        errors.append("missing docker-compose.web.yml")
    else:
        compose = compose_path.read_text(encoding="utf-8")
        for path, (_, _, service, host_port) in EXPECTED.items():
            compose_checks = {
                "service": f"  {service}:",
                "build context": f"build: ./{path}",
                "port": f'"127.0.0.1:{host_port}:5000"',
            }
            for label, needle in compose_checks.items():
                if needle not in compose:
                    errors.append(f"{service}: inconsistent {label} in docker-compose.web.yml")
        if compose.count("internal: true") != len(EXPECTED):
            errors.append("docker-compose.web.yml: every service must have a separate internal network")
        if compose.count("init: true") != len(EXPECTED):
            errors.append("docker-compose.web.yml: every service must enable an init process")

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
