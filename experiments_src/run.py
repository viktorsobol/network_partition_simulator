import sys
import json
from nodes.nodemetadata import NodeMetadata
from distributions.distributions import *
from graph.graphs import *
from copy import deepcopy


def build_base_network_topology(experiment_data):
    if experiment_data.graph_data.network_type == 'SMALL_WORLD':
        return generate_small_world_graph(experiment_data.graph_data.params)
    elif experiment_data.graph_data.network_type == 'REGULAR':
        return generate_random_regular_graph(experiment_data.graph_data.params)
    else:
        raise Exception('Graph type is not supported yet.')


def build_network_with_equal_nodes(g: Graph, experiment_data: ExperimentData) -> Graph:

    up_distribution, down_distribution = build_distribution_for_equal_nodes(experiment_data.distribution_data)

    for node in g.nodes(data=True):
        node_metadata = NodeMetadata(up_distribution, down_distribution)
        node[1]['metadata'] = node_metadata

    if experiment_data.execution_model.run_type == ExecutionModel.SEQUENTIAL_EXECUTION_MODEL:
        for node in g.nodes(data=True):
            node[1]['metadata'].time_left = int(random() * node[1]['metadata'].time_left)

    return g


def build_network_with_different_nodes(g: Graph, experiment_data: ExperimentData) -> Graph:

    for node in g.nodes(data=True):
        up_distribution, down_distribution = build_distribution_for_different_nodes(experiment_data.distribution_data)
        node_metadata = NodeMetadata(up_distribution, down_distribution)
        node[1]['metadata'] = node_metadata

    if experiment_data.execution_model.run_type == ExecutionModel.SEQUENTIAL_EXECUTION_MODEL:
        for node in g.nodes(data=True):
            node[1]['metadata'].time_left = int(random() * node[1]['metadata'].time_left)

    return g


def run_epoch(g: Graph, epoch_length: int) -> int:

    total_count_of_failures = 0

    for i in range(epoch_length):

        print(i)
                
        for node in g.nodes(data=True):
            node[1]['metadata'].tick()

        if split_brain(g):
            total_count_of_failures += 1
  
    print("Total failures: " + str(total_count_of_failures))
    return total_count_of_failures


def save_results(eq_node_results: list, different_node_results: list, experiment_data: ExperimentData):
    file_name = 'results/' + str(experiment_data.id) + '.txt'
    file = open(file_name, 'a+')

    file.write('eq_node_results: ' + str(eq_node_results) + '\n')
    file.write('diff_node_results: ' + str(different_node_results))
    file.write('\njson\n')
    file.write(experiment_data.json())
    file.flush()
    file.close()


def run(experiment_params_file: str):

    experiment_data = ExperimentData(json.load(open(experiment_params_file)))

    g_base = build_base_network_topology(experiment_data)

    network_with_equal_nodes = build_network_with_equal_nodes(deepcopy(g_base), experiment_data)
    network_with_different_nodes = build_network_with_different_nodes(deepcopy(g_base), experiment_data)

    equal_node_results = []
    different_node_results = []

    for _ in range(experiment_data.epochs_count):
        equal_node_result = run_epoch(network_with_equal_nodes, experiment_data.epoch_length)
        different_node_result = run_epoch(network_with_different_nodes, experiment_data.epoch_length)

        equal_node_results.append(equal_node_result)
        different_node_results.append(different_node_result)

    save_results(equal_node_results, different_node_results, experiment_data)


file_with_experiment_metadata = str(sys.argv[1])
run(file_with_experiment_metadata)
