FROM alpine
MAINTAINER Pavel Podkorytov <pod.pavel@gmail.com>

RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/community/ >> /etc/apk/repositories && \
    apk update && \
    apk add openssh bash tini && \
    mkdir -p /var/run/sshd && \
    rm -rf /var/cache/apk/*

# create host keys
RUN ssh-keygen -A && \
    adduser -D user && \
    echo 'root:root' | chpasswd && \
    echo 'user:user' | chpasswd

EXPOSE 22
ENTRYPOINT ["tini", "--"]
CMD ["/usr/sbin/sshd", "-D"]
