#!/bin/bash

cd_dir_1="/Fond-domains/beam-walk/domain.pddl"
cd_dir_2="/Fond-domains/beam-walk/p01.pddl"

eval "cd SAT/src"
eval "python main.py $cd_dir_1 $cd_dir_2"
