#!/bin/bash

echo 'Booting up prestashop in detached mode...'
sudo docker-compose up -d --build

echo 'Progress:'
BAR='##################################################'

for i in {1..50}; do
    echo -ne "\r${BAR:0:$i}" # print $i chars of $BAR from 0 position
    sleep 1
done

echo -e '\nBooted and ready!'
