from inspect import stack


class Solution:
    def maxDepth(self, s: str) -> int:

        stack = []
        res = 0

        for i in s:
            if i == '(':
                stack.append(i)
            if i == ')':
                stack.pop()
            res = max(len(stack), res)

        return res

s = "(1)+((2))+(((3)))"

s1 = Solution()

print(s1.maxDepth(s))