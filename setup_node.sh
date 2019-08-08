#!/bin/bash

if [ ! -d '/home/ubuntu/app']; then
    mkdir /home/ubuntu/app
fi
cd /home/ubuntu/app

if [ ! -d "/home/ubuntu/app/network_partition_simulator" ]; then
    git clone https://github.com/Sobolvitya/network_partition_simulator.git
else 
    cd network_partition_simulator
    git pull origin master
fi

sudo apt-get update 
sudo apt-get install python3-pip
pip3 install networkx matplotlib

echo 'DONE'