# import profiling

from DP.profiling import *


class Solution:
    """
        Given p[i] - price for rod with len i+1
        and rod with len n - find rod cuts to max revenue
        rev(0) = 0
        rev(n) = max(p[0]+rev(n-1), p[1]+rev(n-2),...., p[n-2]+rev(1), p[n-1])
    """
    mem = []

    @profile
    def cutRod(self, n, p):
        """
        :param n: len of the rod
        :param p: List with prices for rod with len 1, 2, ..., n, ...
        :return: max revenue
        """
        if n == 0:
            return 0
        if len(Solution.mem) >= n:
            return Solution.mem[n-1]

        Max = -1
        for i in range(0, n):
            r = p[i] + self.cutRod(n-i-1, p)
            if r > Max:
                Max = r
        Solution.mem.append(Max)
        return Max

    @profile
    def cutRod2(self, n, p):
        """
        :param n: len of the rod
        :param p: List with prices for rod with len 1, 2, ..., n, ...
        :return: max revenue
        """
        R = [0]
        for i in range(1, n+1):
            Max = -1
            for j in range(1, i+1):
                r = p[j-1] + R[i-j]
                if r > Max:
                    Max = r
            R.append(Max)
        return Max


s = Solution()

p = [2, 5, 8, 9, 10, 11, 20, 30, 40, 50, 60, 70, 80, 81, 82]

l = len(p)
print("len", l)

@profile
def test1():
    assert s.cutRod(4, p) == 10
    assert s.cutRod(5, p) == 13
    assert s.cutRod(6, p) == 16
    n = s.cutRod(l-1, p)
    # print(n)
    assert n == 82
    n = s.cutRod(l, p)
    assert n == 85
    n = s.cutRod(l, p)
    n = s.cutRod(l, p)

@profile
def test2():
    assert s.cutRod2(4, p) == 10
    assert s.cutRod2(5, p) == 13
    assert s.cutRod2(6, p) == 16
    n = s.cutRod(l-1, p)
    # print(n)
    assert n == 82
    n = s.cutRod2(l, p)
    assert n == 85
    n = s.cutRod2(l, p)
    n = s.cutRod2(l, p)


test1()
test2()

print_prof_data()
# test1 240 us, test2 120 us
print("all good")