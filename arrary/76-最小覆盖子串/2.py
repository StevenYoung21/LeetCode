

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
        
        while right < len(s):
            if s[right] in t_counter:
                if t_counter[s[right]] > 0:
                    need -= 1
                t_counter[s[right]] -= 1

            while need == 0:
                if right - left + 1 < resLen:
                    resLen = right - left + 1
                    start = left

                if s[left] in t_counter:
                    if t_counter[s[left]] == 0:
                        need += 1
                    t_counter[s[left]] += 1
                left += 1
                
            right += 1    

        if resLen == float('inf'):
            return ''
        else:
            return s[start:start+resLen]

        # return s[start:start+resLen]
        # return "" if res[1] == float("inf") else s[res[0]:res[1] + 1]

s = "ADOBECODEBANC"

t = "ABC"

s1 = Solution()
print(s1.minWindow(s,t))