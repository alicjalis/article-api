FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN apt-get update && apt-get install -y openssl && \
    mkdir -p /app/nginx/certs && \
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /app/nginx/certs/key.pem \
    -out /app/nginx/certs/cert.pem \
    -subj "/C=PL/O=ArticleAPI/CN=localhost" && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]