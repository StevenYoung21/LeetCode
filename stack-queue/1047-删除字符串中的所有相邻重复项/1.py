class Solution:
    def removeDuplicates(self, s: str) -> str:

        stack = []

        for i in s:
            if stack ==[]:
                stack.append(i)
            else:
                if stack[-1] != i:
                    stack.append(i)
                else:
                    stack.pop()

            
        return ''.join(stack)


s = "abbacac"

s1 = Solution()

print(s1.removeDuplicates(s))