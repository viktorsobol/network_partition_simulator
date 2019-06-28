import networkx as nx
import matplotlib.pyplot as plt

class NodeRepresantation:
    def colourOf(self, status: str) -> str:
        if status == 'UP':
            return 'green'
        if status == 'DOWN':
            return 'red'
        raise Exception('No such status')

G = nx.Graph()

G.add_node(1, status='UP')
G.add_node(2, status='DOWN')
G.add_node(3, status='UP')
G.add_node(4, status='UP')
G.add_node(5, status='UP')

G.add_edge(1, 2)
G.add_edge(3, 2)
G.add_edge(4, 2)
G.add_edge(5, 1)
G.add_edge(5, 2)


pos = nx.spring_layout(G)

device_represantation = NodeRepresantation()

edge_colors = ['black' if not edge in [] else 'red' for edge in G.edges()]
node_colors = [ device_represantation.colourOf(node[1]['status']) for node in G.nodes(data=True)]

nx.draw_networkx_edges(G, pos)
nx.draw_networkx_nodes(G, pos, node_color=node_colors)
nx.draw_networkx_labels(G, pos)

plt.show()
