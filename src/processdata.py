import pandas as pd
import csv
import os
import re
from enum import Enum
import gentask
import planner
import utils
import argparse
import sys
import run
import json


KEY_IGNORE = "@@KEY^^IGNORE"
RE_FLOAT = r"\d+\.\d+"
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
        if re.findall(regex,line):
                number = re.findall(regex,line)[0]
                if(float(number) > temp):
                    temp = float(number)
        else:
            print(file.name)
            print(f"Not find corresponding number of [{keyword}] in the following line:")
            print(line)
    return temp

def get_keydata(output_file_path, list_keywords, list_keyfunc, list_keyignore):
    data=[]				
    for i in range(len(list_keyfunc)):
        if(list_keyfunc[i]==KF.FIND_KW):
            with open(output_file_path, 'r') as f:
                d = find_keyword(list_keywords[i], list_keyignore[i], f)
                if d==0 :
                    data.append(d)
                    break		
        elif(list_keyfunc[i]==KF.MAX_FLOAT):
            with open(output_file_path, 'r') as f:
                d = max_number(list_keywords[i], list_keyignore[i],f,RE_FLOAT)
        elif(list_keyfunc[i]==KF.MAX_INT):
            with open(output_file_path, 'r') as f:
                d = max_number(list_keywords[i], list_keyignore[i],f, RE_INT)
                d = int(d)
        data.append(d)
    
    return data

def get_csv_size(abs_data_path):
    csv_files = os.listdir(abs_data_path)
    csv_files.sort()
    list_indx = []
    list_name = []
    list_size = []
    indx=0
    for csvf in csv_files:
        csv_name = file_name_id(csvf)
        df = pd.read_csv(os.path.join(abs_data_path, csvf))
        csv_size = len(df.index)
        indx += 1
        list_indx.append(indx)
        list_name.append(csv_name)
        list_size.append(csv_size)
        print(f"{indx} {csv_name}({csv_size})")
    return list_indx, list_name, list_size

def calcu_mean( csvfile, abs_output_path, column_names, list_size):
    df = pd.read_csv(os.path.join(abs_output_path, csvfile))
    #remove Id from list but not change the orignal list, we dont need calculate the mean of Id
    column_names = column_names[1:]
    means= []
    for i in range(len(column_names)):
        try:
            means.append(df[column_names[i]].iloc[list_size].mean())
        except:
            print(f"ERROR: list is out of range!")
    #print(means)
    return  means

def generate_list(output_folder, alist, planner_name):

    if alist==False:
        abs_data_path = os.path.join(utils.RESULTS_DATA_PATH, output_folder, planner_name)
        (list_indx, list_name, list_size) = get_csv_size(abs_data_path)

        new_list_name=[]
        new_list_size=[]

        show_str = ('\nPlease select data range for processing:\n'+ 
                    '0.All problems for all domains\n'+
                    'a,b-c.Custom specific problems range for selected a,b-c domains'+ ', All problems for remaining domains\n')
        
        list_all =  gentask.get_range(list_indx,show_str, reverse=True)
        list_spec = list(set(list_indx)-set(list_all))
        list_spec.sort()

        print(f"\nCustom range for domains Id={list_spec}")
        for d in list_all:
            new_list_name.append(list_name[list_indx.index(d)])
            size = []
            for i in range(list_size[list_indx.index(d)]):    
                size.append(i)

            new_list_size.append(size)
            #print(prob_ep)

    
        if list_spec:
            show_str1 = ('Please select problems range for testing:\n'+
                    '0.Move to next domain\n'+
                    'a,b-c.Custom specific problems range for selected domain\n')
            for d in list_spec:
                while True:
                    size=[]
                    print('\n',d,'  ', list_name[list_indx.index(d)],'   size:', list_size[list_indx.index(d)])
                    size = gentask.get_range(int(list_size[list_indx.index(d)]),show_str1, true_zero=True)
                    if not size:
                        break
                    print(size)     
                    size = [i - 1 for i in size]
                    new_list_name.append(list_name[list_indx.index(d)])
                    new_list_size.append(size)
        save_list_str= '\nDo you want to save the list for furture use?\n 1.Yes\n 2.No\n'  
        save_list = gentask.check_end(save_list_str)
        if save_list:
            str = '\nPlease enter a list name(exclude ".txt") for saving list into a txt file:\n'
            save_list_name = run.get_input_str(str)
            new_lists = [new_list_name, new_list_size]
            list_outfolder_path = os.path.join(utils.RESULTS_LIST_PATH, output_folder)
            if not os.path.exists(list_outfolder_path):
                os.makedirs(list_outfolder_path)

            with open(os.path.join(list_outfolder_path, f"{save_list_name}.txt"), "w") as fsl:
                json.dump(new_lists, fsl)


        same_list_str = '\nDo you want to use the same range for remaining planners?\n 1.Yes\n 2.No, I wish to custom range remaining planners\n'       
        same_list = gentask.check_end(same_list_str)
        #print(new_list_name)
        #print(new_list_size)
    else:
        alist_path = os.path.join(utils.RESULTS_LIST_PATH, output_folder, alist)
        with open(alist_path, "r") as fp:
            alists = json.load(fp)
        new_list_name = alists[0]
        new_list_size = alists[1]
        same_list = True    

    return new_list_name, new_list_size, same_list


