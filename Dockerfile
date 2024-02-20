FROM python:3.9.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt 

COPY  . .

CMD ["python", "main.py"]
 
