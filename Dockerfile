FROM python:3.9-slim-buster

WORKDIR /app

COPY toy_image_recognition.py /app/toy_image_recognition.py
COPY requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "toy_image_recognition.py"]