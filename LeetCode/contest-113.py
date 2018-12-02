
def find(A, n):
    for i in range(len(A)):
        if A[i] == n:
            return i
    return -1

class Solution:

    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        if len(A) != 4:
            return ""

        s = ""
        a = sorted(A)

        # if last 2 dig > 5 - can't be minute - must be hour in 2nd pos
        # x6/7/8/9, x must be 0/1
        if a[2] > 5:
            if a[3] > a[2]:
                ss = str(a[3])
                del a[3]
            else:
                ss = str(a[2])
                del a[2]
            for n in [1, 0]:
                idx = find(a, n)
                if idx >= 0:
                    s = str(n)
                    del a[idx]
                    break
            s += ss
            if len(s) == 1:
                return ""
            s += ":"
            if a[1] <= 5:
                s += str(a[1])
                s += str(a[0])
            else:
                if a[0] <= 5:
                    s += str(a[0])
                    s += str(a[1])

            if len(s) < 5:
                return ""
            else:
                return s
        # first digit: 2, 1, 0
        for n in [2, 1, 0]:
            idx = find(a, n)
            if idx >= 0:
                s = str(n)
                del a[idx]
                break
        if len(s) == 0:
            return ""

        # 2nd digit if 1st is 2 - 3, 2, 1, 0 if it is 0/1 : 9 - 1
        if s[0] == "2":
            for n in [3, 2, 1, 0]:
                idx = find(a, n)
                if idx >= 0:
                    s += str(n)
                    del a[idx]
                    break
        else:
            # last is largest
            s += str(a[2])
            del a[2]

        if len(s) == 1:
            return ""

        s += ":"

        if a[1] <= 5:
            s += str(a[1])
            s += str(a[0])
        else:
            if a[0] <= 5:
                s += str(a[0])
                s += str(a[1])

        if len(s) < 5:
            return ""

        return s

s = Solution()

a = [1, 9, 6, 0]
x = s.largestTimeFromDigits(a)
print(x)
assert x == "19:06"

a = [2,0,6,6]
x = s.largestTimeFromDigits(a)
print(x)

a = [9,0,7,7]
x = s.largestTimeFromDigits(a)
print(x)

a = [4,2,4,4]
x = s.largestTimeFromDigits(a)
print(x)

a = [2, 0, 0, 0]
x = s.largestTimeFromDigits(a)
print(x)

a = [4, 3, 2, 1]
x = s.largestTimeFromDigits(a)
print(x)
a = [5, 5, 5, 5]
x = s.largestTimeFromDigits(a)
print(x)
a = [5, 9, 9, 1]
x = s.largestTimeFromDigits(a)
print(x)

"""
https://leetcode.com/contest/weekly-contest-113/problems/flip-equivalent-binary-trees/

For a binary tree T, we can define a flip operation as follows: choose any node, 
and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y 
after some number of flip operations.

Write a function that determines whether two binary trees are flip equivalent.  
The trees are given by root nodes root1 and root2.


Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.



950. Reveal Cards In Increasing Order

Difficulty: Medium

In a deck of cards, every card has a unique integer.  You can order the deck in any order you want.

Initially, all the cards start face down (unrevealed) in one deck.

Now, you do the following steps repeatedly, until all cards are revealed:

Take the top card of the deck, reveal it, and take it out of the deck.
If there are still cards in the deck, put the next top card of the deck at the bottom of the deck.
If there are still unrevealed cards, go back to step 1.  Otherwise, stop.
Return an ordering of the deck that would reveal the cards in increasing order.

The first entry in the answer is considered to be the top of the deck.

 

Example 1:

Input: [17,13,11,2,3,5,7]
Output: [2,13,3,11,5,17,7]
Explanation: 
We get the deck in the order [17,13,11,2,3,5,7] (this order doesn't matter), and reorder it.
After reordering, the deck starts as [2,13,3,11,5,17,7], where 2 is the top of the deck.
We reveal 2, and move 13 to the bottom.  The deck is now [3,11,5,17,7,13].
We reveal 3, and move 11 to the bottom.  The deck is now [5,17,7,13,11].
We reveal 5, and move 17 to the bottom.  The deck is now [7,13,11,17].
We reveal 7, and move 13 to the bottom.  The deck is now [11,17,13].
We reveal 11, and move 17 to the bottom.  The deck is now [13,17].
We reveal 13, and move 17 to the bottom.  The deck is now [17].
We reveal 17.
Since all the cards revealed are in increasing order, the answer is correct.


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """



