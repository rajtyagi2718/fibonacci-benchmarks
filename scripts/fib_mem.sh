#!/bin/bash

echo "measuring memory usage" 
rm data/mem_data.txt &> /dev/null

while read line; do
  read name pow <<< "$line"
  n=1
  while  (( pow-- >= 0 )); do
    python -m scripts.fib_mem $name $n
    (( n*=2 ))
  done
done < data/pow_data.txt
