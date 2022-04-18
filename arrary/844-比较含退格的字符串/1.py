class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        

        # sArr = []
        def fun1 (s):
            length1 = len(s)   
            s1 = ''
            for i in range(length1):
                if s[i] == '#':
                    s1 = s1[:-1]
                else:
                    s1 = s1 + s[i]
            return s1

        res = fun1(s) == fun1(t)

        return res



s = "a#c"
t = "b"

s1 = Solution()
res = s1.backspaceCompare(s,t)

print(res)