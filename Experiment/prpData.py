import pandas as pd
import os 
import glob
    
#get number and names of files in SAT/data

csv_files = sorted(glob.glob('PRP/data/*.csv') )
  
csv_names=[]
solve=[]
time=[]
size=[]
num_inst = 0

def calcu_mean(f_path):
	df = pd.read_csv(f_path) 

	# block 1 - simple stats Atoms,Actions,Solve,Time,Size
	mean1 = df['Solve'].mean()
	mean2 = df['Time'].mean()
	mean3 = df['Size'].mean()
	num_inst = len(df.index)
	
	solve.append(mean1)
	time.append(mean2)
	size.append(mean3)
	return num_inst
	

for i in csv_files:
	
	f_name=os.path.splitext(i)[0]
	f_name=os.path.split(f_name)[1]
	f_name = f_name+'('+str(calcu_mean(i))+')'
	csv_names.append(f_name)
	
csv_list = [csv_names, solve, time, size]

csv_list = [[row[i] for row in csv_list] for i in range(len(csv_list[0]))]




df1 = pd.DataFrame(csv_list, columns=['Domain (# inst)','%solve',"time",'size'])
df1.to_csv('prpData.csv', index=False)

print(df1)


