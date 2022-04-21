

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_counter  = {}

        for i in t:
            if i not in t_counter :
                t_counter [i] =  1
            else:
                t_counter [i] += 1

        res = (0, float("inf")) 

        left = 0
        need = len(t)
        
        for right in range(len(s)):
            if s[right] in t_counter:
                if t_counter[s[right]] > 0:
                    need -= 1
                t_counter[s[right]] -= 1
                
                # when slide window includes every chars in t
                while not need:
                    # build up result
                    if right - left + 1 < res[1] - res[0] + 1:
                        res = (left, right)
                    # move left pointer
                    if s[left] in t_counter:
                        if t_counter[s[left]] == 0:
                            need += 1
                        t_counter[s[left]] += 1
                    left += 1

        return "" if res[1] == float("inf") else s[res[0]:res[1] + 1]

s = "ADOBECODEBANC"

t = "ABC"

s1 = Solution()
print(s1.minWindow(s,t))