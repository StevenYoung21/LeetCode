
class Solution:
    def findAnagrams(self, s: str, p: str) :
        res = []

        left =  valid = 0
        right = 0
        needDic = {}

        for i in range(len(p)):
            if p[i] not in needDic:
                needDic[p[i]] = 1
            else:
                needDic[p[i]] += 1

        while right < len(s):
            char = s[right]
            right += 1

            if char in needDic:
                needDic[char] -= 1
                if needDic[char] == 0:
                    valid += 1

            if right - left == len(p):
                if valid == len(needDic)  :
                    res.append(left)
                char = s[left]
                left += 1

                if char in needDic:
                    needDic[char] += 1
                    if needDic[char] == 1:
                        valid -= 1              

        return res


s = "abab"

p = "ab"

s1 = Solution()

print(s1.findAnagrams(s,p))