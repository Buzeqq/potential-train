FROM prestashop/prestashop:1.7

# To run files with the same group as your primary user
ARG GROUP_ID
ARG USER_ID

RUN groupmod -g $GROUP_ID www-data \
  && usermod -u $USER_ID -g $GROUP_ID www-data

COPY ./docker/wait-for-it.sh /tmp/
COPY ./docker/docker_run_git.sh /tmp/

RUN mkdir -p /var/www/.npm
RUN chown -R www-data:www-data /var/www/.npm
RUN mkdir -p /var/www/.composer
RUN chown -R www-data:www-data /var/www/.composer

RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt install -y nodejs

# Install mailutils to make sendmail work
RUN apt install -y \
    apt-utils \
    mailutils

COPY ./src /var/www/html
COPY ./docker/ssl/apache2/000-default.conf /docker/000-default.conf
COPY ./docker/ssl/apache2/ssl.sh /tmp/init-scripts/ssl.sh

RUN chown -R www-data:www-data /var/www/html/

CMD ["/tmp/wait-for-it.sh", "--timeout=60", "--strict", "prestashop-db:3306", "--", "/tmp/docker_run_git.sh"]



