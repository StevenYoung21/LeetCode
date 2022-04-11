class Solution:
    def maxProfit(self, prices) -> int:

        max1 = 0

        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                max1 = max(prices[j]-prices[i],max1)


        return max1

## 暴力超时

prices = [7,6,4,3,1]

s1 = Solution()
res = s1.maxProfit(prices)

print(res)