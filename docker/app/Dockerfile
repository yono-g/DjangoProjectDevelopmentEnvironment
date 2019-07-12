FROM python:3.7-alpine

RUN apk --no-cache add tzdata && \
    cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    apk del tzdata

RUN apk --no-cache add alpine-sdk \
    mariadb-connector-c-dev

RUN pip install gunicorn

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY ./config.py /etc/gunicorn/config.py
CMD [ "gunicorn" , "--config", "/etc/gunicorn/config.py", "mysite.wsgi:application" ]
