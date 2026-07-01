# Решение

Файл `dist/lockbox.pyc` не нужно запускать. Его можно разобрать средствами стандартной библиотеки Python.

## Просмотр bytecode

У `.pyc` есть служебный header, после которого хранится marshalled code object. Для файла, созданного текущим генератором, solver пропускает первые 16 байт header и загружает code object через `marshal.loads`:

```python
import marshal
import dis
from pathlib import Path

blob = Path("dist/lockbox.pyc").read_bytes()
code = marshal.loads(blob[16:])
dis.dis(code)
```

После `dis.dis(code)` видно, что внутри есть функция проверки. Она берёт введённую строку в обратном порядке, применяет XOR и сдвиг, а затем сравнивает результат с массивом чисел.

## Восстановление флага

Проверочный solver `src/solve.py` делает тот же анализ автоматически:

1. открывает `dist/lockbox.pyc`;
2. пропускает первые 16 байт header;
3. загружает code object через `marshal.loads`;
4. рекурсивно просматривает `co_consts`;
5. находит массив чисел, `XOR_KEY` и `SHIFT`;
6. для каждого числа отменяет сдвиг и XOR;
7. разворачивает строку обратно, потому что проверка обрабатывала ввод в обратном порядке.

Флаг: `edu_ctf{pyc_lockbox_open}`.
