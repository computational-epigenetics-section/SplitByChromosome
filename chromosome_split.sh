#!/bin/bash

#SBATCH --time=16:00:00 -n24 -p bynode

#Args: Input_file.bam [--chr]
# Use optional --chr if chromosome IDs start with 'chr'

python3 /home/scott/jobs/scripts/split_bam_by_chromosome.py $1 $2
