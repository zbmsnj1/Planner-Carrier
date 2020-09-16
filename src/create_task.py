import pandas as pd
import os 
import glob

import mysql.connector
from mysql.connector import Error
from utils import get_project_root

#this file is help users to decide 1.which domain 2.how many problems 3.which planner 4.how many cpus
root_path = get_project_root()
cpu_max = 4
planners = ['prp', 'sat']
domain_indexs=[]
domain_names=[]
prob_start_points = []
prob_end_points = []
chosed_planners = []
cpu_nums = []

#get the index of which domain users want to test
def get_domain_index(rowcount):
    while True:
        try:
            domain_index = int(input('Please chose which domain you want to test:\n'))
            if domain_index in range(1,rowcount+1):               
                break
        except (ValueError):
            pass
        print('Wrong input vaule!')
        continue
    return domain_index
    
#get the start point of problems users want to test 
def get_prob_start_point(inst_size):
    while True:
        try:
            prob_sp = int(input('Please enter the START point of the problems you want to test:\n0.All'+'\nFrom range'+' 1-'+ str(inst_size)+'\n'))            
            if prob_sp in range(0,inst_size+1):               
                break
        except (ValueError):
            pass
        print('Wrong input vaule!')
        continue
    return prob_sp   

#get the end point of problems users want to test 
def get_prob_end_point(prob_sp, inst_size):
    while True:
        try:
            prob_ep = int(input('Please enter the END point of the problems you want to test:\n'+'From range '+str(prob_sp)+'-'+ str(inst_size)+'\n'))
            if prob_ep in range(1,inst_size+1) and prob_sp <= prob_ep:               
                break
        except (ValueError):
            pass
        print('Wrong input vaule!')
        continue
    return prob_ep   
    
#get which planner users want to test 
def get_planner():
    while True:
        try:
            planner_id = int(input('Please select one planner for testing:\n 1.prp\n 2.sat\n'))
            if planner_id in range(1,len(planners)+1):               
                break
        except (ValueError):
            pass
        print('Wrong input vaule!')
        continue
    return planner_id   
    
#get the number of cpus users want to test
def get_cpu_num():
    while True:
        try:
            cpu_num = int(input('Please enter how many CPUs you want to use for testing:\n'))
            if cpu_num in range(1,cpu_max+1):               
                break
        except (ValueError):
            pass
        print('Wrong input vaule!')
        continue
    return cpu_num    

#end program
def check_end():
    while True:
        try:
            input_num = int(input('Have you finished entering data?\n 1.Yes\n 2.No, I wish to contiune\n'))
            if input_num in range(1,3):  
                if input_num == 1:
                    return True
                else: 
                    return False             
                break
        except (ValueError):
            pass
        print('Wrong input vaule!')
        continue
    return False  
    
#the online mysql host      
'''  
host="den1.mysql6.gear.host",
      user="benchmarks",
      password="Mx9G0h8q?9W_"  
'''  
    
#the local mysql host        
'''             
try:  
    connection = mysql.connector.connect(host='localhost',
                                         database='planning_benchmarks',
                                         user='root',
                                         password='2747')

    sql_select_Query = "select * from benchmarks"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall() 
    print('MySQL connection is started...')
    print("Total number of domains in benchmarks is: ", cursor.rowcount)   
    mat = "{:1}\t{:28}\t{:1}" 
      
    while True:  
        print(mat.format('\nIndex','Domain name', '#inst'))
        for row in records:       
            print(mat.format(row[0], row[1], row[2]))
          
        domain_index = get_domain_index(cursor.rowcount)    
        domain_indexs.append(domain_index)

        for row in records:   
            if (row[0] == domain_index):
                domain_names.append(row[1])
                inst_size = row[2]    
   
        prob_start_point = get_prob_start_point(inst_size) 
        if prob_start_point == 0:
            prob_start_point = 1
            prob_end_point = row[2]
        else:    
            prob_end_point = get_prob_end_point(prob_start_point, inst_size)
            
        prob_start_points.append(prob_start_point)
        prob_end_points.append(prob_end_point)
        
        planner_id = get_planner()
        chosed_planners.append(planners[planner_id-1])
        
        #cpu_num = get_cpu_num()
        #cpu_nums.append(cpu_num)
        
        if check_end():
            task_name=input('Please enter a task name for saving your task data into a csv file:\n')
            break
        
except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")
'''


#the virtual database in local
while True:
    bm = pd.read_csv(str(root_path) +'/Database/benchmarks.csv') 
    print('\n') 
    print(bm.to_string(index=False))
    
    domain_index = get_domain_index(len(bm))    
    domain_indexs.append(domain_index)
    
    for i in bm['index']:            
            if (i == domain_index):
                domain_names.append(bm['domain_name'][i-1])
                problem_size = bm['problem_size'][i-1] 
                break
    
    prob_start_point = get_prob_start_point(problem_size) 
    if prob_start_point == 0:
        prob_start_point = 1
        prob_end_point = problem_size
    else:    
        prob_end_point = get_prob_end_point(prob_start_point, problem_size)
        
    prob_start_points.append(prob_start_point)
    prob_end_points.append(prob_end_point)
    
    planner_id = get_planner()
    chosed_planners.append(planners[planner_id-1])
    
    #cpu_num = get_cpu_num()
    #cpu_nums.append(cpu_num)
    
    if check_end():
        task_name=input('Please enter a task name for saving your task data into a csv file:\n')
        break            
                


#write task data into csv
csv_list = [ domain_names, prob_start_points, prob_end_points, chosed_planners]
csv_list = [[row[i] for row in csv_list] for i in range(len(csv_list[0]))]

df = pd.DataFrame(csv_list, columns=[ 'domain_name', 'start_problem', 'end_problem', 'planner'])
df.index += 1 
df.to_csv('task/'+task_name+'.csv', index_label='index')

print(df)
















