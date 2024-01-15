CC = gcc
SRC = src/
CFLAGS = -pg -ftree-vectorize -msse4 -mavx -march=native -mtune=native -O3

.DEFAULT_GOAL = MD.exe

MD.exe: $(SRC)/MD.cpp
	$(CC) $(CFLAGS) $(SRC)MD.cpp -lm -o MD.exe

clean:
	rm ./MD.exe

run:
	srun --partition=cpar perf stat -M cpi -e instructions,cycles,cache-misses,cache-references ./MD.exe < inputdata.txt
prof:
	gprof MD.exe gmon.out | gprof2dot -w | dot -Tpng -o output.png