CC = gcc
SRC = src/
CFLAGS = -O3 -pg -Wall -ftree-vectorize -msse4 -mavx -march=native -mtune=native

.DEFAULT_GOAL = all

all: MDseq.exe MDpar.exe

MDseq.exe: $(SRC)/MDseq.cpp
	module load gcc/11.2.0;\
	$(CC) $(CFLAGS) $(SRC)MDseq.cpp -lm -o MDseq.exe

MDpar.exe: $(SRC)/MDpar.cpp
	module load gcc/11.2.0;\
	$(CC) $(CFLAGS) $(SRC)MDpar.cpp -fopenmp -lm -o MDpar.exe

clean:
	rm ./MD*.exe

runseq: MDseq.exe
	./MDseq.exe < inputdata.txt

runpar: MDpar.exe
	export OMP_NUM_THREADS=40;\
	./MDpar.exe < inputdata.txt

runscript:
	sbatch --partition=cpar script.sh

desempenho:
	srun --partition=cpar perf record ./MDpar.exe < inputdata.txt
	srun --partition=cpar perf report -n --stdio > perfreport
