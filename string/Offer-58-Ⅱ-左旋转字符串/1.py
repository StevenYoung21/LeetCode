class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:

        s1 = s[:-k]
        s2 = s[-k:]

        s3 = s2+s1

        return s3

s = "abcdefg"
k = 2

s1 =Solution()
print(s1.reverseLeftWords(s,k))