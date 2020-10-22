import argparse
import os
import subprocess
import csv
import pandas as pd
from distutils.dir_util import copy_tree, remove_tree
import utils
import processdata

PLANNERS_ID = [1,2]
PLANNERS_NAME = ['prp','sat']



class Planner:
    def __init__(self, planner_name):
        self.planner_name = planner_name 
        self.planner_src_folder_name = "src" 
           

    def create_tempsrc(self, job_id):
        abs_src_path = os.path.join(utils.PLANNER_PATH, self.planner_name, self.planner_src_folder_name)
        temp_src_path = f"{abs_src_path}{job_id}"
        copy_tree(abs_src_path,temp_src_path)
        return temp_src_path

    def remove_tempsrc(self, job_id):
        abs_src_path = os.path.join(utils.PLANNER_PATH, self.planner_name, self.planner_src_folder_name)
        abs_temp_path = f"{abs_src_path}{job_id}"
        try:
            remove_tree(abs_temp_path)
        except:
            print("No such file or directory")

    def run_and_save(self, planner_command, job_id, output_file_path):
        print(f"Start job {job_id}:")
        print(f"Create {self.planner_name} planner successfully")
        temp_src = self.create_tempsrc(job_id)
        print('Create temporary work environment successfully')

        os.chdir(temp_src)
        print('Start running the planning job...')

        with open(output_file_path, 'w') as outputf:
            print(f"Writing stdout into {output_file_path}")              
            subprocess.run(planner_command, stdout=outputf, shell=True)   
        print('Finish running the planning job!')

        self.remove_tempsrc(job_id) 
        print('Remove temporary work environment successfully') 

    
                         
 

    

class PRP(Planner):
    def __init__(self):
        self.name = "PRP"
        self.COLUMN_NAMES = ["Id","Solve", "Time","Size"]
        self.TITLE = ['Domain (# inst)','%solve',"time",'size']
        super().__init__(self.name)

    def get_command(self, rel_d_path, rel_p_path):
        abs_d_path = os.path.join(utils.ROOT_PATH, rel_d_path)
        abs_p_path = os.path.join(utils.ROOT_PATH, rel_p_path)
        return f"./prp {abs_d_path} {abs_p_path} --dump-policy 2"
        
    def extract_data(self, output_file_path):
        list_keywords = ["Strong cyclic plan found", "Total time", "State-Action Pairs"]
        list_keyfunc = [processdata.KF.FIND_KW,  processdata.KF.MAX_FLOAT, processdata.KF.MAX_INT]
        list_keyignore = [processdata.KEY_IGNORE,  processdata.KEY_IGNORE, "Forbidden"]
               
        data = processdata.get_keydata(output_file_path, list_keywords, list_keyfunc, list_keyignore)
        return  data



class SAT(Planner):
    def __init__(self):
        self.name ="SAT" 
        self.COLUMN_NAMES = ["Id","Atoms","Actions","Solve","Time","Size"]
        self.TITLE = ['Domain (# inst)','#at','#acts','%solve',"time",'size']
        super().__init__(self.name)

    def get_command(self, rel_d_path, rel_p_path):
        abs_d_path = os.path.join(utils.ROOT_PATH, rel_d_path)
        abs_p_path = os.path.join(utils.ROOT_PATH, rel_p_path)
        return f"python main.py {abs_d_path} {abs_p_path}"

    def extract_data(self, output_file_path):
        list_keywords = ["Atoms","Actions","SATISFIABLE","Elapsed solver time","Trying with"]
        list_keyfunc = [processdata.KF.MAX_INT, processdata.KF.MAX_INT, processdata.KF.FIND_KW, processdata.KF.MAX_FLOAT,  processdata.KF.MAX_INT]
        list_keyignore = [processdata.KEY_IGNORE, processdata.KEY_IGNORE, processdata.KEY_IGNORE, processdata.KEY_IGNORE, processdata.KEY_IGNORE]
                            
        data = processdata.get_keydata(output_file_path, list_keywords, list_keyfunc, list_keyignore)
        return  data



    
        
def get_output_txt_path(rel_p_path, output_folder, planner_name):

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




def create_planner(name):
    if name == 'sat':
        planner_instance = SAT()
    elif name == 'prp':
        planner_instance = PRP()
        
    return planner_instance


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
    (rel_d_path, rel_p_path, planner_name, job_id, output_folder) = get_input_files()
    planner_instance = create_planner(planner_name)
    planner_command = planner_instance.get_command(rel_d_path, rel_p_path)
    output_txt_path = get_output_txt_path(rel_p_path, output_folder, planner_instance.name)
    planner_instance.run_and_save(planner_command, job_id, output_txt_path)
   