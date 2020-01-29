#!/bin/bash


FILES=(ec2-3-16-183-51.us-east-2.compute.amazonaws.com ec2-18-189-13-251.us-east-2.compute.amazonaws.com ec2-18-191-116-57.us-east-2.compute.amazonaws.com ec2-18-223-97-22.us-east-2.compute.amazonaws.com ec2-18-223-187-102.us-east-2.compute.amazonaws.com)

count=1
for NODE in ${FILES[*]}
do
    remote_node_not_equal_file="ubuntu@$NODE:/home/ubuntu/app/network_partition_simulator/NOT_eq_mean_experiment.txt"
    this_node_not_equal_file="/home/viktorsobol/Projects/PhD/network_partition_simulator/row_experiment_data/V222_START_AWS_NOT_eq_mean_experiment$count.txt"

    remote_node_equal_file="ubuntu@$NODE:/home/ubuntu/app/network_partition_simulator/eq_mean_experiment.txt"
    this_node_equal_file="/home/viktorsobol/Projects/PhD/network_partition_simulator/row_experiment_data/V222_START_AWS_eq_mean_experiment$count.txt"
    
    scp -i "~/.ssh/viktor.pem" $remote_node_not_equal_file $this_node_not_equal_file
    scp -i "~/.ssh/viktor.pem" $remote_node_equal_file $this_node_equal_file

    count=$((count+1))
done 
