#!/usr/bin/env python3
import re, struct, zlib
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "dist" / "pixels.png"
PNG_SIG = b"\x89PNG\r\n\x1a\n"
def parse_png(blob: bytes):
    if not blob.startswith(PNG_SIG): raise SystemExit("Это не PNG")
    pos=len(PNG_SIG); width=height=None; idat=[]
    while pos+8 <= len(blob):
        length=struct.unpack("!I", blob[pos:pos+4])[0]; kind=blob[pos+4:pos+8]; data=blob[pos+8:pos+8+length]; pos += 12+length
        if kind == b"IHDR":
            width,height,bit_depth,color_type,_,_,_=struct.unpack("!IIBBBBB", data)
            if bit_depth != 8 or color_type != 0: raise SystemExit("Solver ожидает grayscale PNG с глубиной 8 бит")
        elif kind == b"IDAT": idat.append(data)
        elif kind == b"IEND": break
    return width, height, zlib.decompress(b"".join(idat))
def main() -> None:
    width,height,raw=parse_png(DATA.read_bytes()); pixel_bytes=[]
    for y in range(height):
        row=raw[y*(width+1):(y+1)*(width+1)]
        if row[0] != 0: raise SystemExit("Solver ожидает PNG filter type 0")
        pixel_bytes.extend(row[1:])
    out=bytearray()
    for i in range(0,len(pixel_bytes),8):
        byte=0
        for value in pixel_bytes[i:i+8]: byte=(byte<<1)|(value&1)
        out.append(byte)
        if byte in (0, ord("}")): break
    match=re.search(r"edu_ctf\{[^}]+\}", out.rstrip(b"\0").decode("ascii", errors="ignore"))
    if not match: raise SystemExit("Флаг в LSB не найден")
    print(match.group(0))
if __name__ == "__main__": main()
