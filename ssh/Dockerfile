FROM centos:7
MAINTAINER Pavel Podkorytov <pod.pavel@gmail.com>

# supervisord + sshd
RUN yum install -y epel-release
RUN yum install -y supervisor openssh-server && \
    yum clean all
RUN mkdir -p /var/run/sshd /var/log/supervisor && \
    # create host keys
    ssh-keygen -A && \
    # create users
    useradd -m -s /bin/bash user && \
    echo 'root:root' | chpasswd && \
    echo 'user:user' | chpasswd

COPY supervisord.conf /etc/supervisord.conf
EXPOSE 22
CMD ["/usr/bin/supervisord"]
