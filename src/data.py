import pandas as pd
import csv
import os 
import re
from enum import Enum
from utils import get_project_root
from task import get_range, check_end, PLANNERS_ID, PLANNERS_NAME

ROOT_PATH = get_project_root() 
KEY_IGNORE = "@@KEY^^IGNORE"
RE_FLOAT = r"\d+\.\d+|\d+"
RE_INT = r"\d+"
DOT_ABC = r"\.[a-z]*"
_ABC_NUM_DOT_ABC = r"_[a-z]*\d*.[a-z]*"
ABC_ = r"[a-z]*_"

#Basedata methods
class Basem(Enum): 
	FIND_KW = "method: find_keyword()"
	MAX_INT = "method: max_number(RE_INT)"
	MAX_FLOAT = "method: max_number(RE_FLOAT)"


class Basedata:
	def __init__(self):
		pass
	
	def match_keyword(self,keyword, keyword_ignore, file):
		lines=[]
		RE_KEYWORD = rf"\b{keyword}\b"  
		RE_KEYWORD_IGNORE =  rf"\b{keyword_ignore}\b"  
		for line in file:				
			if bool(re.findall(RE_KEYWORD, line)) and not bool(re.findall(RE_KEYWORD_IGNORE, line)):
				lines.append(line)
								
		return lines

	def file_name_id(self,file, getboth):
		if getboth:
			p_name = re.sub(_ABC_NUM_DOT_ABC, "", file)
			p_id = re.sub(ABC_, "",file)
			p_id = re.findall(RE_INT, p_id)
			return p_name, p_id[0]
		else:
			p_name = re.sub(DOT_ABC, "", file)
			return p_name


	def find_keyword(self,keyword, keyword_ignore, file):
		find = 1
		not_find = 0
		if not self.match_keyword(keyword, keyword_ignore, file):
			return not_find
		else:
			return find

	def max_number(self,keyword, keyword_ignore,file, regex):
		lines = self.match_keyword(keyword, keyword_ignore, file)
		temp = 0.0000000000
		for line in lines:
			try:
				number = re.findall(regex,line)[0]
				if(float(number) > temp):
					temp = float(number)
			except:
				print("ERROR: Not find key word!!!")
		return temp

	def get_keydata(self, abs_res_path, file, list_keywords, list_keyfunc, list_keyignore):
		data=[]				
		for i in range(len(list_keyfunc)):
			if(list_keyfunc[i]==Basem.FIND_KW):
				with open(os.path.join(abs_res_path, file), 'r') as f:
					d = self.find_keyword(list_keywords[i], list_keyignore[i], f)		
			elif(list_keyfunc[i]==Basem.MAX_FLOAT):
				with open(os.path.join(abs_res_path, file), 'r') as f:
					d = self.max_number(list_keywords[i], list_keyignore[i],f,RE_FLOAT)
			elif(list_keyfunc[i]==Basem.MAX_INT):
				with open(os.path.join(abs_res_path, file), 'r') as f:
					d = self.max_number(list_keywords[i], list_keyignore[i],f, RE_INT)
					d = int(d)
			data.append(d)
		
		return data

	def get_allfiles(self, rel_res_path):
		abs_res_path = os.path.join(ROOT_PATH, rel_res_path )
		output_files = os.listdir(abs_res_path)
		output_files.sort()
		return output_files

	def save_into_csv(self, rel_res_path, rel_data_path, csv_head, list_keywords, list_keyfunc, list_keyignore):
		abs_res_path = os.path.join(ROOT_PATH, rel_res_path )
		output_files = os.listdir(abs_res_path)
		output_files.sort()
		filename = ""

		for file in output_files:
			(tempfn, p_id) = self.file_name_id(file, True)
			

			data = self.get_keydata(abs_res_path, file, list_keywords, list_keyfunc, list_keyignore)
			data.insert(0, p_id)

			if(filename != tempfn):
				filename = tempfn	
				#print(filename)
				with open(os.path.join(ROOT_PATH, rel_data_path,f"{filename}.csv"), 'w') as csvf:
					data_writer = csv.writer(csvf)
					data_writer.writerow(csv_head)
					data_writer.writerow(data)
			else:
				with open(os.path.join(ROOT_PATH, rel_data_path,f"{filename}.csv"), 'a+') as csvf:
					data_writer = csv.writer(csvf)
					data_writer.writerow( data)

			#print(p_id)	
			 			
	def get_csv_size(self, rel_data_path):
		abs_res_path = os.path.join(ROOT_PATH, rel_data_path )
		csv_files = os.listdir(abs_res_path)
		csv_files.sort()
		list_indx = []
		list_name = []
		list_size = []
		indx=0
		for csvf in csv_files:
			csv_name = self.file_name_id(csvf, False)
			df = pd.read_csv(os.path.join(abs_res_path, csvf))
			csv_size = len(df.index)
			indx += 1
			list_indx.append(indx)
			list_name.append(csv_name)
			list_size.append(csv_size)
			print(f"{indx} {csv_name}({csv_size})")
		return list_indx, list_name, list_size

	def generate_list(self, rel_data_path):
		(list_indx, list_name, list_size) = self.get_csv_size(rel_data_path)

		new_list_name=[]
		sizes=[]
	
		show_str = ('\nPlease select data range for processing:\n'+ 
					'0.All problems for all domains\n'+
					'a,b-c.Custom specific problems range for selected a,b-c domains'+ ', All problems for remaining domains\n')
		
		list_all =  get_range(list_indx,show_str, True)
		list_spec = list(set(list_indx)-set(list_all))
		list_spec.sort()

		print(f"\nCustom range for domains {list_spec}")
		for d in list_all:
			new_list_name.append(list_name[list_indx.index(d)])
			size = []
			for i in range(list_size[list_indx.index(d)]):    
				size.append(i)

			sizes.append(size)
			#print(prob_ep)

		end_input_str = '\nMove to next domain?\n 1.Yes\n 2.No, I wish to contiune\n'

		if list_spec:
			show_str1 = ('Please select problems range for testing:\n'+
                 '0.All problems for selected domain\n'+
                 'a,b-c.Custom specific problems range for selected domain\n')
			for d in list_spec:
				while True:
					size=[]
					print('\n',d,'  ', list_name[list_indx.index(d)],'   size:', list_size[list_indx.index(d)])
					size = get_range(int(list_size[list_indx.index(d)]),show_str1,False)
					size = [i - 1 for i in size]
					new_list_name.append(list_name[list_indx.index(d)])
					sizes.append(size)
					print(size)
					if check_end(end_input_str):
						break

		#print(new_list_name)
		#print(sizes)

		return new_list_name, sizes
	
	def calcu_mean(self, csvfile, abs_res_path, column_names, list_size):
		df = pd.read_csv(os.path.join(abs_res_path, csvfile))
		#remove Id from list but not change the orignal list, we dont need calculate the mean of Id
		column_names = column_names[1:]
		means= []
		for i in range(len(column_names)):

			means.append(df[column_names[i]].iloc[list_size].mean())
		
		#print(means)
		return  means
	
	def data_mean(self, rel_data_path, rel_mean_path, column_names, title):
		(list_name, list_sizes) = self.generate_list(rel_data_path)
		abs_res_path = os.path.join(ROOT_PATH, rel_data_path )
		csv_files = os.listdir(abs_res_path)
		csv_files.sort()
		#print(csv_files)
		all_means=[]
		new_list_name = []
		for i in range(len(list_name)):
			for csvf in csv_files:
				csv_name = self.file_name_id(csvf, False)
				if list_name[i]==csv_name:
					means = self.calcu_mean(csvf, abs_res_path, column_names, list_sizes[i] )
					all_means.append(means)
					break
			name_ = list_name[i]
			size_ = len(list_sizes[i])
			first_ = list_sizes[i][0]+1
			last_ = list_sizes[i][-1]+1
			name = f"{name_}({size_}:{first_}-{last_})"
			new_list_name.append(name)
				
		for i in range(len(all_means)):
			all_means[i].insert(0, new_list_name[i])

		df = pd.DataFrame(all_means, columns=title)
		save_file_name=input('\nPlease enter a task name(exclude ".csv") for saving mean data into a csv file:\n')
		save_file = f"{save_file_name}.csv"
		df.to_csv(f"{os.path.join(ROOT_PATH, rel_mean_path, save_file)}", index=False)
		print(f"{df}\n")



