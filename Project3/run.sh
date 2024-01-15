#!/bin/bash
#SBATCH --time=5:00
#SBATCH --partition=cpar
#SBATCH --constraint=k20

time nvprof ./bin/MD < inputdata.txt
