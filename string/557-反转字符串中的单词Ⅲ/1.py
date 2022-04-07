from turtle import left, right


class Solution:
    def reverseWords(self, s: str) -> str:

        stack = []
        res = ''
        s = s + ' '

        for i in s:
            if i != ' ':
                stack.append(i)
            else:
                while(stack):
                    res = res + stack.pop()
                res = res + ' '


        # return stack
        return res[0:-1]


## 栈

s = "Let's take LeetCode contest"

s1 = Solution()
res = s1.reverseWords(s)

print(res)