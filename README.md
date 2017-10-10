# SplitByChromosome
Python wrapper for samtools which will split a BAM file into standard chromosomes (1-22, X, Y) in parallel 

This python script spawns multiple processes
of samtools to split a bam file by chromosome in parallel.
Because this is executing 24 jobs simultaneously it is
best to execute this as a batch script on the bynode queue
as it should use all of the available cores.

Usage: `python3 split_by_chromosome.py [-h] [--chr] input.bam`
Input bam must be coordinate sorted and have a .bai index file.

## Requirements
* Samtools must be installed and present on the PATH
* Python3.5 (I have not tested it with python 2.7)

## Options
-h Display help

--chr Set this flag if your bam file is aligned to a genome where chromosomes start with 'chr'



Created by Anthony Scott
Sep 9, 2017
