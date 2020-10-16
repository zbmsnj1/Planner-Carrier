# User Manual 

**This is an user manual of Planner Carrier.**

## Table of Contents

* [Generate tasks](#background)
	* [Command](##command)
	* [Details](##details)
* [Run planner](#usage)
	* [Command](##command)
	* [Details](##details)
	* [Planner class](###planner-class)
* [Process data](#process-data)
	* [Command](##command)
	* [Details](##details)
	* [Planner class](###basedata-class)


## Generate tasks
### Command:
```
$ python3 gentask.py
```
### Details:

 * Step background: It will update the database automatically and save all benchmark's relative paths and an overview as `.csv` files in `Database/` folder, based on the current benchmark files in `benchmarks/` folder. It will also show the `Database/benchmarks.csv` on console.
   * **console**:

      ```
      index             domain_name  problem_size
      1              acrobatics             8
      2               beam-walk            11
      3       blocksworld-ipc08            30
      4                   doors            15
      5       earth_observation            40
      6               elevators            15
      7            faults-ipc08            55
      8  first-responders-ipc08           100
      9                 islands            60
      10                   miner            50
      11         spiky-tireworld            11
      12               tireworld            15
      13         tireworld-truck            74
      14      triangle-tireworld            40
      15              zenotravel            15

      ```

* Step 1: Choose range of domains for testing, based on the table.
  * 0: Choose all domains
  * a,b-c: Choose a custom range of domains
    ```
    Please chose which domain you want to test:
    0.All
    a,b-c.From range 1-15 select a,b-c domains
    0
    ```

* Step 2: Choose range of domains of selected domains for customizing problems size.
  * 0: Choose all problems for all selected domains
  * a,b-c: Choose a custom range of domains to customize specific problem sizes, all remaining domains will automatically choose complete problem sizes. (*We usually test the complete problems size, this function is designed just in case we want to test part of the problems.*)

    ```
    Selected domains are: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    Please select problems range for testing:
    0.All problems for all selected domains
    a,b-c.Custom specific problems range for selected a,b-c domains,All problems for remaining domains
    7-10 13
    ```

* Step 3: Choose range of problems size for selected domains one by one. (*If choose 0 in Step 2, the Step 3 will not appear.*)
  * 0: Choose all problems for current domain
  * a,b-c: Choose specific problem sizes for current domain 
  
    ```
    7  faults-ipc08   size:55
    Please select problems range for testing:
    0.All problems for selected domain
    a,b-c.Custom specific problems range for selected domain
    1-40

    8  first-responders-ipc08   size:100
    Please select problems range for testing:
    0.All problems for selected domain
    a,b-c.Custom specific problems range for selected domain
    20-60

    9  islands   size:60
    Please select problems range for testing:
    0.All problems for selected domain
    a,b-c.Custom specific problems range for selected domain
    30-60

    10  miner   size:50
    Please select problems range for testing:
    0.All problems for selected domain
    a,b-c.Custom specific problems range for selected domain
    20-40

    13  tireworld-truck   size:74
    Please select problems range for testing:
    0.All problems for selected domain
    a,b-c.Custom specific problems range for selected domain
    12-65

    ```

* Step 4: Choose range of planners for testing selected domains. (*Current only two planners.*)
  * 0: Choose all planners 
  * a,b-c: Choose specific planners
    ```
    Please select one planner for testing:
     1.prp
     2.sat
    0.All planners
    a,b-c.Select specific planners
    0
    ```

* Step 5: Decide whether to end the choosing. 
  * 1: End choosing 
  * 2: Go back to Step 1, start choosing  again
    ```
    Have you finished entering data?
     1.Yes
     2.No, I wish to contiune
     1
    ```

* Step 6: Save selected testing data in a csv file.
  * Enter a name to save the selected domains for testing in `.csv` file. (*name should exclude ".csv"*)
  * It will also show the `test1.csv`  on console.
    ```
    Please enter a task name(exclude ".csv") for saving your task data into a csv file:
    test1
                   domain_name  start_problem  end_problem planner
    1               acrobatics              1            8     prp
    2                beam-walk              1           11     prp
    3        blocksworld-ipc08              1           30     prp
    4                    doors              1           15     prp
    5        earth_observation              1           40     prp
    6                elevators              1           15     prp
    7          spiky-tireworld              1           11     prp
    8                tireworld              1           15     prp
    9       triangle-tireworld              1           40     prp
    10              zenotravel              1           15     prp
    11            faults-ipc08              1           40     prp
    12  first-responders-ipc08             20           60     prp
    13                 islands             30           60     prp
    14                   miner             20           40     prp
    15         tireworld-truck             12           65     prp
    16              acrobatics              1            8     sat
    17               beam-walk              1           11     sat
    18       blocksworld-ipc08              1           30     sat
    19                   doors              1           15     sat
    20       earth_observation              1           40     sat
    21               elevators              1           15     sat
    22         spiky-tireworld              1           11     sat
    23               tireworld              1           15     sat
    24      triangle-tireworld              1           40     sat
    25              zenotravel              1           15     sat
    26            faults-ipc08              1           40     sat
    27  first-responders-ipc08             20           60     sat
    28                 islands             30           60     sat
    29                   miner             20           40     sat
    30         tireworld-truck             12           65     sat

    ```

## Run planner
### Command:
```
 $ python3 run.py [task.csv]
```

### Details:
* Step 1: Choose mode to run task.
  * 1: Run task on your local machine, running n-jobs in parallel(*n depends on the number of CPU*), can change n in `run.py` in line: 
    ```python
    cluster = LocalCluster(n_workers=n_cpu, ...)
    ```
  * 2: To run task on cluster, you need set up clusters by writing ip address, user name and password for remote hosts in `run.py` in lines:
  
    ```python
    ["localhost",  "118.138.246.177", "romote2 ip", "romote3 ip"],
    connect_options={"known_hosts": None, 'username':'root', 'password':'pword'},
    ```
   * **console**:
	    ```
	    Which mode you wish to run tasks?
	     1.Local machine
	     2.SSH Cluster
	    1
	    Start 18 jobs on local machine....

	    Start job 13:
	    Create sat planner successfully
	    Create temporary work environment successfully
	    Start running the planning job...
	    Writing stdout into /home/yifan/plan/Planner-Carrier/results/SAT/output/islands_p01.txt
	    Finish running the planning job!
	    Remove temporary work environment successfully

	    .......

	    Start job 1:
	    Create prp planner successfully
	    Create temporary work environment successfully
	    Start running the planning job...
	    Writing stdout into /home/yifan/plan/Planner-Carrier/results/PRP/output/islands_p02.txt
	    Finish running the planning job!
	    Remove temporary work environment successfully

	    Finish 18 jobs using 31.810213327407837(s)
	    ```

  * Step background: All **standard output** (**stdout**) of each job will be stored as `.txt` files in `results/corresponding-planner-folder/output/domain_name_problem_id.txt` .
  
### Planner class

* It is very easy to add new planner subclass inherit from the class (**Planner**), just need add the source code of new planner in `planners/`, and create a new subclass in `planner.py` with relative source code path and relative output path. 

* Below is an example of subclass: **SAT(Planner)**)
  ```python
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
  ```


## Process data
### Command:
```
 $ python3 processdata.py
```

### Details:
 
 
* Step 1: Choose range of planners for processing data.
  * 0: Process data for all planners
  * a,b-c: Process data for specific planners
 
    ```
    Please select which planner's results for data processing:
     1.prp
     2.sat
    0.All planners 
    a,b-c.Select specific planners
    0
    ```
* Step background: After selecting planners, it will collect data with the key words in class (**Basedata**) and save all data as `.csv` files in `results/corresponding-planner-folder/data` folder. Then show collected data overview on console.
  * **Console**：
    ```
    Selected planners: ['prp', 'sat']
    
    Collecting data:PRP......
        1 acrobatics(8)
        2 islands(5)
    ```
 
* Step 2: Start from the first planner of selected planners, customzie the problems size for processing data.
  * 0: Choose all problems for all domains to process data.
  * a,b-c: Choose specific domains to customize problems size, and automatically choose complete problems size for remaining domains. (*This function can split the large problems size to small pieces, customized size is very convenient for data analysis.*)
  * **Start from first planner in list: PRP**
  
    ```
    Collecting data:PRP......
    1 acrobatics(8)
    2 islands(5)

    Please select data range for processing:
    0.All problems for all domains
    a,b-c.Custom specific problems range for selected a,b-c domains, All problems for remaining domains
    0

    ```
 * Step 3: Decide to use same problems size as the previous planner or not.
 
   * 1: Will apply the previous problems size to remainging planners.
   * 2: Go to Step 2 again with next planner after Step 4.
  
      ```
      Custom range for domains Id=[]

      Do you want to use the same range for remaining planners?
       1.Yes
       2.No, I wish to custom range remaining planners
      2
      ```  
  * Step 4: Save processed data into a csv file. (*For now, only have one method: mean, so the data will be stored in `results/corresponding-planner-folder/mean`*)
 
   	* 1:  Enter a name to save the selected domains for testing in `.csv` file. (*name should exclude ".csv"*)
  	 * Will automatically collect data(Step background) then start from Step 2 again:：
        ```
        Please enter a task name(exclude ".csv") for saving mean data into a csv file:
        prp

        Domain (# inst)  %solve     time   size
        0  acrobatics(8:1-8)     1.0  18.8425  127.5
        1     islands(5:1-5)     1.0   0.0280    4.0

        Collecting data:SAT......
        1 islands(5)
       ```     
     
 * Step 2, 3, 4 for remaining planners one by one: 
   * **Console**：
        ```
        Please select data range for processing:
        0.All problems for all domains
        a,b-c.Custom specific problems range for selected a,b-c domains, All problems for remaining domains
        0

        Custom range for domains Id=[]

        Do you want to use the same range for remaining planners?
         1.Yes
         2.No, I wish to custom range remaining planners
        1

        Please enter a task name(exclude ".csv") for saving mean data into a csv file:
        sat
          Domain (# inst)   #at  #acts  %solve      time  size
        0  islands(5:1-5)  30.6   80.0     1.0  0.031659   4.0

       ```     
     

### Basedata class
* It is very easy to add new planner-data subclass inherit from the class (**Basedata**), just create a new subclass in `planner.py` with relative output path, relative daat path and relative result path for methods(e.g. **mean()**) path. Also need to customize the KEY_WORDS, KEY_WORDS_METHOD and KEY_WORDS_IGNORE.
  * KEY_WORDS: to find data corresponding with the key words
  * KEY_WORDS_METHOD: the method of **Basedata** to apply to each key word, for example, FIND_KW return ture if finding the key word in output file, and MAX_INT return the max integer of all found integers by key word in output file
  * KEY_WORDS_IGNORE: while use KEY_WORDS_METHOD, it will find interferential data with key word, this help to ignore the unuseful data. (*for example: it will find both `get plan` and `not get plan`, but  if we wish to find only `get plan`, we can add `not` into `KEY_WORDS_IGNORE` to avoid this kind of situation*)

* Below is an example of subclass: **PRPdata(Basedata)**

  ```python
  class PRPdata(Basedata):
	def __init__(self):
		self.REL_RES_PATH = "results/PRP/output"
		self.REL_DATA_PATH = "results/PRP/data"
		self.REL_MEAN_PATH = "results/PRP/mean"
		self.COLUMN_NAMES = ["Id","Solve","Time","Size"]
		self.TITLE = ['Domain (# inst)','%solve',"time",'size']
		self.KEY_WORDS = ["Strong cyclic plan found", "Total time", "State-Action Pairs"]
		self.KEY_WORDS_METHOD = [Basem.FIND_KW, Basem.MAX_FLOAT, Basem.MAX_INT]
		self.KEY_WORDS_IGNORE = [KEY_IGNORE, KEY_IGNORE, "Forbidden"]
		super().__init__()

	def save_into_csv(self):
		print("Collecting data:PRP......")
		super().save_into_csv(self.REL_RES_PATH, self.REL_DATA_PATH, self.COLUMN_NAMES, self.KEY_WORDS, self.KEY_WORDS_METHOD, self.KEY_WORDS_IGNORE )
		
	def generate_list(self):
		return super().generate_list(self.REL_DATA_PATH)
			
	def data_mean(self, list_name, list_size):
		super().data_mean(self.REL_DATA_PATH, self.REL_MEAN_PATH, self.COLUMN_NAMES, self.TITLE, list_name, list_size)

  ```
* Now we only implement the **mean()** method. If  more methods are needed in future, we can easily add new methods in class : **Basedata** and let subclasss **newPlannerdata** to inherit.
