import argparse
import os
import time
import math
import copy
import subprocess
import multiprocessing
import pandas as pd
import shutil
from utils import get_project_root
import dask
from dask.distributed import Client, SSHCluster, LocalCluster, progress
import asyncssh, asyncio
import logging
#logging.basicConfig(level='DEBUG')
#import ray
from distutils.dir_util import copy_tree, remove_tree



#ray.init(address='192.168.232.129:6379')

root_path = get_project_root()
task_path=str(root_path)+'/src/task/'
path_path=str(root_path)+'/Database/path/'
prp_path=str(root_path)+'/planners/PRP/src/'
prp =str(root_path)+'/planners/PRP/src/'
sat_path=str(root_path)+'/planners/SAT/src/'
text_path_prp=str(root_path)+'/text/prp/'
text_path_sat=str(root_path)+'/text/sat/'



def copy_dir(src_dir, i):
    src_dir = src_dir[:-1]
    copy_tree(str(src_dir), str(src_dir+str(i)))
    return str(src_dir+str(i))

new_dir=copy_dir(str(prp_path),1)



print(str(new_dir))

remove_tree(str(new_dir)) 

