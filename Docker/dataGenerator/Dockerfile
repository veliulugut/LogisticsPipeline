FROM python:3.9-slim

WORKDIR /app

# Install curl for healthcheck
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install "fastapi==0.95.2" "uvicorn==0.22.0" "kafka-python==2.0.2" \
       "faker==18.11.2" "faker-vehicle==0.2.0" "python-json-logger==2.0.7" \
       "email-validator==2.0.0" "pydantic==1.10.8"

COPY . .

CMD ["python", "-m", "uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8088", "--reload"]
