
class Solution:
    """
    How many ways to get to step N of staircase
    if you can jump 1, 2, or 3 steps
    """
    # DP array with precomputed value up to given max
    w = [0, 1, 2, 4]
    max = 3

    def howManyWays(self, n):
        if n <= Solution.max:
            return Solution.w[n]
        for i in range(Solution.max+1, n+1):
            Solution.w.append(Solution.w[i-3] + Solution.w[i-2] + Solution.w[i-1])
        Solution.max = n
        return Solution.w[n]


s = Solution()

assert s.howManyWays(0) == 0
assert s.howManyWays(1) == 1
assert s.howManyWays(2) == 2
assert s.howManyWays(3) == 4
assert s.howManyWays(4) == 7
assert s.howManyWays(5) == 13
assert s.howManyWays(6) == 24
