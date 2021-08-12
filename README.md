
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
  * F(n) = F(n-1) + F(n-2)
* Quadratic recurrence
  * F(2n) = F(n) * [2F(n+1) - F(n)]
  * F(2n+1) = F(n)^2 + F(n+1)^2
* Closed form
  * F(n) = [phi^n - psi^n] / sqrt(5)
  * phi = [1 + sqrt(5)] / 2
  * psi = [1 - sqrt(5)] / 2

Three implementations are considered
* Recursive: call stack grows with each function call from n to 1
* Memoized: hash map grows with each cached output from 1 to n
* Iterative: minimal set of parameters adjusted from 1 to n

The functions *recursive*, *memoized*, *iterative* use linear recurrence, *recursive++*, *memoized++*, *iterative++* use quadratic, *closed++* uses arbitrary precision floats.

### Notes

* Linear algebra provides a beautiful derivation of the closed formula. Floating points are required and overflow after n = 2^10, but arbitrary precision floats are scalable.
* The iterative qudratic implementation is tricky! It's fast exponentiation 
of matrices.

## Asymptotic analysis

| algorithm   | time    | space   |
| :---------- | :----:  | ------: |
| recursive   | O(2^n)  | O(n)    |
| memoized    | O(n)    | O(n)    |
| iterative   | O(n)    | O(1)    |
| closed      | O(1)    | O(1)    |
| recursive++ | O(n)    | O(logn) |
| memoized++  | O(logn) | O(logn) |
| iterative++ | O(logn) | O(1)    |
| closed++    | O(1)    | O(1)    |


### Notes
* arithmetic operations assumed constant
* *recursive* has a tight bound of O(phi^n)
* *recursive++* has a tighter upper bound closer to O(n^.75) 
* *memoized++* runs faster than *iterative++* after 2^12
* *closed++* arbitrary precision floats use constant memory until 2^12 

## Tests

## Scripts

## References
