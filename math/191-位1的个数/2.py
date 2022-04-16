
class Solution:
    def hammingWeight(self, n: int) -> int:


        k = 0

        while n:
            if n & 1 == 1:
                k += 1
            n = n >> 1

        return k



n = 0B00000000001000000000000000001011

s1 = Solution()

res = s1.hammingWeight(n)

print(res)