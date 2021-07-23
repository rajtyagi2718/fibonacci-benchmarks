#!/bin/bash

file='fib_pow.txt'
while read line; do
  read name pow <<< "$line"
  n=1
  while  (( --pow > 0 )); do
    python fib_mem.py $name $n
    (( n*=2 ))
  done
done < $file
