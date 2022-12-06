# potential-train

## Running
To run use: `sudo docker-compose up -d`

## SSL
To enable ssl use: `scripts/ssl.sh` when all containers are running and after shop installation.

## Prestashop configuration synchronization
To synchronize settings after shop is up, go to `phpMyAdmin -> prestashop database -> import` and import file from `docker/db`
