import timeit

from fib.fib import fibs


def time_fib(name, n, repeat):
    setup = "from fib.fib import fibs\nfib = fibs['%s']" % name
    stmt = 'fib(%d)' % n
    time = timeit.repeat(setup=setup, stmt=stmt, repeat=repeat, number=1)    
    return sum(time) / len(time) * 1e6

def time_fibs(repeat):
    nums = [2**i for i in range(25)]
    times = {}

    with open('data/pow_data.txt', 'r') as f:
        print("measuring execution times: average over %d runs" % repeat)
        for line in f:
            name, pow = line.split() 
            times[name] = [(n, time_fib(name, n, repeat)) 
                           for n in nums[:int(pow)+1]]

    return times

def write_times(times):
    with open('data/time_data.txt', 'w') as f:
        for name,values in times.items():
            for num,time in values:
                f.write("%s %s %s\n" % (name, num, time))


if __name__ == '__main__':
    times = time_fibs(5)
    write_times(times)
