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

echo "Please select the system you want to use, enter the number:
      1.SAT
      2.PRP"
read selected_num


#defind functions
run_sat () {
         eval "cd SAT/src"
         eval "python main.py ${arr[$1]} ${arr[$2]}"  | egrep -w 'Atoms|Actions|Trying with|Cumulated solver time|SATISFIABLE' >$DIR/test.txt                      #find keywords from termianl output and save them to the test.txt 

         grep -w "Atoms" "$DIR/test.txt" | head -n1 | sed 's/[^0-9^.]*//g' | tr '\n' ','  >> $DIR/SAT/data/$folder_name.csv
         grep -w "Actions" "$DIR/test.txt" | head -n1 |sed 's/[^0-9^.]*//g' | tr '\n' ','  >> $DIR/SAT/data/$folder_name.csv
         if grep -q -w "SATISFIABLE" "$DIR/test.txt"; 
         then
             haveSolution="1,"          #if there is a solution, we set vaule to 1, else 0           
             printf $haveSolution >> $DIR/SAT/data/$folder_name.csv
             grep -w "Cumulated solver time" "$DIR/test.txt" | sed 's/[^0-9^.]*//g' | awk '{if(min==""){min=max=$1}; if($1>max) {max=$1}} END {print max}'| tr '\n' ','  >> $DIR/SAT/data/$folder_name.csv
             grep -w "Trying with" "$DIR/test.txt" | sed 's/[^0-9^.]*//g' | awk '{if(min==""){min=max=$1}; if($1>max) {max=$1}} END {print max}'  >> $DIR/SAT/data/$folder_name.csv           #find largest state(size)
         else
             haveSolution="0,"
             totalTime=" ,"
             policysize=" \n"
             printf $haveSolution >> $DIR/SAT/data/$folder_name.csv
             printf $totalTime >> $DIR/SAT/data/$folder_name.csv
             printf $policysize >> $DIR/SAT/data/$folder_name.csv
         fi
         
         
         #in csv file, 5 columns represent:  Atoms, Actions, solution, time,  polciy size

         eval "cd $DIR"
       }  
       
run_prp () {
         eval "cd PRP/src"
         eval "./prp  ${arr[$1]} ${arr[$2]} --dump-policy 2"  | egrep -w 'Strong cyclic plan found|Total time|   State-Action Pairs' >$DIR/test.txt                      #find keywords from termianl output and save them to the test.txt 

         if grep -q -w "Strong cyclic plan found" "$DIR/test.txt"; 
         then            
             haveSolution="1,"          #if there is a solution, we set vaule to 1, else 0           
             printf $haveSolution >> $DIR/PRP/data/$folder_name.csv
             grep -w "Total time" "$DIR/test.txt" | sed 's/[^0-9^.]*//g'| tr '\n' ','  >> $DIR/PRP/data/$folder_name.csv
             grep -w "State-Action Pairs" "$DIR/test.txt" | sed 's/[^0-9^.]*//g' | awk '{if(min==""){min=max=$1}; if($1>max) {max=$1}} END {print max}'  >> $DIR/PRP/data/$folder_name.csv           #find largest state(size)
         else
             haveSolution="0,"
             totalTime=" ,"
             policysize=" \n"
             printf $haveSolution >> $DIR/PRP/data/$folder_name.csv
             printf $totalTime >> $DIR/PRP/data/$folder_name.csv
             printf $policysize >> $DIR/PRP/data/$folder_name.csv
         fi
         
         
         #in csv file, 3 columns represent:  solution, time,  polciy size

         eval "cd $DIR"
       }         


case $selected_num in
[1])    #run sat

eval : > $DIR/SAT/data/$folder_name.csv        #reset the csv file   

echo "Atoms,Actions,Solve,Time,Size" >> $DIR/SAT/data/$folder_name.csv

if [ -f Fond-domains/$folder_name/domain.pddl ];          
then                              
    echo "for PDDL files: domain, p1, p2, p3, p4 ..."
    
    for ((i=1;i<num;i++))

       {
         run_sat 0 i
       }  

else                               
    echo "for PDDL files: d1, p1, d2, p2, d3, p3, d4, p4 ..."
    for ((i=0;i<half_num;i++))

       {
         run_sat i half_num+i
       }  

fi 
eval "python3 satData.py"  
      
;;

[2])   #run prp

eval : > $DIR/PRP/data/$folder_name.csv        #reset the csv file   

echo "Solve,Time,Size" >> $DIR/PRP/data/$folder_name.csv

if [ -f Fond-domains/$folder_name/domain.pddl ];          
then                              
    echo "for PDDL files: domain, p1, p2, p3, p4 ..."
    
    for ((i=1;i<num;i++))

       {
       run_prp 0 i
       }  

else                               
    echo "for PDDL files: d1, p1, d2, p2, d3, p3, d4, p4 ..."
    for ((i=0;i<half_num;i++))

       {
       run_prp i half_num+i        
       }  

fi 

eval "python3 prpData.py"     
;;

*)
echo 'Your entry does not match any of the conditions.'

esac



