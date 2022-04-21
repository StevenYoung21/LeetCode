class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        res = ''

        a1 = 0

        a2 = 0


        while a1 < min(len(word1),len(word2)) :
            res = res + word1[a1] + word2[a1]
            a1 += 1

        s =  len(word1) > len(word2)

        if s > 0:
            res = res + word1[a1:]
        else:
            res = res + word2[a1:]

        return res


word1 = "ab"
word2 = "pqrs"

s1 = Solution()

print(s1.mergeAlternately(word1,word2))