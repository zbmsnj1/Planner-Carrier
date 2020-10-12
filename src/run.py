import argparse
import os
import time
import math
import copy
import subprocess
import multiprocessing
import pandas as pd
import csv
from distutils.dir_util import copy_tree, remove_tree
from utils import get_project_root
import dask
from dask.distributed import Client, SSHCluster, LocalCluster, progress
import asyncssh, asyncio
import logging
import json
#logging.basicConfig(level='DEBUG')



root_path = get_project_root()
json_path = str(root_path)+'/src/planners.json'
task_path=str(root_path)+'/src/task/'
path_path=str(root_path)+'/Database/path/'


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
    with open(json_path, 'r') as json_file:
        # parse file
        data = json.load(json_file)

    # get values
    for d in data['planners']:
        if(planner_name==d['name']):
            planner = Planner(d['name'])
            break
       
    return planner

#the function create a new copy of planner src, avoid bug while parallel
def temp_dir(src_dir, i):
    src_dir = src_dir[:-1]
    return str(src_dir+str(i))


#the function generate command line for assigned planner
       
    


#the function run planner with domain and problem    
def run_planner(d, p, planner_name,i):  
    #create planner instance by planner name
    planner = create_planner(planner_name)

    src_path = str(str(root_path)+planner.src_path)
    temp_src_path =temp_dir(src_path,i)

    #call copy_tree in temp_dir() function will have bug, attributeerror: 'NoneType' object has no attribute 'endswith'
    copy_tree(src_path,temp_src_path)

    os.chdir(temp_src_path)
    #.run
    subprocess.run(generate_command(d, p, planner), shell=True)

    remove_tree(str(temp_src_path)) 

def test(d, p, planner_name):
    print(d,p,planner_name)


#get the name of task file
parser = argparse.ArgumentParser()
parser.add_argument("task")
args = parser.parse_args()


#if task exist
if os.path.exists(task_path+args.task):
    '''
    with open(task_path+args.task) as csvfile:
        d=[]
        s=[]
        e=[]
        p=[]
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            d.append(row[1])
            s.append(row[2])
            e.append(row[3])
            p.append(row[4])
    '''       
    #print(d,s,e,p)
    df = pd.read_csv(task_path+args.task) 
    d = df['domain_name']
    s = df['start_problem']    
    e = df['end_problem']
    p = df['planner']
     
   # print(d,s,e,p) 
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
            #future = client.submit(test, all_d[i], all_p[i], all_planner[i]) 
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
    
        
