from io import BytesIO
from pathlib import Path
import zipfile

from flask import Flask, render_template, request
from lxml import etree

app = Flask(__name__)

FLAG_FILE = Path("/flag.txt")
MAX_UPLOAD_BYTES = 2 * 1024 * 1024
MAX_XML_BYTES = 256 * 1024
REQUIRED_FIELDS = ("name", "family", "father", "team", "type")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    if any(not request.form.get(field) for field in REQUIRED_FIELDS):
        return render_template("index.html", error="Заполните все поля!")

    uploaded = request.files.get("file")
    if uploaded is None or not uploaded.filename:
        return render_template("index.html", error="Загрузите заявление в формате DOCX.")

    payload = uploaded.read(MAX_UPLOAD_BYTES + 1)
    if len(payload) > MAX_UPLOAD_BYTES:
        return render_template("index.html", error="Файл слишком большой.")

    try:
        with zipfile.ZipFile(BytesIO(payload)) as docx:
            xml_content = docx.read("word/document.xml")
        if len(xml_content) > MAX_XML_BYTES:
            raise ValueError("document.xml is too large")
    except (KeyError, ValueError, zipfile.BadZipFile):
        return render_template(
            "index.html",
            error="Ваше заявление не соответствует требованиям нормативных актов!",
        )

    try:
        # resolve_entities=True is the intentional XXE vulnerability of this task.
        parser = etree.XMLParser(
            load_dtd=True,
            resolve_entities=True,
            no_network=True,
            huge_tree=False,
        )
        root = etree.fromstring(xml_content, parser)
        parsed_content = etree.tostring(root, pretty_print=True, encoding="unicode")
    except (etree.XMLSyntaxError, ValueError):
        return render_template(
            "index.html",
            error="Вы неверно заполнили заявление! Проверьте образец.",
        )

    expected_flag = FLAG_FILE.read_text(encoding="utf-8").strip()
    if expected_flag not in parsed_content:
        return render_template(
            "index.html",
            error="Мы не можем обработать ваше заявление, потому что у нас обед.",
        )
    return render_template("index.html", success=parsed_content)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
