**How to run the test and get data**

*Run the testAll*

From `Experiment/` folder run:

```
$ testAll.sh

1         #for test SAT

2         #for test PRP
```
This will test all problems in Fond-domains/*

*Run the test*

From `Experiment/` folder run:

```
$ test.sh

folder_name  #enter the folder(domain) name you want to test

1         #for test SAT

2         #for test PRP
```

Then the data after test will be stored as csv files in 'SAT/data' or 'PRP/data'.


*Get the data*


From the `Experiment/` folder run:

```
>python3 satData.py

>python3 prpData.py

```

Will create satData.csv or prpData.csv stored the calculated data means from above data files.


