FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install pandas pyarrow

CMD ["python", "app.py"]
