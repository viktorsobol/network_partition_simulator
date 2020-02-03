import networkx as nx
from networkx import Graph


def generate_random_regular_graph(params: dict) -> nx.Graph:
    d = params['connectivity']
    n = params['nodes_number']
    return nx.random_regular_graph(d, n)


def generate_small_world_graph(params: dict):
    n = params['nodes_count']
    k = params['join_nearest_node_count']
    p = params['probability_of_rewiring']
    return nx.watts_strogatz_graph(n, k, p)


def split_brain(g: Graph) -> bool:
    nodes_up = [x for x, y in g.nodes(data=True) if y['metadata'].status == 'UP']

    to_visit = {nodes_up[0]: 1} if len(nodes_up) > 0 else {}
    visited = {}

    while len(to_visit) > 0:
        to_visit_node = to_visit.popitem()
        new_nodes = list(g.adj[to_visit_node[0]])
        visited[to_visit_node[0]] = 1
        for new_node in new_nodes:
            if g.nodes(data=True)[new_node]['metadata'].status == 'DOWN':
                continue
            if new_node in visited:
                continue
            to_visit[new_node] = 1

    return len(visited) != len(nodes_up)
