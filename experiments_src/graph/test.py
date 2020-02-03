import networkx as nx


def random_regular_graph() -> nx.Graph:
    return nx.random_regular_graph(1, 4)


G = random_regular_graph()

for n in G.nodes(data=True):
    print(n)
    tmp = list(G.adj[n[0]])
    for n1 in  tmp:
        print(n1)
  
    print('\n')

res = nx.edge_connectivity(G)
print(res)
