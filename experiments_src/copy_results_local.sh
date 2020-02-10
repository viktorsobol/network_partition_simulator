#!/bin/bash

scp -r "$1"@"$2":/home/app/network_partition_simulator/experiments_src/results/* results/


