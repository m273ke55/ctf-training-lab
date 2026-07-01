# Решение

1. Определяем тип файла и убеждаемся, что его не нужно запускать.
2. Ищем читаемые строки:

```bash
file dist/demo_blob.bin
strings dist/demo_blob.bin
```

3. В выводе находится флаг `edu_ctf{reverse_demo_strings}`.
