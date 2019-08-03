import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
import time
import uuid
import constants

class NodeRepresantation:
    def colourOf(self, status: str) -> str:
        if status == 'UP':
            return 'green'
        if status == 'DOWN':
            return 'red'
        raise Exception('No such status')

class NetworkTopologyGenerator:
    def get(self) -> nx.Graph:
        return nx.random_regular_graph(6, 100)

class Node:
    status = 'UP'
    timLeft = 0

    def __init__ (self):
        self.timLeft = np.random.poisson(constants.MEAN.get('UP'))

    def tick(self):
        self.timLeft -= 1

        if self.timLeft <= 0:
            self.statusChange()    
            self.timLeft = np.random.poisson(constants.MEAN.get(self.status))

    def statusChange(self):
        if self.status == 'UP':
            self.status = 'DOWN'
            return
        if self.status == 'DOWN':
            self.status = 'UP'
            return
    
    def __str__(self):
        return self.status + ':  ' + str(self.timLeft)

def split_brain(nodes: list, G) -> bool:
    if (len(nodes) == 0):
        return False
    nodes_up = nodes
    to_visit = [nodes_up[0]]
    visited = set()
   
    while(len(to_visit) > 0):
        new_nodes = list(G.adj[to_visit[0]])
        visited.add(to_visit[0])
        to_visit.remove(to_visit[0])
       
        for new_node in new_nodes:
            if (G.nodes(data=True)[new_node]['metadata'].status == 'DOWN'):
                continue
            if (new_node in visited):
                continue
            to_visit.append(new_node)
    
    return len(visited) != len(nodes)

# G = nx.Graph()

# G.add_node(1, status='UP')
# G.add_node(2, status='DOWN')
# G.add_node(3, status='UP')
# G.add_node(4, status='UP')
# G.add_node(5, status='UP')

# G.add_edge(1, 2)
# G.add_edge(3, 2)
# G.add_edge(4, 2)
# G.add_edge(5, 1)
# G.add_edge(5, 2)

# G1 = nx.complete_graph(10)
# G1 = nx.star_graph(10)
# G1 = nx.margulis_gabber_galil_graph(3)

def run_epoch(G) -> int:



    for node in G.nodes(data=True):
        node[1]['metadata'] = Node()

    # pos = nx.spring_layout(G)

    # device_represantation = NodeRepresantation()

    total_count_of_failures = 0

    for i in  range(1000):
        
        # print('Starting iteration #' + str(i))
        
        for node in G.nodes(data=True):
            node[1]['metadata'].tick()
            # print(node)
            # print(node[1]['metadata'])

        up_nodes = [x for x,y in G.nodes(data=True) if y['metadata'].status == 'UP']

        # print(up_nodes)
        res = split_brain(list(up_nodes), G)
        if res == True:
            total_count_of_failures += 1
        # print("Result is " + str(res))

        # edge_colors = ['black' if not edge in [] else 'red' for edge in G.edges()]
        # node_colors = [ device_represantation.colourOf(node[1]['metadata'].status) for node in G.nodes(data=True)]

        # nx.draw_networkx_edges(G, pos)
        # nx.draw_networkx_nodes(G, pos, node_color=node_colors)
        # nx.draw_networkx_labels(G, pos)

        # plt.pause(0.2)
    # plt.show()
    print("Total failures: " + str(total_count_of_failures))
    return total_count_of_failures

res = 0
topologyGenerator = NetworkTopologyGenerator()

G = topologyGenerator.get()

for i in range(0, 100):
    print("Iteration #" + str(i))
    res += run_epoch(G)
print("Average: " + str(res/100))