class SATdata(Basedata):
	def __init__(self):
		self.REL_RES_PATH = "results/SAT/output"
		self.REL_DATA_PATH = "results/SAT/data"
		self.REL_MEAN_PATH = "results/SAT/mean"
		self.COLUMN_NAMES = ["Id","Atoms","Actions","Solve","Time","Size"]
		self.TITLE = ['Domain (# inst)','#at','#acts','%solve',"time",'size']
		self.KEY_WORDS = ["Atoms","Actions","SATISFIABLE","Cumulated solver time","Trying with"]
		self.KEY_WORDS_METHOD = [Basem.MAX_INT, Basem.MAX_INT, Basem.FIND_KW, Basem.MAX_FLOAT,  Basem.MAX_INT]
		self.KEY_WORDS_IGNORE = [KEY_IGNORE, KEY_IGNORE, KEY_IGNORE, KEY_IGNORE, KEY_IGNORE]
		super().__init__()

	def save_into_csv(self):
		print("Collecting data:SAT......")
		super().save_into_csv(self.REL_RES_PATH, self.REL_DATA_PATH, self.COLUMN_NAMES, self.KEY_WORDS, self.KEY_WORDS_METHOD, self.KEY_WORDS_IGNORE)

	def data_mean(self):
		super().data_mean(self.REL_DATA_PATH, self.REL_MEAN_PATH, self.COLUMN_NAMES, self.TITLE)	

