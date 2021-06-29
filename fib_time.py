from fib import fibs
import timeit

def time_fib(name, n):
    setup = "from fib import fibs\nfib = fibs['%s']" % name
    stmt = 'fib(%d)' % n
    time = timeit.repeat(setup=setup, stmt=stmt, repeat=10, number=1)    
    return min(time) * 1e6

nums = {}
values = [2**i for i in range(11)]
nums['recursive'] = [2**i for i in range(5)]
nums['memoized']  = [2**i for i in range(11)]
nums['iterative'] = [2**i for i in range(13)]
nums['closed']    = [2**i for i in range(11)]
nums['recursive++'] = [2**i for i in range(8)]
nums['memoized++'] = [2**i for i in range(14)]

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
