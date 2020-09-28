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
eval : > $folder_name.csv        #reset the csv file 

num=${#arr[@]} 
for ((i=0;i<num;i++))
do
       {
       printf ${arr[i]} >> $folder_name.csv
       }  
done




