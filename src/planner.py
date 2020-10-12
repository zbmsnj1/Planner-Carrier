import argparse
import os
import subprocess
from distutils.dir_util import copy_tree, remove_tree
from utils import get_project_root

ROOT_PATH = get_project_root()


class Planner:
    def __init__(self):
        pass
      
    def get_command(self, rel_d_path, rel_p_path):
        abs_d_path = os.path.join(ROOT_PATH, rel_d_path)
        abs_p_path = os.path.join(ROOT_PATH, rel_p_path)
        files_command = f"{abs_d_path} {abs_p_path}"
        return files_command

    def create_tempsrc(self, rel_src_path, job_id):
        abs_src_path = os.path.join(ROOT_PATH, rel_src_path)
        temp_src_path = f"{abs_src_path}{job_id}"
        copy_tree(abs_src_path,temp_src_path)
        return temp_src_path

    def remove_tempsrc(self, rel_src_path, job_id):
        abs_src_path = os.path.join(ROOT_PATH, rel_src_path)
        abs_temp_path = f"{abs_src_path}{job_id}"
        try:
            remove_tree(abs_temp_path)
        except:
            print("No such file or directory")
    
    def output_path(self, rel_res_path, rel_p_path):
        abs_res_path = os.path.join(ROOT_PATH, rel_res_path)
        prob_pddl = os.path.basename(rel_p_path)
        prob_id = os.path.splitext(prob_pddl)[0]

        prob_dir = os.path.dirname(rel_p_path)
        prob_name = os.path.basename(prob_dir)

        output = f"{prob_name}_{prob_id}.txt"
        abs_out_path = os.path.join(abs_res_path, output)

        return abs_out_path
        

class SAT(Planner):
    def __init__(self):
        self.REL_SRC_PATH = "planners/SAT/src"  
        self.REL_RES_PATH = "results/SAT/output" 
        super().__init__()

    def get_command(self, rel_d_path, rel_p_path):
        command=f"python main.py {super().get_command(rel_d_path, rel_p_path)}"
        return command

    def create_tempsrc(self, job_id):      
        return super().create_tempsrc(self.REL_SRC_PATH, job_id)

    def remove_tempsrc(self, job_id):
        super().remove_tempsrc(self.REL_SRC_PATH, job_id)

    def output_path(self, rel_p_path):
        return super().output_path(self.REL_RES_PATH, rel_p_path)
        

class PRP(Planner):
    def __init__(self):
        self.REL_SRC_PATH = "planners/PRP/src" 
        self.REL_RES_PATH = "results/PRP/output"   
        super().__init__()

    def get_command(self, rel_d_path, rel_p_path):
        command=f"./prp {super().get_command(rel_d_path, rel_p_path)} --dump-policy 2"
        return command

    def create_tempsrc(self, job_id):    
        return super().create_tempsrc(self.REL_SRC_PATH, job_id)

    def remove_tempsrc(self, job_id):
        super().remove_tempsrc(self.REL_SRC_PATH, job_id)

    def output_path(self, rel_p_path):
        return super().output_path(self.REL_RES_PATH, rel_p_path)

def create_planner(name, job_id):
    if name == 'sat':
        planner = SAT()
    elif name == 'prp':
        planner = PRP()

    print(f"Start job {job_id}:")
    print(f"Create {name} planner successfully")
    return planner

def run_planner(planner, d, p, job_id):
    
    temp_src = planner.create_tempsrc(job_id)
    print('Create temporary work environment successfully')

    os.chdir(temp_src)
    print('Start running the planning job...')

    with open(planner.output_path(p), 'w') as outputf:
        print(f"Writing stdout into {planner.output_path(p)}")              
        subprocess.run(planner.get_command(d,p), stdout=outputf, shell=True)   
    print('Finish running the planning job!')

    planner.remove_tempsrc(job_id) 
    print('Remove temporary work environment successfully')

def get_input_files():
    parser = argparse.ArgumentParser()
    parser.add_argument("domain")
    parser.add_argument("problem")
    parser.add_argument("planner")
    parser.add_argument("job_id")
    args = parser.parse_args()

    return args.domain, args.problem, args.planner, args.job_id
    
if __name__ == '__main__':
    (d, p, planner_name, job_id) = get_input_files()
    planner = create_planner(planner_name, job_id)
    run_planner(planner, d, p, job_id)