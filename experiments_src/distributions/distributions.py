import logging
import numpy as np
from random import random
from experiment_data import *

logging.basicConfig(level=logging.INFO)


class BaseDistribution:

    def __init__(self, name: str):
        logging.info(name + ' distribution is created')

    def next(self) -> int:
        logging.error('BaseDistribution next() is not implemented')
        return -1


class PoissonDistribution(BaseDistribution):

    def __init__(self, params: dict):
        self.mean = params['mean']
        BaseDistribution.__init__(self, 'poisson')

    def next(self) -> int:
        return np.random.poisson(self.mean)


class NormalDistribution(BaseDistribution):

    def __init__(self, params: dict):
        logging.info(params)
        self.mean = params['mean']
        self.deviation = params['deviation']
        BaseDistribution.__init__(self, 'normal')

    def next(self) -> int:
        return int(np.random.normal(loc=self.mean, scale=self.deviation, size=None))


def build_distribution_for_equal_nodes(d: DistributionData) -> (BaseDistribution, BaseDistribution):
    if d.distribution_type == 'poisson':
        return PoissonDistribution(d.equal_node_params['up']), PoissonDistribution(d.equal_node_params['down'])
    elif d.distribution_type == 'normal':
        return NormalDistribution(d.equal_node_params['up']), NormalDistribution(d.equal_node_params['down'])
    else:
        raise Exception('Distribution type is not supported yet.')


def build_distribution_for_different_nodes(d: DistributionData) -> (BaseDistribution, BaseDistribution):

    deviation = int(d.different_node_params['deviation'])
    diff_coefficient = (1 + deviation * (2 * random() - 1))

    if d.distribution_type == 'poisson':
        adjusted_params_up = d.different_node_params['up']
        adjusted_params_up['mean'] = adjusted_params_up['mean'] * diff_coefficient

        adjusted_params_down = d.different_node_params['down']
        adjusted_params_down['mean'] = adjusted_params_down['mean'] * diff_coefficient

        return PoissonDistribution(adjusted_params_up), PoissonDistribution(adjusted_params_down)

    elif d.distribution_type == 'normal':
        adjusted_params_up = d.different_node_params['up']
        adjusted_params_up['mean'] = adjusted_params_up['mean'] * diff_coefficient
        adjusted_params_up['deviation'] = adjusted_params_up['deviation'] * diff_coefficient

        adjusted_params_down = d.different_node_params['down']
        adjusted_params_down['mean'] = adjusted_params_down['mean'] * diff_coefficient
        adjusted_params_down['deviation'] = adjusted_params_down['deviation'] * diff_coefficient

        return NormalDistribution(adjusted_params_up), NormalDistribution(adjusted_params_down)

    else:
        raise Exception('Distribution type is not supported yet.')

