import argparse
import os
import time
import math
import subprocess
import multiprocessing
import pandas as pd
from utils import get_project_root

import asyncssh, asyncio
import logging
#logging.basicConfig(level='DEBUG')
import ray



ray.init()

root_path = get_project_root()
task_path=str(root_path)+'/src/task/'
path_path=str(root_path)+'/Database/path/'
prp_path=str(root_path)+'/planners/PRP/src/'
sat_path=str(root_path)+'/planners/SAT/src/'
text_path_prp=str(root_path)+'/text/prp/'
text_path_sat=str(root_path)+'/text/sat/'


def prp_command(domain_path, problem_path):
    problem_name = problem_path.replace("/", "_");
    return './prp '+domain_path+' '+problem_path+' --dump-policy 2' +' | egrep -w "Strong cyclic plan found|Total time|   State-Action Pairs" >'+text_path_prp+problem_name+'.txt'

def sat_command(domain_path, problem_path):
    problem_name = problem_path.replace("/", "_");
    return 'python main.py '+domain_path+' '+problem_path +' | egrep -w "Atoms|Actions|Trying with|Cumulated solver time|SATISFIABLE" >'+text_path_sat+problem_name+'.txt'



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
 
#the function run planner with domain and problem
@ray.remote     
def run_planner(d, p, planner):    
    if planner=='prp':
        os.chdir(prp_path)
        #subprocess.Popen(prp_command(d, p), shell=True)
        subprocess.call(prp_command(d, p), shell=True)
        #return output
        os.system(prp_command(d, p))
    elif planner=='sat':
        os.chdir(sat_path)
        #subprocess.Popen(sat_command(d, p), shell=True)
        subprocess.call(sat_command(d, p), shell=True)
        #os.system(sat_command(d, p))
    

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
        st = time.time()
        count=0

        for i in range(len(all_p)):
            count+=1          
            futures.append(run_planner.remote(all_d[i], all_p[i], all_planner[i]))            

        results = ray.get(futures)

        
        print(results) 
        et = time.time()
        print(et - st)
        print('count:'+str(count))

else:    
    print('Task does not exist!\nPlease use command: python3 run.py task')
    exit()
    
        
