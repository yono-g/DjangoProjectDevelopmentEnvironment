FROM python:3.7-alpine

RUN apk --no-cache add tzdata && \
    cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    apk del tzdata \
    && \
    apk --no-cache add alpine-sdk \
        mariadb-connector-c-dev \
        gettext \
    && \
    pip install --upgrade pip \
    && \
    pip install supervisor \
        gunicorn \
        pipenv \
    && \
    echo_supervisord_conf > /etc/supervisord.conf && \
    sed -i -e "s/^nodaemon=false/nodaemon=true/" /etc/supervisord.conf && \
    sed -i -e "s/^;[include]/[include]/" /etc/supervisord.conf && \
    sed -i -e "s!^;files = relative/directory/\*.ini!files = supervisord.d/*.ini!" /etc/supervisord.conf

COPY supervisord.d/gunicorn.ini /etc/supervisord.d/gunicorn.ini

COPY ./gunicorn/config.py /etc/gunicorn/config.py

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD [ "supervisord" , "-c", "/etc/supervisord.conf" ]
