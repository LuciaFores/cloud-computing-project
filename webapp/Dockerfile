FROM python:3.9-slim-buster

WORKDIR /app

COPY webapp.py /app/webapp.py
COPY requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "webapp.py"]

EXPOSE 8501