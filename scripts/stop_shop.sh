#!/bin/bash

echo 'Removing old dump file'
pushd ../mysql-db && rm -f * && popd
echo 'Making db dump file'
bash db-backup.sh
docker-compose stop && echo y | docker-compose rm
