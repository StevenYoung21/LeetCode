class Solution:
    def isPowerOfFour(self, n: int) -> bool:


        for i in range(0,33):
            if 4 ** i == n:
                return True

        return False


n = 0

s1 = Solution()

print(s1.isPowerOfFour(n))