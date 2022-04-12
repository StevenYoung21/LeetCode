
class Solution:
    def arrangeCoins(self, n: int) -> int:

        all = 0
        other = 0

        if n == 1 or n == 2 : return 1

        for i in range(1,n):
            sumPoint = (i+1)*i/2
            if sumPoint == n:
                all = i
                return all
            elif sumPoint > n:
                other = i - 1
                break

        return other




n = 9

s1 = Solution()

res = s1.arrangeCoins(n)

print(res)