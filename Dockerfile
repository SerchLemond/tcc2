FROM python:3.11.9-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    postgresql-client \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && apt-get purge -y --auto-remove build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN chmod +x /app/docker-entrypoint.sh

RUN pip install watchgod

EXPOSE 8000

ENTRYPOINT ["/app/docker-entrypoint.sh"]
