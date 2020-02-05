#!/bin/bash

echo root@"$1"
scp -r root@"$1":/home/app/network_partition_simulator/experiments_src/results/* results/

