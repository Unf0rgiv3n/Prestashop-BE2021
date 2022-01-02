#!/bin/bash

CONTAINER=""
DATABASE_NAME="BE_176023"

docker cp ./*.sql $CONTAINER:/tmp/$DATABASE_NAME.sql
docker cp ./create_db.sh $CONTAINER:/tmp/create_db.sh
docker exec -it $CONTAINER chmod 777 /tmp/create_db.sh
docker exec -it $CONTAINER /bin/sh /tmp/create_db.sh
echo "${DATABASE_NAME} db utworzona"