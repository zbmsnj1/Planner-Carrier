import pandas as pd
import os 
import glob

fpath='../benchmarks/' 
folder_name=os.listdir(fpath)
folder_name.sort()





def listdir(path, list_name):  # 传入存储的list
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
            
        elif os.path.splitext(file_path)[1] == '.pddl':
              list_name.append(file_path)
                
 
def savecsv():
    list_name=[]
    listdir(path,list_name)
    list_name.sort()
	
    csv_list = [ list_name]
    csv_list = [[row[i] for row in csv_list] for i in range(len(csv_list[0]))]

    df1 = pd.DataFrame(csv_list, columns=['path'])
    df1.to_csv(folder_name[i]+'.csv', index=True)

    print(df1)
    

for i in range(len(folder_name)):
    path='../benchmarks/'+folder_name[i]+'/'   #文件夹路径
    savecsv()



