FROM php:8.3-apache

COPY src/ /var/www/html/
COPY flag.txt /flag.txt
RUN mkdir -p /var/www/html/uploads \
    && chown -R www-data:www-data /var/www/html/uploads \
    && chmod 0755 /var/www/html/uploads \
    && chmod 0444 /flag.txt \
    && sed -i 's/80/5000/' /etc/apache2/ports.conf /etc/apache2/sites-enabled/000-default.conf
EXPOSE 5000
HEALTHCHECK --interval=10s --timeout=3s --retries=5 CMD ["php", "-r", "$c=@file_get_contents('http://127.0.0.1:5000/'); if ($c===false) { exit(1); }"]
