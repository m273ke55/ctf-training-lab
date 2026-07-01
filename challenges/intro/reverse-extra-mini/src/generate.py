#!/usr/bin/env python3
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; DIST = ROOT / "dist"; SHIFT = 7
TEMPLATE = '''#!/usr/bin/env python3
SHIFT = {shift}
DATA = {data}

def check(candidate):
    return [ord(ch) + SHIFT for ch in candidate] == DATA

if __name__ == "__main__":
    value = input("Введите флаг: ").strip()
    print("Верно" if check(value) else "Неверно")
'''
def main():
    flag=(ROOT/'flag.txt').read_text(encoding='utf-8').strip(); data=[ord(ch)+SHIFT for ch in flag]
    DIST.mkdir(exist_ok=True); (DIST/'tiny_checker.py').write_text(TEMPLATE.format(shift=SHIFT,data=data),encoding='utf-8'); return 0
if __name__=='__main__': raise SystemExit(main())
