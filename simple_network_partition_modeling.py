import networkx as nx
from networkx import Graph
import matplotlib.pyplot as plt
import numpy as np
import random
import time
import uuid
import constants
import Config as c
from Config import Configuration

class NodeRepresantation:
    def colourOf(self, status: str) -> str:
        if status == 'UP':
            return 'green'
        if status == 'DOWN':
            return 'red'
        raise Exception('No such status')

class Node:
    status = 'UP'
    timLeft = 0
    generator = 0

    def __init__ (self, configuration):
        self.generator = configuration.generator()
        self.timLeft = self.generator.getTime(self.status)

    def tick(self):
        self.timLeft -= 1

        if self.timLeft <= 0:
            self.statusChange()    
            self.timLeft = self.generator.getTime(self.status)

    def statusChange(self):
        if self.status == 'UP':
            self.status = 'DOWN'
            return
        if self.status == 'DOWN':
            self.status = 'UP'
            return
    
    def __str__(self):
        return self.status + ':  ' + str(self.timLeft)

def split_brain(nodes: list, G: Graph) -> bool:
    if (len(nodes) == 0):
        return False
    nodes_up = nodes
    to_visit = {nodes_up[0]:1}
    visited = {}
   
    while(len(to_visit) > 0):
        to_visit_node = to_visit.popitem()
        new_nodes = list(G.adj[to_visit_node[0]])
        visited[to_visit_node[0]] = 1
       
        for new_node in new_nodes:
            if (G.nodes(data=True)[new_node]['metadata'].status == 'DOWN'):
                continue
            if (new_node in visited):
                continue
            to_visit[new_node] = 1
    
    return len(visited) != len(nodes)

# return total count of split_brain occurances during epoch
def run_epoch(G, configuration: Configuration, epoch_lenght = 1000, run_one_by_one = False) -> int:
    
    for node in G.nodes(data=True):
        node_metadata = Node(configuration)
        if run_one_by_one:
            node_metadata.timLeft += random.randint(0, int(configuration.mean_up * 0.9))
        node[1]['metadata'] = node_metadata

    total_count_of_failures = 0

    for i in  range(epoch_lenght):
                
        for node in G.nodes(data=True):
            node[1]['metadata'].tick()

        up_nodes = [x for x,y in G.nodes(data=True) if y['metadata'].status == 'UP']

        res = split_brain(list(up_nodes), G)
        if res == True:
            total_count_of_failures += 1
  
    print("Total failures: " + str(total_count_of_failures))
    return total_count_of_failures

