import argparse
import os
import subprocess
import csv
import pandas as pd
from distutils.dir_util import copy_tree, remove_tree
import utils
import processdata
import gentask
import json
import run

PLANNERS_ID = [1,2]
PLANNERS_NAME = ['prp','sat']



class Planner:
    def __init__(self):
        self.planner_src_folder_name = "src"      
      
    def get_command(self, rel_d_path, rel_p_path):
        abs_d_path = os.path.join(utils.ROOT_PATH, rel_d_path)
        abs_p_path = os.path.join(utils.ROOT_PATH, rel_p_path)
        files_command = f"{abs_d_path} {abs_p_path}"
        return files_command

    def create_tempsrc(self, planner_name, job_id):
        abs_src_path = os.path.join(utils.PLANNER_PATH, planner_name, self.planner_src_folder_name)
        temp_src_path = f"{abs_src_path}{job_id}"
        copy_tree(abs_src_path,temp_src_path)
        return temp_src_path

    def remove_tempsrc(self, planner_name, job_id):
        abs_src_path = os.path.join(utils.PLANNER_PATH, planner_name, self.planner_src_folder_name)
        abs_temp_path = f"{abs_src_path}{job_id}"
        try:
            remove_tree(abs_temp_path)
        except:
            print("No such file or directory")
    
    def output_path(self, rel_p_path, output_folder, planner_name):

        abs_output_path = os.path.join(utils.RESULTS_OUTPUT_PATH, output_folder)
        if not os.path.exists(abs_output_path):
            os.makedirs(abs_output_path)

        abs_output_planner_path = os.path.join(abs_output_path, planner_name)
        if not os.path.exists(abs_output_planner_path):
            os.makedirs(abs_output_planner_path)

        prob_pddl = os.path.basename(rel_p_path)
        prob_id = os.path.splitext(prob_pddl)[0]

        prob_dir = os.path.dirname(rel_p_path)
        prob_name = os.path.basename(prob_dir)

        output = f"{prob_name}_{prob_id}.txt"
        abs_out_path = os.path.join(abs_output_planner_path, output)

        return abs_out_path   

    def save_into_csv(self, output_folder, planner_name, csv_head, list_keywords, list_keyfunc, list_keyignore):
        #clear all files in /results/output folder before process data
        abs_data_output_path = os.path.join(utils.RESULTS_DATA_PATH, output_folder)
        if not os.path.exists(abs_data_output_path):
            os.makedirs(abs_data_output_path)

        abs_data_output_planner_path = os.path.join(abs_data_output_path, planner_name)
        if not os.path.exists(abs_data_output_planner_path):
            os.makedirs(abs_data_output_planner_path)

        old_files =  os.listdir(abs_data_output_planner_path)
        for f in old_files:
            os.remove(os.path.join(abs_data_output_planner_path, f))

        
        #get all txt files in /results/output folder
        abs_output_path = os.path.join(utils.RESULTS_OUTPUT_PATH, output_folder, planner_name)
        output_files = os.listdir(abs_output_path)
        output_files.sort()
        filename = ""

        for file in output_files:
            (tempfn, p_id) = processdata.file_name_id(file, getboth=True)
            

            data = processdata.get_keydata(abs_output_path, file, list_keywords, list_keyfunc, list_keyignore)
            data.insert(0, p_id)

            if(filename != tempfn):
                filename = tempfn	
                #print(filename)
                with open(os.path.join(abs_data_output_planner_path,f"{filename}.csv"), 'w') as csvf:
                    data_writer = csv.writer(csvf)
                    data_writer.writerow(csv_head)
                    data_writer.writerow(data)
            else:
                with open(os.path.join(abs_data_output_planner_path,f"{filename}.csv"), 'a+') as csvf:
                    data_writer = csv.writer(csvf)
                    data_writer.writerow( data)

            #print(p_id)	
                            
    

    def generate_list(self,planner_name, output_folder, alist):

        if alist==False:
            abs_data_path = os.path.join(utils.RESULTS_DATA_PATH, output_folder, planner_name)
            (list_indx, list_name, list_size) = processdata.get_csv_size(abs_data_path)

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

    def data_mean(self, planner_name, output_folder, column_names, title, list_name, list_size):
        
        abs_data_path = os.path.join(utils.RESULTS_DATA_PATH, output_folder, planner_name )
        csv_files = os.listdir(abs_data_path)
        csv_files.sort()
        #print(csv_files)
        all_means=[]
        new_list_name = []
        for i in range(len(list_name)):
            for csvf in csv_files:
                csv_name = processdata.file_name_id(csvf)
                if list_name[i]==csv_name:
                    means = processdata.calcu_mean(csvf, abs_data_path, column_names, list_size[i] )
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
        mean_planner_path = os.path.join(mean_outfolder_path, output_folder)
        if not os.path.exists(mean_planner_path):
            os.makedirs(mean_planner_path)
        abs_mean_path = os.path.join(mean_planner_path, save_file_name)
        df.to_csv(abs_mean_path, index=False)
        print(f"{df}\n")


