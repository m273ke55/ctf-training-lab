#!/usr/bin/env python3
from pathlib import Path
import re, zipfile
ROOT=Path(__file__).resolve().parents[1]
def main():
    with zipfile.ZipFile(ROOT/'dist'/'unknown.dat') as z: text=z.read('note.txt').decode('utf-8')
    print(re.search(r'edu_ctf\{[^}]+\}', text).group(0)); return 0
if __name__=='__main__': raise SystemExit(main())
