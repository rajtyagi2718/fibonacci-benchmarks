from fib import fibs
import timeit

def time_fib(name, n):
    setup = "from fib import fibs\nfib = fibs['%s']" % name
    stmt = 'fib(%d)' % n
    time = timeit.repeat(setup=setup, stmt=stmt, repeat=10, number=1)    
    return min(time) * 1e6

values = [2**i for i in range(25)]
powers = {'recursive'   : 5,
          'memoized'    : 11,
          'iterative'   : 13,
          'closed'      : 11,
          'recursive++' : 8,
          'memoized++'  : 16,
          'iterative++' : 16,
}
nums = {name : values[:i] for name,i in powers.items()}
# default to power 5
for name in fibs:
    if name not in nums:
        nums[name] = values[:5]

times = {}
for name, num in nums.items():
    times[name] = [time_fib(name, n) for n in num]

"""
with open('data.txt', 'w') as f:
    f.write('fib ' + ' '.join(str(x) for x in nums['closed']) + '\n')
    for name, value in times.items():
        f.write(name + ' ' + ' '.join(str(x) for x in value) + '\n') 
    print('data write complete.')
"""
