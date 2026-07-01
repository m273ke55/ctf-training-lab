#!/usr/bin/env python3
import math, re, struct, wave
from pathlib import Path
ALPHABET = "abcdefghijklmnopqrstuvwxyz_{}"
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "dist" / "signal.wav"
TONE_SECONDS = 0.10
PAUSE_SECONDS = 0.02
def goertzel(samples, rate, freq):
    coeff = 2 * math.cos(2 * math.pi * freq / rate)
    s_prev = s_prev2 = 0.0
    for sample in samples:
        s = sample + coeff * s_prev - s_prev2
        s_prev2, s_prev = s_prev, s
    return s_prev2*s_prev2 + s_prev*s_prev - coeff*s_prev*s_prev2
def main() -> None:
    with wave.open(str(DATA), "rb") as wav:
        if wav.getnchannels() != 1 or wav.getsampwidth() != 2: raise SystemExit("Ожидается mono WAV 16-bit")
        rate = wav.getframerate(); frames = wav.readframes(wav.getnframes())
    samples = list(struct.unpack("<" + "h" * (len(frames)//2), frames))
    tone_len = int(rate * TONE_SECONDS); step = int(rate * (TONE_SECONDS + PAUSE_SECONDS))
    freqs = [800 + i * 40 for i in range(len(ALPHABET))]
    chars=[]
    for start in range(0, len(samples) - tone_len + 1, step):
        window = samples[start:start + tone_len]
        if max(abs(x) for x in window) < 1000: continue
        best = max(range(len(freqs)), key=lambda i: goertzel(window, rate, freqs[i]))
        chars.append(ALPHABET[best])
    text = "".join(chars)
    match = re.search(r"edu_ctf\{[^}]+\}", text)
    if not match: raise SystemExit("Флаг по частотам не найден")
    print(match.group(0))
if __name__ == "__main__": main()
