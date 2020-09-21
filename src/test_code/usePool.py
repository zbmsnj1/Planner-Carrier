import pandas as pd
import os 
import glob

import time
import multiprocessing 
from multiprocessing import Pool

domain = '../../../benchmarks/acrobatics/domain.pddl'

prob= [
'../../../benchmarks/acrobatics/p01.pddl',
'../../../benchmarks/acrobatics/p02.pddl',
'../../../benchmarks/acrobatics/p03.pddl',
'../../../benchmarks/acrobatics/p04.pddl',
'../../../benchmarks/acrobatics/p05.pddl',
'../../../benchmarks/acrobatics/p06.pddl',
'../../../benchmarks/acrobatics/p07.pddl',
'../../../benchmarks/acrobatics/p08.pddl',
'../../../benchmarks/elevators/p09.pddl',
'../../../benchmarks/elevators/p10.pddl',
'../../../benchmarks/elevators/p11.pddl',
'../../../benchmarks/elevators/p12.pddl',
'../../../benchmarks/elevators/p13.pddl',
'../../../benchmarks/elevators/p14.pddl',
'../../../benchmarks/elevators/p15.pddl']

os.chdir('../Experiment/PRP/src/')

def basic_func(doma, prob):
    os.system('./prp '+doma+' '+prob+' --dump-policy 2')


    
if __name__ == '__main__':
    starttime = time.time()
    
    #pool = Pool(processes = 8)  # 可以同时跑3个进程
    pool = Pool(multiprocessing.cpu_count()-1)
    for i in range(0,8):
        pool.apply_async(basic_func,(domain, prob[i]))
    pool.close()
    pool.join()
    
    
        
    print('That took {} seconds'.format(time.time() - starttime))



