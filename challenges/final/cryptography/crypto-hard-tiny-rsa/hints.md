# Hints

1. **Hint 1 — мягкая:** Real RSA depends on `n` being too large to factor. Is this `n` large enough?
2. **Hint 2 — подход:** Use trial division to factor `n`, then compute `phi = (p - 1) * (q - 1)`.
3. **Hint 3 — почти решение:** Compute `d = pow(e, -1, phi)`, decrypt each block with `pow(c, d, n)`, and convert each integer back to 4 bytes.
