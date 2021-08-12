
# Profiling Fibonacci sequence algorithms

Analysis of nth Fibonacci algorithms implemented in Python. 

## Plots

![alt text](https://github.com/rajtyagi2718/fibonacci-benchmarks/blob/main/plots/time_plot.png)

![alt text](https://github.com/rajtyagi2718/fibonacci-benchmarks/blob/main/plots/mem_plot.png)

### Notes

* Beware of the log scale on the x-axis. 
* The memory profiler includes overhead from the module.

## Algorithms

The algorithms are derived from the following identities
1. linear recurrence: F(n) = F(n-1) + F(n-2)
2. quadratic recurrence: F(2n) = [F(n-1) + F(n+1)] * F(n)
                         F(2n-1) = F(n)^2 + F(n-1)^2
3. closed form: F(n) = [phi^n - (-phi)^(-n)] / sqrt(5)
                 phi = [1 + sqrt(5)] / 2
with time complexities: exponential, logarithmic, constant.

Three implementations are considered
1. recursive: call stack grows with each function call from n to 1
2. memoized: hash map grows with each cached output from 1 to n
3. iterative: minimal set of parameters adjusted from 1 to n
with space complexities: exponential, linear, constant.  

The functions named 'recursive', 'memoized', 'iterative' use linear recurrence, 'recursive++', 'memoized++', 'iterative++' use quadratic, 'closed++' uses arbitrary precision floats.

### Notes

* Linear algebra provides a beautiful derivation of the closed formula. Floating points are required and overflow after n = 2^10, but arbitrary precision floats are scalable.
* The iterative qudratic implementation is tricky! It's fast exponentiation 
on matrices.

## Analysis

Interestingly, 'memoized++' runs faster than 'iterative++' after 2^12. Also 'closed++' memory consumption from arbitrary precision stays constant until 2^12. 

## Tests

## Scripts

## Errors

## References
