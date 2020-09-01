#!/bin/bash

echo "Please select the system you want to use, enter the number:
      1.SAT
      2.PRP"
read selected_num

case $selected_num in
[1])    #run all files in sat

for fileName in "Fond-domains"/*
do
  eval "printf '$(basename $fileName)\n1\n' | . test.sh"
done
      
;;

[2])   #run all files in prp

for fileName in "Fond-domains"/*
do
  eval "printf '$(basename $fileName)\n2\n' | . test.sh"
done

;;

*)
echo 'Your entry does not match any of the conditions.'

esac





