import argparse
import os
import math
import pandas as pd
from utils import get_project_root


root_path = get_project_root()
task_path=str(root_path)+'/src/task/'
path_path=str(root_path)+'/Database/path/'
prp_path=str(root_path)+'/planners/PRP/src/'
sat_path=str(root_path)+'/planners/SAT/src/'

#all task domain files and problem files
all_d = []
all_p = []
all_planner=[]

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
def run_planner(d, p, planner):    
    if planner=='prp':
        os.chdir(prp_path)
        os.system('./prp '+d+' '+p+' --dump-policy 2')
    elif planner=='sat':
        os.chdir(sat_path)
        os.system('python main.py '+d+' '+p)
    print('\n\n\n\n')

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
     
    (all_d,all_p,all_planner)=get_path(d, s, e, p)
    
    count=0
    for i in range(len(all_p)):
        count+=1
        run_planner(all_d[i], all_p[i], all_planner[i])
    
    print('count:'+str(count))
    '''
    csv_list = [ all_d,all_p,all_planner]
    csv_list = [[row[i] for row in csv_list] for i in range(len(csv_list[0]))]
    
    df2 = pd.DataFrame(csv_list, columns=[ 'domain_path', 'problem_path',  'planner'])
    df2.index += 1 
    df2.to_csv('123.csv', index_label='index')
    print(df2)
    '''
   
else:    
    print('Task does not exist!\nPlease use command: python3 run.py task')
    exit()
