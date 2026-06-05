FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app
COPY ../data ./data
COPY ../mock_data ./mock_data
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
