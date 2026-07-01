# Cryptography

Encoding (Base64, hex) обратимо без секрета, encryption требует ключ, hashing необратим. Caesar/ROT13 — сдвиг, XOR и repeating-key XOR часто ломаются known plaintext, Vigenere — повторяющийся ключ, RSA зависит от модульной арифметики. Ошибки: называть Base64 шифром, не проверять формат флага, использовать слишком большой brute force.
