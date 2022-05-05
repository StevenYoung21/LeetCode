
class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        mapping = {
                    '(': ')',
                    '[': ']',
                    '{': '}'
                }

        for item in s:
            if item in mapping.keys():
                stack.append(mapping[item])
            elif stack == [] or stack[-1] != item:
                return False
            else:
                stack.pop()
           
                    
        if stack :
            return False
        else:
            return True

s = "()[[]{}"

s1 = Solution()

print(s1.isValid(s))