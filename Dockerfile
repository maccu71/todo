FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY todo_app.py .

CMD ["python", "while True: pass"]
# CMD ["python", "todo_app.py"]
