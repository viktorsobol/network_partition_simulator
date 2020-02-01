import logging
import numpy as np

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
    
