# Solution

Try all alphabet rotations and look for text that matches the flag format.

## Steps

1. Open `dist/ciphertext.txt` and copy the ciphertext.
2. Try all 26 Caesar shifts.
3. Stop when the plaintext contains a readable flag beginning with `edu_ctf{`.

## Command

```bash
python3 src/solve.py
```

The script prints:

```text
edu_ctf{mini_crypto_rotates}
```
