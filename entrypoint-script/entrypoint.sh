#!/bin/sh

cd /var/www/html

chown -R www-data:www-data /var/www/html
find . -type f -exec chmod 644 -- {} +
find . -type d -exec chmod 755 -- {} +

/bin/sh /tmp/docker_run.sh
