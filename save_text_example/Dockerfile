FROM python:3.9-slim-buster

WORKDIR /app

COPY save_text.py /app/save_text.py
COPY requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "save_text.py"]