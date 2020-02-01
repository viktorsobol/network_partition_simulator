import sys
import json
import matplotlib.pyplot as plt
from distributions import PoissonDistribution
from distributions import NormalDistribution

def show_poisson_distribution(params: dict):
    poisson_distribution = PoissonDistribution(params)
    l = {}
    for _ in range(0, 10000):
        res = poisson_distribution.next()
        if res in l:
            l[res] += 1
        else:
            l[res] = 1

    plt.scatter(list(l.keys()), list(l.values()))
    plt.ylabel('Poisson distribution')
    plt.show()

def show_normal_distribution(params: dict):
    normal_distribution = NormalDistribution(params)
    l = {}
    for _ in range(0, 10000):
        res = normal_distribution.next()
        if res in l:
            l[res] += 1
        else:
            l[res] = 1

    plt.scatter(list(l.keys()), list(l.values()))
    plt.ylabel('Normal distribution')
    plt.show()


args = sys.argv
if args[1] == 'normal':
    show_normal_distribution(json.loads(args[2]))
elif args[1] == 'poisson':
    show_poisson_distribution(json.loads(args[2]))
else:
    print('Distribution is not supported.')



