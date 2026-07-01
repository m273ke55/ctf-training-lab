# Hints

1. **Hint 1 — мягкая:** XOR becomes easy when part of the plaintext is known.
2. **Hint 2 — подход:** Use the known prefix `edu_ctf{` to recover bytes of a repeating key.
3. **Hint 3 — почти решение:** For each possible key length, XOR the first ciphertext bytes with `edu_ctf{`; keep the key that decrypts the whole message to printable text ending in `}`.
