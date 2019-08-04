#!/bin/bash

DIRECTORY='experiments-data'
if [ ! -d "$DIRECTORY" ]; then
    mkdir $DIRECTORY
    echo 'Created directory - ' + $DIRECTORY
fi

docker-compose -f docker-compose.yml up -d

