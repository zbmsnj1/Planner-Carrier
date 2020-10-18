from pathlib import Path
import os


#define the root path 
def get_project_root() -> Path:
    return Path(__file__).parent.parent
    

ROOT_PATH = get_project_root() 
TASK_PATH = os.path.join(ROOT_PATH, "src/task")
DB_PATH_PATH = os.path.join(ROOT_PATH, "Database/path")
BENCHMARK_PATH= os.path.join(ROOT_PATH, "benchmarks")
RESULTS_OUTPUT_PATH = os.path.join(ROOT_PATH, "results/output")
RESULTS_DATA_PATH = os.path.join(ROOT_PATH, "results/data")
RESULTS_MEAN_PATH = os.path.join(ROOT_PATH, "results/mean")
RESULTS_LIST_PATH = os.path.join(ROOT_PATH, "results/list")
DB_BENCHMARKS_PATH = os.path.join(ROOT_PATH, "Database/benchmarks.csv")
PLANNER_PATH = os.path.join(ROOT_PATH, "planners")
