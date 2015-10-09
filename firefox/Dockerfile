FROM alpine
MAINTAINER Podkorytov Pavel <pod.pavel@gmail.com>

RUN apk update && \
    apk add firefox dbus ttf-ubuntu-font-family ttf-liberation && \
    rm -rf /var/cache/apk/*

ENTRYPOINT ["firefox", "--no-remote"]
