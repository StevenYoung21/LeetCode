
class Solution:
    def maxSubArray(self, nums) -> int:

        length = len(nums)

        if length == 1 :return nums[0]

        dp = [0]
        dp[0] = nums[0]


        for i in range(1,length):
                dp.append(max([nums[i],dp[i-1] + nums[i]]))

        return max(dp)


nums = [-2,1,-3,4,-1,2,1,-5,4]

## 动态规划
# dp[i]=max{nums[i],dp[i−1]+nums[i]}

s1 = Solution()
res = s1.maxSubArray(nums)

print(res)