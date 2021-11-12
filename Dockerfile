FROM prestashop/prestashop:1.7

COPY ./scripts/entrypoint.sh /var/www/entrypoint.sh
RUN chmod 755 /var/www/entrypoint.sh

RUN mkdir /var/www/ssl
COPY ./scripts/ssl/000-default.conf /var/www/ssl/000-default.conf
COPY ./scripts/ssl/default-ssl.conf /var/www/ssl/default-ssl.conf
COPY ./scripts/ssl/create-ssl.sh /var/www/ssl/create-ssl.sh
RUN chmod 755 /var/www/ssl/create-ssl.sh
RUN chmod 755 /var/www/ssl/000-default.conf
RUN chmod 755 /var/www/ssl/default-ssl.conf

CMD ["/bin/sh", "/var/www/entrypoint.sh"]
