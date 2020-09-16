import pandas as pd
import os 
import glob

import time
import multiprocessing 
from multiprocessing import Pool

import ray
ray.init(address='192.168.232.129:30000', redis_password='5241590000000000')

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


    
futures=[]

@ray.remote
def basic_func(doma, prob):
    os.chdir('../Experiment/PRP/src/')
    os.system('./prp '+doma+' '+prob+' --dump-policy 2')


if __name__ == '__main__':
    starttime = time.time()
    for i in range(0,8):
        futures.append(basic_func.remote(domain, prob[i]))
        

ray.get(futures)


print('That took {} seconds'.format(time.time() - starttime))






