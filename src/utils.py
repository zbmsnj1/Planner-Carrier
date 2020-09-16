from pathlib import Path


#define the root path 
def get_project_root() -> Path:
    return Path(__file__).parent.parent
    

