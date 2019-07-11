FROM python:3.7-alpine

RUN apk --no-cache add tzdata && \
    cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    apk del tzdata

RUN apk --no-cache add alpine-sdk \
    linux-headers \
    mariadb-connector-c-dev

RUN pip install uwsgi

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY ./uwsgi.ini /etc/uwsgi/uwsgi.ini
CMD [ "uwsgi" , "--ini", "/etc/uwsgi/uwsgi.ini" ]
