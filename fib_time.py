from fib import fibs
import timeit

def time_fib(name, n):
    setup = "from fib import fibs\nfib = fibs['%s']" % name
    stmt = 'fib(%d)' % n
    time = timeit.repeat(setup=setup, stmt=stmt, repeat=10, number=1)    
    return sum(time) / len(time) * 1e6

if __name__ == '__main__':
    nums = [2**i for i in range(25)]
    times = {}

    with open('fib_pow_time.txt', 'r') as f:
        print("measuring execution times.")
        for line in f:
            name,pow = line.split() 
            times[name] = [(n, time_fib(name, n)) for n in nums[:int(pow)+1]]

    with open('data_time.txt', 'w') as f:
        print("writing to file.")
        for name,values in times.items():
            for num,time in values:
                f.write("%s %s %s\n" % (name, num, time))

    print("fib_time complete.")
