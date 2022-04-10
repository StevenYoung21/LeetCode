class Solution:
    def maxProfit(self, prices) -> int:

        maxProfit = 0

        minPrices = prices[0]

        for price in prices:
            if price <= minPrices:
                minPrices = price
            
            maxProfit = max( price - minPrices, maxProfit )

        return maxProfit


"""
思路:

最理想的状态当然是在最低点买入, 最高点卖出, 但这种情况要保证最高点在最低点的后面.

如果先在最低点之前就出现了最大值, 则需要动态考虑: 我昨天的收益和今天的收益对比一下,哪个更大呢?

即: maxProfit = max( price - minPrices, maxProfit )

当天的收益, 就是当天的价格 减去 过去的最低价格, 所以要动态记录出现的最小价格.


"""


prices = [7,1,5,3,6,4]

s1 = Solution()
res = s1.maxProfit(prices)

print(res)