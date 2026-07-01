#!/usr/bin/env python3
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
def main():
    data=(ROOT/'dist'/'comment.wav').read_bytes()
    print(re.search(rb'edu_ctf\{[^}]+\}', data).group(0).decode()); return 0
if __name__=='__main__': raise SystemExit(main())
