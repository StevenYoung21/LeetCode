from turtle import left, right


class Solution:
    def reverseWords(self, s: str) -> str:

        word = s.split(' ')

        res = []

        for i in word:
            res.append(i[::-1])

        string = ' '.join(res)

        return string


## 切片

s = "Let's take LeetCode contest"

s1 = Solution()
res = s1.reverseWords(s)

print(res)