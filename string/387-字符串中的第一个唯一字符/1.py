class Solution:
    def firstUniqChar(self, s: str) -> int:

        dic = {}

        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1

        for value in dic:
            if dic[value] == 1:
                return s.index(value)

        return -1



s = "leetcode"

s1 = Solution()
res = s1.firstUniqChar(s)

print(res)