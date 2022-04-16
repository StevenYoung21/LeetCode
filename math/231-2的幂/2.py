
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n == 0 : return False

        if (n) & (n-1)  == 0:
            return True
        else:
            return False



n = 3

s1 = Solution()

res = s1.isPowerOfTwo(n)

print(res)