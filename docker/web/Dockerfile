FROM nginx:1.17.0-alpine

RUN apk --no-cache add tzdata && \
    cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    apk del tzdata

COPY default.conf /etc/nginx/conf.d/default.conf