def save_data_into_csv(planner, output_folder):
    #clear all files in /results/output folder before process data
    abs_data_output_path = os.path.join(utils.RESULTS_DATA_PATH, output_folder)
    if not os.path.exists(abs_data_output_path):
        os.makedirs(abs_data_output_path)

    abs_data_output_planner_path = os.path.join(abs_data_output_path, planner.name)
    if not os.path.exists(abs_data_output_planner_path):
        os.makedirs(abs_data_output_planner_path)

    old_files =  os.listdir(abs_data_output_planner_path)
    for f in old_files:
        os.remove(os.path.join(abs_data_output_planner_path, f))

    
    #get all txt files in /results/output folder
    abs_output_path = os.path.join(utils.RESULTS_OUTPUT_PATH, output_folder, planner.name)
    output_files = os.listdir(abs_output_path)
    output_files.sort()
    filename = ""

    for file_path in output_files:
        (problem_name, p_id) = file_name_id(file_path, getboth=True)
        output_file_path = os.path.join(abs_output_path, file_path)
        data = planner.extract_data(output_file_path)
        data.insert(0, p_id)

        if(filename != problem_name):
            filename = problem_name	
            #print(filename)
            with open(os.path.join(abs_data_output_planner_path,f"{filename}.csv"), 'w') as csvf:
                data_writer = csv.writer(csvf)
                data_writer.writerow(planner.COLUMN_NAMES)
                data_writer.writerow(data)
        else:
            with open(os.path.join(abs_data_output_planner_path,f"{filename}.csv"), 'a+') as csvf:
                data_writer = csv.writer(csvf)
                data_writer.writerow( data)

        #print(p_id)
    # sort by prob id
    new_files =  os.listdir(abs_data_output_planner_path)
    for f in new_files:
        df = pd.read_csv(os.path.join(abs_data_output_planner_path, f))
        df["Id"] = df["Id"].astype('int')
        df = df.sort_values(by=['Id'])   
        df.to_csv(os.path.join(abs_data_output_planner_path, f),index=False)


def data_mean( output_folder, column_names, title, list_name, list_size, planner_name ):
        
    abs_data_path = os.path.join(utils.RESULTS_DATA_PATH, output_folder, planner_name )
    csv_files = os.listdir(abs_data_path)
    csv_files.sort()
    #print(csv_files)
    all_means=[]
    new_list_name = []
    for i in range(len(list_name)):
        for csvf in csv_files:
            csv_name = file_name_id(csvf)
            if list_name[i]==csv_name:
                means = calcu_mean(csvf, abs_data_path, column_names, list_size[i] )
                all_means.append(means)
                break
        name_ = list_name[i]
        size_ = len(list_size[i])
        first_ = list_size[i][0]+1
        last_ = list_size[i][-1]+1
        name = f"{name_}({size_}:{first_}-{last_})"
        new_list_name.append(name)
            
    for i in range(len(all_means)):
        all_means[i].insert(0, new_list_name[i])

    df = pd.DataFrame(all_means, columns=title)
    save_file=input('\nPlease enter a task name(exclude ".csv") for saving mean data into a csv file:\n')
    save_file_name = f"{save_file}.csv"
    mean_outfolder_path = os.path.join(utils.RESULTS_MEAN_PATH, output_folder)
    if not os.path.exists(mean_outfolder_path):
        os.makedirs(mean_outfolder_path)
    mean_planner_path = os.path.join(mean_outfolder_path, planner_name)
    if not os.path.exists(mean_planner_path):
        os.makedirs(mean_planner_path)
    abs_mean_path = os.path.join(mean_planner_path, save_file_name)
    df.to_csv(abs_mean_path, index=False)
    print(f"{df}\n")
    

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

def get_output_folder_and_list():
    #get the name of task file 
    parser = argparse.ArgumentParser()
    parser.add_argument("output_folder")
    parser.add_argument("list")
    args = parser.parse_args()
    output_folder_path = os.path.join(utils.RESULTS_OUTPUT_PATH, args.output_folder)
    list_path = os.path.join(utils.RESULTS_LIST_PATH, args.output_folder, args.list)


    if os.path.exists(output_folder_path):
        if os.path.exists(list_path):
            return args.output_folder, args.list
        elif args.list=="nolist":
            return args.output_folder, False
        else:
            print("Error: can not find the list!")
            print("Please use command: python3 processdata.py [output folder] [list]")
            print("If no suitable lists, input 'nolist' in [list], then you can generate a list manually")
            sys.exit()
        
    else:
        print("Error: can not find the folder!")
        sys.exit()

	

if __name__ == '__main__':    
    same_list = False
    (output_folder, alist) = get_output_folder_and_list()           
    select_planners = choose_planner()
    for planner_name in select_planners:
        planner_instance = planner.create_planner(planner_name)
        save_data_into_csv(planner_instance, output_folder)
        if not same_list:
            (list_name, list_size, same_list) = generate_list(output_folder, alist, planner_instance.name)			
        data_mean(output_folder, planner_instance.COLUMN_NAMES, planner_instance.TITLE, list_name, list_size, planner_instance.name)

	






