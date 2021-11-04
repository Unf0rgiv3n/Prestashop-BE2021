#!/bin/bash

DB_CONTAINER_NAME=presta-db
DB_NAME=prestashop
DB_USER=root
DB_PASSWD=admin

sudo docker exec -it $DB_CONTAINER_NAME bash -c "cd docker-entrypoint-initdb.d && mysqldump -u $DB_USER -p$DB_PASSWD $DB_NAME > databasedump.sql";
