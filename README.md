# Profiling Fibonacci sequence algorithms
Analysis of nth Fibonacci algorithms implemented in Python. 

## Plots
Beware of the log scale in the x-axis. All graphs transcribe their theoretical complexity. 

![alt text](https://github.com/rajtyagi2718/timestable/blob/master/plots/time_plot.png)


![alt text](https://github.com/rajtyagi2718/timestable/blob/master/plots/mem_plot.png)

## Algorithms
Three algorithms are considered, derived from the following identities.
(1) linear recurrence: F(n) = F(n-1) + F(n-2)
(2) quadratic recurrence: F(2n) = [F(n-1) + F(n+1)] * F(n)
                          F(2n-1) = F(n)^2 + F(n-1)^2
(3) closed form: F(n) = [phi^n - (-phi)^(-n)] / sqrt(5)
                 phi = [1 + sqrt(5)] / 2
This leads to exponential, logarithmic, constant time complexities. ++ indicates fast exponentiation algorithms derived from the quadratice recurrence.

Three implementations are considered: recursive, memoized, iterative.  
(1) recursive: call stack grows with each function call from n down to 1
(2) memoized: hash map grows with each cached output from n down to 1
(3) iterative: minimal set of parameters adjusted from 1 up to n
This leads to exponential, linear, constant space complexities.  

Notes:
* Linear algebra provides a beautiful derivation of the closed formula. Although in practice, phi is only approximated. Rounding floating points leads to overflow error after n = 2^10.
* The iterative qudratic implementation is tricky! It's fast exponentiation 
applied to the matrix formulation.
## Tests

## Scripts

## Plots

## Errors

## Notes





## References
