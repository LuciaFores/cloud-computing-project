FROM python:3.9-slim-buster

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8501

CMD ["python", "webapp.py"]
