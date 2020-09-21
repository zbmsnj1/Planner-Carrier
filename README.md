Evaluation of FOND planners
===========================

This is the project to evaluate the-state-of-art FOND planners by experiments. We will place all the details of experiments and a report about the evaluation.


folders
-----

#benchmarks
>the current benchmarks of FOND planning, all '.pddl' files

#Database
>store relative path of corresponding benchmark file

#planner
>the source code for the-state-of-art of FOND planners
    **Original links of FOND planners**
>>FIP [link](Experiment/FIP)

>>PRP * [Wiki](https://github.com/QuMuLab/planner-for-relevant-policies/wiki)

>>MBP [link](Experiment/MBP)

>>SAT [link](Experiment/SAT)

>>myND [link](Experiment/myND)

#src
>including the code files to updat database, to create task file, to run the planning benchmarks in parallel on a single machine or on a distrubted cluster

##before running
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
    *Create a task.csv file manually, following the format of the example task files in src/task*
    *Create a task.csv file using code*
```
python3 create_task.py
```
#results
>the folder contains all the data created by the system




