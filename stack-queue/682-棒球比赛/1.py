from tempfile import tempdir
from turtle import st


class Solution:
    def calPoints(self, ops) -> int:

        stack = []

        temp = []

        for i in ops:
            if i != 'C' and i != 'D' and i != '+':
                stack.append(int(i))
            elif i == 'C':
                stack.pop()
            elif i == 'D':
                temp = int(stack[-1]) * 2
                stack.append(temp)
            elif i == '+':
                temp = int(stack[-1]) + int(stack[-2])
                stack.append(temp)


        return sum(stack)

ops = ["1"]

s1 = Solution()

print(s1.calPoints(ops))