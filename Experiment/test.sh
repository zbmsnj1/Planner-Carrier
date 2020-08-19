#!/bin/bash

echo "Please enter the name of domain you want to test:"
read folder_name

unset arr
for file in Fond-domains/$folder_name/*
do
    if [ ${file: -5} == ".pddl" ]               #find all ppdl files
    then
        curPath=$(realpath $file)
        arr=(${arr[*]} $curPath)                #store all paths of the pddl files into an array
    fi
done
echo ${arr[@]}
num=${#arr[@]}                                  #get the length of the arr
echo $num

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"   #the path of Experiment folder

eval : > $DIR/SAT/data/$folder_name.csv        #reset the csv file   


for ((i=1;i<num;i++))

       {
         eval "cd SAT/src"
         eval "python main.py ${arr[0]} ${arr[i]}"  | egrep -w 'Atoms|Actions|Trying with|Elapsed total time|SATISFIABLE$' >$DIR/test.txt                      #find keywords from termianl output and save them to the test.txt 

         if grep -q -w "SATISFIABLE" "$DIR/test.txt"; 
         then
             haveSolution="1"          #if there is a solution, we set vaule to 1, else 0
         else
             haveSolution="0"
         fi
         tail -4 "$DIR/test.txt" | sed 's/[^0-9^.]*//g' | tr '\n' ','  >> $DIR/SAT/data/$folder_name.csv     #get the digital number(incloud float) of last four lines, and save them to the csv file
         #in csv file, 5 columns represent: polciy size, Atoms, Actions, time, solution
         echo $haveSolution >> $DIR/SAT/data/$folder_name.csv       #save the solution sitution to the csv file

         eval "cd $DIR"
       }  


