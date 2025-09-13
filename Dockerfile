FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY .env .  # Make sure .env is available inside the container

CMD ["gunicorn", "order_management.wsgi:application", "--bind", "0.0.0.0:8000"]
