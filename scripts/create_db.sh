#!/bin/bash

DB_NAME="BE_176023"
DB_USER="BE_176023"
DB_PWD="password"
DB_ROOT_PWD="student"
SHOP_URL="localhost:6023"
SHOP_SSL_URL="localhost:6022"

mysql -p$DB_ROOT_PWD -e "DROP DATABASE IF EXISTS ${DB_NAME};"
mysql -p$DB_ROOT_PWD -e "CREATE DATABASE ${DB_NAME};"
mysql -p$DB_ROOT_PWD -e "USE ${DB_NAME};"
mysql -p$DB_ROOT_PWD -e "CREATE USER IF NOT EXISTS ${DB_USER}@'%' IDENTIFIED BY '${DB_PWD}';"
mysql -p$DB_ROOT_PWD -e "GRANT ALL PRIVILEGES ON ${DB_NAME}.* TO '${DB_USER}'@'%';"
mysql -p$DB_ROOT_PWD -e "FLUSH PRIVILEGES;"
mysql -u $DB_USER -p$DB_PWD $DB_NAME < /tmp/${DB_NAME}.sql
mysql -u $DB_USER -p$DB_PWD $DB_NAME -e "UPDATE ps_shop_url SET domain='${SHOP_URL}', domain_ssl='${SHOP_SSL_URL}' WHERE id_shop_url=1;"

rm /tmp/${DB_NAME}.sql
rm /tmp/create_db.sh