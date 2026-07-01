# Решение

В PCAP есть небольшой HTTP-ответ. В теле ответа находится параметр `note`, содержащий base64 от флага.

## Путь через Wireshark или tshark

1. Откройте `dist/traffic.pcap` в Wireshark.
2. Примените фильтр:

```text
http
```

3. Найдите HTTP-ответ и посмотрите тело ответа. Там есть строка вида:

```text
note=ZWR1X2N0Znt0cmFmZmljX25vdGVfZm91bmR9
```

4. Декодируйте значение как base64:

```bash
printf 'ZWR1X2N0Znt0cmFmZmljX25vdGVfZm91bmR9' | base64 -d
```

## Путь через strings и Python

1. Извлеките читаемые строки:

```bash
strings dist/traffic.pcap
```

2. Найдите `note=`.
3. Декодируйте значение после `note=` как base64.

Solver делает те же шаги без Wireshark:

```bash
python3 src/solve.py
```

Флаг: `edu_ctf{traffic_note_found}`.
