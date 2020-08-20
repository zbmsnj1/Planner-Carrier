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
half_num=`expr $num / 2`
echo $num

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"   #the path of Experiment folder

eval : > $DIR/SAT/data/$folder_name.csv        #reset the csv file   



if [ -f Fond-domains/$folder_name/domain.pddl ];          
then                              
    echo "for PDDL files: domain, p1, p2, p3, p4 ..."
    for ((i=1;i<num;i++))

       {
         eval "cd SAT/src"
         eval "python main.py -time_limit 3600 ${arr[0]} ${arr[i]}"  | egrep -w 'Atoms|Actions|Trying with|Elapsed total time|SATISFIABLE' >$DIR/test.txt                      #find keywords from termianl output and save them to the test.txt 

         grep -w "Atoms" "$DIR/test.txt" | head -n1 | sed 's/[^0-9^.]*//g' | tr '\n' ','  >> $DIR/SAT/data/$folder_name.csv
         grep -w "Actions" "$DIR/test.txt" | head -n1 |sed 's/[^0-9^.]*//g' | tr '\n' ','  >> $DIR/SAT/data/$folder_name.csv
         if grep -q -w "SATISFIABLE" "$DIR/test.txt"; 
         then
             haveSolution="1,"          #if there is a solution, we set vaule to 1, else 0           
             printf $haveSolution >> $DIR/SAT/data/$folder_name.csv
             grep -w "Elapsed total time" "$DIR/test.txt" | sed 's/[^0-9^.]*//g' | tr '\n' ','  >> $DIR/SAT/data/$folder_name.csv
         else
             haveSolution="0,"
             totalTime=" ,"
             printf $haveSolution >> $DIR/SAT/data/$folder_name.csv
             printf $totalTime >> $DIR/SAT/data/$folder_name.csv
         fi
         grep -w "Trying with" "$DIR/test.txt" | sed 's/[^0-9^.]*//g' | awk '{if(min==""){min=max=$1}; if($1>max) {max=$1}} END {print max}'  >> $DIR/SAT/data/$folder_name.csv           #find largest state(size)
         
         #in csv file, 5 columns represent:  Atoms, Actions, solution, time,  polciy size

         eval "cd $DIR"
       }  

else                               
    echo "for PDDL files: d1, p1, d2, p2, d3, p3, d4, p4 ..."
    for ((i=0;i<half_num;i++))

       {
         eval "cd SAT/src"
         eval "python main.py -time_limit 3600 ${arr[i]} ${arr[half_num+i]}"  | egrep -w 'Atoms|Actions|Trying with|Elapsed total time|SATISFIABLE' >$DIR/test.txt                      #find keywords from termianl output and save them to the test.txt 

         grep -w "Atoms" "$DIR/test.txt" | head -n1 | sed 's/[^0-9^.]*//g' | tr '\n' ','  >> $DIR/SAT/data/$folder_name.csv
         grep -w "Actions" "$DIR/test.txt" | head -n1 |sed 's/[^0-9^.]*//g' | tr '\n' ','  >> $DIR/SAT/data/$folder_name.csv
         if grep -q -w "SATISFIABLE" "$DIR/test.txt"; 
         then
             haveSolution="1,"          #if there is a solution, we set vaule to 1, else 0           
             printf $haveSolution >> $DIR/SAT/data/$folder_name.csv
             grep -w "Elapsed total time" "$DIR/test.txt" | sed 's/[^0-9^.]*//g' | tr '\n' ','  >> $DIR/SAT/data/$folder_name.csv
         else
             haveSolution="0,"
             totalTime=" ,"
             printf $haveSolution >> $DIR/SAT/data/$folder_name.csv
             printf $totalTime >> $DIR/SAT/data/$folder_name.csv
         fi
         grep -w "Trying with" "$DIR/test.txt" | sed 's/[^0-9^.]*//g' | awk '{if(min==""){min=max=$1}; if($1>max) {max=$1}} END {print max}'  >> $DIR/SAT/data/$folder_name.csv           #find largest state(size)
         
         #in csv file, 5 columns represent:  Atoms, Actions, solution, time,  polciy size

         eval "cd $DIR"
       }  

fi       



