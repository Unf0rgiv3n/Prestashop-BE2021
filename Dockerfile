FROM prestashop/prestashop:1.7

RUN chown -R www-data:www-data /var/www/html
RUN find . -type f -exec chmod 644 -- {} +
RUN find . -type d -exec chmod 755 -- {} +
