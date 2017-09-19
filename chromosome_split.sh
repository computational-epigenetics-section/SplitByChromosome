#!/bin/bash

#SBATCH --time=16:00:00 -n24 -p bynode

python3 split_by_chromosome.py $1
