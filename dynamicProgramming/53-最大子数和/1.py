
class Solution:
    def maxSubArray(self, nums) -> int:

        length = len(nums)

        if length == 1 :return nums[0]

        # sum = -float('inf') 

        max1 = []

        for i in range(length):
            sum = 0
            for j in range(i,length):
                sum = sum + nums[j] 
                max1.append(sum)

        return max(max1)


nums = [5,4,-1,7,8]

## 暴力解法超时

s1 = Solution()
res = s1.maxSubArray(nums)

print(res)