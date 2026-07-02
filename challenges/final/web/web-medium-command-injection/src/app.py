
from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        ip = request.form.get("ip", "").strip()
        forbidden_chars = [';', '&', '|', '`', '$', '>', '<']
        if len(ip) > 120 or any(char in ip for char in forbidden_chars):
            result = "Недопустимый ввод!"
        elif "cat" in ip.lower():
            result = "Недопустимый ввод. Попробуйте другой IP-адрес."
        else:
            try:
                # shell=True is the intentional command-injection vulnerability.
                completed = subprocess.run(
                    f"ping -c 1 {ip}",
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=3,
                    check=False,
                )
                result = (completed.stdout + completed.stderr)[:8192]
            except subprocess.TimeoutExpired:
                result = "Команда выполнялась слишком долго."

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
