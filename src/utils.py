from pathlib import Path
import os


#define the root path 
def get_project_root() -> Path:
    return Path(__file__).parent.parent
    

ROOT_PATH = get_project_root() 
TASK_PATH = os.path.join(ROOT_PATH, "src/task")
DB_PATH_PATH = os.path.join(ROOT_PATH, "Database/path")
BENCHMARK_PATH= os.path.join(ROOT_PATH, "benchmarks")
DB_BENCHMARKS_PATH = os.path.join(ROOT_PATH, "Database/benchmarks.csv")