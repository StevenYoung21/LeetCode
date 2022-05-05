from inspect import stack


class Solution:
    def evalRPN(self, tokens) -> int:

        stack = []

        for i in tokens:
            if i != '+' and i != '-' and i != '*' and i !='/' :
                stack.append(i)
            else:
                temp = 0
                # if i == '+' or i == '-' or i == '*' or i =='/':
                s1 = int(stack.pop())
                s2 = int(stack.pop())
                if i == '+':
                    temp = s1 + s2
                elif i == '-':
                    temp = s2 - s1
                elif i == '*':
                    temp = s2 * s1
                else:
                    temp = s2 / s1
                stack.append(temp)


        return stack[0]


tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

s1 = Solution()
print (s1.evalRPN(tokens))