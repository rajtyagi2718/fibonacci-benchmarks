
# Profiling Fibonacci sequence algorithms

Analysis of nth Fibonacci algorithms implemented in Python. 

## Plots

![alt text](https://github.com/rajtyagi2718/fibonacci-benchmarks/blob/main/plots/time_plot.png)

![alt text](https://github.com/rajtyagi2718/fibonacci-benchmarks/blob/main/plots/mem_plot.png)

### Notes

* Beware of the log scale on the x-axis. 
* Times are in microseconds, best of 5 runs.
* Memory is peak usage, including overhead from the profiler.

## Algorithms

Algorithms are derived from the following identities
* Linear recurrence
	F(n) = F(n-1) + F(n-2)
* Quadratic recurrence
	F(2n) = [F(n-1) + F(n+1)] * F(n)
	F(2n-1) = F(n)^2 + F(n-1)^2
* Closed form
	F(n) = [phi^n - (-phi)^(-n)] / sqrt(5)
	phi = [1 + sqrt(5)] / 2
with time complexities: exponential, logarithmic, constant.

Three implementations are considered
* Recursive: call stack grows with each function call from n to 1
* Memoized: hash map grows with each cached output from 1 to n
* Iterative: minimal set of parameters adjusted from 1 to n
with space complexities: exponential, linear, constant.  

The functions *recursive*, *memoized*, *iterative* use linear recurrence, *recursive++*, *memoized++*, *iterative++* use quadratic, *closed++* uses arbitrary precision floats.

### Notes

* Linear algebra provides a beautiful derivation of the closed formula. Floating points are required and overflow after n = 2^10, but arbitrary precision floats are scalable.
* The iterative qudratic implementation is tricky! It's fast exponentiation 
on matrices.

## Analysis

Interestingly, *memoized++* runs faster than *iterative++* after 2^12. Also *closed++* arbitrary precision floats use constant memory until 2^12. 

## Tests

## Scripts

## References
