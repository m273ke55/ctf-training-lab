# Решение

1. Определяем тип файла и убеждаемся, что его не нужно запускать.
2. Ищем читаемые строки:

```bash
strings dist/mini_blob.bin | grep edu_ctf
```

3. В выводе находится флаг `edu_ctf{mini_reverse_strings}`.
