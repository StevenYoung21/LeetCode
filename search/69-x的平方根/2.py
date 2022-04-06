from turtle import left, right


class Solution:
    def mySqrt(self, x: int) -> int:
        
        C = x
        x0 = x

        while 1:
            xi = 0.5 * (x0+C/x0)
            print(xi)

            if abs(xi-x0) < 1e-7:
                break
            x0 = xi
        return int(x0)
                

## 牛顿法



x = 8

s1 = Solution()

rseult = s1.mySqrt(x)

print(rseult) 