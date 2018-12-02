import heapq


class Solution:

    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        sz = len(pushed)
        if len(popped) != sz:
            return False
        if sz == 0:
            return True

        stack = []
        i = 0
        j = 0

        while i < sz and j < sz:
            v = pushed[i]
            p = popped[j]
            # print("v", v, "p", p)
            if v == p:
                i += 1
                j += 1
                continue

            if len(stack) > 0 and p == stack[-1]:
                x = stack.pop()
                j += 1
                # print("pop", x)
            else:
                # print("push", v)
                stack.append(v)
                i += 1

        sz = len(stack)
        for i in range(sz):
            v = stack.pop()
            if v != popped[j]:
                return False
            j += 1

        return True

    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = 0
        a = sorted(A)
        for i in range(len(a) - 1):
            x = a[i]
            y = a[i + 1]
            if x < y:
                continue
            # x >= y
            d = x - y + 1
            y += d
            n += d
            a[i + 1] = y
        return n

    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """

        return 0

    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """

        return 0

    def countSameRowCol(self, stone, stones):
        c = 0
        for s in stones:
            if s == stone:
                continue
            if s[0] == stone[0]:
                c += 1
            if s[1] == stone[1]:
                c += 1
        return c

s = Solution()

# x = [1,2,3]
# print(x[-1])

stones = [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]

h = []
# heapq.heappush(h, (0, [0, 0]))
# a = heapq.heappop(h)
# print(a)

# print(stones)
m = {}
for st in stones:
    cnt = s.countSameRowCol(st, stones)
    # print(st, cnt)
    heapq.heappush(h, (cnt, [0, 1]))

print(len(h))

while len(h) > 0:
    p = heapq.heappop(h)
    print(p)
    if p[0] == 0:

        continue
    q = p

# a = [1, 2, 2]
# n = s.minIncrementForUnique(a)
# assert n == 1
#
# a = [3, 2, 1, 2, 1, 7]
# n = s.minIncrementForUnique(a)
# assert n == 6

# pushed = [1, 2, 3, 4, 5]
# popped = [4, 5, 3, 2, 1]
# ok = s.validateStackSequences(pushed, popped)
# assert ok
#
# popped = [4, 3, 5, 1, 2]
# ok = s.validateStackSequences(pushed, popped)
# assert not ok

"""
947. Most Stones Removed with Same Row or Column

On a 2D plane, we place stones at some integer coordinate points.  
Each coordinate point may have at most one stone.

Now, a move consists of removing a stone that shares a column or row with 
another stone on the grid.

What is the largest possible number of moves we can make? 

Example 1:
Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5

Example 2:
Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3

Example 3:
Input: stones = [[0,0]]
Output: 0
 

Note:

1 <= stones.length <= 1000
0 <= stones[i][j] < 10000

        
948. Bag of Tokens

You have an initial power P, an initial score of 0 points, and a bag of tokens.

Each token can be used at most once, has a value token[i], and has 
potentially two ways to use it.

If we have at least token[i] power, we may play the token face up, 
losing token[i] power, and gaining 1 point.

If we have at least 1 point, we may play the token face down, 
gaining token[i] power, and losing 1 point.

Return the largest number of points we can have after playing any number of tokens.

Example 1:
Input: tokens = [100], P = 50
Output: 0

Example 2:
Input: tokens = [100,200], P = 150
Output: 1

Example 3:
Input: tokens = [100,200,300,400], P = 200
Output: 2        
        
"""
