fibs = {}

def register(name):
    def decorator(fib):
        fibs[name] = fib
        def wrapper(n):
            return fib(n)
        return wrapper
    return decorator

@register('recursive')
def fib_rec(n):
    if n < 2:
        return n
    return fib_rec(n-2) + fib_rec(n-1)

@register('memoized')
def fib_mem(n):
    mem = {0:0, 1:1}
    def helper(n):
        if n not in mem:
            mem[n] = helper(n-2) + helper(n-1)
        return mem[n]
    return helper(n)

@register('iterative')
def fib_itr(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b 
    return a

@register('closed')
def fib_cls(n):
    phi = (1 + 5 ** .5) / 2
    return round(phi**n / 5 ** .5)

@register('recursive++')
def fib_rec_pp(n):
    if n < 2:
        return n
    if n == 2:
        return 1
    m = n // 2
    if n % 2:
        return fib_rec_pp(m)**2 + fib_rec_pp(m+1)**2
    return fib_rec_pp(m) * (2*fib_rec_pp(m+1) - fib_rec_pp(m))

@register('memoized++')
def fib_mem_pp(n):
    mem = {0:0, 1:1, 2:1}
    def helper(n):
        if n not in mem:
            m = n // 2
            if n % 2:
                mem[n] = helper(m)**2 + helper(m+1)**2
            else:
                mem[n] = helper(m) * (2*helper(m+1) - helper(m))
        return mem[n]
    return helper(n)

@register('iterative++')
def fib_itr_pp(n):
    # F0 = [0]  Fn = [ fn ]  M = [0 1]  R = [1 0] = [a b]
    #      [1]       [fn+1]      [1 1]      [0 1]   [b c]
    # Fn = M**n * F0
    a, b, c = 1, 0, 1
    # bin(6) = '0b110'
    for x in bin(n)[2:]:
        # R **= 2
        s = b*b
        a, b, c = s+a*a, b*(a+c), s+c*c
        if x == '1':
            # R *= M  
            a, b, c = b, c, b+c
    # R = M**n 
    return b
