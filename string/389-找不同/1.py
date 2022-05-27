class Solution:
    def findTheDifference(self, s: str, t: str) -> str:


        s1 = [i for i in s.encode()]
        s2 = [i for i in t.encode()]

        s3 = s1 + s2

        res = 0

        for i in s3:
            res ^= i

        return chr(res)



s = "ab"
t = "aab"

s1 = Solution()

print(s1.findTheDifference(s,t))