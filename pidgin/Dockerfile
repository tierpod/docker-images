FROM alpine
MAINTAINER Podkorytov Pavel <pod.pavel@gmail.com>

RUN apk update && \
    apk add pidgin libpurple-xmpp dbus ttf-ubuntu-font-family && \
    rm -rf /var/cache/apk/*

ENTRYPOINT ["pidgin"]
