from DP.profiling import *


class Solution:
    """
        House Robber
        n houses - each with p[i] money to steal
        can't rob 2 adjacent houses - will trigger alarm

        s(0) = p[0] = 0
        s(1) = p[1]
        s(2) = max(p[1], p[2])
        if we rob last house n - recurse 1..n-2
        if we skip last house - recurse 1..n-1
        s(n) = max(s(n-2)+p[n-1], s(n-1))
    """
    Mem = []

    @profile
    def steal(self, p, n):
        """
        max amnt from house 1 to n (inclusive)
        :param p:
        :param n:
        :return:
        """
        if n < 1:
            return 0
        mem = Solution.Mem
        # print("n", n, "p", p, "mem", mem)
        if n <= len(mem):
            return mem[n-1]

        if n == 1:
            Max = p[0]
        elif n == 2:
            Max = max(p[0], p[1])
        else:
            # n >= 3
            # print("n", n, "p", p, "mem", mem)
            Max = max(self.steal(p, n-2) + p[n-1], self.steal(p, n-1))

        mem.append(Max)
        # print("Max", Max)
        return Max


s = Solution()

p = [10, 20, 30, 100]

@profile
def test1():
    a = s.steal(p, 1)
    assert a == 10

    a = s.steal(p, 2)
    assert a == 20

    a = s.steal(p, 3)
    assert a == 40

    a = s.steal(p, 4)
    assert a == 120

test1()
# test2()

print_prof_data()
# test1 22 us
print("all good")
