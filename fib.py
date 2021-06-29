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
    # F0 = [0]  Fn = [ fn ]  M = [0 1]  R = [1 0]
    #      [1]       [fn+1]      [1 1]    = [0 1]
    # Fn = M**n * F0
    m01 = m10 = m11 = r00 = r11 = 1
    m00 = r10 = r01 = 0
    print(n, bin(n)[2:][::-1])
    print('%d %d\t%d %d\n%d %d\t%d %d\n' % (m00, m01, r00, r01, m10, m11, r10, r11))
    for x in bin(n)[2:][::-1]:
        if x == '1':
            # R *= M  
            r00, r01, r10, r11 = r00*m00+r01*m10, r00*m01+r01*m11, r10*m00+r11*m10, r10*m01+r11*m11
        # M **= 2
        m00, m01, m10, m11 = m00**2+m01*m10, m01*(m01+m10), m01*(m00+m11), m11*2+m01*m10
        print('%d %d\t%d %d\n%d %d\t%d %d\n' % (m00, m01, r00, r01, m10, m11, r10, r11))
    # R = M**n 
    return r01

    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':    v1, v2, v3 = v1+v2, v1, v2
    return v2
    
