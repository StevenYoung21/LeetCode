class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        stack = []
        res = ''

        for i in s:
            if i == '(':
                if stack != []:
                    res += i
                stack.append(i)

            if i == ')':
                stack.pop()
                if stack != []:
                    res += i

        return res

## 思路:
'''
1. (：入栈
2. ):出栈

删除最外层的括号, 即栈底的 ( 和最后的 ) , 这两个不用记录到结果res中:
1. 当遇到 ( 入栈时, 如果栈是空的, 则说明此时进入栈的是最外层的 ( , 不用记入到res中;
   但如果栈是非空的, 此时要记入res中.
   注意: 入栈操作时, 要先判断栈是否非空.

2. 当遇到 ) 出栈时, 如果栈是空的, 说明此时出栈的是最外层的栈底元素 ( , 不用记入到res中;
   但如果非空, 则记入到res中.
   注意: 出栈操作时, 要先出栈再判断是否非空.
'''



s = "(()())(())"

s1 = Solution()

print(s1.removeOuterParentheses(s))