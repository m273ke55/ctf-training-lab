# Финальные задачи: Cryptography

Эта категория содержит безопасные локальные учебные задачи по криптографии: от классических шифров до небольших ошибок в криптографии с открытым ключом.

## Реализованные задачи

| Challenge | Сложность | Баллы | Концепция |
| --- | --- | ---: | --- |
| `crypto-easy-caesar-shift` | easy | 100 | brute force сдвига Caesar и распознавание формата флага |
| `crypto-medium-repeating-xor` | medium | 200 | repeating-key XOR и восстановление ключа по known plaintext |
| `crypto-hard-tiny-rsa` | hard-but-fair | 300 | факторизация маленького модуля RSA и расшифровка целочисленных блоков |
| `crypto-bonus-vigenere-keyword` | medium | 200 | bonus-расшифровка Vigenere по мягкой подсказке на ключ |

Все публичные артефакты генерируются в каталог `dist/` каждой задачи скриптом `src/generate.py`.
