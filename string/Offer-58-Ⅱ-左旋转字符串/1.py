class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:

        k = n % len(s)

        s1 = s[0:k]
        s2 = s[k:]
        s3 = s2+s1

        return s3

s = "abcdefg"
k = 9

s1 =Solution()
print(s1.reverseLeftWords(s,k))