#!/usr/bin/env python3
import math, struct, wave
from pathlib import Path
FLAG = "edu_ctf{spectrogram_says_hi}"
ALPHABET = "abcdefghijklmnopqrstuvwxyz_{}"
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist" / "signal.wav"
RATE = 8000
TONE_SECONDS = 0.10
PAUSE_SECONDS = 0.02
AMPLITUDE = 9000
def frequency(ch: str) -> int:
    return 800 + ALPHABET.index(ch) * 40
def tone(freq: int):
    count = int(RATE * TONE_SECONDS)
    for n in range(count):
        fade = min(1.0, n / 80, (count - n - 1) / 80)
        yield int(AMPLITUDE * fade * math.sin(2 * math.pi * freq * n / RATE))
def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    samples=[]
    pause=[0] * int(RATE * PAUSE_SECONDS)
    for ch in FLAG:
        samples.extend(tone(frequency(ch)))
        samples.extend(pause)
    with wave.open(str(OUT), "wb") as wav:
        wav.setnchannels(1); wav.setsampwidth(2); wav.setframerate(RATE)
        wav.writeframes(b"".join(struct.pack("<h", s) for s in samples))
if __name__ == "__main__": main()
