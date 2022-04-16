
class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        s1,s2 = 1, 0

        if n < 10 : return n

        while n >= 1:
            s1 = (n % 10 )*s1
            s2 = (n % 10 ) + s2
            n = int(n / 10)

        return s1-s2


n = 114

s1 = Solution()

print(s1.subtractProductAndSum(n))