class PRP(Planner):
    def __init__(self):
        self.name = "PRP"
        self.COLUMN_NAMES = ["Id","Solve", "Time","Size"]
        self.TITLE = ['Domain (# inst)','%solve',"time",'size']
        self.KEY_WORDS = ["Strong cyclic plan found", "Total time", "State-Action Pairs"]
        self.KEY_WORDS_FUNCTION = [processdata.KF.FIND_KW,  processdata.KF.MAX_FLOAT, processdata.KF.MAX_INT]
        self.KEY_WORDS_IGNORE = [processdata.KEY_IGNORE,  processdata.KEY_IGNORE, "Forbidden"]
        super().__init__()

    def get_command(self, rel_d_path, rel_p_path):
        command=f"./prp {super().get_command(rel_d_path, rel_p_path)} --dump-policy 2"
        return command

    def create_tempsrc(self, job_id):    
        return super().create_tempsrc(self.name, job_id)

    def remove_tempsrc(self, job_id):
        super().remove_tempsrc(self.name, job_id)

    def output_path(self, rel_p_path, output_folder):
        return super().output_path( rel_p_path, output_folder, self.name)

    def save_into_csv(self, output_folder):
        print("Collecting data:PRP......")
        super().save_into_csv(output_folder, self.name,  self.COLUMN_NAMES, self.KEY_WORDS, self.KEY_WORDS_FUNCTION, self.KEY_WORDS_IGNORE )
        
    def generate_list(self, output_folder, alist):
        return super().generate_list(self.name, output_folder, alist)
            
    def data_mean(self, list_name, list_size, output_folder):
        super().data_mean(self.name, output_folder, self.COLUMN_NAMES, self.TITLE, list_name, list_size)   


class SAT(Planner):
    def __init__(self):
        self.name ="SAT" 
        self.COLUMN_NAMES = ["Id","Atoms","Actions","Solve","Time","Size"]
        self.TITLE = ['Domain (# inst)','#at','#acts','%solve',"time",'size']
        self.KEY_WORDS = ["Atoms","Actions","SATISFIABLE","Cumulated solver time","Trying with"]
        self.KEY_WORDS_FUNCTION = [processdata.KF.MAX_INT, processdata.KF.MAX_INT, processdata.KF.FIND_KW, processdata.KF.MAX_FLOAT,  processdata.KF.MAX_INT]
        self.KEY_WORDS_IGNORE = [processdata.KEY_IGNORE, processdata.KEY_IGNORE, processdata.KEY_IGNORE, processdata.KEY_IGNORE, processdata.KEY_IGNORE]
        super().__init__()

    def get_command(self, rel_d_path, rel_p_path):
        command=f"python main.py {super().get_command(rel_d_path, rel_p_path)}"
        return command

    def create_tempsrc(self, job_id):      
        return super().create_tempsrc(self.name, job_id)

    def remove_tempsrc(self, job_id):
        super().remove_tempsrc(self.name, job_id)

    def output_path(self, rel_p_path, output_folder):
        return super().output_path( rel_p_path, output_folder, self.name)

    def save_into_csv(self, output_folder):
        print("Collecting data:SAT......")
        super().save_into_csv(output_folder, self.name,  self.COLUMN_NAMES, self.KEY_WORDS, self.KEY_WORDS_FUNCTION, self.KEY_WORDS_IGNORE)

    def generate_list(self, output_folder, alist):
        return super().generate_list(self.name, output_folder, alist)

    def data_mean(self, list_name, list_size, output_folder):
        super().data_mean(self.name, output_folder, self.COLUMN_NAMES, self.TITLE, list_name, list_size)	
        




def create_planner(name, job_id, hide_info:bool=False):
    if name == 'sat':
        planner_instance = SAT()
    elif name == 'prp':
        planner_instance = PRP()

    if not hide_info:
        print(f"Start job {job_id}:")
        print(f"Create {name} planner successfully")
    return planner_instance

def run_planner(planner_instance, d, p, job_id, output_folder):
    
    temp_src = planner_instance.create_tempsrc(job_id)
    print('Create temporary work environment successfully')

    os.chdir(temp_src)
    print('Start running the planning job...')

    with open(planner_instance.output_path(p, output_folder), 'w') as outputf:
        print(f"Writing stdout into {planner_instance.output_path(p, output_folder)}")              
        subprocess.run(planner_instance.get_command(d,p), stdout=outputf, shell=True)   
    print('Finish running the planning job!')

    planner_instance.remove_tempsrc(job_id) 
    print('Remove temporary work environment successfully')

def get_input_files():
    parser = argparse.ArgumentParser()
    parser.add_argument("domain")
    parser.add_argument("problem")
    parser.add_argument("planner")
    parser.add_argument("job_id")
    parser.add_argument("output_folder")
    args = parser.parse_args()

    return args.domain, args.problem, args.planner, args.job_id, args.output_folder
    
if __name__ == '__main__':
    (d, p, planner_name, job_id, output_folder) = get_input_files()
    planner_instance = create_planner(planner_name, job_id)
    run_planner(planner_instance, d, p, job_id, output_folder)