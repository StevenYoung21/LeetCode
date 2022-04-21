class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        res = ''

        a1 = 0

        a2 = 0

        while a1 < len(word1) and a2 < len(word2):
            if  a1 == len(word1) :
                res = res + word2[a2]
            if a2 == len(word2):
                res = res + word1[a1]
                
            res = res + word1[a1] + word2[a2]

            a1 += 1
            a2 += 1

        return res


word1 = "ab"
word2 = "pqrs"

s1 = Solution()

print(s1.mergeAlternately(word1,word2))