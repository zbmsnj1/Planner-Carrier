Evaluation of FOND planners
===========================

This is the project to evaluate the-state-of-art FOND planners by experiments. We will place all the details of experiments and a report about the evaluation.


Directory Structure
-----

`benchmarks/`: the current benchmarks of FOND planning, all '.pddl' files
`Database/`: store relative path of corresponding benchmark file
`planner/`: the source code for the-state-of-art of FOND planners


**Original links of FOND planners**
>>FIP [link](Experiment/FIP)

>>PRP * [Wiki](https://github.com/QuMuLab/planner-for-relevant-policies/wiki)

>>MBP [link](http://mbp.fbk.eu/)

>>SAT [link](https://github.com/tomsons22/FOND-SAT)

>>myND * [Public myND repository](https://bitbucket.org/robertmattmueller/mynd)

### src
>including the code files to updat database, to create task file, to run the planning benchmarks in parallel on a single machine or on a distrubted cluster

#### before running
**there are some packages needed install**

```
python3 -m pip install jupyter-server-proxy
python3 -m pip install asyncssh
python3 -m pip install "dask[complete]"
```
*Update the database after add benchmarks in benchmark folder*
```
python3 update_database.py
```

**Two ways to create task file:**

   ##### Create a task.csv file manually, following the format of the example task files in src/task
   ##### Create a task.csv file using code
    
```
python3 create_task.py
```
![choose domain](https://github.com/lslll0302/Eval-of-FOND-planners-/blob/master/IMG_readme/Screenshot%20from%202020-09-21%2015-36-59.png)
>Choose the index of domains
![start point non-0](https://github.com/lslll0302/Eval-of-FOND-planners-/blob/master/IMG_readme/Screenshot%20from%202020-09-21%2015-43-19.png)
>select how many problems wanted to test in one domain
0. all problems in a domain
non-0. start point or end point
![select a planner](https://github.com/lslll0302/Eval-of-FOND-planners-/blob/master/IMG_readme/Screenshot%20from%202020-09-21%2015-42-53.png)
>Select one planner to test
![finish](https://github.com/lslll0302/Eval-of-FOND-planners-/blob/master/IMG_readme/Screenshot%20from%202020-09-21%2015-43-02.png)
>Check finish enter data or not
**run the main.py to generate the text files including test data**
```
python3 main.py [task.csv]
```
### results
>the folder contains all the data created by the system




