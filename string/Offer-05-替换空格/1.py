
class Solution:
    def replaceSpace(self, s: str) -> str:

        res = ''

        for i in range(len(s)):
            if s[i] != ' ':
                res += s[i]
            else:
                res += '%20'

        return res

        return "%20".join(s.split(" "))


s = "We are happy."

s1 = Solution()

print(s1.replaceSpace(s))