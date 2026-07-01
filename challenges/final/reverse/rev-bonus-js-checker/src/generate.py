#!/usr/bin/env python3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; DIST=ROOT/'dist'; KEY=37
def main():
    flag=(ROOT/'flag.txt').read_text(encoding='utf-8').strip(); data=[ord(c)^KEY for c in flag]
    js=f'''const KEY = {KEY};\nconst DATA = {data};\n\nfunction check(candidate) {{\n  if (candidate.length !== DATA.length) return false;\n  for (let i = 0; i < candidate.length; i++) {{\n    if ((candidate.charCodeAt(i) ^ KEY) !== DATA[i]) return false;\n  }}\n  return true;\n}}\n\nconsole.log(check(process.argv[2] || "") ? "Верно" : "Неверно");\n'''
    DIST.mkdir(exist_ok=True); (DIST/'checker.js').write_text(js,encoding='utf-8'); return 0
if __name__=='__main__': raise SystemExit(main())
