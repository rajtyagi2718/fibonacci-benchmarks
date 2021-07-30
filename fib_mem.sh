#!/bin/bash

echo "measuring memory usage." 
rm data_mem.txt &> /dev/null

while read line; do
  read name pow <<< "$line"
  n=1
  while  (( pow-- >= 0 )); do
    python fib_mem.py $name $n
    (( n*=2 ))
  done
done < fib_pow_mem.txt

echo "writing to file."
echo "fib_mem complete."
