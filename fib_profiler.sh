#!/bin/bash

echo "running fib profiler"
python -m tests.fib_test
python -m scripts.fib_pow
python -m scripts.fib_time
bash scripts/fib_mem.sh
python -m scripts.fib_plot
