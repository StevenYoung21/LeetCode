from cmath import sqrt
from re import T


class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        a = num ** 0.5

        b = int(a)

        c = a - b

        if c > 0 : 
            return False
        else:
            return True
    

num = 14

s1 = Solution()

rseult = s1.isPerfectSquare(num)

print(rseult) 