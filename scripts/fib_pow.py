from contextlib import contextmanager
import signal

from fib.fib import fibs


def raise_timeout(signum, frame):
    raise TimeoutError

@contextmanager
def timeout(fib, num, time):
    signal.signal(signal.SIGALRM, raise_timeout)
    signal.alarm(time)

    try:
        fib(num)
        yield True
    except TimeoutError:
        yield False
    except RecursionError:
        yield False
    except OverflowError:
        yield False
    except Exception as inst:
        print('unexpected exception: %s' % str(inst))
        yield False
    finally:
        signal.signal(signal.SIGALRM, signal.SIG_IGN)

def timeout_fibs(time):
    print("testing max fib inputs: timeouts after %d sec" % time)
    pows = {}
    nums = [2**i for i in range(25)]

    for name, fib in fibs.items():
        pow = len(nums)  
        for i, num in enumerate(nums):
            with timeout(fib, num, time) as result:
                if not result:
                    pow = i-1
                    break
        pows[name] = pow

    return pows

def write_pows(pows):
    with open('data/pow_data.txt', 'w') as f:
        for name, pow in pows.items():
            f.write("%s %s \n" % (name, pow))


if __name__ == '__main__':
    pows = timeout_fibs(2) 
    write_pows(pows)
