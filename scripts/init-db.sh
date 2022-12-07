echo "Importing database..."
sudo docker exec prestashop-db bash -c 'mkdir /var/lib/mysql/backups 2> /dev/null'
sudo docker exec prestashop-db cp /docker-entrypoint-initdb.d/backup.sql.gz /var/lib/mysql/backups
sudo docker exec prestashop-db gunzip /var/lib/mysql/backups/backup.sql.gz
sudo docker exec prestashop-db bash -c 'mysql -u root -pprestashop prestashop < /var/lib/mysql/backups/backup.sql'
sudo docker exec prestashop-db rm -r /var/lib/mysql/backups
echo "Database imported!"