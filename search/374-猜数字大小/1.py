# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0


class Solution:
    def guessNumber(self, n: int) -> int:

        left , right = 1 , n

        while left<=right:
            mid = left + (right-left)//2
            if guess(mid) == -1:
                right = mid - 1
            elif guess(mid) == 1:
                left = mid + 1
            else:
                return mid




n = 10

pick = 6

s1 = Solution()

rseult = s1.guessNumber(n)

print(rseult) 