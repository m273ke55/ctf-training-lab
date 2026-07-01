# Solution

For the live demo, start with the idea that encoding is a reversible representation, while encryption uses a rule or key. Here the rule is a Caesar shift, so only 26 possible rotations exist.

## Steps

1. Open `dist/message.txt` and copy the ciphertext.
2. Try all 26 Caesar shifts.
3. Stop when the plaintext contains a readable flag beginning with `edu_ctf{`.

## Command

```bash
python3 src/solve.py
```

The script prints:

```text
edu_ctf{crypto_demo_shift}
```
