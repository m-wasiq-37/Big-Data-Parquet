FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y curl && \
    pip install pandas pyarrow hdfs && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

CMD ["python", "app.py"]
