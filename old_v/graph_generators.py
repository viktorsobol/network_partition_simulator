import networkx as nx

def random_regular_graph() -> nx.Graph:
    return nx.random_regular_graph(6, 10)

def small_world_generator(n = 100, k = 6):
    return nx.watts_strogatz_graph(n, k, 0.5)

