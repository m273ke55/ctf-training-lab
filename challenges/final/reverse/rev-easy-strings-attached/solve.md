# Решение

1. Определяем тип файла и убеждаемся, что его не нужно запускать.
2. Ищем читаемые строки:

```bash
strings dist/strings_attached.bin | grep edu_ctf
```

3. В выводе находится флаг `edu_ctf{strings_attached}`.
Если `strings` недоступен, можно прочитать байты через Python, выделить печатные строки и найти regex `edu_ctf{...}`. Именно так работает `src/solve.py`.
