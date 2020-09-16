import pandas as pd
import os 
import glob
import time
from utils import get_project_root


root_path = get_project_root()

domain = '../../../benchmarks/acrobatics/domain.pddl'

prob= [
str(root_path)+'/benchmarks/acrobatics/p01.pddl',
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
    
starttime = time.time()
for i in range(0,1):
    
    #time.sleep(2)
    basic_func(domain, prob[i])
  
#print(os.getcwd())  
print('That took {} seconds'.format(time.time() - starttime))
