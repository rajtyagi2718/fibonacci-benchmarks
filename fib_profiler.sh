#!/bin/bash

echo "running fib profiler"
python -m unittest -v fib_test.py
python fib_pow.py
python fib_time.py
bash fib_mem.sh
python fib_plot.py
