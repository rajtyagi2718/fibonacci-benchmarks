import tracemalloc
import gc

from fib import fibs, fib_rec

def memory_fib(name, n):
    gc.collect()
    tracemalloc.start()
    fibs[name](n)
    _,peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    gc.collect()
    return peak
    

values = [2**i for i in range(25)]
powers = {'recursive'   : 5,
          'memoized'    : 5,
          'iterative'   : 5,
          'closed'      : 5,
          'recursive++' : 5,
          'memoized++'  : 5,
          'iterative++' : 5,
}
nums = {name : values[:i] for name,i in powers.items()}
# default to power 5
for name in fibs:
    if name not in nums:
        nums[name] = values[:1]

mems = {}
for name, num in nums.items():
    mems[name] = [memory_fib(name, n) for n in num]

mems1 = {}
for name, num in nums.items():
    mems1[name] = [memory_fib(name, n) for n in num]


if __name__ == '__main__':
    print(*mems.items(), sep='\n')
    print()
    print(*mems1.items(), sep='\n')
