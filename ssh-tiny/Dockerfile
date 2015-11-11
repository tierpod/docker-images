FROM alpine
MAINTAINER Pavel Podkorytov <pod.pavel@gmail.com>

ENV TINI_VERSION v0.5.0

# supervisord + sshd
RUN apk update && \
    apk add openssh bash && \
    mkdir -p /var/run/sshd && \
    rm -rf /var/cache/apk/*

ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini-static /bin/tini-static

# create host keys
RUN chmod +x /bin/tini-static && \
    ssh-keygen -A && \
    adduser -D user && \
    echo 'root:root' | chpasswd && \
    echo 'user:user' | chpasswd

EXPOSE 22
ENTRYPOINT ["tini-static", "--"]
CMD ["/usr/sbin/sshd", "-D"]
