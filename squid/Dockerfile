FROM centos:7
MAINTAINER Podkorytov Pavel <pod.pavel@gmail.com>

RUN yum -y install epel-release && \
    yum clean all

RUN yum -y install squid supervisor && \
    mkdir -p /var/log/supervisor && \
    rm -f /etc/squid/squid.conf && \
    yum clean all

COPY supervisord.conf /etc/supervisord.conf

EXPOSE 3128
VOLUME ["/etc/squid/squid.conf"]
CMD ["/usr/bin/supervisord"]
