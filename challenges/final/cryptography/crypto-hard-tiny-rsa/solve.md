# Solution

The challenge uses textbook RSA with intentionally tiny primes. The flag is split into 4-byte blocks so every block is smaller than `n`.

## Steps

1. Read `n`, `e`, and the ciphertext blocks from `dist/public.txt`.
2. Factor `n` by trial division.
3. Compute `phi = (p - 1) * (q - 1)`.
4. Compute the private exponent with `d = pow(e, -1, phi)`.
5. Decrypt each block using `m = pow(c, d, n)`.
6. Convert each decrypted integer back to 4 bytes and remove padding zeros.

## Command

```bash
python3 src/solve.py
```

Expected output:

```text
edu_ctf{tiny_rsa_done}
```
