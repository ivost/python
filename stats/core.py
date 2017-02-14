"""
Task
Given an array of n integers, calculate and print the the respective mean, median,
and mode on separate lines.
If your array contains more than one modal value, choose the numerically smallest one.
    if n == 0:
        raise(ValueError("n is 0"))
"""
import math

eps = 0.0001

def mean(a):
    """
    average
    :param a:
    :return: average
    """
    n = len(a)
    return float(sum(a))/n


def weighted_mean(a, w):
    """
    sum(Ai * Wi) / sum(Wi)
    :param w:
    :param a:
    :return: average
    """
    t = 0.0
    for i in range(len(a)):
        t += a[i] * w[i]

    return t / sum(w)


def median(a):
    """
    median
    :param a: sorted array
    :return:
    """
    n = len(a)
    m = n / 2
    if n % 2 == 1:
        return float(a[m])
    else:
        return float(a[m-1]+a[m])/2.


def quartiles(a):
    """
    3 quartiles
    The quartiles of an ordered data set are the  points that split the data set into  equal groups.
    The  quartiles are defined as follows:
    Q1: The first quartile is the middle number between the smallest number in a data set and its median.
    Q2: The second quartile is the median ( percentile) of the data set.
    Q3: The third quartile is the middle number between a data set's median and its largest number.
    :param a: sorted array
    :return: tupple (Q1, Q2, Q3)
    """
    n = len(a)
    # n = 5 -> m = 2   0:2 3:5
    # n = 4 -> m = 2   0:2 2:4
    m = n / 2
    q1 = median(a[0:m])
    q2 = median(a)
    if n % 2 == 0:
        k = m
    else:
        k = m + 1
    q3 = median(a[k:])
    return q1, q2, q3


def mode(a):
    """
    most frequent number
    :param a: sorted array
    :param n:
    :return: most frequent number or smallest
    """
    # frequency dict - keys are numbers, values are count of occurences
    d = {}
    for x in a:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    # sorted array - get last as max
    min_mode = a[len(a)-1]
    max_count = 1
    for k, v in d.iteritems():
        if v > max_count:
            max_count = v
            min_mode = k
        elif v == max_count:
            # tie? keep min value
            if min_mode > k:
                min_mode = k

    return min_mode


def stdev(a):
    """
    standard deviation
    sqrt(sum(Ai - mean)**2)/N)
    :param a:
    :return:
    """
    n = len(a)
    m = mean(a)
    s = 0.0
    for x in a:
        s += (x - m) ** 2
    return math.sqrt(s/n)


fact_memo = {0: 1, 1: 1}
perm_memo = {(0, 0): 1}


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


def num_perm(n, r):
    """
    Number of permutations (order matters)
    An ordered arrangement of  objects from a set A, of  n objects (where 0 < r <= n)
    is called an r-element permutation of A.
    You can also think of this as a permutation of A's elements taken r at a time.
    :param n:
    :param r:
    :return:
    """
    if (n, r) in perm_memo:
        return perm_memo.get((n, r))
    p = float(fact(n))/fact(n - r)
    perm_memo[(n, r)] = p
    return p


def num_comb(n, r):
    """
    Number of permutations (order doesn't matter)
    An unordered arrangement of  objects from a set A, of n objects (where 0 < r <= n)
    is called an r-element combination of A.
    :param n:
    :param r:
    :return:
    """
    return num_perm(n, r)/fact(r)


def binomial_distr(x, n, p):
    res = float(num_comb(n, x)) * math.pow(p, x) * math.pow(1.-p, n-x)
    #print('binomial_distr x {}, n {}, p {:.5f} -> {:.5f}'.format(x, n, p, res))
    return res


def geom_distr(n, p):
    """
    geometric distribution is negative binomial distr. with num success = 1
    g(n, p) = p * q ** n-1
    :param n:
    :param p:
    :return:
    """
    res = p * math.pow(1.-p, n-1)
    return res


def cumulative_prob(from_num, to_num, n, p):
    total = 0.
    for x in range(from_num, to_num+1):
        total += binomial_distr(x, n, p)
    #print('cumulative_prob {}:{}, n {}, p {:.5f} -> {:.5f}'.format(from_num, to_num, n, p, total))
    return total


def feq(a, b):
    return abs(a - b) < eps


def pint(x):
    print('{}'.format(x))


def pfloat(x):
    print('{:.3f}'.format(x))


def solution(a, n):
    a = sorted(a)
    pfloat(mean(a))
    pfloat(median(a))
    pint(mode(a))


def test():
    """
    unit test
    a = [3, 2, 1]
    a = sorted(a)
    assert mean(a) == 2.
    assert median(a) == 2.
    assert mode(a) == 1

    a = [20, 30, 10, 20]
    a = sorted(a)
    assert mean(a) == 20.
    assert median(a) == 20.
    assert mode(a) == 20
    a = [1, 2, 3]
    w = [1, 1, 1]
    assert feq(weighted_mean(a, w), 2.)

    w = [2, 3, 1]
    assert feq(weighted_mean(a, w), 11./6.)

    a = [10, 40, 30, 50, 20]

    sd = stdev(a)

    assert feq(sd, 14.1)

    a = [1, 2, 3]
    assert quartiles(a) == (1, 2, 3)

    a = [6, 7, 15, 36, 39, 40, 41, 42, 43, 47, 49]
    assert quartiles(a) == (15, 40, 43)

    a = [7, 15, 36, 39, 40, 41]
    assert quartiles(a) == (15, 37.5, 40)

    assert fact(0) == 1
    assert fact(1) == 1
    assert fact(2) == 2
    assert fact(3) == 6
    assert fact(4) == 24

    assert fact(4) == 24

    assert feq(num_perm(3, 1), 3.0)
    assert feq(num_perm(3, 2), 6.0)

    assert feq(num_comb(3, 1), 3.0)
    assert feq(num_comb(3, 2), 3.0)

    # prob. of getting exactly 5 heads
    assert feq(binomial_distr(5, 10, 0.5), 0.24609)

    pfloat(binomial_distr(3, 6, 0.55215))


    # prob. of getting at least 5 heads
    assert feq(cumulative_prob(0, 5, 10, 0.5), 0.62305)

    # prob. of getting at most 5 heads
    #cumulative_prob(0, 5, 10, 0.5)
    #cumulative_prob(5, 10, 10, 0.5)
    """

    assert feq(geom_distr(5, 0.7), 0.00567)


if __name__ == '__main__':
    test()

"""
input:
The first line contains the respective space-separated numerator and denominator for the probability of a defect, and the second line contains the inspection we want the probability of being the first defect for:
1 3
5

ar = [float(x) for x in raw_input().split()]
p = ar[0] / ar[1]
n = input()
#pfloat(p)
#pint(n)
pfloat(geom_distr(n, p))

"""
