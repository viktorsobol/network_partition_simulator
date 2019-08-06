import graph_generators as gg
import simple_network_partition_modeling as modeling
import Config as c
from datetime import datetime
from Config import Configuration
import threading

class Means:
    up = 0
    down = 0

    def __init__(self, up, down):
        self.up = up
        self.down = down

file_for_equal_mean = open('eq_mean_experiment.txt', 'a+', buffering=0)
file_for_NOT_equal_mean = open('NOT_eq_mean_experiment.txt', 'a+', buffering=0)

means = [Means(50, 15), Means(50, 10), Means(50, 5), Means(50,1)]

epoch_lenght = 1000

def write_result_to_file(mean: Means, result: int, g_number: int, file):
    result_string = '[{}],g_number={},m_up={},m_down={},epoch_lenght={},res={}\n'.format(str(datetime.now()),g_number, mean.up, mean.down, epoch_lenght, result)
    file.write(result_string)    



def write_equals_means_experiment_results(mean: Means, res: int, g_number: int):
    result_string = '[{}],g_number={},m_up={},m_down={},epoch_lenght={},res={}\n'.format(str(datetime.now()),g_number, mean.up, mean.down, epoch_lenght, res)
    file_for_equal_mean.write(result_string)
    
def experiment_equal_means(G, g_number):
    #Trying different means
    for mean in means:
        # 100 epochs for each mean
        for iteration in range(100):
            res = modeling.run_epoch(G, Configuration(mean.up, mean.down))
            write_equals_means_experiment_results(mean, res, g_number)
            print('EQ_MEAN::: g_number={}, iteration={}, mean_down={}'.format(g_number, iteration, mean.down))
        

##########################
def write_NOT_equals_means_experiment_results(mean: Means, res: int, g_number: int):
    result_string = '[{}],g_number={},m_m_up={},m_m_down={},epoch_lenght={},res={}\n'.format(str(datetime.now()), g_number, mean.up, mean.down, epoch_lenght, res)
    file_for_NOT_equal_mean.write(result_string)
    
def experiment_NOT_equal_means(G, g_number):
    #Trying different means
    for mean in means:
        # 100 epochs for each mean
        for iteration in range(100):
            res = modeling.run_epoch(G, Configuration(mean.up, mean.down).withDeltas(int(mean.up / 10), int(mean.down / 10)))
            write_NOT_equals_means_experiment_results(mean, res, g_number)
            print('EQ_NOT_MEAN::: g_number={}, iteration={}, mean_up={}'.format (g_number, iteration, mean.up))
    

# Run experiment on 100 different graphs 
for g_number in range(100):
    G = gg.small_world_generator(100, 6)
    equal_means_thread = threading.Thread(target = experiment_equal_means, args= (G, g_number))
    NOT_equal_means_thread = threading.Thread(target = experiment_NOT_equal_means, args= (G, g_number))

    equal_means_thread.start()
    NOT_equal_means_thread.start()

    equal_means_thread.join()
    NOT_equal_means_thread.join()



file_for_equal_mean.close()
file_for_NOT_equal_mean.close()