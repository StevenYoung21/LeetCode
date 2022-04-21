

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_counter  = {}

        for i in t:
            if i not in t_counter :
                t_counter [i] =  1
            else:
                t_counter [i] += 1

        start = 0
        resLen = float('inf')

        left = 0
        right = 0
        need = len(t)
        
        

        if resLen == float('inf'):
            return ''
        else:
            return s[start:start+resLen]


s = "ADOBECODEBANC"

t = "ABC"

s1 = Solution()
print(s1.minWindow(s,t))