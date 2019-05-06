FROM ubuntu:latest

MAINTAINER sid

RUN apt-get update && apt-get install -y apache2 libapache2-mod-python  && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2


RUN mkdir -p /etc/apache2/sites-available
RUN chown root:root /etc/apache2/sites-available
RUN chmod 755 /etc/apache2/sites-available

EXPOSE 80

CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]