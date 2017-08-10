memo = {'0': 1, '1': 1}


def fib(n):
    if n < 2:
        return 1
    s = str(n)
    if s in memo:
        return memo[s]
    f = fib(n - 2) + fib(n - 1)
    memo[s] = f
    return f

def fibon(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a


for i in range(10):
    print(fibon(i))
