class Solution:
    def countOdds(self, low: int, high: int) -> int:

        k = 0

        if low % 2 == 1:                             # 首: 奇
            if high % 2 == 1:
                k = 1 + (high - low) // 2            # 尾: 奇
            else:
                k = 1 + (high - 1 - low) // 2        # 尾: 偶

        if low % 2 == 0:                              # 首: 偶
            if high % 2 == 1:
                k = (high + 1 - low) // 2             # 尾: 奇
            else:   
                k = (high - low) // 2                 # 尾: 偶

        return k


low = 3
high = 7

s1 = Solution()

res = s1.countOdds(low,high)

print(res)