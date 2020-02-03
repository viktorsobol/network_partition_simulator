import numpy as np
from random import randrange
from queue import Queue

QUEUE_SIZE = 20

class PoissonGenerator:
    mean_up = 0
    mean_down = 0
    queueUp = Queue(QUEUE_SIZE)
    queueDown = Queue(QUEUE_SIZE)

    def __init__(self, mean_up, mean_down):
        self.mean_up = mean_up
        self.mean_down = mean_down
    
    def getTime(self, status: str)-> int:
        if status == 'UP':
            # if self.queueUp.empty():
            #     for i in np.random.poisson(self.mean_up, QUEUE_SIZE):
            #         self.queueUp.put(i)
            # return self.queueUp.get()
            return np.random.poisson(self.mean_up)
        if status == 'DOWN':
            # if self.queueDown.empty():
            #     for i in np.random.poisson(self.mean_down, QUEUE_SIZE):
            #         self.queueDown.put(i)
            # return self.queueDown.get()
            return np.random.poisson(self.mean_down)
        raise Exception('No such status' + status)


class Configuration:
    mean_up = 0
    mean_down = 0
    name = ''
    delta_up = 0
    delta_down = 0

    def __init__(self, mean_up, mean_down):
        self.mean_up = mean_up
        self.mean_down = mean_down
        self.name = 'EQ_NODE_EXP'
    
    def withDeltas(self, delt_up: int, delta_down: int):
        self.delta_up = delt_up
        self.delta_down = delta_down
        self.name = 'NOT_EQ_NODE_EXP'
        return self
    
    def generator(self) -> PoissonGenerator:
        if self.name == 'NOT_EQ_NODE_EXP':
            r_up = 0 if self.delta_up <= 0 else randrange(self.delta_up * 2)
            r_down = 0 if self.delta_down <= 0 else randrange(self.delta_down * 2)
            up_change = (0 - self.delta_up + r_up)
            down_change = (0 - self.delta_down + r_down)
            mu = self.mean_up + up_change
            md = self.mean_down + down_change
            return PoissonGenerator(mu, md)
        else:
            return PoissonGenerator(self.mean_up, self.mean_down)