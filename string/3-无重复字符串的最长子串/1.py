from operator import length_hint
from turtle import clear


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0 : return 0

        length = len(s)

        maxlen = 0
        cur = []

        for i in range(length):
            if s[i] not in cur:
                cur.append(s[i])
                maxlen = max(len(cur),maxlen)
            else:
                while s[i] in cur:
                    cur.pop(0)
                cur.append(s[i])

        return cur


s = "tmmzuxt"

s1 = Solution()
res = s1.lengthOfLongestSubstring(s)

print(res)