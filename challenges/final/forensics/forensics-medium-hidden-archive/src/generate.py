#!/usr/bin/env python3
from io import BytesIO
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

FLAG = "edu_ctf{archive_inside}"
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist" / "holiday_photo.jpg"

# Минимальный безопасный JPEG 1x1 и учебный комментарий перед приклеенным архивом.
JPEG_PREFIX = bytes.fromhex(
    "ffd8ffe000104a46494600010101006000600000"
    "ffdb004300" + "08" * 64 +
    "ffc0000b080001000101011100"
    "ffc4001400010000000000000000000000000000000000000000"
    "ffda0008010100003f00d2cf20ffd9"
)


def build_zip() -> bytes:
    buffer = BytesIO()
    with ZipFile(buffer, "w", ZIP_DEFLATED) as archive:
        archive.writestr("note.txt", "Скрытая заметка: " + FLAG + "\n")
    return buffer.getvalue()


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes(JPEG_PREFIX + b"\n# appended training data follows\n" + build_zip())


if __name__ == "__main__":
    main()
