# Solution

This task uses repeating-key XOR. XOR has a useful property: if `cipher = plain XOR key`, then `key = cipher XOR plain`.

Because every flag starts with `edu_ctf{`, we can use that prefix as known plaintext.

## Steps

1. Read the hex ciphertext from `dist/ciphertext.hex`.
2. Convert it to bytes.
3. Try short key lengths.
4. Recover key bytes from the known prefix where possible.
5. Decrypt and keep the candidate that looks like `edu_ctf{...}`.

## Command

```bash
python3 src/solve.py
```

Expected output:

```text
edu_ctf{xor_key_found}
```
