import pandas as pd
import csv
import os
import re
from enum import Enum
import gentask
import planner
import utils


KEY_IGNORE = "@@KEY^^IGNORE"
RE_FLOAT = r"\d+\.\d+|\d+"
RE_INT = r"\d+"
DOT_ABC = r"\.[a-z]*"
NUM_TXT = r"\d+.txt"
_PNUM_TXT = r"_p\d+.txt"


#Key Functions
class KF(Enum): 
	FIND_KW = "find_keyword()"
	MAX_INT = "max_number(RE_INT)"
	MAX_FLOAT = "max_number(RE_FLOAT)"

def match_keyword(keyword, keyword_ignore, file):
    lines=[]
    RE_KEYWORD = rf"\b{keyword}\b"  
    RE_KEYWORD_IGNORE =  rf"\b{keyword_ignore}\b"  
    for line in file:				
        if bool(re.findall(RE_KEYWORD, line)) and not bool(re.findall(RE_KEYWORD_IGNORE, line)):
            lines.append(line)
                            
    return lines

def file_name_id(file, getboth: bool=False):
    if getboth:
        p_name = re.sub(_PNUM_TXT, "", file)
        p_id = re.findall(NUM_TXT, file)
        p_id = re.findall(RE_INT, p_id[0])
        return p_name, p_id[0]
    else:
        p_name = re.sub(DOT_ABC, "", file)
        return p_name


def find_keyword(keyword, keyword_ignore, file):
    find = 1
    not_find = 0

    if match_keyword(keyword, keyword_ignore, file):
        return find
    else:
        return not_find
        

def max_number(keyword, keyword_ignore,file, regex):
    lines = match_keyword(keyword, keyword_ignore, file)
    temp = 0.0000000000
    for line in lines:
        try:
            number = re.findall(regex,line)[0]
            if(float(number) > temp):
                temp = float(number)
        except:
            print(f"ERROR: Not find key word!!!  {file.name}")
    return temp

def get_keydata(abs_res_path, file, list_keywords, list_keyfunc, list_keyignore):
    data=[]				
    for i in range(len(list_keyfunc)):
        if(list_keyfunc[i]==KF.FIND_KW):
            with open(os.path.join(abs_res_path, file), 'r') as f:
                d = find_keyword(list_keywords[i], list_keyignore[i], f)		
        elif(list_keyfunc[i]==KF.MAX_FLOAT):
            with open(os.path.join(abs_res_path, file), 'r') as f:
                d = max_number(list_keywords[i], list_keyignore[i],f,RE_FLOAT)
        elif(list_keyfunc[i]==KF.MAX_INT):
            with open(os.path.join(abs_res_path, file), 'r') as f:
                d = max_number(list_keywords[i], list_keyignore[i],f, RE_INT)
                d = int(d)
        data.append(d)
    
    return data

def get_allfiles(rel_res_path):
    abs_res_path = os.path.join(utils.ROOT_PATH, rel_res_path )
    output_files = os.listdir(abs_res_path)
    output_files.sort()
    return output_files

def get_csv_size(rel_data_path):
    abs_res_path = os.path.join(utils.ROOT_PATH, rel_data_path )
    csv_files = os.listdir(abs_res_path)
    csv_files.sort()
    list_indx = []
    list_name = []
    list_size = []
    indx=0
    for csvf in csv_files:
        csv_name = file_name_id(csvf)
        df = pd.read_csv(os.path.join(abs_res_path, csvf))
        csv_size = len(df.index)
        indx += 1
        list_indx.append(indx)
        list_name.append(csv_name)
        list_size.append(csv_size)
        print(f"{indx} {csv_name}({csv_size})")
    return list_indx, list_name, list_size

def calcu_mean( csvfile, abs_res_path, column_names, list_size):
    df = pd.read_csv(os.path.join(abs_res_path, csvfile))
    #remove Id from list but not change the orignal list, we dont need calculate the mean of Id
    column_names = column_names[1:]
    means= []
    for i in range(len(column_names)):

        means.append(df[column_names[i]].iloc[list_size].mean())
    
    #print(means)
    return  means

def choose_planner( ):

    show_str = ("\nPlease select which planner's results for data processing:\n 1.prp\n 2.sat\n"+
                 "0.All planners \n"+
                 'a,b-c.Select specific planners\n')
    select_planners = gentask.get_range(planner.PLANNERS_ID,show_str)
    planners_name = []
    for planner_id in select_planners:
        planners_name.append(planner.PLANNERS_NAME[planner.PLANNERS_ID.index(planner_id)])  
    print(f"Selected planners: {planners_name}\n")

    return planners_name
	

if __name__ == '__main__':
	same_list = False
	select_planners = choose_planner()
	for planner_name in select_planners:
		planner_instance = planner.create_planner(planner_name, 0, hide_info=True)

		planner_instance.save_into_csv()
		if not same_list:
			(list_name, list_size, same_list) = planner_instance.generate_list()			
		planner_instance.data_mean(list_name, list_size)

	






