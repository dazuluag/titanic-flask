FROM python:3

RUN mkdir /Python && \
    git clone https://github.com/dazulu4/titanic-flask.git /Python/app && \
    pip3 install -r /Python/app/requirements.txt

WORKDIR /Python/app
EXPOSE 8000
ENV SURA_APP_PORT=8000

USER daemon

CMD ["python3", "/Python/app/main.py"]