class PRPdata(Basedata):
	def __init__(self):
		self.REL_RES_PATH = "results/PRP/output"
		self.REL_DATA_PATH = "results/PRP/data"
		self.REL_MEAN_PATH = "results/PRP/mean"
		self.COLUMN_NAMES = ["Id","Solve","Time","Size"]
		self.TITLE = ['Domain (# inst)','%solve',"time",'size']
		self.KEY_WORDS = ["Strong cyclic plan found", "Total time", "State-Action Pairs"]
		self.KEY_WORDS_METHOD = [Basem.FIND_KW, Basem.MAX_FLOAT, Basem.MAX_INT]
		self.KEY_WORDS_IGNORE = [KEY_IGNORE, KEY_IGNORE, "Forbidden"]
		super().__init__()

	def save_into_csv(self):
		print("Collecting data:PRP......")
		super().save_into_csv(self.REL_RES_PATH, self.REL_DATA_PATH, self.COLUMN_NAMES, self.KEY_WORDS, self.KEY_WORDS_METHOD, self.KEY_WORDS_IGNORE )
		
			
	def data_mean(self):
		super().data_mean(self.REL_DATA_PATH, self.REL_MEAN_PATH, self.COLUMN_NAMES, self.TITLE)


def choose_planner( ):

    show_str = ("\nPlease select which planner's results for data processing:\n 1.prp\n 2.sat\n"+
                 "0.All planners \n"+
                 'a,b-c.Select specific planners\n')
    select_planners = get_range(PLANNERS_ID,show_str, False)
    planners_name = []
    for planner_id in select_planners:
        planners_name.append(PLANNERS_NAME[PLANNERS_ID.index(planner_id)])  
    print(f"Selected planners: {planners_name}\n")

    return planners_name
	

if __name__ == '__main__':

	select_planners = choose_planner()
	for planner_name in select_planners:
		if planner_name == 'prp':
			planner = PRPdata()
		elif planner_name == 'sat':
			planner = SATdata()
		planner.save_into_csv()
		planner.data_mean()

	






