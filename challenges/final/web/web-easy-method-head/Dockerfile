FROM python:3.12-slim-trixie

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN addgroup --system challenge \
    && adduser --system --ingroup challenge --home /nonexistent challenge

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src /app
COPY flag.txt /flag.txt
RUN chmod 0444 /flag.txt

USER challenge
EXPOSE 5000
HEALTHCHECK --interval=10s --timeout=3s --retries=5 CMD ["python", "-c", "import urllib.request; urllib.request.urlopen('http://127.0.0.1:5000/', timeout=2)"]
CMD ["gunicorn", "--no-control-socket", "--bind", "0.0.0.0:5000", "--workers", "2", "--threads", "2", "--timeout", "10", "server:app"]
