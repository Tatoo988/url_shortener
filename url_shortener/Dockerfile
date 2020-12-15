FROM python:3.8-alpine

RUN adduser -D urlshortener

WORKDIR /home/urlshortener
RUN apk update && apk add sqlite
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn


COPY app app

COPY migrations migrations
COPY url_shortener.py config.py boot.sh tests.py ./

RUN chmod a+x boot.sh

ENV URL_SHORTENER_APP url_shortener.py

RUN chown -R urlshortener:urlshortener ./

USER urlshortener

EXPOSE 5000

ENTRYPOINT ["./boot.sh"]
