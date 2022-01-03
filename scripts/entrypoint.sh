#!/bin/sh

cd /var/www/html

#chown -R www-data:www-data /var/www/html
#find . -type f -exec chmod 644 -- {} +
#find . -type d -exec chmod 755 -- {} +

apt-get update
echo "y" | apt-get install sendmail

echo "127.0.0.1 localhost.localdomain localhost $(hostname)" >> /etc/hosts
service sendmail start

echo "wchodzimy do create-ssl"

/bin/sh /var/www/ssl/create-ssl.sh
/bin/sh /tmp/docker_run.sh
