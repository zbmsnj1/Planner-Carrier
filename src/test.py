import pandas as pd
import os 
import glob

import time
import multiprocessing 
from multiprocessing import Pool

import ray
ray.init()



    
futures=[]
def basic_func(x):
    if x == 0:
        return 'zero'
    elif x%2 == 0:
        return 'even'
    else:
        return 'odd'

@ray.remote
def multiprocessing_func(x):
    y = x*x
    time.sleep(2)
    print('{} squared results in a/an {} number'.format(x, basic_func(y)))


if __name__ == '__main__':
    starttime = time.time()
    for i in range(0,100):
        futures.append(multiprocessing_func.remote(i))
        
ray.get(futures)

#print(ray.get(futures))

print('That took {} seconds'.format(time.time() - starttime))


















