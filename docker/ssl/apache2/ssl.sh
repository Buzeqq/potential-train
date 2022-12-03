#!/bin/bash

openssl req -newkey rsa:2048 -new -nodes -x509 -days 365 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt -subj "/C=PL/ST=Pomerania/L=Gdansk/O=PG/OU=./CN=." > /dev/null 2>&1
echo "SSL Configuration [1/5]: Created private key and certifacate..."

rm -rf /etc/apache2/sites-available/000-default.conf
echo "SSL Configuration [2/5]: Removed default apache2 site config..."

cp /docker/000-default.conf /etc/apache2/sites-available/000-default.conf
echo "SSL Configuration [3/5]: Created new apache2 site config..."

a2enmod ssl > /dev/null 2>&1
echo "SSL Configuration [4/5]: Enabled SSL for apache2..."

echo "ServerName localhost" >> /etc/apache2/apache2.conf
if [[ $(apache2ctl configtest 2>&1) == "Syntax OK" ]]
then
    service apache2 reload > /dev/null 2>&1
    echo "SSL Configuration [5/5]: Reloaded apache2 service..."
else
    echo "Apache config syntax failed!"
    exit 1
fi


