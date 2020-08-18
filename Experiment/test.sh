#!/bin/bash

unset arr
for file in Fond-domains/acrobatics/*
do
    if [ ${file: -5} == ".pddl" ]
    then
        curPath=$(realpath $file)
        arr=(${arr[*]} $curPath)
    fi
done
echo ${arr[@]}

num=${#arr[@]} 

for ((i=1;i<2;i++))

       {
         eval "cd SAT/src"
         eval "python main.py ${arr[0]} ${arr[i]}"
         
         #| awk -F '# Atoms:' '{print $1 }'
         eval "cd .."
         eval "cd .."
       }  



