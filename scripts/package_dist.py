#!/usr/bin/env python3
"""Package public dist/ files for CTFd upload."""
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
CHALLENGES = ROOT / "challenges"
OUT = ROOT / "build" / "packages"

EXCLUDED_NAMES = {"solve.md", "flag.txt"}

def is_public_file(path: Path) -> bool:
    return path.is_file() and not path.name.startswith(".") and path.name not in EXCLUDED_NAMES and "src" not in path.parts

def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    created = []
    for dist in sorted(CHALLENGES.rglob("dist")):
        if not dist.is_dir():
            continue
        files = [p for p in sorted(dist.rglob("*")) if is_public_file(p)]
        if not files:
            print(f"[SKIP] {dist.relative_to(ROOT)} has no public files.")
            continue
        challenge_dir = dist.parent
        archive_name = "-".join(challenge_dir.relative_to(CHALLENGES).parts) + ".zip"
        archive_path = OUT / archive_name
        with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
            for file_path in files:
                zf.write(file_path, file_path.relative_to(dist))
        created.append(archive_path)
        print(f"[OK] Created {archive_path.relative_to(ROOT)}")
    if not created:
        print("No archives created: dist/ folders contain no public files yet.")
    else:
        print("\nCreated archives:")
        for path in created:
            print(f"- {path.relative_to(ROOT)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
