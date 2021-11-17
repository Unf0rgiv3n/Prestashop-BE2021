#!/bin/bash

#rm -f /etc/apache2/sites-available/default-ssl.conf
#cp /ssl/default-ssl.conf /etc/apache2/sites-available/default-ssl.conf

#openssl genrsa -out myCA.key 2048
#openssl req -new -out website.csr -sha256 -key myCA.key
#openssl x509 -req -in website.csr -days 365 -signkey myCA.key

#openssl req -newkey rsa:4096 -x509 -sha256 -days 3650 -nodes -out ./ssl-bestcinema-selfsigned.crt -keyout ./ssl-bestcinema-selfsigned.key -subj "/C=PL/ST=Pomerania/L=Gdansk/O=Politechnika Gdanska/OU=./CN=localhost"

rm -rf /etc/apache2/sites-available/default-ssl.conf
rm -rf /etc/apache2/sites-available/000-default.conf
cp /var/www/ssl/000-default.conf /etc/apache2/sites-available/000-default.conf
cp /var/www/ssl/default-ssl.conf /etc/apache2/sites-available/default-ssl.conf
cp /var/www/ssl/ssl-bestcinema-selfsigned.crt /etc/ssl/certs/ssl-bestcinema-selfsigned.crt
cp /var/www/ssl/ssl-bestcinema-selfsigned.key /etc/ssl/private/ssl-bestcinema-selfsigned.key

#sed 's|;openssl.cafile=|openssl.cafile=/etc/ssl/certs/ssl-bestcinema-selfsigned.crt|g' /usr/local/etc/php/php.ini
#;openssl.cafile=
echo "ServerName localhost:8080" | tee /etc/apache2/conf-available/servername.conf
a2enconf servername

a2enmod ssl
a2enmod rewrite
a2ensite default-ssl
a2enconf ssl-params

apache2ctl configtest

service apache2 reload


echo 'tu powinien byc sed'
sed -i 's|;openssl.cafile=|openssl.cafile=/etc/ssl/certs/ssl-bestcinema-selfsigned.crt|g' /usr/local/etc/php/php.ini

service apache2 reload

apachectl -D FOREGROUND
