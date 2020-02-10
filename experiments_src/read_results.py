import os
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chisquare


def read_results(exp_id: str) -> (list, list):
    file_name = 'results/' + exp_id + '.txt'

    result_file = open(file_name, 'r')

    eq_node_results_line = result_file.readline()
    eq_node_results = list(
        map(int,
            eq_node_results_line[len('eq_node_results: ['):len(eq_node_results_line) - 2].split(', '))
    )

    different_node_results_line = result_file.readline()
    different_node_results = list(
        map(int,
            different_node_results_line[len('diff_node_results: ['):len(different_node_results_line) - 2].split(', '))
    )
    return eq_node_results, different_node_results


def print_pearson_checks(exp_id: str):
    eq_node_results, different_node_results = read_results(exp_id)

    print(eq_node_results)
    result = chisquare(eq_node_results, f_exp=different_node_results)

    print(exp_id + ': ' + str(result))



def save_experiments_hist(exp_id: str):
    eq_node_results, different_node_results = read_results(exp_id)

    print(exp_id)
    min_bin = min(min(different_node_results), min(eq_node_results))
    max_bin = max(max(different_node_results), max(eq_node_results))
    bins = list(
        np.arange(
            min_bin,
            max_bin,
            (max_bin - min_bin) / 20
        )
    )

    plt.hist(np.asarray(eq_node_results), bins=bins, alpha=0.5,  density=True, label='eq')
    plt.hist(np.asarray(different_node_results), bins=bins, alpha=0.5, density=True, label='diff')
    plt.title('Histogram of Reliability\n' + exp_id)
    plt.legend(loc='upper right')
    plt.xlabel('Fails')
    plt.ylabel('Probability')
    plt.savefig('results/' + exp_id + '.png')
    plt.clf()


files = os.listdir('results/')
exp_ids = list(map(lambda x: x[:len(x) - 4], files))

# [save_experiments_hist(exp_id) for exp_id in exp_ids]
[print_pearson_checks(exp_id) for exp_id in exp_ids]
