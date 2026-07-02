import os
import subprocess
import sys
from pathlib import Path

from flask import Flask, request, render_template

app = Flask(__name__)
EXECUTION_TIMEOUT_SECONDS = 2
MAX_OUTPUT_BYTES = 8192
SANDBOX_DIR = Path("/tmp")


def execute_code(user_code: str) -> str:
    """Run submitted code in the challenge container with bounded resources."""
    try:
        completed = subprocess.run(
            [sys.executable, "-I", "-c", user_code],
            cwd=SANDBOX_DIR,
            env={"PATH": os.environ.get("PATH", "")},
            capture_output=True,
            text=True,
            timeout=EXECUTION_TIMEOUT_SECONDS,
            check=False,
        )
    except subprocess.TimeoutExpired:
        return "Ошибка: превышен лимит выполнения (2 секунды)."

    output = completed.stdout + completed.stderr
    if not output:
        output = "Код выполнен без вывода."
    encoded = output.encode("utf-8", errors="replace")
    if len(encoded) > MAX_OUTPUT_BYTES:
        output = encoded[:MAX_OUTPUT_BYTES].decode("utf-8", errors="replace") + "\n[вывод обрезан]"
    return output.strip()

@app.route('/', methods=['GET', 'POST'])
def index():
    output = ""
    user_code = ""
    if request.method == 'POST':
        user_code = request.form.get('code', '')
        output = execute_code(user_code)

    return render_template("index.html", output=output, user_code=user_code)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
