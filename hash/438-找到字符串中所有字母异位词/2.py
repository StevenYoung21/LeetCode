
import re


class Solution:
    def findAnagrams(self, s: str, p: str) :
        res = []

        left = right = 0
        needDic = [0 for _ in range(26)]
        windowDic = [0 for _ in range(26)]

        for i in range(len(p)):
            needDic[ord(p[i]) - ord('a')] += 1
            windowDic[ord(s[i]) - ord('a')] += 1

        if needDic == windowDic:
            res.append(0)

        for i in range(len(p),len(s)):
            windowDic[ord(s[i-len(p)]) - ord('a')] -= 1
            windowDic[ord(s[i]) - ord('a')] += 1
            if windowDic == needDic:
                res.append(i-len(p)+1)

        return res
            

        


s = "abab"

p = "ab"

s1 = Solution()

print(s1.findAnagrams(s,p))