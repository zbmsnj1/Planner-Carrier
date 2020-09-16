import pandas as pd
import os 
import glob
    
#get number and names of files in SAT/data

csv_files = sorted(glob.glob('SAT/data/*.csv') )
  
csv_names=[]
atoms=[]
actions=[]
solve=[]
time=[]
size=[]
num_inst = 0

def calcu_mean(f_path):
	df = pd.read_csv(f_path) 

	# block 1 - simple stats Atoms,Actions,Solve,Time,Size
	mean1 = df['Atoms'].mean()
	mean2 = df['Actions'].mean()
	mean3 = df['Solve'].mean()
	mean4 = df['Time'].mean()
	mean5 = df['Size'].mean()
	num_inst = len(df.index)
	
	atoms.append(mean1)
	actions.append(mean2)
	solve.append(mean3)
	time.append(mean4)
	size.append(mean5)
	return num_inst
	

for i in csv_files:
	
	f_name=os.path.splitext(i)[0]
	f_name=os.path.split(f_name)[1]
	f_name = f_name+'('+str(calcu_mean(i))+')'
	csv_names.append(f_name)
	
csv_list = [csv_names, atoms, actions, solve, time, size]

csv_list = [[row[i] for row in csv_list] for i in range(len(csv_list[0]))]




df1 = pd.DataFrame(csv_list, columns=['Domain (# inst)','#at','#acts','%solve',"time",'size'])
df1.to_csv('satData.csv', index=False)

print(df1)


