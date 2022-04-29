class Solution:
    def reverseWords(self, s: str) -> str:

        # s = s.strip()

        seq = []
        res = ''

        for i in range(len(s)):
            if s[i] != ' ':
                seq.append(s[i])
                if i == len(s) - 1:
                    res =  ''.join(seq) + res
            else:
                if s[i] == s[i-1] : continue
                res =  ' ' + ''.join(seq) + res
                seq = []

        return res.strip()


s = " a good   example  "

s1=Solution()
print(s1.reverseWords(s))