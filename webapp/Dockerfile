FROM cicirello/pyaction:4.14.0

WORKDIR /app

COPY webapp.py /app/webapp.py
COPY requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 8501

CMD streamlit run webapp.py

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
RUN mkdir -p /root/.streamlit
RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /root/.streamlit/credentials.toml'

RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
" > /root/.streamlit/config.toml'