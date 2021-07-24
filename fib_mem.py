import argparse
import tracemalloc
from fib import fibs

parser = argparse.ArgumentParser(
    description="Find the nth fibonacci number. Profile memory used.")
parser.add_argument('name', help="fibonacci function name") 
parser.add_argument('n', type=int, help="nth fibonacci number")

if __name__ == '__main__':
    args = parser.parse_args()
    tracemalloc.start()
    fibs[args.name](args.n)
    _,peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    with open('data_mem.txt', 'a') as f:
        f.write(' '.join(map(str, (args.name, args.n, peak))) + '\n')
