import argparse
import os
import time
import subprocess
from subprocess import PIPE
import multiprocessing
import pandas as pd
#from dask import dataframe as dd 
from distutils.dir_util import copy_tree, remove_tree
import dask
from dask.distributed import Client, SSHCluster, LocalCluster, progress
import utils


def set_cluster(jobs_sum):
    while True:
        try:
            input_num = int(input('\nWhich mode you wish to run tasks?\n 1.Local machine\n 2.SSH Cluster\n'))
            if input_num in range(1,3):  
                if input_num == 1:
                    n_cpu=multiprocessing.cpu_count()
                    #set up local cluster using dask
                    cluster = LocalCluster(n_workers=n_cpu, threads_per_worker=1,  dashboard_address='0')
                    print(f"Start {jobs_sum} jobs on local machine....\n")
                else: 
                    cluster = SSHCluster(
                    #["localhost",  "118.138.246.177"],
                    #connect_options={"known_hosts": None, 'username':'yifan', 'password':'prp2020'},
                    ["localhost", "192.168.232.129"],
                    connect_options={"known_hosts": None, },
                    worker_options={"nthreads": 5, "nprocs": 1},
                    scheduler_options={"port": 0, "dashboard_address": ":8790"},)   
                    print(f"Start {jobs_sum} jobs on SHH cluster....\n")   
                break
        except (ValueError):
            pass
        print('Wrong input vaule!')
        continue
    return cluster





#get all problem and domain paths 
def get_path(d, s, e, p):    
    for di,si,ei, planneri in zip(d,s,e,p):
        di_file = f"{di}.csv"
        df=pd.read_csv(os.path.join(utils.DB_PATH_PATH, di_file))
        for pi in range(int(si-1), int(ei)):
            if df['domain_path'].isnull().values.any():     #if any value is NaN, so the style is (domain p1) (domain p2) (domain p3) (domain p4)... not (d1 p1) (d2 p2) (d3 p3) (d4 p4)...               
                all_d.append(df['domain_path'][0])
            else:
                all_d.append(df['domain_path'][pi])           
            all_p.append(df['problem_path'][pi])
            all_planner.append(planneri)
    return all_d, all_p, all_planner


def run_jobs(d, p, planner, job_id):
    #if pyhton version >3.6, change stdout=PIPE to capture_output=True
    result = subprocess.run(f"python3 planner.py {d} {p} {planner} {job_id}", stdout=PIPE, shell=True)
    print(result.stdout.decode("utf-8"))
    return result.stdout




def get_files_path():
    #get the name of task file 
    parser = argparse.ArgumentParser()
    parser.add_argument("task")
    args = parser.parse_args()
    task_path = os.path.join(utils.TASK_PATH, args.task)

    try:
        df = pd.read_csv(task_path) 
    except:
        print("Task does not exist!\nPlease use command: python3 run.py [task.csv]")
    
    return df['domain_name'],df['start_problem'],df['end_problem'],df['planner']


if __name__ == '__main__':
    (d,s,e,p) = get_files_path()
    #all task domain files and problem files
    all_d = []
    all_p = []
    all_planner=[] 
     
    (all_d,all_p,all_planner)=get_path(d, s, e, p)

    futures=[]
    cluster = set_cluster(len(all_p))
    client = Client(cluster,asynchronous=True)

    st = time.time()

    #'''
    for i in range(len(all_p)):    
        #run_planner(all_d[i], all_p[i], all_planner[i], i)  
        future = client.submit(run_jobs, all_d[i], all_p[i], all_planner[i], i)             
        futures.append(future)
    results = client.gather(futures)
    '''
    for result in results:
        print(result.decode("utf-8"))
    '''
    #print(results)
 
    et = time.time()
    print(f"Finish {len(all_p)} jobs using {et - st}(s)")

    


