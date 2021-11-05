FROM prestashop/prestashop:1.7

COPY ./entrypoint-script/entrypoint.sh /var/www/entrypoint.sh
RUN chmod 755 /var/www/entrypoint.sh

CMD ["/bin/sh", "/var/www/entrypoint.sh"]
