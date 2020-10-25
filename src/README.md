# User Manual 

**This is an user manual of Planner Carrier.**

## Table of Contents

* [Generate task](#generate-task)
* [Run task](#run-task)
* [Process data](#process-data)
* [Planner class](#planner-class)
* [Appendix](#Appendix)


## Generate task
### Command:
```
$ python3 gentask.py
```
### Details:

 * Step background: It will update the database automatically and save all benchmark's relative paths and an overview as `.csv` files in `Database/` folder, based on the current benchmark files in `benchmarks/` folder. It will also show the `Database/benchmarks.csv` on console.
 
* Step 1: Choose range of domains for testing, based on the table.
  * 0: Choose all domains
  * [a,b-c](#Usage-of-a-b-c): Choose a custom range of domains
 
* Step 2: Choose range of domains of selected domains for customizing problems size.
  * 0: Choose all problems for all selected domains
  * [a,b-c](#Usage-of-a-b-c): Choose a custom range of domains to customize specific problem sizes, all remaining domains will automatically choose complete problem sizes. (*We usually test the complete problems size, this function is designed just in case we want to test part of the problems.*)
  
* Step 3: Choose range of problems size for selected domains one by one. (*If choose 0 in Step 2, the Step 3 will not appear.*)
  * 0: Choose all problems for current domain
  * [a,b-c](#Usage-of-a-b-c): Choose specific problem sizes for current domain 

* Step 4: Choose range of planners for testing selected domains. (*Current only two planners.*)
  * 0: Choose all planners 
  * [a,b-c](#Usage-of-a-b-c): Choose specific planners

* Step 5: Save selected testing data in a csv file.
  * Enter a name to save the selected domains for testing in `.csv` file. (*name should exclude ".csv"*), it will also show the `test1.csv`  on console.
  
* **Console**:

	```
	$python3 gentask.py 
	
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
	10                  miner            50
	11        spiky-tireworld            11
	12              tireworld            15
	13        tireworld-truck            74
	14     triangle-tireworld            40
	15             zenotravel            15


	Please chose which domain you want to test:
	0.All
	a,b-c.From range 1-15 select a,b-c domains
	0

	Selected domains are: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

	Please select problems range for testing:
	0.All problems for all selected domains
	a,b-c.Custom specific problems range for selected a,b-c domains,All problems for remaining domains
	7-10 13

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

	Please select one planner for testing:
	1.prp
	2.sat
	0.All planners
	a,b-c.Select specific planners
	0

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

## Run task
### Command:
```
 $ python3 run.py [task.csv]
```

### Details:
* Step 1: Enter a folder name, all **standard output** (**stdout**) of each job will be stored as `.txt` files in `results/output/[task]/[planner]/domain_name_problem_id.txt` .

* Step 2: Choose mode to run task.
  * 1: Run task on your local machine, running n-jobs in parallel(*n depends on the number of CPU*), can change n in `run.py` in line: 
    ```python
    cluster = LocalCluster(n_workers=n_cpu, ...)
    ```
  * 2: To run task on cluster, you need set up clusters by writing ip address, user name and password for remote hosts in `run.py` in lines:
  
    ```python
    ["localhost",  "118.138.246.177", "romote2 ip", "romote3 ip"],
    connect_options={"known_hosts": None, 'username':'root', 'password':'pword'},
    ```
 * **Console**:
    ```
    	$python3 run.py task1.csv
	
	Please enter a folder name for saving output data of all jobs:
	task1

	Which mode you wish to run tasks?
	 1.Local machine
	 2.SSH Cluster
	1
	Start 539 jobs on local machine....

	Start job 16:
	Create sat planner successfully
	Create temporary work environment successfully
	Start running the planning job...
	Writing stdout into /home/yifan/plan/Planner-Carrier/results/output/task1/PRP/islands_p04.txt
	Finish running the planning job!
	Remove temporary work environment successfully

	Start job 17:
	Create sat planner successfully
	Create temporary work environment successfully
	Start running the planning job...
	Writing stdout into /home/yifan/plan/Planner-Carrier/results/output/task1/PRP/islands_p05.txt
	Finish running the planning job!
	Remove temporary work environment successfully


	.......

	Start job 441:
	Create prp planner successfully
	Create temporary work environment successfully
	Start running the planning job...
	Writing stdout into /home/yifan/Planner-Carrier/results/output/task1/PRP/tireworld-truck_p33.txt
	Finish running the planning job!
	Remove temporary work environment successfully

	Finish 539 jobs using 19193.952842712402(s)

    ```
## Process data
### Command:
```
 $ python3 processdata.py [output folder] [list.txt]
```

### Details:
 
 
* Step 1: Choose range of planners for processing data.
  * 0: Process data for all planners
  * [a,b-c](#Usage-of-a-b-c): Process data for specific planners
  
* Step background: After selecting planners, it will collect data with the key words in subclass(prp or sat) of (**Planner()**) and save all data as `.csv` files in `results/corresponding-planner-folder/data` folder. Then show collected data overview on console. If not find the key word, it will log on console: ERROR: Not find the key word {file_path}. 
 
* Step 2(Generate list): if `[list]` is "nolist", we can generate new list by following steps:
	* Step 2.1: Start from the first planner of selected planners, customzie the problems size for processing data.
		* 0: Choose all problems for all domains to process data.
		* [a,b-c](#Usage-of-a-b-c): Choose specific domains to customize problems size, and automatically choose complete problems size for remaining domains. (*This function can split the large problems size to small pieces, customized size is very convenient for data analysis.*)
	 * Step 2.2: Customize the specific size of problems. (* will loop Step 3 for  selected domains: 3, 5-10, 12, 14, then move to Step 4*)
		* 0: End choose problems size for current selected domain, move to next domain.    
		* [a,b-c](#Usage-of-a-b-c): Choose specific problems size for selected domain.
	 * Step 2.3: Save the list for future use
	 	* 1. Yes, the list will be saved as `.txt` in `results/list/[output folder]/[list].txt`
		* 2. No
	 * Step 2.4: Enter the list file name.
	 * Step 2.5: Decide to use same problems size as the previous planner or not.
		* 1: Will apply the previous problems size to remainging planners.(*will loop Step 5 for remaining planners*)
		* 2: Go to Step 2.1 again with next planner (*loop Step 2, generate list for next planner*), afer Step 3.
		
 * Step 2(Use existing list): Will skip generate list, and use the existing list for all planners. 
 
 * Step 3: Save processed data into a csv file. (*For now, only have one method: mean, so the data will be stored in `results/mean/[task]/[planner]/`*)
 	* Enter a name to save the selected domains for testing in `.csv` file. (*name should exclude ".csv"*)
   	* Then 
  	   * loop Step background and Step 2(Generate list) again: if choose 2 in Step 2.5
  	   * loop Step 3: if choose 1 in Step 2.5
	  
   	

 * **Console(without input list, need to generate list manually)**:
	```
	$ python3 processdata.py task1 nolist
	
	Please select which planner's results for data processing:
	1.prp
	2.sat
	0.All planners 
	a,b-c.Select specific planners
	0

	Selected planners: ['prp', 'sat']

	Collecting data:PRP......
	1 acrobatics(8)
	2 beam-walk(11)
	3 blocksworld-ipc08(30)
	4 doors(15)
	5 earth_observation(40)
	6 elevators(15)
	7 faults-ipc08(55)
	8 first-responders-ipc08(100)
	9 islands(60)
	10 miner(50)
	11 spiky-tireworld(11)
	12 tireworld-truck(74)
	13 tireworld(15)
	14 triangle-tireworld(40)
	15 zenotravel(15)

	Please select data range for processing:
	0.All problems for all domains
	a,b-c.Custom specific problems range for selected a,b-c domains, All problems for remaining domains
	3 5-10 12 14

	Custom range for domains Id=[3, 5, 6, 7, 8, 9, 10, 12, 14]

	3    blocksworld-ipc08    size: 30
	Please select problems range for testing:
	0.Move to next domain
	a,b-c.Custom specific problems range for selected domain
	1-15
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

	3    blocksworld-ipc08    size: 30
	Please select problems range for testing:
	0.Move to next domain
	a,b-c.Custom specific problems range for selected domain
	16-30
	[16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

	3    blocksworld-ipc08    size: 30
	Please select problems range for testing:
	0.Move to next domain
	a,b-c.Custom specific problems range for selected domain
	0
	
	...........(*loop above for all selected domains*)
	
	Do you want to save the list for furture use?
	 1.Yes
	 2.No
	1

	Please enter a list name(exclude ".txt") for saving list into a txt file:
	task1
	
	Do you want to use the same range for remaining planners?
	1.Yes
	2.No, I wish to custom range remaining planners
	1

	Please enter a task name(exclude ".csv") for saving mean data into a csv file:
	prp
		      Domain (# inst)    %solve         time         size
	0                   acrobatics(8:1-8)  1.000000    17.012500   127.500000
	1                  beam-walk(11:1-11)  1.000000    25.843636  1488.727273
	2                      doors(15:1-15)  0.800000     1.424000    18.400000
	3            spiky-tireworld(11:1-11)  0.090909  1655.652727    29.363636
	4                  tireworld(15:1-15)  0.800000     0.084000    11.200000
	5                 zenotravel(15:1-15)  1.000000     3.246667    54.600000
	6          blocksworld-ipc08(15:1-15)  1.000000     0.112000    15.133333
	7         blocksworld-ipc08(15:16-30)  1.000000     0.468000    33.666667
	8          earth_observation(20:1-20)  1.000000     0.190000    62.500000
	9         earth_observation(20:21-40)  1.000000     0.908000   234.400000
	10                 elevators(10:1-10)  1.000000     0.086000    29.100000
	11                 elevators(5:11-15)  1.000000     0.576000    81.400000
	12              faults-ipc08(20:1-20)  1.000000     0.026000     9.800000
	13             faults-ipc08(20:21-40)  1.000000     0.065000    16.650000
	14             faults-ipc08(15:41-55)  1.000000     0.093333    20.400000
	15    first-responders-ipc08(30:1-30)  0.766667     0.051333    10.666667
	16   first-responders-ipc08(40:31-70)  0.675000     1.039000    11.900000
	17  first-responders-ipc08(30:71-100)  0.833333     0.090000    18.666667
	18                   islands(30:1-30)  0.766667    90.018667     4.133333
	19                  islands(30:31-60)  0.266667    49.295333     2.933333
	20                     miner(30:1-30)  0.333333  1333.060667    12.733333
	21                    miner(20:31-50)  0.050000  1751.315000    11.650000
	22           tireworld-truck(24:1-24)  0.375000  1225.618333     9.791667
	23          tireworld-truck(25:25-49)  0.280000  1404.905600    15.520000
	24          tireworld-truck(25:50-74)  0.160000  1594.185600    12.520000
	25        triangle-tireworld(20:1-20)  1.000000     3.674000   125.000000
	26       triangle-tireworld(20:21-40)  1.000000   312.669000   365.000000
	Collecting data:SAT......
	ERROR: Not find key word!!!  /home/yifan/plan/Planner-Carrier/results/output/task1/SAT/beam-walk_p03.txt
	ERROR: Not find key word!!!  /home/yifan/plan/Planner-Carrier/results/output/task1/SAT/earth_observation_p03.txt
	ERROR: Not find key word!!!  /home/yifan/plan/Planner-Carrier/results/output/task1/SAT/earth_observation_p16.txt
	ERROR: Not find key word!!!  /home/yifan/plan/Planner-Carrier/results/output/task1/SAT/earth_observation_p21.txt
	ERROR: Not find key word!!!  /home/yifan/plan/Planner-Carrier/results/output/task1/SAT/faults-ipc08_p16.txt
	ERROR: Not find key word!!!  /home/yifan/plan/Planner-Carrier/results/output/task1/SAT/faults-ipc08_p22.txt
	ERROR: Not find key word!!!  /home/yifan/plan/Planner-Carrier/results/output/task1/SAT/tireworld-truck_p24.txt
	ERROR: Not find key word!!!  /home/yifan/plan/Planner-Carrier/results/output/task1/SAT/tireworld-truck_p25.txt
	ERROR: Not find key word!!!  /home/yifan/plan/Planner-Carrier/results/output/task1/SAT/tireworld-truck_p33.txt
	ERROR: Not find key word!!!  /home/yifan/plan/Planner-Carrier/results/output/task1/SAT/tireworld-truck_p34.txt
	ERROR: Not find key word!!!  /home/yifan/plan/Planner-Carrier/results/output/task1/SAT/tireworld-truck_p35.txt
	ERROR: Not find key word!!!  /home/yifan/plan/Planner-Carrier/results/output/task1/SAT/tireworld-truck_p57.txt
	ERROR: Not find key word!!!  /home/yifan/plan/Planner-Carrier/results/output/task1/SAT/tireworld-truck_p58.txt
	ERROR: Not find key word!!!  /home/yifan/plan/Planner-Carrier/results/output/task1/SAT/tireworld-truck_p59.txt
	ERROR: Not find key word!!!  /home/yifan/plan/Planner-Carrier/results/output/task1/SAT/triangle-tireworld_p02.txt

	Please enter a task name(exclude ".csv") for saving mean data into a csv file:
	sat
		      Domain (# inst)          #at        #acts    %solve          time       size
	0                   acrobatics(8:1-8)    67.500000   623.500000  0.375000   3915.349352  16.500000
	1                  beam-walk(11:1-11)   746.363636  2231.090909  0.181818   3924.156910  19.272727
	2                      doors(15:1-15)    48.000000    69.000000  0.600000   2545.554658  15.933333
	3            spiky-tireworld(11:1-11)   243.454545   462.545455  0.181818   4449.502825  21.636364
	4                  tireworld(15:1-15)    63.933333   304.000000  0.800000    604.336047  14.600000
	5                 zenotravel(15:1-15)   377.333333  8424.000000  0.333333    230.534534   9.066667
	6          blocksworld-ipc08(15:1-15)    78.666667  1350.000000  0.666667   1577.223892  12.400000
	7         blocksworld-ipc08(15:16-30)   238.666667  8116.666667  0.000000   1930.191845  11.000000
	8          earth_observation(20:1-20)    46.300000    87.700000  0.250000   4588.539241  18.050000
	9         earth_observation(20:21-40)   110.100000   224.300000  0.000000   5884.907390  21.900000
	10                 elevators(10:1-10)    64.000000    58.800000  0.600000   1959.410967  17.400000
	11                 elevators(5:11-15)   123.000000   116.400000  0.000000   5443.033360  19.400000
	12              faults-ipc08(20:1-20)    43.650000    35.500000  1.000000     23.330556   9.800000
	13             faults-ipc08(20:21-40)    84.550000    92.500000  0.400000   8229.917757  14.950000
	14             faults-ipc08(15:41-55)   129.600000   174.000000  0.000000  13819.699475  14.666667
	15    first-responders-ipc08(30:1-30)    83.000000   567.066667  0.600000   3238.780404  38.666667
	16   first-responders-ipc08(40:31-70)    68.900000   243.450000  0.375000   3000.705584  46.400000
	17  first-responders-ipc08(30:71-100)   167.833333  1078.833333  0.333333   7729.803927  23.600000
	18                   islands(30:1-30)   100.800000   333.400000  1.000000      0.495620   5.600000
	19                  islands(30:31-60)   388.966667  1588.600000  1.000000     85.690146  10.400000
	20                     miner(30:1-30)   598.266667  1230.866667  1.000000    162.791618  19.100000
	21                    miner(20:31-50)  1445.600000  2993.750000  0.800000   1130.388942  22.600000
	22           tireworld-truck(24:1-24)    64.083333   111.750000  1.000000     60.938769  11.708333
	23          tireworld-truck(25:25-49)    80.800000   150.400000  0.960000   1456.490207  15.920000
	24          tireworld-truck(25:50-74)   101.680000   198.720000  0.680000   2729.839874  17.280000
	25        triangle-tireworld(20:1-20)   669.500000  1406.000000  0.100000   5110.786480  19.100000
	26       triangle-tireworld(20:21-40)  4129.500000  9006.000000  0.000000   1268.615202  14.750000

	```     
 * **Console(using existing list)**:
	```
	$ python3 processdata.py task1 paper.txt

	Please select which planner's results for data processing:
	 1.prp
	 2.sat
	0.All planners 
	a,b-c.Select specific planners
	0
	Selected planners: ['prp', 'sat']

	Collecting data:PRP......

	Please enter a task name(exclude ".csv") for saving mean data into a csv file:
	prp
			      Domain (# inst)    %solve        time         size
	0                   acrobatics(8:1-8)  1.000000   17.012500   127.500000
	1                  beam-walk(11:1-11)  1.000000   25.843636  1488.727273
	2                      doors(15:1-15)  0.800000    1.776667    22.000000
	3            spiky-tireworld(11:1-11)  0.090909   69.560000    23.000000
	4                  tireworld(15:1-15)  0.800000    0.076667    10.083333
	5                 zenotravel(15:1-15)  1.000000    3.246667    54.600000
	6          blocksworld-ipc08(15:1-15)  1.000000    0.112000    15.133333
	7         blocksworld-ipc08(15:16-30)  1.000000    0.468000    33.666667
	8          earth_observation(20:1-20)  1.000000    0.190000    62.500000
	9         earth_observation(20:21-40)  1.000000    0.908000   234.400000
	10                 elevators(10:1-10)  1.000000    0.086000    29.100000
	11                 elevators(5:11-15)  1.000000    0.576000    81.400000
	12              faults-ipc08(20:1-20)  1.000000    0.026000     9.800000
	13             faults-ipc08(20:21-40)  1.000000    0.065000    16.650000
	14             faults-ipc08(15:41-55)  1.000000    0.093333    20.400000
	15    first-responders-ipc08(30:1-30)  0.766667    0.066957    13.913043
	16   first-responders-ipc08(40:31-70)  0.675000    1.539259    17.629630
	17  first-responders-ipc08(30:71-100)  0.833333    0.108000    22.400000
	18                   islands(30:1-30)  0.766667  117.415652     5.391304
	19                  islands(30:31-60)  0.266667  184.857500    11.000000
	20                     miner(30:1-30)  0.333333  399.074000    19.800000
	21                    miner(20:31-50)  0.050000  816.260000    29.000000
	22           tireworld-truck(24:1-24)  0.375000  242.773333    18.777778
	23          tireworld-truck(25:25-49)  0.280000  349.045714    27.857143
	24          tireworld-truck(25:50-74)  0.160000  440.750000    21.000000
	25        triangle-tireworld(20:1-20)  1.000000    3.674000   125.000000
	26       triangle-tireworld(20:21-40)  1.000000  312.669000   365.000000

	Collecting data:SAT......
	ERROR: Not find key word!!!  /home/yifan/plan/Planner-Carrier/results/output/task1/SAT/beam-walk_p03.txt
	ERROR: Not find key word!!!  /home/yifan/plan/Planner-Carrier/results/output/task1/SAT/earth_observation_p03.txt
	ERROR: Not find key word!!!  /home/yifan/plan/Planner-Carrier/results/output/task1/SAT/earth_observation_p16.txt
	ERROR: Not find key word!!!  /home/yifan/plan/Planner-Carrier/results/output/task1/SAT/earth_observation_p21.txt
	ERROR: Not find key word!!!  /home/yifan/plan/Planner-Carrier/results/output/task1/SAT/faults-ipc08_p16.txt
	ERROR: Not find key word!!!  /home/yifan/plan/Planner-Carrier/results/output/task1/SAT/faults-ipc08_p22.txt
	ERROR: Not find key word!!!  /home/yifan/plan/Planner-Carrier/results/output/task1/SAT/tireworld-truck_p24.txt
	ERROR: Not find key word!!!  /home/yifan/plan/Planner-Carrier/results/output/task1/SAT/tireworld-truck_p25.txt
	ERROR: Not find key word!!!  /home/yifan/plan/Planner-Carrier/results/output/task1/SAT/tireworld-truck_p33.txt
	ERROR: Not find key word!!!  /home/yifan/plan/Planner-Carrier/results/output/task1/SAT/tireworld-truck_p34.txt
	ERROR: Not find key word!!!  /home/yifan/plan/Planner-Carrier/results/output/task1/SAT/tireworld-truck_p35.txt
	ERROR: Not find key word!!!  /home/yifan/plan/Planner-Carrier/results/output/task1/SAT/tireworld-truck_p57.txt
	ERROR: Not find key word!!!  /home/yifan/plan/Planner-Carrier/results/output/task1/SAT/tireworld-truck_p58.txt
	ERROR: Not find key word!!!  /home/yifan/plan/Planner-Carrier/results/output/task1/SAT/tireworld-truck_p59.txt
	ERROR: Not find key word!!!  /home/yifan/plan/Planner-Carrier/results/output/task1/SAT/triangle-tireworld_p02.txt

	Please enter a task name(exclude ".csv") for saving mean data into a csv file:
	sat
			      Domain (# inst)          #at        #acts    %solve         time       size
	0                   acrobatics(8:1-8)    67.500000   623.500000  0.375000     6.066671   9.333333
	1                  beam-walk(11:1-11)   746.363636  2231.090909  0.181818     9.339560  12.000000
	2                      doors(15:1-15)    48.000000    69.000000  0.600000   485.842953  13.000000
	3            spiky-tireworld(11:1-11)   243.454545   462.545455  0.181818  2751.657836  23.000000
	4                  tireworld(15:1-15)    63.933333   304.000000  0.800000     1.138916   5.583333
	5                 zenotravel(15:1-15)   377.333333  8424.000000  0.333333    58.700949  12.800000
	6          blocksworld-ipc08(15:1-15)    78.666667  1350.000000  0.666667    26.698214  11.000000
	7         blocksworld-ipc08(15:16-30)   238.666667  8116.666667  0.000000          NaN        NaN
	8          earth_observation(20:1-20)    46.300000    87.700000  0.250000    11.790682   9.800000
	9         earth_observation(20:21-40)   110.100000   224.300000  0.000000          NaN        NaN
	10                 elevators(10:1-10)    64.000000    58.800000  0.600000   462.480578  14.666667
	11                 elevators(5:11-15)   123.000000   116.400000  0.000000          NaN        NaN
	12              faults-ipc08(20:1-20)    43.650000    35.500000  1.000000    23.488362   9.800000
	13             faults-ipc08(20:21-40)    84.550000    92.500000  0.400000  1751.640754  14.875000
	14             faults-ipc08(15:41-55)   129.600000   174.000000  0.000000          NaN        NaN
	15    first-responders-ipc08(30:1-30)    83.000000   567.066667  0.600000   808.720770   9.222222
	16   first-responders-ipc08(40:31-70)    68.900000   243.450000  0.375000  1061.495365  10.066667
	17  first-responders-ipc08(30:71-100)   167.833333  1078.833333  0.333333   313.299976  10.400000
	18                   islands(30:1-30)   100.800000   333.400000  1.000000     0.495620   5.600000
	19                  islands(30:31-60)   388.966667  1588.600000  1.000000    85.690146  10.400000
	20                     miner(30:1-30)   598.266667  1230.866667  1.000000   162.791618  19.100000
	21                    miner(20:31-50)  1445.600000  2993.750000  0.800000   753.263142  22.187500
	22           tireworld-truck(24:1-24)    64.083333   111.750000  1.000000    60.914601  11.708333
	23          tireworld-truck(25:25-49)    80.800000   150.400000  0.960000  1279.819242  15.833333
	24          tireworld-truck(25:50-74)   101.680000   198.720000  0.680000  1031.202705  16.705882
	25        triangle-tireworld(20:1-20)   669.500000  1406.000000  0.100000    25.081657  12.000000
	26       triangle-tireworld(20:21-40)  4129.500000  9006.000000  0.000000          NaN        NaN

	```     
     
## Planner class

* It is very easy to add new planner subclass inherit from the class (**Planner**), just need add the source code of new planner in `planners/`, and create a new subclass in `planner.py` with name, COLUMN_NAMES, TITLE, KEY_WORDS, KEY_WORDS_METHOD and KEY_WORDS_IGNORE. Now we only implement the **data_mean()** method. If  more methods are needed in future, we can easily add new methods in class : **Planner** and let subclasss **newPlanner** to inherit.
  * COLUMN_NAMES: the column names corresponds to key word, used for collecting key words data and saving in `.csv` (*should be one size larger than the size of KEY_WORDS, coz of Id for each problem*)
  * TITLE: the column names corresponds to key word, used for processing collected data and saving in `.csv` (*should be one size larger than the size of KEY_WORDS, coz of Domain(# inst) for each domain(range of problems)*)
  * KEY_WORDS: to find data corresponding with the key words
  * KEY_WORDS_FUNCTION: the funtion of `processdata.py` to apply for each key word, for example, FIND_KW return ture if finding the key word in output file, and MAX_INT return the max integer of all found integers by key word in output file (*should be same size as the size of KEY_WORDS*)
  * KEY_WORDS_IGNORE: while use KEY_WORDS_METHOD, it will find interferential data with key word, this help to ignore the unuseful data. For example: it will find both `get plan` and `not get plan`, but  if we wish to find only `get plan`, we can add `not` into `KEY_WORDS_IGNORE` to avoid this kind of situation (*should be same size as the size of KEY_WORDS*)

* Below is an example of subclass: **PRP(Planner)**)
  ```python
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

  ```   
 
## Appendix
### Usage of a b-c
* Select single: use either `space` or `,` to separate numbers
	```
	1, 4 5 9, 15 19
	```
* Select range: use `-` to indicates the connection range
	```
	1-20 25-60, 70-80, 90-100
	```
* Combination:
	```
	1 5-10,15 19,25-30 40-50 65
	```
*  Wrong usage:
	```
	-10 20-30-40 50-a 
	```


