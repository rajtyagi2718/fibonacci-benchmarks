#!/bin/bash

echo "measuring memory usage" 
rm mem_data.txt &> /dev/null

while read line; do
  read name pow <<< "$line"
  n=1
  while  (( pow-- >= 0 )); do
    python fib_mem.py $name $n
    (( n*=2 ))
  done
done < pow_data.txt

echo "writing to file"
