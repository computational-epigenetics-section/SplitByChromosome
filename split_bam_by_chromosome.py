####################################
#
# Created by Anthony Scott
# Aug 9, 2017
#
# This python script spawns multiple processes
# of samtools to split a bam file by chromosome in parallel.
#
# Because this is executing 24 jobs simultaneously it is
# best to execute this as a batch script on the bynode queue
# as it should use all of the available cores.
#
# Usage: "python3 split_by_chromosome.py input.bam"
#   Input bam must be coordinate sorted and have a .bai index file
# But consider starting this with an sbatch job script
#
####################################

import subprocess
import time
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_bam", help="Input bam file to split")
parser.add_argument("--chr", help="Set if input bam has chromosome IDs beginning with 'chr'", action="store_true")

args = parser.parse_args()

if args.chr:
    chromosomes = ["chr1", "chr2", "chr3", "chr4", "chr5", "chr6", "chr7", "chr8", "chr9", "chr10",
               "chr11", "chr12", "chr13", "chr14", "chr15", "chr16", "chr17", "chr18", "chr19",
               "chr20", "chr21", "chr22", "chrX", "chrY"]
else:
    chromosomes = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                   "11", "12", "13", "14", "15", "16", "17", "18", "19",
                   "20", "21", "22", "X", "Y"]



# Get the input file from the command line
input_bam = args.input_bam
file_name = input_bam.split('.')[0]
print("Input file is %s" % input_bam)
sys.stdout.flush()  # This is used to force a write to stdout on slurm

# create list to hold all spawned job references
procs = []

# Start splitting every chromosome simultaneously
for chromosome in chromosomes:  # Make sure this is set for testing or production
    output_bam = file_name + '.chr' + chromosome + ".bam"
    command = "samtools view -b %s %s > %s" % (input_bam, chromosome, output_bam)
    print("Command is: " + command)
    print("Output file is %s" % output_bam)
    p = subprocess.Popen("samtools view -b %s %s > %s" % (input_bam, chromosome, output_bam), shell=True)
    procs.append(p)
    sys.stdout.flush()

# Loop over all of the spawned jobs checking for completion
while True:
    counter = 0
    for p in procs:
        p.poll()
        print (p.returncode)
        sys.stdout.flush()
        if p.returncode is not None:
            counter += 1

    # If all are completed break the loop to end the python script
    if counter == len(chromosomes):  # Make sure this is set for testing or production
        break

    # Wait a little bit and check again
    else:
        print("Waiting 1 minute and check job status again")
        sys.stdout.flush()
        time.sleep(60)
