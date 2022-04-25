
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s1 = Counter(s)
        s2 = Counter(t)

        return s2 == s1


s = "aa"

t = "bb"

s1 = Solution()
res = s1.isAnagram(s,t)

print(res)