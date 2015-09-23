FROM centos:7
MAINTAINER Pavel Podkorytov <pod.pavel@gmail.com>

# supervisord + sshd
RUN yum install -y epel-release
RUN yum install -y bash supervisor mc vim nginx && \
    yum clean all && \
    mkdir -p /var/log/supervisor && \
    ln -s -f /usr/share/zoneinfo/Asia/Yekaterinburg /etc/localtime

COPY supervisord.conf /etc/supervisord.conf

EXPOSE 80 81
CMD ["/usr/bin/supervisord"]
