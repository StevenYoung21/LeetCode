
from operator import xor


class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        C0 = num
        x0 = num

        while 1:
            xi = (x0+C0/x0)/2

            if abs(xi-x0) < 1e-7:
                break
            x0 = xi

        k =  int(x0)

        if k*k == num :
            return True
        else:
            return False



num = 16

s1 = Solution()

rseult = s1.isPerfectSquare(num)

print(rseult) 