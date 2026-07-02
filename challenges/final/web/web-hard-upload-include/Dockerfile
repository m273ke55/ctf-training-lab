FROM php:8.3-apache-trixie

COPY src/ /var/www/html/
COPY flag.txt /flag.txt
RUN mkdir -p /var/www/html/uploads \
    && chown -R www-data:www-data /var/www/html/uploads \
    && chmod 0755 /var/www/html/uploads \
    && chmod 0444 /flag.txt
EXPOSE 80
HEALTHCHECK --interval=10s --timeout=3s --retries=5 CMD ["php", "-r", "$c=@file_get_contents('http://127.0.0.1/'); if ($c===false) { exit(1); }"]
