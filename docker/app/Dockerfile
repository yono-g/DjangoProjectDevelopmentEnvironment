FROM python:3.7-alpine

RUN apk --no-cache add tzdata && \
    cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    apk del tzdata

RUN apk --no-cache add alpine-sdk \
    mariadb-connector-c-dev

RUN pip install supervisor && \
    echo_supervisord_conf > /etc/supervisord.conf && \
    sed -i -e "s/^nodaemon=false/nodaemon=true/" /etc/supervisord.conf && \
    sed -i -e "s/^;[include]/[include]/" /etc/supervisord.conf && \
    sed -i -e "s!^;files = relative/directory/\*.ini!files = supervisord.d/*.ini!" /etc/supervisord.conf
COPY supervisord.d/gunicorn.ini /etc/supervisord.d/gunicorn.ini

RUN pip install gunicorn
COPY ./gunicorn/config.py /etc/gunicorn/config.py

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

CMD [ "supervisord" , "-c", "/etc/supervisord.conf" ]
