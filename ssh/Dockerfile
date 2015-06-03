FROM centos:latest
MAINTAINER Pavel Podkorytov <pod.pavel@gmail.com>

# supervisord + sshd
RUN yum install -y epel-release
RUN yum install -y supervisor openssh-server
RUN mkdir -p /var/run/sshd /var/log/supervisor

COPY supervisord.conf /etc/supervisord.conf

# create host keys
RUN ssh-keygen -A

RUN echo 'root:root' | chpasswd
RUN useradd -m -s /bin/bash user ;\
    echo 'user:user' | chpasswd

EXPOSE 22
CMD ["/usr/bin/supervisord"]
