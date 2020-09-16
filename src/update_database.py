import pandas as pd
import os 
import glob
from utils import get_project_root

problems_sum = []
root_path = get_project_root()
fpath=str(root_path)+'/benchmarks/' 


folder_name=os.listdir(fpath)
folder_name.sort()


def listdir(path, char_, list_name):  # 
    
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
                
        elif os.path.splitext(file_path)[1] == '.pddl':
            f_name=os.path.splitext(file_path)[0]
            f_name=os.path.split(f_name)[1]
            if char_ in f_name:
                list_name.append(file_path)
            
	        
            
                

                
 
def save_file_path_to_csv():
    domain_path=[]
    problem_path=[]
    listdir(path,'d',domain_path)
    listdir(path,'p',problem_path)
    domain_path.sort()
    problem_path.sort()
    
    problems_sum.append(len(problem_path))
    csv_list = [domain_path, problem_path]

    df = pd.DataFrame(csv_list)
    df=df.T
    df.columns=['domain_path','problem_path']
    df.index += 1 
    df.to_csv(str(root_path)+'/Database/path/'+folder_name[i]+'.csv', index_label='index')

    #print(df)

def save_folder_to_csv():  
    csv_list = [folder_name, problems_sum]
    df = pd.DataFrame(csv_list)
    df=df.T
    df.columns=['domain_name','problem_size']
    df.index += 1 
    df.to_csv(str(root_path)+'/Database/benchmarks.csv', index_label='index')

    print(df)  

for i in range(len(folder_name)):
    path='benchmarks/'+folder_name[i]+'/'   #
    os.chdir(root_path)
    save_file_path_to_csv()

save_folder_to_csv()

