class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:

        s1 = s[0:n][::-1]
        s2 = s[n:][::-1]
        s3 = s1+s2

        return s3[::-1]

s = "abcdefg"
k = 2

s1 =Solution()
print(s1.reverseLeftWords(s,k))