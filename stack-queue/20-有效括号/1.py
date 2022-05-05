
class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        n = len(s)

        for i in range(n):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            elif s[i] == ')':
                if stack == []:
                    return False
                else:
                    t =  stack.pop()
                    if t != '(':
                        return False
            elif s[i] == ']':
                if stack == []:
                    return False
                else:
                    t =  stack.pop()
                    if t != '[':
                        return False
            elif s[i] == '}':
                if stack == []:
                    return False
                else:
                    t =  stack.pop()
                    if t != '{':
                        return False
                    
        if stack :
            return False
        else:
            return True

s = "()[[]{}"

s1 = Solution()

print(s1.isValid(s))