#!/bin/bash

mkdir -p "/home/ubuntu/app/" 
cd "/home/ubuntu/app/" 

if [ ! -d "/home/ubuntu/app/network_partition_simulator" ]; then
    git clone https://github.com/Sobolvitya/network_partition_simulator.git
    cd "network_partition_simulator"
else 
    cd "network_partition_simulator"
    git pull origin master
fi

sudo apt-get update 
sudo apt-get install python3-pip
pip3 install networkx matplotlib

rm -rf NOT_eq_mean_experiment.txt
rm -rf eq_mean_experiment.txt
nohup python3 -u experiments.py &