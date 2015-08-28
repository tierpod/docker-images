FROM alpine
MAINTAINER Podkorytov Pavel <pod.pavel@gmail.com>

RUN apk update && \
    apk add pidgin dbus ttf-ubuntu-font-family && \
    rm -rf /var/cache/apk/*

ENTRYPOINT ["pidgin"]
