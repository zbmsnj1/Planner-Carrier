import argparse
import os
import time
import math
import copy
import subprocess
import multiprocessing
import pandas as pd
from distutils.dir_util import copy_tree, remove_tree
from utils import get_project_root
import dask
from dask.distributed import Client, SSHCluster, LocalCluster, progress
import asyncssh, asyncio
import logging
import json
#logging.basicConfig(level='DEBUG')


class Planner:
    def __init__(self, name,src_path,result_path,command,optional_command,key_words):
        self.name = name
        self.src_path = src_path
        self.result_path = result_path
        self.command = command
        self.optional_command = optional_command
        self.key_words = key_words


root_path = get_project_root()
task_path=str(root_path)+'/src/task/'
path_path=str(root_path)+'/Database/path/'



def set_cluster():
    n_cpu=multiprocessing.cpu_count()
    #set up local cluster using dask
    cluster = LocalCluster(n_workers=n_cpu, threads_per_worker=1,  dashboard_address='0')
    
    #set up ssh cluster using dask
    '''
    cluster = SSHCluster(
            #["localhost",  "118.138.246.177"],
            #connect_options={"known_hosts": None, 'username':'yifan', 'password':'prp2020'},
            ["localhost", "192.168.232.129"],
            connect_options={"known_hosts": None, },
            worker_options={"nthreads": 5, "nprocs": 1},
            scheduler_options={"port": 0, "dashboard_address": ":8790"},)
    '''
    return cluster




#get all problem and domain paths 
def get_path(d, s, e, p):    
    for di,si,ei, planneri in zip(d,s,e,p):
        df1=pd.read_csv(path_path+di+'.csv')
        for pi in range(int(si-1), int(ei)):
            if df1['domain_path'].isnull().values.any():     #if any value is NaN, so the style is (domain p1) (domain p2) (domain p3) (domain p4)... not (d1 p1) (d2 p2) (d3 p3) (d4 p4)...
                all_d.append(str(root_path)+'/'+df1['domain_path'][0])
            else:
                all_d.append(str(root_path)+'/'+df1['domain_path'][pi])                   
            all_p.append(str(root_path)+'/'+df1['problem_path'][pi])
            all_planner.append(planneri)
    return all_d, all_p, all_planner
 
#the function create instance of Planner classs by name
def create_planner(planner_name): 
    # read file
    with open('planners.json', 'r') as json_file:
        # parse file
        data = json.load(json_file)

    # get values
    for d in data['planners']:
        if(planner_name==d['name']):
            planner = Planner(d['name'],d['src_path'], d['result_path'],d['command'],d['optional_command'],d['key_words'])
            break
       
    return planner

#the function create a new copy of planner src, avoid bug while parallel
def copy_dir(src_dir, i):
    src_dir = src_dir[:-1]
    copy_tree(str(src_dir), str(src_dir+str(i)))
    return str(src_dir+str(i))


#the function generate command line for assigned planner
def generate_command(domain_path, problem_path, planner):
    #reduce the prefix of file name
    problem_name = problem_path.replace("/", "_")
    problem_name = problem_name[51:]
    problem_name = problem_name.replace('.pddl', '')
    command = (planner.command + ' ' + domain_path + ' ' + problem_path + ' ' + planner.optional_command + 
              ' | egrep -w ' + planner.key_words + 
              ' >' + str(root_path) + planner.result_path + problem_name + '.txt')

    return command        
    


#the function run planner with domain and problem    
def run_planner(d, p, planner_name,i):  
    #create planner instance by planner name
    planner = create_planner(planner_name)

    new_dir =copy_dir(str(str(root_path)+planner.src_path),i)
    os.chdir(new_dir)
    subprocess.call(generate_command(d, p, planner), shell=True)
    remove_tree(str(new_dir)) 



#get the name of task file
parser = argparse.ArgumentParser()
parser.add_argument("task")
args = parser.parse_args()


#if task exist
if os.path.exists(task_path+args.task):
    df = pd.read_csv(task_path+args.task) 
    d = df['domain_name']
    s = df['start_problem']    
    e = df['end_problem']
    p = df['planner']
     
    #all task domain files and problem files
    all_d = []
    all_p = []
    all_planner=[] 
     
    (all_d,all_p,all_planner)=get_path(d, s, e, p)

    futures=[]

    if __name__ == '__main__':

        cluster = set_cluster()
        client = Client(cluster,asynchronous=True)

        st = time.time()
        count=0
        #dask.config.set(scheduler='threads')

        #'''
        for i in range(len(all_p)):
            count+=1         
            #future = client.submit(run_planner1, i,i) 
            future = client.submit(run_planner, all_d[i], all_p[i], all_planner[i], i) 
            futures.append(future)
        #'''
        '''
        for i in range(len(all_p)):
            run_planner(all_d[i], all_p[i], all_planner[i])
        '''    

        #more efficient
        results = client.gather(futures)
        
        #print(client.get_worker_logs())
        
        #print(results)
        #progress(results)  
        et = time.time()
        print(et - st)
        print('count:'+str(count))

else:    
    print('Task does not exist!\nPlease use command: python3 run.py task')
    exit()
    
        
