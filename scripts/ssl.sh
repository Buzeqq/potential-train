#!/bin/bash

#sudo docker exec prestashop chmod +x /docker/ssl.sh
#sudo docker exec prestashop /docker/ssl.sh

docker exec prestashop-db chmod +x /docker/ssl.sh
docker exec prestashop-db /docker/ssl.sh