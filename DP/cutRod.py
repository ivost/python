
class Solution:
    """
        Given p[i] - price for rod with len i+1
        and rod with len n - find rod cuts to max revenue
        rev(0) = 0
        rev(n) = max(p[0]+rev(n-1), p[1]+rev(n-2),...., p[n-2]+rev(1), p[n-1])
    """
    mem = []

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


s = Solution()

p = [2, 5, 8, 9, 10, 11]
assert s.cutRod(4, p) == 10
assert s.cutRod(5, p) == 13
assert s.cutRod(6, p) == 16

print("all good")