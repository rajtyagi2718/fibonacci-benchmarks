from fib import fibs
from memory_profiler import memory_usage

def memory_fib(name, n):
    return memory_usage((fibs[name], (n,)), max_usage=True)

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

if __name__ == '__main__':
    memory = {}
    for name, num in nums.items():
        print(name, num)
        memory[name] = [memory_fib(name, n) for n in num]
    print(memory)

