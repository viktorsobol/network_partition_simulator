import networkx as nx
import matplotlib.pyplot as plt

def show(G):

    pos = nx.spring_layout(G)

    node_colors = [ 'green' for node in G.nodes(data=True)]

    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_nodes(G, pos, node_color=node_colors)
    nx.draw_networkx_labels(G, pos)

    plt.pause(0.2)
    plt.show()