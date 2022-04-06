from turtle import left, right


class Solution:
    def mySqrt(self, x: int) -> int:
        

        left = 0 
        right = x 

        while left <= right :
            mid = left + (right-left) // 2
            if mid * mid <= x:
                left = mid+1
            elif mid * mid > x:
                right = mid-1
        
        return right





x = 4

s1 = Solution()

rseult = s1.mySqrt(x)

print(rseult) 