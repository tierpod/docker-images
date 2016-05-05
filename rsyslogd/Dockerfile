FROM centos:7
MAINTAINER Pavel Podkorytov <pod.pavel@gmail.com>

ENV TINI_VERSION v0.9.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini-static /bin/tini-static
RUN chmod +x /bin/tini-static

RUN yum install -y rsyslog && \
    yum clean all

RUN groupadd -r testgroup

EXPOSE 514 514/udp

VOLUME ["/var/log", "/etc/rsyslog.d"]

ENTRYPOINT ["tini-static", "--"]
CMD ["rsyslogd", "-n"]
