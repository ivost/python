
fact_memo = {0: 1, 1: 1}


def fact(n):
    """
    factorial
    :param n:
    :return:
    """
    if n in fact_memo:
        return fact_memo.get(n)
    f = n * fact(n-1)
    fact_memo[n] = f
    return f

def poisson_distr(k, s):
    """
    A Poisson experiment is a statistical experiment that has the following properties:

    The outcome of each trial is either success or failure.
    The average number of successes sigma that occurs in a specified region is known.
    The probability that a success will occur is proportional to the size of the region.
    The probability that a success will occur in an extremely small region is virtually zero.
    A Poisson random variable is the number of successes that result from a Poisson experiment.
    The probability distribution of a Poisson random variable is called a Poisson distribution.
    example: for k=3, s=3 -> 0.180

    :param k:
    :param s:
    :return:
    """
    return (float(pow(s, k)) * math.exp(-s)) / fact(k)


"""
    poisson 2

    Task
    The manager of a industrial plant is planning to buy a machine of either type A  or type B.
    For each day’s operation:
    The number of repairs, X, that machine A needs is a Poisson random variable with mean 0.88.
    The daily cost of operating A is 160 + 40 * X**2
    The number of repairs, Y, that machine B needs is a Poisson random variable with mean 1.55.
    The daily cost of operating B is 128 + 40 * Y**2

    On the first line, print the expected daily cost of machine A.
    On the second line, print the expected daily cost of machine B.


"""


import math

fact = lambda x: 1 if x <= 1 else x * fact(x - 1)
poisson = lambda mean, value: (mean ** value * math.exp(-mean)) / fact(value)
cost_a = lambda x: 160 + 40 * (x ** 2)
cost_b = lambda y: 128 + 40 * (y ** 2)

#mean_a, mean_b = [float(x) for x in input().split(' ')]
mean_a = 0.88
mean_b = 1.55

expected_a = sum([cost_a(x) * poisson(mean_a, x) for x in range(11)])
expected_b = sum([cost_b(y) * poisson(mean_b, y) for y in range(11)])
print('{:.3f}'.format(expected_a))
print('{:.3f}'.format(expected_b))



