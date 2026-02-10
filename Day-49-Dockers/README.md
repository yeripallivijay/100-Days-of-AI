# Sample Dockerfile for ML App
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r
