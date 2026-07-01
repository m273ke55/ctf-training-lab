#!/usr/bin/env python3
from pathlib import Path
import base64, re
ROOT=Path(__file__).resolve().parents[1]
def main():
    text=(ROOT/'dist'/'server.log').read_text(encoding='utf-8')
    for token in re.findall(r'payload=([A-Za-z0-9+/=]{16,})|\b([A-Za-z0-9+/=]{16,})\b', text):
        token = token[0] or token[1]
        try: dec=base64.b64decode(token, validate=True).decode('utf-8')
        except Exception: continue
        m=re.search(r'edu_ctf\{[^}]+\}', dec)
        if m: print(m.group(0)); return 0
    return 1
if __name__=='__main__': raise SystemExit(main())
