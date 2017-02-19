
def firstn(g, n):
    for i in range(n):
        yield next(g)


def intsfrom(i):
    while 1:
        yield i
        i += 1


def exclude_multiples(n, ints):
    for i in ints:
        if i % n: yield i


def sieve(ints):
    while 1:
        prime = next(ints)
        yield prime
        ints = exclude_multiples(prime, ints)


if __name__ == '__main__':
    for i in firstn(sieve(intsfrom(2)), 40):
        print(i)
